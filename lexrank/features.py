import json
from .core import Index,tokenize

def chunk(text,words=80,overlap=16):
    if words<1 or overlap<0 or overlap>=words:raise ValueError('need 0<=overlap<words')
    tokens=text.split();out=[]
    for start in range(0,len(tokens),words-overlap):
        out.append(' '.join(tokens[start:start+words]))
        if start+words>=len(tokens):break
    return out

def passages(documents,words=80,overlap=16):
    return {f'{key}:{i}':part for key,text in documents.items() for i,part in enumerate(chunk(text,words,overlap))}

def save(documents,path):
    with open(path,'w') as f:json.dump(documents,f,indent=2,sort_keys=True)

def load(path):
    with open(path) as f:docs=json.load(f)
    if not isinstance(docs,dict) or not all(isinstance(k,str) and isinstance(v,str) for k,v in docs.items()):raise ValueError('expected document-id to text mapping')
    return docs

def evaluate(index,queries,k=3):
    if not queries or k<1:raise ValueError('queries and positive k required')
    reciprocal=[];recalls=[]
    for query in queries:
        relevant=set(query['relevant'])
        if not relevant:raise ValueError('each query needs relevance labels')
        ids=[row[0] for row in index.search(query['query'],k)]
        reciprocal.append(next((1/(i+1) for i,key in enumerate(ids) if key in relevant),0))
        recalls.append(len(set(ids)&relevant)/len(relevant))
    return {'mrr':sum(reciprocal)/len(queries),'recall_at_k':sum(recalls)/len(queries),'k':k}
