"""Dependency-free validator for every keyword used in the supplied case schema.

Fail closed on unsupported keywords. This is not a general Draft 2020-12 engine.
The delivered schema uses no references or unevaluated/dynamic keywords.
"""
import re

SUPPORTED={'$schema','title','type','required','properties','const','enum','minItems','maxItems','items','pattern','minLength','additionalProperties','allOf','if','then'}
def check_supported(schema):
    unknown=set(schema)-SUPPORTED
    if unknown:raise ValueError('Unsupported schema keywords: '+', '.join(sorted(unknown)))
    for sub in schema.get('properties',{}).values():check_supported(sub)
    for key in ['items','if','then']:
        if isinstance(schema.get(key),dict):check_supported(schema[key])
    for sub in schema.get('allOf',[]):check_supported(sub)

def validate(value,schema,path='$'):
    errors=[]
    def fail(rule,message):errors.append({'path':path,'rule':rule,'message':message})
    types={'object':lambda x:isinstance(x,dict),'array':lambda x:isinstance(x,list),'string':lambda x:isinstance(x,str),'number':lambda x:isinstance(x,(int,float)) and not isinstance(x,bool),'boolean':lambda x:isinstance(x,bool),'null':lambda x:x is None}
    required_type=schema.get('type')
    if required_type:
        names=required_type if isinstance(required_type,list) else [required_type]
        if not any(types[t](value) for t in names):fail('type','Expected '+str(required_type));return errors
    if 'const' in schema and (value!=schema['const'] or type(value)!=type(schema['const'])):fail('const','Value differs from constant')
    if 'enum' in schema and not any(value==v and type(value)==type(v) for v in schema['enum']):fail('enum','Value not in enum')
    if isinstance(value,dict):
        for k in schema.get('required',[]):
            if k not in value:errors.append({'path':path+'.'+k,'rule':'required','message':'Required property missing'})
        props=schema.get('properties',{})
        for k,v in value.items():
            if k in props:errors+=validate(v,props[k],path+'.'+k)
            elif schema.get('additionalProperties') is False:errors.append({'path':path+'.'+k,'rule':'additionalProperties','message':'Unexpected property'})
    if isinstance(value,list):
        if len(value)<schema.get('minItems',0):fail('minItems','Too few items')
        if len(value)>schema.get('maxItems',float('inf')):fail('maxItems','Too many items')
        if 'items' in schema:
            for i,v in enumerate(value):errors+=validate(v,schema['items'],f'{path}[{i}]')
    if isinstance(value,str):
        if len(value)<schema.get('minLength',0):fail('minLength','String too short')
        if 'pattern' in schema and not re.search(schema['pattern'],value):fail('pattern','Pattern mismatch')
    for sub in schema.get('allOf',[]):errors+=validate(value,sub,path)
    if 'if' in schema and not validate(value,schema['if'],path) and 'then' in schema:errors+=validate(value,schema['then'],path)
    return errors
