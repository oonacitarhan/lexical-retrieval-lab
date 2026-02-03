import tempfile
from pathlib import Path
from lexrank.core import Index
from lexrank.features import chunk,passages,save,load,evaluate
def test_chunk_overlap():
    assert chunk('a b c d e',3,1)==['a b c','c d e']
    assert chunk('',3,1)==[]
def test_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/'corpus.json';save({'a':'quantum optics'},path)
        assert load(path)=={'a':'quantum optics'}
def test_metrics():
    index=Index({'a':'quantum','b':'robot'})
    result=evaluate(index,[{'query':'quantum','relevant':['a']},{'query':'missing','relevant':['b']}],1)
    assert result['mrr']==.5 and result['recall_at_k']==.5
def test_bad_overlap():
    try:chunk('a b',2,2)
    except ValueError:return
    raise AssertionError('bad overlap accepted')
