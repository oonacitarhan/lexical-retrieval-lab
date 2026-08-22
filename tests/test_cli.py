import subprocess,sys
def test_help():
    result=subprocess.run([sys.executable,'-m','lexrank','--help'],text=True,capture_output=True)
    assert result.returncode==0 and 'usage:' in result.stdout
def test_cli_rejects_unknown_argument():
    result=subprocess.run([sys.executable,'-m','lexrank','--unknown-option'],text=True,capture_output=True)
    assert result.returncode!=0

def test_documented_workflow():
    import json
    result=subprocess.run([sys.executable,'-m','lexrank',*['examples/corpus.json','quantum photons']],text=True,capture_output=True)
    assert result.returncode==0, result.stderr
    data=json.loads(result.stdout)
    assert data[0]['id']=='quantum' and data[0]['score']>0
