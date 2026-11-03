"""Exploratory regional release associations. No raw or merged rows exported."""
from pathlib import Path
import argparse, hashlib, json, sys, platform
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from analysis import read_table, sha

HERE=Path(__file__).resolve().parent
def run(data,out):
    if out.exists() and any(out.iterdir()):raise ValueError('Use an empty output directory')
    out.mkdir(parents=True,exist_ok=True)
    plan=json.loads((HERE/'plan.json').read_text())
    names=['demographics_diagnosis','biomarkers','imaging_amyloid','imaging_tau']
    frames={k:read_table(data/(k+'.csv')) for k in names}
    a,t=frames['imaging_amyloid'],frames['imaging_tau']
    prefix=('Mean.ctx-lh-','Mean.ctx-rh-')
    ar={c for c in a if c.startswith(prefix)};tr={c for c in t if c.startswith(prefix)}
    if ar!=tr or len(ar)!=plan['expected_regions']:raise ValueError('Region schema differs from plan')
    regions=sorted(ar)
    d=frames['demographics_diagnosis'][['adrc_id','age_at_visit','sex','sex_orth_male','sex_orth_female']].copy()
    roster=set(d.adrc_id)
    if any(not set(f.adrc_id)<=roster for f in frames.values()):raise ValueError('Orphan keys')
    flow=[dict(stage='roster',n=len(d))]
    for key,subset in [('blood',frames['biomarkers'][['adrc_id','GFAP','NFL']]),
        ('amyloid',a[['adrc_id']+regions].rename(columns={c:'amy__'+c for c in regions})),
        ('tau',t[['adrc_id']+regions].rename(columns={c:'tau__'+c for c in regions}))]:
        d=d.merge(subset,on='adrc_id',how='inner',validate='one_to_one');flow.append(dict(stage=key,n=len(d)))
    if not set(d.sex.dropna()).issubset({'male','female'}):raise ValueError('Unexpected sex labels')
    d['sex_label']=d.sex.map({'female':0,'male':1})
    numeric=['GFAP','NFL','age_at_visit','sex_label','sex_orth_male','sex_orth_female']+['amy__'+c for c in regions]+['tau__'+c for c in regions]
    d[numeric]=d[numeric].apply(pd.to_numeric,errors='raise')
    good=np.isfinite(d[numeric].to_numpy()).all(axis=1)
    dropped=int((~good).sum());d=d.loc[good].sort_values('adrc_id').reset_index(drop=True)
    flow.append(dict(stage='common_finite',n=len(d)))
    if len(d)<=10:raise ValueError('Insufficient observations')
    if (d[numeric].std(ddof=1)==0).any():raise ValueError('Constant variable')
    z=d[numeric].copy();scaling=[]
    for c in ['age_at_visit']+['amy__'+r for r in regions]+['tau__'+r for r in regions]:
        mean,sd=d[c].mean(),d[c].std(ddof=1);z[c]=(d[c]-mean)/sd
        scaling.append(dict(field=c,mean=mean,sd=sd))
    results=[];diags=[];sens=[];checks=[];models=[]
    for region in regions:
        X=pd.DataFrame({'const':1.,'amyloid':z['amy__'+region],'tau':z['tau__'+region],
            'age':z.age_at_visit,'sex_label':z.sex_label})
        if np.linalg.matrix_rank(X)!=5:raise ValueError('Rank deficient '+region)
        for outcome in ['GFAP','NFL']:
            y=d[outcome].to_numpy();x=X.to_numpy();n,p=x.shape
            fit=sm.OLS(y,X,missing='raise').fit();rob=fit.get_robustcov_results(cov_type='HC3',use_t=True)
            inf=fit.get_influence();h=inf.hat_matrix_diag;resid=fit.resid.to_numpy()
            # Independent QR/least-squares coefficients, explicit HC3 covariance and tests.
            beta=np.linalg.lstsq(x,y,rcond=None)[0];inv=np.linalg.inv(x.T@x)
            independent_h=np.einsum('ij,jk,ik->i',x,inv,x)
            e=y-x@beta;cov=inv@(x.T@((e/(1-independent_h))[:,None]**2*x))@inv
            se=np.sqrt(np.diag(cov));manual_ci=np.column_stack((beta-stats.t.ppf(.975,n-p)*se,beta+stats.t.ppf(.975,n-p)*se))
            np.testing.assert_allclose(beta,rob.params,rtol=1e-8,atol=1e-9)
            np.testing.assert_allclose(cov,rob.cov_params(),rtol=1e-8,atol=1e-9)
            np.testing.assert_allclose(2*stats.t.sf(abs(beta/se),n-p),rob.pvalues,rtol=1e-8,atol=1e-10)
            np.testing.assert_allclose(manual_ci,rob.conf_int(),rtol=1e-8,atol=1e-9)
            checks.append(dict(region=region,outcome=outcome,beta_error=float(abs(beta-rob.params).max()),covariance_error=float(abs(cov-rob.cov_params()).max())))
            # Exact linear-model case-deletion formula; cross-check every deleted-row fit.
            loo=beta[None,:]-(x@inv)*(e/(1-independent_h))[:,None]
            for i in range(n):
                keep=np.arange(n)!=i
                b=np.linalg.lstsq(x[keep],y[keep],rcond=None)[0]
                if np.linalg.matrix_rank(x[keep])!=p:raise ValueError('Deletion loses rank')
                np.testing.assert_allclose(loo[i],b,rtol=1e-8,atol=1e-8)
            variants={}
            q=X.copy();q['age_squared']=q.age**2;variants['quadratic_age']=q
            s=X.drop(columns='sex_label').copy();s['sex_orth_male']=z.sex_orth_male;variants['numeric_sex_contrast']=s
            alternate={}
            for name,xv in variants.items():
                if np.linalg.matrix_rank(xv)!=xv.shape[1]:raise ValueError('Sensitivity rank failure')
                alternate[name]=sm.OLS(y,xv).fit(cov_type='HC3',use_t=True)
            for j,pred in [(1,'amyloid'),(2,'tau')]:
                reduced=sm.OLS(y,X.drop(columns=pred)).fit()
                partial=(reduced.ssr-fit.ssr)/reduced.ssr
                # Residual-correlation identity provides a separate partial-R2 check.
                xr=X.drop(columns=pred).to_numpy();yr=y-xr@np.linalg.lstsq(xr,y,rcond=None)[0]
                pr=X[pred].to_numpy()-xr@np.linalg.lstsq(xr,X[pred],rcond=None)[0]
                np.testing.assert_allclose(partial,np.corrcoef(yr,pr)[0,1]**2,atol=1e-10)
                ci=rob.conf_int()[j];ysd=d[outcome].std(ddof=1)
                results.append(dict(region=region.removeprefix('Mean.'),outcome=outcome,predictor=pred,n=n,beta=rob.params[j],se_HC3=rob.bse[j],
                    ci95_low=ci[0],ci95_high=ci[1],p_raw=rob.pvalues[j],standardized_beta=rob.params[j]/ysd,
                    standardized_ci95_low=ci[0]/ysd,standardized_ci95_high=ci[1]/ysd,partial_R2=partial))
                row=dict(region=region.removeprefix('Mean.'),outcome=outcome,predictor=pred,base_beta=rob.params[j],
                    leave_one_out_min=loo[:,j].min(),leave_one_out_max=loo[:,j].max(),conventional_se=fit.bse.iloc[j],HC3_se=rob.bse[j])
                for name,m in alternate.items():
                    row[name+'_beta']=m.params[pred];row[name+'_ci_low']=m.conf_int().loc[pred,0];row[name+'_ci_high']=m.conf_int().loc[pred,1]
                sens.append(row)
            diags.append(dict(region=region.removeprefix('Mean.'),outcome=outcome,n=n,df_resid=fit.df_resid,R2=fit.rsquared,
                PET_correlation=np.corrcoef(X.amyloid,X.tau)[0,1],VIF_amyloid=variance_inflation_factor(x,1),VIF_tau=variance_inflation_factor(x,2),
                max_leverage=h.max(),leverage_flag_count=int((h>2*p/n).sum()),cooks_flag_count=int((inf.cooks_distance[0]>4/n).sum()),
                max_abs_studentized_residual=abs(inf.resid_studentized_internal).max(),residual_skewness=stats.skew(resid,bias=False)))
            models.append((region,outcome,X,fit))
    r=pd.DataFrame(results);r['p_Holm_272']=multipletests(r.p_raw,method='holm')[1]
    order=np.argsort(r.p_raw.to_numpy());manual=np.empty(len(r));manual[order]=np.minimum(1,np.maximum.accumulate(r.p_raw.to_numpy()[order]*np.arange(len(r),0,-1)))
    np.testing.assert_allclose(manual,r.p_Holm_272,atol=1e-12)
    if len(r)!=272:raise ValueError('Unexpected test family')
    r['passes_Holm_0_05']=r.p_Holm_272<.05
    r.to_csv(out/'regional_results.csv',index=False);pd.DataFrame(sens).to_csv(out/'sensitivities.csv',index=False)
    pd.DataFrame(diags).to_csv(out/'diagnostics.csv',index=False);pd.DataFrame(checks).to_csv(out/'independent_numeric_checks.csv',index=False)
    pd.DataFrame(scaling).to_csv(out/'scaling.csv',index=False);pd.DataFrame(flow).to_csv(out/'sample_flow.csv',index=False)
    pd.DataFrame([dict(file=k+'.csv',sha256=sha(data/(k+'.csv')),rows=len(f)) for k,f in frames.items()]).to_csv(out/'input_manifest.csv',index=False)
    pd.DataFrame([dict(region=r,amyloid_source=r,tau_source=r) for r in regions]).to_csv(out/'field_mapping.csv',index=False)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    # Every model gets the same diagnostics, without selecting by p-value.
    with PdfPages(out/'all_model_diagnostics.pdf') as pdf:
        for region,outcome,X,fit in models:
            fig,axs=plt.subplots(1,3,figsize=(12,3.7),layout='constrained')
            axs[0].scatter(fit.fittedvalues,fit.resid,s=9);axs[0].axhline(0,color='grey');axs[0].set(xlabel='Fitted value',ylabel='Residual')
            stats.probplot(fit.resid,plot=axs[1]);axs[1].set_title('Residual Q-Q')
            axs[2].scatter(fit.get_influence().hat_matrix_diag,fit.resid,s=9);axs[2].set(xlabel='Leverage',ylabel='Residual')
            fig.suptitle('EXPLORATORY synthetic release: '+outcome+' / '+region)
            pdf.savefig(fig);plt.close(fig)
    # Fixed alphabetical panels: standardized slopes; no significance ranking.
    fig,axs=plt.subplots(1,4,figsize=(13,15),sharey=True,layout='constrained')
    for ax,(outcome,pred) in zip(axs,[(y,p) for y in ['GFAP','NFL'] for p in ['amyloid','tau']]):
        sub=r[(r.outcome==outcome)&(r.predictor==pred)].sort_values('region');yy=np.arange(len(sub))
        ax.errorbar(sub.standardized_beta,yy,xerr=np.vstack([sub.standardized_beta-sub.standardized_ci95_low,sub.standardized_ci95_high-sub.standardized_beta]),fmt='.',ms=4,lw=.5,color='#246780')
        ax.axvline(0,color='grey',lw=.7);ax.set(title=outcome+' / '+pred,xlabel='Standardized slope; marginal 95% CI');ax.set_yticks(yy,sub.region,fontsize=6)
    axs[0].invert_yaxis();fig.suptitle('Exploratory associations in released synthetic fields\nSame-region mutual PET adjustment, age, readable sex label; clinical normalization unresolved')
    fig.savefig(out/'regional_effects.png',dpi=170);plt.close(fig)
    status=dict(status='EXECUTED: exploratory regional release associations',original_H1_H4='NOT EXECUTED',n=len(d),finite_exclusions=dropped,
        regions=len(regions),models=len(models),tests=len(r),Holm_pass_count=int(r.passes_Holm_0_05.sum()),
        by_outcome_predictor=r.groupby(['outcome','predictor']).passes_Holm_0_05.sum().astype(int).to_dict() if False else [dict(outcome=y,predictor=p,passes=int(g.passes_Holm_0_05.sum())) for (y,p),g in r.groupby(['outcome','predictor'])],
        core_GFAP_nonpositive=int((d.GFAP<=0).sum()),core_NFL_nonpositive=int((d.NFL<=0).sum()),
        sex_counts=d.sex.value_counts().to_dict(),plan_sha256=sha(HERE/'plan.json'),code_sha256=sha(__file__),
        validation='Independent OLS/HC3/p/CI checked for every main model; all case deletions cross-checked; partial R2 and Holm independently checked',
        versions=dict(python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,statsmodels=statsmodels.__version__,matplotlib=matplotlib.__version__))
    (out/'run_status.json').write_text(json.dumps(status,indent=2,allow_nan=False)+'\n')
    print(json.dumps(status,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();run(args.data_dir,args.output)
