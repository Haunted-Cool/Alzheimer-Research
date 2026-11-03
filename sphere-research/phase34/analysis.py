"""Auditable analysis functions. No PET summary is guessed. No data downloaded.

audit: reads the authorized original exports and writes aggregates only.
fit_models: accepts an explicitly prepared, documented common analysis matrix.
The CLI deliberately supports audit only until the measurement contract is resolved.
"""
from pathlib import Path
import argparse, csv, hashlib, json, platform
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.outliers_influence import variance_inflation_factor

BASE = Path(__file__).resolve().parent

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def read_table(path):
    with open(path, newline='') as f:
        header = next(csv.reader(f))
    if len(header) != len(set(header)):
        raise ValueError('Duplicate headers')
    d = pd.read_csv(path, dtype={'adrc_id': 'string'})
    if 'adrc_id' not in d:
        raise ValueError('Missing adrc_id')
    ids = d.adrc_id
    if ids.isna().any() or ids.eq('').any() or ids.duplicated().any() or ids.ne(ids.str.strip()).any():
        raise ValueError('Missing, duplicate or whitespace-padded ID')
    return d

def validate_matrix(d):
    cols = ['GFAP','NFL','amyloid','tau','age','sex']
    if not set(cols).issubset(d.columns):
        raise ValueError('Missing model fields')
    a = d[cols].to_numpy(dtype=float)
    if not np.isfinite(a).all():
        raise ValueError('Explicit common-case selection required: missing or nonfinite model values')
    if len(d) <= 10 or (d[cols].std(ddof=1) == 0).any():
        raise ValueError('Insufficient rows or constant variable')
    X = np.column_stack([np.ones(len(d)), d[['amyloid','tau','age','sex']].to_numpy(float)])
    if np.linalg.matrix_rank(X) != X.shape[1]:
        raise ValueError('Rank-deficient design')
    return X

def fit_models(d):
    """Released outcome units per one analysis-sample SD of each PET predictor.
    sex is ONE externally documented numeric contrast (binary only if documented).
    No automatic missing-value deletion or model selection.
    """
    validate_matrix(d)
    z = d.copy()
    for c in ['amyloid','tau','age']:
        z[c] = (d[c]-d[c].mean())/d[c].std(ddof=1)
    X = sm.add_constant(z[['amyloid','tau','age','sex']], has_constant='add')
    rows, diagnostics, models = [], {}, {}
    for outcome in ['GFAP','NFL']:
        ordinary = sm.OLS(z[outcome], X, missing='raise').fit()
        robust = ordinary.get_robustcov_results(cov_type='HC3', use_t=True)
        influence = ordinary.get_influence()
        ci = robust.conf_int()
        models[outcome] = (ordinary, robust, X)
        for pred in ['amyloid','tau']:
            j = X.columns.get_loc(pred)
            reduced = sm.OLS(z[outcome], X.drop(columns=pred)).fit()
            rows.append(dict(outcome=outcome,predictor=pred,n=len(d),beta=robust.params[j],
                se_HC3=robust.bse[j],ci95_low=ci[j,0],ci95_high=ci[j,1],p_raw=robust.pvalues[j],
                standardized_beta=robust.params[j]/d[outcome].std(ddof=1),
                partial_R2=(reduced.ssr-ordinary.ssr)/reduced.ssr))
        h = influence.hat_matrix_diag
        diagnostics[outcome] = dict(n=len(d),rank=int(np.linalg.matrix_rank(X)),df_resid=float(ordinary.df_resid),
            R2=float(ordinary.rsquared),adjusted_R2=float(ordinary.rsquared_adj),
            max_leverage=float(h.max()),leverage_above_2p_n=int((h>2*X.shape[1]/len(d)).sum()),
            cooks_above_4_n=int((influence.cooks_distance[0]>4/len(d)).sum()),
            max_abs_studentized_residual=float(np.abs(influence.resid_studentized_internal).max()),
            condition_number=float(np.linalg.cond(X)),
            VIF={c:float(variance_inflation_factor(X.to_numpy(),i)) for i,c in enumerate(X.columns) if c!='const'})
    table = pd.DataFrame(rows)
    table.insert(0,'hypothesis',['H1','H2','H3','H4'])
    table['p_secondary_Holm'] = np.nan
    table.loc[1:3,'p_secondary_Holm'] = multipletests(table.loc[1:3,'p_raw'],method='holm')[1]
    return table, diagnostics, models

def sensitivities(d):
    """Prespecified diagnostics, no selection of a preferred p-value.
    Standardization constants remain fixed from the original common sample.
    Returns aggregate coefficient ranges and alternate age-shape estimates.
    """
    _, _, models = fit_models(d)
    out = []
    for y,(ols,rob,X) in models.items():
        nonlinear = X.copy()
        nonlinear['age_squared'] = X.age**2
        quadratic = sm.OLS(d[y],nonlinear).fit(cov_type='HC3',use_t=True)
        loo = []
        for i in range(len(d)):
            keep = np.arange(len(d)) != i
            if np.linalg.matrix_rank(X.iloc[keep]) != X.shape[1]:
                raise ValueError('Leave-one-out design loses rank')
            loo.append(sm.OLS(d[y].iloc[keep],X.iloc[keep]).fit().params[['amyloid','tau']].to_numpy())
        loo = np.asarray(loo)
        for j,pred in enumerate(['amyloid','tau']):
            out.append(dict(outcome=y,predictor=pred,primary_beta=float(ols.params[pred]),
                quadratic_age_beta=float(quadratic.params[pred]),
                quadratic_age_ci95_low=float(quadratic.conf_int().loc[pred,0]),
                quadratic_age_ci95_high=float(quadratic.conf_int().loc[pred,1]),
                leave_one_out_min=float(loo[:,j].min()),leave_one_out_max=float(loo[:,j].max())))
    return pd.DataFrame(out)

