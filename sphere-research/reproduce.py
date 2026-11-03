"""Run in an isolated workspace; never overwrite checked-in reference outputs."""
from pathlib import Path
import argparse, hashlib, json, os, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_manifest():
    manifest=json.loads((ROOT/'REFERENCE_MANIFEST.json').read_text())
    for name,digest in manifest.items():
        if sha(ROOT/name)!=digest: raise ValueError('Reference changed: '+name)
    return len(manifest)
def run(args):
    if sys.flags.optimize: raise ValueError('Do not use python -O; assertions verify numerical results')
    checked=verify_manifest()
    if args.check_only:
        print(f'PASS: {checked} reference files verified');return
    target=args.output.resolve()
    if target.exists(): raise ValueError('Choose a new output directory; existing evidence is preserved')
    target.mkdir(parents=True);work=target/'workspace';work.mkdir()
    log=[]
    for name in ['phase34','phase4_results','chat10_final_results']:
        shutil.copytree(ROOT/name,work/name,ignore=shutil.ignore_patterns('__pycache__','.venv'))
    # Only remove disposable copies; the repository evidence remains untouched.
    for name in ['phase4_results/deliverables','chat10_final_results/deliverables']:
        shutil.rmtree(work/name)
    for p in (work/'chat10_final_results').glob('*.zip'):p.unlink()
    env=os.environ.copy();env['MPLCONFIGDIR']=str(target/'matplotlib_cache')
    def execute(script,*arguments):
        command=[sys.executable,str(work/script),*map(str,arguments)]
        result=subprocess.run(command,cwd=work,env=env,text=True,capture_output=True)
        log.append(dict(script=script,arguments=list(map(str,arguments)),exit_code=result.returncode,stdout=result.stdout,stderr=result.stderr))
        (target/'execution_log.json').write_text(json.dumps(log,indent=2)+'\n')
        if result.returncode:raise RuntimeError(f'{script} failed; see {target / "execution_log.json"}\n'+result.stderr)
        print('PASS:',script,flush=True)
    execute('phase34/validate.py')
    mode='reference_outputs_only'
    if args.data_dir:
        import numpy as np
        import pandas as pd
        from pypdf import PdfReader
        data=args.data_dir.resolve()
        manifest=pd.read_csv(ROOT/'phase34/regional_extension/results/input_manifest.csv')
        for row in manifest.itertuples():
            if sha(data/row.file)!=row.sha256:raise ValueError('Source file hash mismatch: '+row.file)
        regional=work/'phase34/regional_extension'
        for folder in ['results','repeat']:
            shutil.rmtree(regional/folder)
            execute('phase34/regional_extension/run.py','--data-dir',data,'--output',regional/folder)
        # Compare scientific outputs with the checked-in original execution.
        comparisons=[]
        for reference in sorted((ROOT/'phase34/regional_extension/results').glob('*.csv')):
            old=pd.read_csv(reference,float_precision='round_trip')
            new=pd.read_csv(regional/'results'/reference.name,float_precision='round_trip')
            pd.testing.assert_frame_equal(old,new,check_exact=False,rtol=1e-8,atol=1e-10)
            comparisons.append(dict(file=reference.name,status='PASS',comparison='numeric rtol=1e-8 atol=1e-10; labels/schema exact'))
        oldpdf=PdfReader(ROOT/'phase34/regional_extension/results/all_model_diagnostics.pdf')
        newpdf=PdfReader(regional/'results/all_model_diagnostics.pdf')
        assert len(oldpdf.pages)==len(newpdf.pages)==136
        assert all(a.extract_text()==b.extract_text() for a,b in zip(oldpdf.pages,newpdf.pages))
        (target/'model_reference_comparison.json').write_text(json.dumps(comparisons,indent=2)+'\n')
        execute('phase34/regional_extension/verify_and_report.py')
        completion=regional/'completion'
        docs={n:(completion/n).read_bytes() for n in ['Final_Verified_Results_Summary.md','Diagnostic_Review.md']}
        shutil.rmtree(completion)
        execute('phase34/regional_extension/complete_verification.py','--data-dir',data,'--output',completion)
        for name,content in docs.items():(completion/name).write_bytes(content)
        mode='fresh_models_compared_to_reference'
    execute('phase4_results/build_results.py','--output',work/'phase4_results/deliverables')
    execute('chat10_final_results/build_final_report.py')
    verify_manifest()
    final=work/'chat10_final_results/deliverables/Chat10_Final_Results_Report.html'
    summary=dict(status='PASS',mode=mode,reference_files_checked=checked,source_data_included=False,
        reference_files_unchanged=True,final_report=str(final),
        note='Graphical review notes are the prior reference review; this command does not perform a new visual review.')
    (target/'run_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir',type=Path,help='Authorized four-file SPHERE folder; omit for reference-only regeneration')
    p.add_argument('--output',type=Path,default=Path('runs/reproduction'),help='New directory for isolated reproduction')
    p.add_argument('--check-only',action='store_true',help='Check file fingerprints without third-party dependencies')
    run(p.parse_args())
