"""Audit the existing build and local routes. Does not rebuild or change data."""
from pathlib import Path
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import urlparse,unquote
from html.parser import HTMLParser
import json,hashlib,collections,re,subprocess,sys,argparse
from schema_check import check_supported,validate

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;DIST=HERE/'dist'
parser=argparse.ArgumentParser();parser.add_argument('--url',default='http://127.0.0.1:8765');args=parser.parse_args()
assert urlparse(args.url).hostname in ['127.0.0.1','localhost','::1'],'Local host only'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
reg=read(ROOT/'DECISION_REGISTER.json');data=read(DIST/'site-data.json');draft=read(ROOT/'submission.draft.json')
manifest=read(HERE/'build-manifest.json');schema=read(DIST/'submission.schema.json');sv=read(HERE/'schema-validation.json')
checks=[]
def passed(name,detail):checks.append({'check':name,'status':'PASS','detail':detail})
subprocess.run([sys.executable,str(HERE/'build.py'),'--check'],check=True,capture_output=True,text=True)
passed('build','Recomputed in memory and compared with existing canonical JSON/draft/assets; no rebuild written.')
expected=[f'D{i:03d}' for i in range(1,101)]
for obj in [reg,data,draft]:
    assert [d['id'] for d in obj['decisions']]==expected
    assert len({d['id'] for d in obj['decisions']})==100
    assert collections.Counter(d['reviewTier'] for d in obj['decisions'])=={'operational':75,'material_judgment':25}
passed('decision_identity','100 unique D001-D100; 75 operational / 25 material_judgment in register, canonical data and draft.')
for r,c,d in zip(reg['decisions'],data['decisions'],draft['decisions']):
    for key in d:
        if key=='guidedReview':
            expected_guided=dict(r[key]);expected_guided.pop('sourcePath',None)
            assert d[key]==c[key]==expected_guided
        else:assert d[key]==c[key]==r[key],(r['id'],key)
    for key in ['originalA','originalB','adjudicationRationale','amountEUR','candidateAmountEUR']:
        assert r.get(key)==c.get(key)
    assert all(isinstance(d[k],str) and d[k].strip() for k in ['question','answer','confidence','category'])
    assert d['evidence'] and d['primaryEvidence']
    if d['reviewTier']=='material_judgment':
        assert d['aiProposal'] and len(d['independentChallenge'])>=20 and d['studentFinalAnswer']
        assert d['studentReasoning'] is None and d['changedFromAI'] is None
        assert d['guidedReview']['independentSourceReviewEstablished'] is False
        assert d['guidedReview']['noAIReviewEstablished'] is False
passed('answers_and_fidelity','100 required AI/coordinator answers present; 25 guided outcomes present; no inferred personal reasoning or change flags; A/B history unchanged.')
assert reg['student']==data['student']==draft['student']=={'id':None,'name':None}
assert reg['studentCertification'] is None and all(d['certifiedByStudent'] is False for d in reg['decisions'])
assert reg['guidedReview']['clarificationRequiredIds']==[]
d049=next(d for d in data['decisions'] if d['id']=='D049')
assert 'current-period' in d049['studentFinalAnswer'] and 'чистая непогашенная сумма' in d049['guidedReview']['clarification']['textVerbatim']
assert d049['guidedReview']['originalHandoffOutcome']
passed('student_integrity','Identity null; personal reasoning null; guided disclosure retained; D049 clarification present with original retained.')
assert len(data['schedules'])==7 and len(data['statements'])==3 and len(data['reconciliations'])==7
assert draft['schedules']=={str(i+1):s for i,s in enumerate(data['schedules'])}
assert draft['statements']==data['statements'] and draft['reconciliations']==data['reconciliations']
assert draft['boardRecommendation']==data['boardRecommendation']
assert data['unresolved']==[d['id'] for d in reg['decisions'] if d['resolutionStatus']=='unresolved']
assert len(data['unresolved'])==30 and all(d['confidence']=='low' for d in data['decisions'] if d['id'] in data['unresolved'])
assert data['metrics']['inventoryGap']==9000 and data['metrics']['cash']==60000
assert all(s['status']=='preliminary_qualified' for s in data['statements'].values())
assert [r['id'] for r in data['reconciliations']]==['R'+str(i) for i in range(1,8)]
passed('financial_fidelity','7 schedules, 3 qualified statements, R1-R7, 30 unresolved and EUR 9,000 gap preserved; draft equals canonical financial structures.')
for p in data['provenance']:assert sha(ROOT/p['file'])==p['sha256']
assert sha(DIST/'site-data.json')==manifest['canonicalSHA256']
assert (ROOT/'submission.draft.json').read_bytes()==(DIST/'submission.draft.json').read_bytes()
for doc in data['documents'].values():assert doc['markdown']==(ROOT/doc['sourceFile']).read_text(encoding='utf-8')
passed('source_hashes','Current input hashes and canonical build manifest match; root/dist draft byte-identical; complete financial source Markdown retained.')
evidence={e['name']:e for e in data['evidence']};links=set()
manifest_text=(ROOT/'SOURCE_MANIFEST.md').read_text(encoding='utf-8')
for e in evidence.values():
    assert re.fullmatch(r'https://drive\.google\.com/file/d/[A-Za-z0-9_-]+/view',e['url'])
    fileid=e['url'].split('/')[5]
    assert fileid in manifest_text,e['name']
    assert sha(ROOT/'tmp/stage4_sources'/e['name'])==e['sha256']
