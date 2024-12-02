"""Small BM25 retrieval baseline. Retrieval only: no LLM or generated answers."""
import math,re
from collections import Counter

def tokenize(text): return re.findall(r'[a-z0-9]+',text.lower())

class Index:
    def __init__(self,documents,k1=1.5,b=.75):
        if not documents or k1<=0 or not 0<=b<=1:
            raise ValueError('need documents, k1>0 and b in [0,1]')
        self.documents=dict(documents)
        self.counts={key:Counter(tokenize(text)) for key,text in documents.items()}
        self.lengths={key:sum(count.values()) for key,count in self.counts.items()}
        self.average=sum(self.lengths.values())/len(documents) or 1
        self.df=Counter(term for count in self.counts.values() for term in count)
        self.k1,self.b=k1,b

    def search(self,query,limit=3):
        if limit<0: raise ValueError('limit must be nonnegative')
        scores=[]
        for key,count in self.counts.items():
            score=0
            for term in set(tokenize(query)):
                tf=count[term]
                if tf:
                    df=self.df[term]
                    idf=math.log(1+(len(self.counts)-df+.5)/(df+.5))
                    norm=tf+self.k1*(1-self.b+self.b*self.lengths[key]/self.average)
                    score += idf*tf*(self.k1+1)/norm
            if score>0: scores.append((key,score,self.documents[key]))
        return sorted(scores,key=lambda item:(-item[1],item[0]))[:limit]

def self_test():
    docs={'quantum':'Quantum entanglement correlates two qubits.',
          'ai':'Neural networks learn parameters with gradient descent.',
          'systems':'A priority queue schedules experiments.'}
    index=Index(docs)
    assert index.search('entanglement')[0][0]=='quantum'
    assert index.search('gradient neural')[0][0]=='ai'
    assert index.search('unseenword')==[]
    assert index.search('quantum',0)==[]
    assert Index({'empty':''}).search('anything')==[]
    return index.search('quantum qubits')

if __name__=='__main__':
    for key,score,text in self_test(): print(f'[{key}] {score:.3f}: {text}')
    print('Self-tests passed')
