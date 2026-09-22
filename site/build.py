"""Build the private, English report display from the completed submission."""
from pathlib import Path
import hashlib, json, shutil
from schema_check import check_supported, validate

HERE=Path(__file__).resolve().parent; ROOT=HERE.parent; DIST=HERE/'dist'
SCHEMA=ROOT/'tmp/stage4_sources/02 GIVE TO CODEX - Submission Rules.json'
METHOD=['01 GIVE TO CODEX - Answer Template.json','02 GIVE TO CODEX - Submission Rules.json']
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ref(e): return {'sourceId':e['sourceId'],'filename':e['file'],'documentType':e['file'].rsplit('.',1)[-1].upper(),'locator':'Recorded location in source file','checksumReference':'SHA-256 '+e['sha256'][:16]+'…'}
def outcome(d):
    if d.get('studentFinalAnswer'): return d['studentFinalAnswer']
    state='remains unresolved pending the specified evidence' if d['resolutionStatus']=='unresolved' else 'is recorded as resolved within the stated scope'
    return f"{d['question']} The final register determination {state}. Refer to the evidence references and statement-effect summary for this decision."
def financial_details():
    # English presentation of existing final-package schedules and statements; no new calculation is made here.
    return {
      'schedules':[
        {'title':'Revenue / AR','rows':[['Four delivered contracts','Revenue €600,000; cash €487,000; gross AR €113,000','Confirmed for the four contracts; not complete company AR'],['Web cohort','Revenue €360,000 candidate; cash €287,000; gross AR €73,000 candidate','Delivery, settlement and full AR not confirmed'],['September deposits','€90,000 contract liabilities; revenue €0','Recognise once only'],['R-17 allowance','€18,000 specific allowance','Total closing allowance not determinable'],['All customer receipts','€899,000','Bank receipts only; not a complete revenue conclusion']]},
        {'title':'Inventory / COGS','rows':[['Opening inventory','€80,000','Warehouse-document value; not a complete opening balance'],['Materials received','€459,000','Recorded purchases'],['Physical COGS','€405,000 candidate','Conflicts with count; not final'],['Net inventory: movement / count','€112,000 candidate / €121,000 candidate','€9,000 unresolved gap'],['Damaged stock','€22,000 write-off','Recognised once only'],['Future disposal','€2,000 estimate','No recognised amount is supported']]},
        {'title':'Payroll','rows':[['Events','Expense €80,000; cash €75,000; current-period unpaid €5,000','Direct service COGS; not a full closing departmental payable'],['Sales','Expense €72,000; cash €68,000; unpaid €4,000','Selling Opex'],['Office / finance','Expense €96,000; cash €88,000; unpaid €8,000','Administrative Opex'],['Total','Expense €248,000; cash €231,000; current-period increase €17,000','Known payroll schedule; final total payable is qualified']]},
        {'title':'Opex','rows':[['Sales and office payroll','Cash €156,000; expense €168,000','Known payroll classification'],['Rent, marketing, software and utilities','Amounts recorded in the final package','Period expense and accrual completeness not confirmed'],['Insurance','Not determinable','No supported final expense or prepayment amount'],['Owner-related payments','€110,000 cash','Classification unresolved; not business expense by default']]},
        {'title':'PPE / Depreciation','rows':[['PPE cost','€260,000','Recorded cost'],['Packaging machine and photo booth','€60,000 and €20,000','Capitalised; depreciation begins when available for use'],['Repair','€10,000','Period repair expense, not PPE'],['Accumulated depreciation','Opening €45,000 plus undetermined current period','Final accumulated depreciation and net PPE not determinable'],['Candidate depreciation','€24,000 candidate','Not asserted as final']]},
        {'title':'Debt / Interest','rows':[['Loan principal','€131,000','Maturity split not known'],['Interest payable','€2,000','Confirmed current-period amount'],['Interest expense less cash paid','€2,000; difference €0','Full interest roll-forward remains qualified'],['New borrowing','€50,000','Loan liability and financing inflow, not revenue']]},
        {'title':'Equity / Distributions','rows':[['Owner-related cash','€110,000','Distribution versus recoverable owner balance unresolved'],['Opening equity','Not determinable','No independent opening equity roll-forward'],['Current profit','Not confirmed','No final profit conclusion'],['Closing equity','Not determinable','Not derived as a balancing residual']]}
      ],
      'statements':[
        {'title':'Profit and Loss','rows':[['Revenue','Not confirmed','€600,000 is confirmed for four contracts; broader CRM revenue is candidate only'],['Physical COGS','€405,000 candidate','Conflicts with inventory count'],['Direct service payroll','€80,000','Known classification'],['Opex payroll','€168,000','Known classification'],['Depreciation','Not determinable','€24,000 remains a candidate only'],['Profit','Not confirmed','No final profit or management-profit substitute is asserted']]},
        {'title':'Balance Sheet','rows':[['Cash','€60,000','Agrees to bank within the stated scope'],['Gross AR / allowance / net AR','Not determinable','€113,000 for four contracts; €186,000 / €168,000 are cohort candidates only'],['Inventory','Not determinable','€121,000 count versus €112,000 movement; €9,000 gap'],['PPE cost','€260,000','Accumulated depreciation and net PPE not determinable'],['Known listed liabilities','€406,000','Trade AP €126,000; payroll €32,000; contract liabilities €90,000; loan €131,000; interest €2,000; provision €25,000. Not complete liabilities'],['Equity','Not determinable','Opening equity, profit and distributions are not confirmed']]},
        {'title':'Cash Flow','rows':[['Opening cash','€80,000','Bank opening balance'],['Closing cash','€60,000','Bank confirmation within stated scope'],['Net change','€(20,000)','Reconciles to bank net change'],['Known owner cash','€(110,000)','Cash is known; classification remains unresolved'],['Cash flow conclusion','Preliminary / qualified','No complete category split is asserted']]}
      ],
      'reconciliations':[
        {'id':'R1','status':'NOT VERIFIABLE','calculation':'Assets − liabilities − equity: not determinable. Listed liabilities total €406,000, but this is not complete liabilities.','scope':'Known listed balances only.','limitation':'AR, inventory, depreciation, insurance, owner recovery and equity are not complete; unknown is not zero.'},
        {'id':'R2','status':'PASS (CSV + confirmation)','calculation':'€80,000 + €949,000 − €969,000 = €60,000; difference €0.','scope':'Bank account and confirmation scope.','limitation':'€110,000 owner cash classification keeps full cash-flow categorisation qualified.'},
        {'id':'R3','status':'PARTIAL','calculation':'Four delivered contracts reconcile to €0; the CRM cohort arithmetic also reconciles but is not fully recognised.','scope':'Four contracts and stated CRM cohort.','limitation':'Full AR and web-revenue completeness are not determinable.'},
        {'id':'R4','status':'FAIL','calculation':'Net count €121,000 − net movement €112,000 = €9,000.','scope':'Warehouse count, recorded purchases and candidate physical COGS.','limitation':'Cause and correcting entry are unresolved; no balancing entry is made.'},
        {'id':'R5','status':'PARTIAL','calculation':'PPE cost-register difference €0.','scope':'Recorded PPE cost.','limitation':'Accumulated depreciation and net PPE are not determinable.'},
        {'id':'R6','status':'PARTIAL','calculation':'Principal difference €0; interest expense less cash paid = €2,000, difference €0.','scope':'Known principal and current-period interest.','limitation':'Full interest roll-forward is not determinable.'},
        {'id':'R7','status':'NOT VERIFIABLE','calculation':'Opening equity, profit, distributions and other movements are not determinable.','scope':'No complete equity roll-forward.','limitation':'Closing equity and the balance-sheet difference cannot be calculated.'}
      ]
    }
