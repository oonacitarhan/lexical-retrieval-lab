import sys,time,statistics,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from lexrank.features import *
durations=[]
for _ in range(5):
    start=time.perf_counter()
    Index({str(i):'quantum optics photon '+str(i) for i in range(100)}).search('photon optics',5)
    durations.append(time.perf_counter()-start)
print(json.dumps({'workload':"Index({str(i):'quantum optics photon '+str(i) for i in range(100)}).search('photon optics',5)",'repetitions':len(durations),'median_seconds':statistics.median(durations),'min_seconds':min(durations)}))
