import argparse,json
from .core import Index
from .features import load,evaluate
def main():
    parser=argparse.ArgumentParser(description='Retrieve ranked passages or evaluate a labeled query set')
    parser.add_argument('corpus');parser.add_argument('query',nargs='?',default='quantum');parser.add_argument('--top',type=int,default=3);parser.add_argument('--evaluate')
    args=parser.parse_args()
    try:
        index=Index(load(args.corpus))
        if args.evaluate:
            with open(args.evaluate) as f:result=evaluate(index,json.load(f),args.top)
        else:result=[{'id':key,'score':score,'text':text} for key,score,text in index.search(args.query,args.top)]
        print(json.dumps(result,indent=2))
    except (ValueError,KeyError,OSError,TypeError) as error:parser.error(str(error))
