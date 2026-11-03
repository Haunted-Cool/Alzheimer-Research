"""Finish sensitivity verification without modifying earlier analysis outputs.

Independently rebuild the common sample with indexed intersections and use QR
matrix calculations (no statsmodels fit) to verify saved sensitivity estimates.
No new outcome tests, model selection, exclusions, or publication claims.
"""
from pathlib import Path
import argparse, hashlib, json, platform
import numpy as np
import pandas as pd
from scipy import stats
from pypdf import PdfReader

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def qr_estimates(x,y):
    n,p=x.shape
    if np.linalg.matrix_rank(x)!=p:raise ValueError('Rank deficiency')
    q,r=np.linalg.qr(x,mode='reduced')
    rinv=np.linalg.solve(r,np.eye(p))
    beta=np.linalg.solve(r,q.T@y)
    residual=y-x@beta;h=(q*q).sum(axis=1)
    if (h>=1).any():raise ValueError('Unit leverage')
    variance=(residual/(1-h))**2
    covariance=rinv@(q.T@(variance[:,None]*q))@rinv.T
    se=np.sqrt(np.diag(covariance));crit=stats.t.ppf(.975,n-p)
    classical=np.sqrt(np.diag(rinv@rinv.T)*(residual@residual)/(n-p))
    return beta,np.column_stack([beta-crit*se,beta+crit*se]),classical

