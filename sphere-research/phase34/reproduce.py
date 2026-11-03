"""Run actual audit twice in fresh processes and compare all aggregate artifacts."""
from pathlib import Path
import argparse, hashlib, importlib.metadata, json, os, subprocess, sys, tempfile
import pandas as pd

base=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);args=p.parse_args()
env=os.environ.copy();env['MPLCONFIGDIR']=str(base/'verification'/'matplotlib_cache')
log=[]
for dest in [base/'results',base/'verification'/'repeat']:
    cmd=[sys.executable,str(base/'analysis.py'),'--data-dir',str(args.data_dir),'--output',str(dest)]
    r=subprocess.run(cmd,capture_output=True,text=True,env=env)
    log.append({'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode:raise RuntimeError(r.stderr)
r=subprocess.run([sys.executable,str(base/'validate.py')],capture_output=True,text=True,env=env)
log.append({'command':'validate.py','exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
if r.returncode:raise RuntimeError(r.stderr)
checks=[]
for f in sorted((base/'results').iterdir()):
    other=base/'verification'/'repeat'/f.name
    assert f.read_bytes()==other.read_bytes(),f'Nonreproducible: {f.name}'
    checks.append({'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'byte_identical':True})
# Reconcile current local files to the prior attachment manifest; never count copies twice.
old=base.parent/'phase2'/'verification'/'input_manifest.json'
matches=[]
if old.exists():
    prior=json.loads(old.read_text()); current=pd.read_csv(base/'results'/'input_manifest.csv')
    for row in current.to_dict('records'):
        matching=[v['name'] for v in prior if v['sha256']==row['sha256']]
        matches.append({'file':row['file'],'matching_prior_attachment_names':matching})
    assert sum(bool(x['matching_prior_attachment_names']) for x in matches)==5
versions={n:importlib.metadata.version(n) for n in ['numpy','pandas','scipy','statsmodels','matplotlib','patsy','formulaic']}
(base/'requirements.txt').write_text(''.join(f'{k}=={v}\n' for k,v in versions.items()))
(base/'verification'/'reproduction.json').write_text(json.dumps({'status':'PASS','runs':log,'outputs':checks,
    'attachment_provenance':'Compared with prior attachment manifest, not a fresh retrieval of library-only CSVs',
    'attachment_matches':matches,'versions':versions},indent=2)+'\n')
print('PASS: two fresh-process data audits match byte-for-byte; independent numerical checks pass')