def build():
    final=json.loads((ROOT/'submission.json').read_text(encoding='utf-8')); reg=json.loads((ROOT/'DECISION_REGISTER.json').read_text(encoding='utf-8')); schema=json.loads(SCHEMA.read_text(encoding='utf-8'))
    check_supported(schema); errors=validate(final,schema)
    if errors: raise ValueError(json.dumps(errors,ensure_ascii=False))
    assert len(final['decisions'])==100 and sum(x['reviewTier']=='material_judgment' for x in final['decisions'])==25
    decisions=[]
    for d in final['decisions']:
        resolved='supports the recorded determination' if d['resolutionStatus']=='resolved' else 'remains subject to the recorded unresolved qualification'
        decisions.append({'id':d['id'],'question':d['question'],'outcome':outcome(d),'confidence':d['confidence'],'resolutionStatus':d['resolutionStatus'],'reviewTier':d['reviewTier'],'statementEffect':d.get('statementEffect'),'aPosition':'Recorded Position A '+resolved+'.','bPosition':'Recorded Position B '+resolved+'.','guidedConfirmation':d.get('studentFinalAnswer'),'disagreement':d.get('originalA',{}).get('confidence')!=d.get('originalB',{}).get('confidence') or d.get('originalA',{}).get('statementEffect')!=d.get('originalB',{}).get('statementEffect'),'evidence':[ref(e) for e in d['primaryEvidence']],'guidedStatus':d.get('guidedReview',{}).get('sourceStatusVerbatim')})
    evidence=[{'filename':s['name'],'documentType':s['name'].rsplit('.',1)[-1].upper(),'checksumReference':'SHA-256 '+s['sha256'][:16]+'…','bytes':s['bytes']} for s in reg['sourceVerification']['sources'] if s['name'] not in METHOD]
    data={'case':{'id':final['caseId'],'company':'Divorce Party International Ltd.','period':'1 January – 31 August 2026','status':'PRELIMINARY / QUALIFIED','currency':'EUR','guidedDisclosure':'Guided review records confirmations in an educational workflow. It does not assert independent source verification or a no-AI review.','displayDisclosure':'This English report display is a presentation layer. The completed submission.json remains the canonical register package.'},'metrics':{'decisions':100,'material':25,'unresolved':30,'inventoryGap':9000},'executiveConclusion':'A €9,000 inventory gap remains unresolved across 30 decisions. Final profit and equity are not confirmed.','decisions':decisions,'featuredIds':[d['id'] for d in decisions if d['reviewTier']=='material_judgment' and (d['confidence']=='low' or d['resolutionStatus']=='unresolved')],'financial':financial_details(),'boardRecommendation':'Approve corrective actions and qualification disclosures, but do not use the current accounts as a final valuation or earn-out basis.','evidence':evidence,'methodology':[{'filename':n,'documentType':'JSON','checksumReference':'SHA-256 '+sha(ROOT/'tmp/stage4_sources'/n)[:16]+'…'} for n in METHOD],'validation':{'schemaValid':True,'schema':SCHEMA.name,'finalPackage':'submission.json','errorCount':0}}
    if DIST.exists(): shutil.rmtree(DIST)
    (DIST/'review').mkdir(parents=True); dump(DIST/'site-data.json',data)
    for n in ['index.html','app.js','styles.css','favicon.svg']: shutil.copyfile(HERE/n,DIST/n)
    shutil.copyfile(HERE/'index.html',DIST/'review'/'index.html'); dump(HERE/'schema-validation.json',data['validation']); dump(HERE/'build-manifest.json',{'finalPackage':'submission.json','schemaValid':True,'schemaErrorCount':0,'routes':['/','/review/'],'publicData':'site-data.json'})
    print(json.dumps({'build':'PASS','decisions':100,'material':25,'schemaErrors':0,'finalPackage':'submission.json'}))
if __name__=='__main__': build()
