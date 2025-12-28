from lexrank.core import *

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

def test_original_reference_cases():
    self_test()