def main(data_dir,out):
    if out.exists():raise ValueError('Use a new output directory; existing evidence is preserved')
    old_files=[p for folder in ['results','repeat'] for p in (HERE/folder).iterdir() if p.is_file()]
    old_files += [HERE/n for n in ['plan.json','run.py','verification.json','verify_and_report.py','Exploratory_Regional_Results_and_Methods.md']]
    before={str(p.relative_to(HERE)):sha(p) for p in old_files}
    saved=json.loads((HERE/'verification.json').read_text())
    state=json.loads((HERE/'results/run_status.json').read_text())
    assert sha(HERE/'plan.json')==state['plan_sha256']
    assert sha(HERE/'run.py')==state['code_sha256']
    repeats=[]
    for item in saved['comparisons']:
        f=HERE/'results'/item['file'];g=HERE/'repeat'/item['file']
        assert sha(f)==item['sha256']
        if f.suffix=='.pdf':
            a,b=PdfReader(f),PdfReader(g)
            assert len(a.pages)==len(b.pages)==136
            assert all(x.extract_text()==y.extract_text() for x,y in zip(a.pages,b.pages))
        else:assert f.read_bytes()==g.read_bytes()
        repeats.append({'file':item['file'],'verified':True,'comparison':item['comparison']})
    manifest=pd.read_csv(HERE/'results/input_manifest.csv')
    frames={}
    for row in manifest.itertuples():
        file=data_dir/row.file
        assert sha(file)==row.sha256
        frame=pd.read_csv(file,dtype={'adrc_id':'string'}).set_index('adrc_id',verify_integrity=True)
        if frame.index.isna().any():raise ValueError('Missing ID')
        frames[Path(row.file).stem]=frame
    common=sorted(set.intersection(*(set(x.index) for x in frames.values())))
    demo=frames['demographics_diagnosis'].loc[common]
    blood=frames['biomarkers'].loc[common]
    amy=frames['imaging_amyloid'].loc[common];tau=frames['imaging_tau'].loc[common]
    regions=sorted(c for c in amy if c.startswith(('Mean.ctx-lh-','Mean.ctx-rh-')))
    assert len(regions)==68 and all(c in tau for c in regions)
    sex=demo.sex.map({'female':0.,'male':1.})
    finite=np.isfinite(np.column_stack([blood[['GFAP','NFL']],demo[['age_at_visit','sex_orth_male','sex_orth_female']],sex,amy[regions],tau[regions]])).all(axis=1)
    assert finite.all() and len(common)==165
    age=(demo.age_at_visit-demo.age_at_visit.mean())/demo.age_at_visit.std(ddof=1)
    scales=pd.read_csv(HERE/'results/scaling.csv').set_index('field')
    for c,values in [('age_at_visit',demo.age_at_visit)]+[(p+'__'+c,f[c]) for p,f in [('amy',amy),('tau',tau)] for c in regions]:
        np.testing.assert_allclose([values.mean(),values.std(ddof=1)],scales.loc[c,['mean','sd']].to_numpy(float),rtol=1e-12,atol=1e-12)
    sensitivities=pd.read_csv(HERE/'results/sensitivities.csv').set_index(['region','outcome','predictor'])
    main_results=pd.read_csv(HERE/'results/regional_results.csv')
    checks=[]
    for region in regions:
        za=(amy[region]-amy[region].mean())/amy[region].std(ddof=1)
        zt=(tau[region]-tau[region].mean())/tau[region].std(ddof=1)
        x=np.column_stack([np.ones(165),za,zt,age,sex])
        variants={'quadratic_age':np.column_stack([x,age**2]),
                  'numeric_sex_contrast':np.column_stack([x[:,:4],demo.sex_orth_male])}
        for outcome in ['GFAP','NFL']:
            y=blood[outcome].to_numpy()
            _,_,classical=qr_estimates(x,y)
            for j,predictor in [(1,'amyloid'),(2,'tau')]:
                stored=sensitivities.loc[(region.removeprefix('Mean.'),outcome,predictor)]
                np.testing.assert_allclose(classical[j],stored.conventional_se,rtol=1e-9,atol=1e-10)
            for name,xv in variants.items():
                beta,ci,_=qr_estimates(xv,y)
                for j,predictor in [(1,'amyloid'),(2,'tau')]:
                    stored=sensitivities.loc[(region.removeprefix('Mean.'),outcome,predictor)]
                    expected=stored[[name+'_beta',name+'_ci_low',name+'_ci_high']].to_numpy(float)
                    observed=np.r_[beta[j],ci[j]]
                    np.testing.assert_allclose(observed,expected,rtol=1e-8,atol=1e-9)
                    checks.append(dict(region=region.removeprefix('Mean.'),outcome=outcome,predictor=predictor,
                        variant=name,max_abs_discrepancy=float(abs(observed-expected).max()),verified=True))
    # Summaries describe all stored sensitivity results; no alternate p-value search.
    merged=main_results.merge(sensitivities.reset_index(),on=['region','outcome','predictor'],validate='one_to_one')
    for outcome in ['GFAP','NFL']:
        mask=merged.outcome==outcome;ysd=blood[outcome].std(ddof=1)
        for name in ['quadratic_age','numeric_sex_contrast']:
            merged.loc[mask,name+'_standardized_change']=(merged.loc[mask,name+'_beta']-merged.loc[mask,'beta'])/ysd
        merged.loc[mask,'leave_one_out_max_standardized_change']=np.maximum(abs(merged.loc[mask,'leave_one_out_min']-merged.loc[mask,'beta']),abs(merged.loc[mask,'leave_one_out_max']-merged.loc[mask,'beta']))/ysd
    merged['HC3_to_conventional_SE_ratio']=merged.HC3_se/merged.conventional_se
    rows=[]
    for scope,g in [('all_272',merged),('base_Holm_pass_50',merged.loc[merged.passes_Holm_0_05])]:
        for (outcome,predictor),sub in g.groupby(['outcome','predictor']):
            row=dict(scope=scope,outcome=outcome,predictor=predictor,n_tests=len(sub))
            for name in ['quadratic_age','numeric_sex_contrast']:
                delta=abs(sub[name+'_standardized_change'])
                relative=abs((sub[name+'_beta']-sub.beta)/sub.beta)*100
                row.update({name+'_sign_reversals':int((sub.beta*sub[name+'_beta']<0).sum()),
                    name+'_median_abs_standardized_change':float(delta.median()),name+'_max_abs_standardized_change':float(delta.max()),
                    name+'_median_abs_percent_change':float(relative.median()),name+'_max_abs_percent_change':float(relative.max())})
            row.update(loo_ranges_crossing_zero=int(((sub.leave_one_out_min<=0)&(sub.leave_one_out_max>=0)).sum()),
                loo_max_abs_standardized_change=float(sub.leave_one_out_max_standardized_change.max()),
                SE_ratio_min=float(sub.HC3_to_conventional_SE_ratio.min()),SE_ratio_max=float(sub.HC3_to_conventional_SE_ratio.max()))
            rows.append(row)
    diag=pd.read_csv(HERE/'results/diagnostics.csv')
    overview=[]
    for (outcome,predictor),g in main_results.groupby(['outcome','predictor']):
        overview.append(dict(outcome=outcome,predictor=predictor,tests=len(g),Holm_passes=int(g.passes_Holm_0_05.sum()),
            standardized_beta_min=float(g.standardized_beta.min()),standardized_beta_max=float(g.standardized_beta.max()),
            Holm_p_min=float(g.p_Holm_272.min()),Holm_p_max=float(g.p_Holm_272.max())))
    for p in old_files:assert sha(p)==before[str(p.relative_to(HERE))]
    out.mkdir(parents=True)
    pd.DataFrame(checks).to_csv(out/'independent_sensitivity_checks.csv',index=False)
    pd.DataFrame(rows).to_csv(out/'sensitivity_summary.csv',index=False)
    merged.to_csv(out/'all_tests_with_sensitivity_changes.csv',index=False)
    pd.DataFrame(overview).to_csv(out/'main_results_summary.csv',index=False)
    pd.DataFrame([dict(region=row.region,outcome=row.outcome,page_number=i+1,max_abs_studentized_residual=row.max_abs_studentized_residual,
        max_leverage=row.max_leverage,cooks_flag_count=row.cooks_flag_count) for i,row in enumerate(diag.itertuples())]).to_csv(out/'diagnostic_page_index.csv',index=False)
    summary=dict(status='PASS',date_local='2026-11-02',purpose='Complete independent sensitivity verification; no new hypothesis tests',
        original_artifacts_unchanged=True,baseline_sha256=before,repeated_outputs=repeats,
        source_files_checked=len(frames),common_sample_independently_rebuilt=165,scaling_fields_verified=len(scales),
        sensitivity_models_verified=272,sensitivity_coefficients_and_intervals_verified=len(checks),
        max_sensitivity_numeric_discrepancy=max(c['max_abs_discrepancy'] for c in checks),conventional_SE_checks=272,
        previous_leave_one_out_evaluations_verified_in_original_run=22440,
        script_sha256=sha(Path(__file__)),python=platform.python_version())
    (out/'completion_verification.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ['baseline_sha256','repeated_outputs']},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();main(args.data_dir,args.output)