def audit(data_dir, output):
    output.mkdir(parents=True,exist_ok=True)
    names=['demographics_diagnosis','biomarkers','imaging_amyloid','imaging_tau','wgs','proteomics_csf']
    frames={n:read_table(data_dir/(n+'.csv')) for n in names}
    manifest=[]
    for n,d in frames.items():
        numeric=d.select_dtypes('number')
        manifest.append(dict(file=n+'.csv',sha256=sha(data_dir/(n+'.csv')),rows=len(d),columns=len(d.columns),
            parsed_missing_cells=int(d.isna().sum().sum()),infinite_numeric_cells=int(np.isinf(numeric).sum().sum())))
    master=set(frames['demographics_diagnosis'].adrc_id)
    if any(not set(d.adrc_id).issubset(master) for d in frames.values()):
        raise ValueError('Orphan IDs outside demographics')
    selected=master.copy(); flow=[]
    for n in names[:4]:
        before=len(selected);selected &= set(frames[n].adrc_id)
        flow.append(dict(step=n,n=len(selected),lost_from_previous=before-len(selected)))
    demo=frames['demographics_diagnosis']; blood=frames['biomarkers']
    joined=demo.merge(blood,on='adrc_id',how='inner',validate='one_to_one')
    core=joined.loc[joined.adrc_id.isin(selected)]
    distributions=[]
    for population,d in [('all_blood',blood),('dual_PET_blood',core)]:
        for c in ['GFAP','NFL','PTAU217']:
            s=d[c].dropna()
            distributions.append(dict(population=population,field=c,n=len(s),mean=s.mean(),sd=s.std(ddof=1),
                minimum=s.min(),q1=s.quantile(.25),median=s.median(),q3=s.quantile(.75),maximum=s.max(),
                skewness=stats.skew(s,bias=False),excess_kurtosis=stats.kurtosis(s,bias=False),
                nonpositive=int((s<=0).sum()),missing=int(d[c].isna().sum())))
    pd.DataFrame(manifest).to_csv(output/'input_manifest.csv',index=False)
    pd.DataFrame(flow).to_csv(output/'sample_flow.csv',index=False)
    pd.DataFrame(distributions).to_csv(output/'biomarker_distributions.csv',index=False)
    patterns=pd.DataFrame({n:demo.adrc_id.isin(set(frames[n].adrc_id)) for n in names[1:4]})
    patterns.value_counts().rename('n').reset_index().to_csv(output/'availability_patterns.csv',index=False)
    comparison=[]
    for included in [True,False]:
        s=demo.loc[demo.adrc_id.isin(selected)==included]
        comparison.append(dict(in_core=included,n=len(s),age_mean=s.age_at_visit.mean(),age_sd=s.age_at_visit.std(ddof=1),
            sex_counts=s.sex.value_counts().to_dict(),diagnosis_counts=s.diagnosis_consensus.value_counts().to_dict()))
    a,b=[demo.loc[demo.adrc_id.isin(selected)==v,'age_at_visit'] for v in [True,False]]
    age_smd=(a.mean()-b.mean())/np.sqrt((a.var(ddof=1)+b.var(ddof=1))/2)
    status=dict(hypothesis_models_executed=False,reason='PET summaries and scale, sex encoding, plasma scale, and inference qualification unresolved',
        structural_core_n=len(core),core_GFAP_nonpositive=int((core.GFAP<=0).sum()),core_NFL_nonpositive=int((core.NFL<=0).sum()),
        selection_description=comparison,age_standardized_mean_difference=float(age_smd),
        code_sha256=sha(__file__),protocol_sha256=sha(BASE/'protocol.json'),
        versions=dict(python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,statsmodels=statsmodels.__version__))
    (output/'audit_status.json').write_text(json.dumps(status,indent=2,allow_nan=False)+'\n')
    # Distribution plots are descriptive and contain no identifiers.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(2,2,figsize=(10,7),layout='constrained')
    for row,c in enumerate(['GFAP','NFL']):
        axs[row,0].hist(core[c],bins='fd',color='#286b83',edgecolor='white')
        axs[row,0].set(title=f'{c}: dual-PET/blood subset (n={len(core)})',xlabel='Released numeric units',ylabel='Synthetic records')
        stats.probplot(core[c],plot=axs[row,1])
        axs[row,1].set(title=f'{c}: normal Q-Q plot',ylabel='Released numeric units')
    fig.savefig(output/'biomarker_distributions.png',dpi=160)
    plt.close(fig)
    print(json.dumps({'structural_core_n':len(core),'hypothesis_models_executed':False}))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    audit(args.data_dir,args.output)
