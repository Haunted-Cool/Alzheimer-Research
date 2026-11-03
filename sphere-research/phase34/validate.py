"""Independent numerical checks using an artificial fixture, never SPHERE rows."""
from pathlib import Path
import json, tempfile, subprocess, sys, os
import numpy as np
import pandas as pd
from scipy import stats
from analysis import fit_models, sensitivities, read_table, validate_matrix

def main():
    rng=np.random.default_rng(20261102)
    n=240
    d=pd.DataFrame(dict(amyloid=rng.normal(size=n),tau=rng.normal(size=n),age=rng.normal(70,9,n),sex=rng.integers(0,2,n)))
    d['GFAP']=10+2*d.amyloid-1.5*d.tau+.3*d.age+d.sex+rng.normal(size=n)*(1+abs(d.amyloid))
    d['NFL']=3-.4*d.amyloid+1.2*d.tau+.2*d.age+.5*d.sex+rng.normal(size=n)
    result,diag,models=fit_models(d)
    errors=[]
    for y,(ordinary,rob,Xdf) in models.items():
        X=Xdf.to_numpy(); Y=d[y].to_numpy()
        inv=np.linalg.inv(X.T@X)
        beta=np.linalg.lstsq(X,Y,rcond=None)[0]
        residual=Y-X@beta
        h=np.einsum('ij,jk,ik->i',X,inv,X)
        cov=inv@(X.T@(((residual/(1-h))**2)[:,None]*X))@inv
        se=np.sqrt(np.diag(cov));df=n-X.shape[1]
        p=2*stats.t.sf(abs(beta/se),df)
        ci=np.column_stack([beta-stats.t.ppf(.975,df)*se,beta+stats.t.ppf(.975,df)*se])
        for name,a,b in [('beta',beta,rob.params),('HC3_covariance',cov,rob.cov_params()),('p',p,rob.pvalues),('CI',ci,rob.conf_int())]:
            np.testing.assert_allclose(a,b,rtol=1e-9,atol=1e-10)
            errors.append(dict(outcome=y,quantity=name,max_abs_error=float(np.max(np.abs(a-b)))))
    p=result.loc[1:3,'p_raw'].to_numpy();order=np.argsort(p)
    manual=np.empty(3);manual[order]=np.minimum(1,np.maximum.accumulate(p[order]*np.arange(3,0,-1)))
    np.testing.assert_allclose(manual,result.loc[1:3,'p_secondary_Holm'])
    # Nontrivial hand-worked Holm example catches all-zero/very-small p pitfalls.
    from statsmodels.stats.multitest import multipletests
    np.testing.assert_allclose(multipletests([.03,.01,.04],method='holm')[1],[.06,.03,.06])
    shuffled=fit_models(d.sample(frac=1,random_state=19))[0]
    pd.testing.assert_frame_equal(result,shuffled,check_exact=False,rtol=1e-9,atol=1e-10)
    for failure in ['missing','infinite','collinear','constant']:
        bad=d.copy()
        if failure=='missing':bad.loc[0,'GFAP']=np.nan
        if failure=='infinite':bad.loc[0,'tau']=np.inf
        if failure=='collinear':bad['tau']=bad.amyloid
        if failure=='constant':bad['sex']=1
        try:validate_matrix(bad)
        except ValueError:pass
        else:raise AssertionError(f'{failure} accepted')
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/'invalid.csv'
        for txt in ['adrc_id,x\na,1\na,2\n','adrc_id,x\n,1\n','adrc_id,x\n a,1\n','adrc_id,x,x\na,1,2\n']:
            path.write_text(txt)
            try:read_table(path)
            except ValueError:pass
            else:raise AssertionError('Invalid key/header accepted')
    sensitivity=sensitivities(d)
    assert len(sensitivity)==4 and np.isfinite(sensitivity.select_dtypes('number')).all().all()
    # Exercise the user-facing command with artificial data and its unresolved gate.
    base=Path(__file__).parent
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp)
        fixture=d.copy();fixture.insert(0,'adrc_id',[f'fixture_{i}' for i in range(n)])
        fixture.to_csv(root/'fixture.csv',index=False)
        cmd=[sys.executable,str(base/'run_models.py'),'--prepared-data',str(root/'fixture.csv'),
             '--protocol',str(base/'protocol.json'),'--output',str(root/'models')]
        blocked=subprocess.run(cmd,capture_output=True,text=True)
        assert blocked.returncode!=0 and 'unresolved definitions' in blocked.stderr
        contract=json.loads((base/'protocol.json').read_text())
        contract['measurement_contract']={k:'Artificial fixture for software validation only' for k in contract['measurement_contract']}
        (root/'fixture_protocol.json').write_text(json.dumps(contract))
        cmd[cmd.index('--protocol')+1]=str(root/'fixture_protocol.json')
        env=os.environ.copy();env['MPLCONFIGDIR']=str(root/'mpl')
        smoke=subprocess.run(cmd,capture_output=True,text=True,env=env)
        assert smoke.returncode==0,smoke.stderr
        assert (root/'models'/'GFAP_diagnostics.png').exists()
        pd.testing.assert_frame_equal(pd.read_csv(root/'models'/'hypothesis_results.csv'),result,check_exact=False,rtol=1e-8,atol=1e-10)
    out=Path(__file__).parent/'verification';out.mkdir(exist_ok=True)
    result.to_csv(out/'artificial_fixture_results.csv',index=False)
    sensitivity.to_csv(out/'artificial_fixture_sensitivities.csv',index=False)
    (out/'numerical_validation.json').write_text(json.dumps(dict(status='PASS',data='Artificial fixture, not SPHERE',
        seed=20261102,n=n,comparisons=errors,checks=['Independent least-squares coefficients','Independent HC3 sandwich',
        'Student-t p-values and confidence intervals','Hand-calculated Holm example','Row-order invariance',
        'Missing/nonfinite/rank/constant rejection','Invalid key and duplicate header rejection',
        'Quadratic-age and all-row leave-one-out sensitivity execution',
        'Unresolved protocol rejects hypothesis run','Full command smoke test on artificial fixture']),indent=2)+'\n')
    print('PASS: independent numerical validation and invalid-input tests; artificial fixture only')

if __name__=='__main__':main()