for d in data['decisions']:
    for e in d['primaryEvidence']:
        assert e['file'] in evidence and e['url']==evidence[e['file']]['url'] and e['sha256']==evidence[e['file']]['sha256']
        assert e['locator'].strip();links.add(e['url'])
passed('primary_evidence','14 URL identities match SOURCE_MANIFEST and local primary SHA-256; every decision has matching primary links and locators. Live Drive access not rechecked.')
class Links(HTMLParser):
    def __init__(self):super().__init__();self.hrefs=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':self.hrefs.extend(v for k,v in attrs if k=='href')
all_links=set()
for doc in list(data['documents'].values())+data['schedules']+list(data['statements'].values())+data['reconciliations']:
    p=Links();p.feed(doc['html']);all_links.update(p.hrefs)
for url in all_links:
    if url.startswith('https:'):assert url in {e['url'] for e in evidence.values()},url
    elif url.startswith('/#decision-'):assert url.split('-')[-1] in expected
    else:assert url.startswith('/documents/') and (DIST/unquote(url[1:])).is_file(),url
passed('rendered_links',f'{len(all_links)} unique compiled links resolve to known D-IDs, local documents or primary file URLs; no arbitrary local path links.')
check_supported(schema);errors=validate(draft,schema)
assert errors==sv['schemaErrors'] and len(errors)==50
assert all(e['path'].endswith(('.studentReasoning','.changedFromAI')) for e in errors)
assert len(sv['contentBlockers'])==52
assert all(data['submission'][k]==v for k,v in sv.items())
assert len(data['submission']['contentBlockers'])==52 and data['submission']['schemaErrors']==errors
assert not data['submission']['canSubmit'] and draft['isFinalSubmission'] is False
# Test the exact schema features used, including boolean/number distinction and conditional requirements.
assert not validate({'x':3},{'type':'object','required':['x'],'properties':{'x':{'type':'number'}}})
assert validate(True,{'type':'number'}) and validate(None,{'type':'boolean'})
assert validate('abc',{'type':'string','minLength':4})
assert validate('D101x',{'pattern':'^D[0-9]{3}$'})
assert validate({'kind':'m'},{'allOf':[{'if':{'properties':{'kind':{'const':'m'}},'required':['kind']},'then':{'required':['reason']}}]})
assert not validate({'kind':'o'},{'if':{'properties':{'kind':{'const':'m'}}},'then':{'required':['reason']}})
assert validate([1],{'type':'array','minItems':2}) and validate([1,2],{'maxItems':1})
assert validate({'x':0},{'type':'object','additionalProperties':False})
try:check_supported({'$ref':'x'})
except ValueError:pass
else:raise AssertionError('Unsupported keywords must fail closed')
passed('schema','50 genuine missing-personal-field schema errors, 52 content blockers including identity; exact schema keyword implementation tested. Not claimed as a general-purpose Draft 2020-12 engine.')
routes=[]
for route in ['/','/review','/review/','/app.js','/styles.css','/favicon.svg','/site-data.json','/submission.draft.json','/submission.schema.json']+['/documents/'+p['file'] for p in data['provenance']]:
    with urlopen(args.url+route,timeout=15) as response:
        body=response.read();assert response.status==200
        if route=='/site-data.json':assert body==(DIST/'site-data.json').read_bytes()
        if route=='/submission.draft.json':assert body==(ROOT/'submission.draft.json').read_bytes()
        routes.append({'route':route,'status':response.status,'finalURL':response.url,'bytes':len(body)})
for route in ['/submission.json','/.git/config','/not-a-route']:
    try:urlopen(args.url+route,timeout=10)
    except HTTPError as e:assert e.code==404;routes.append({'route':route,'status':404})
    else:raise AssertionError('Unexpected exposed route: '+route)
assert not (ROOT/'submission.json').exists() and not (DIST/'submission.json').exists()
assert (DIST/'index.html').read_bytes()==(DIST/'review/index.html').read_bytes()
script=(DIST/'app.js').read_text(encoding='utf-8')
assert script.count("fetch('/site-data.json')")==1 and re.findall(r'fetch\(',script)==['fetch(']
passed('routes_and_single_data_source','Home and /review share identical shell/app.js; only data fetch is /site-data.json; HTTP bytes match canonical file. Final submission and git path return 404.')
result={'status':'PASS_WITH_DECLARED_SUBMISSION_BLOCKERS','checks':checks,'routes':routes,'schemaErrorCount':50,'contentBlockerCount':52,'canonicalSHA256':sha(DIST/'site-data.json'),'draftSHA256':sha(ROOT/'submission.draft.json'),'browserChecksRecordedSeparately':'AUDIT_LOG.md'}
(HERE/'audit-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'checks':len(checks),'routes':len(routes),'schemaErrors':50,'blockers':52,'canonicalSHA256':result['canonicalSHA256']},ensure_ascii=False))
