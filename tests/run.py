import importlib,inspect,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
count=0
for file in sorted(Path(__file__).parent.glob('test_*.py')):
    module=importlib.import_module('tests.'+file.stem)
    for name,function in inspect.getmembers(module,inspect.isfunction):
        if name.startswith('test_'):
            function();count+=1;print('PASS '+file.stem+'.'+name)
print(str(count)+' tests passed')
