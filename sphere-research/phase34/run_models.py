"""Future analysis entrypoint. Refuses unresolved protocol; never derives PET summaries."""
from pathlib import Path
import argparse, json
import pandas as pd
from analysis import read_table, fit_models, sensitivities, sha

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prepared-data',type=Path,required=True)
    p.add_argument('--protocol',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    protocol=json.loads(args.protocol.read_text())
    contract=protocol['measurement_contract']
    missing=[k for k,v in contract.items() if not isinstance(v,str) or not v.strip()]
    if missing:
        raise SystemExit('Analysis not run: unresolved definitions: '+', '.join(missing))
    if args.output.exists() and any(args.output.iterdir()):
        raise SystemExit('Use a new output directory to preserve earlier results')
    d=read_table(args.prepared_data)
    results,diagnostics,models=fit_models(d)
    sensitivity=sensitivities(d)
    args.output.mkdir(parents=True,exist_ok=True)
    results.to_csv(args.output/'hypothesis_results.csv',index=False)
    sensitivity.to_csv(args.output/'prespecified_sensitivities.csv',index=False)
    ordinary=[]
    for y,(fit,rob,X) in models.items():
        for c in ['amyloid','tau']:
            ordinary.append(dict(outcome=y,predictor=c,se_conventional=fit.bse[c],p_conventional=fit.pvalues[c]))
    pd.DataFrame(ordinary).to_csv(args.output/'conventional_covariance_sensitivity.csv',index=False)
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from scipy import stats
    for y,(fit,rob,X) in models.items():
        fig,axs=plt.subplots(2,3,figsize=(13,8),layout='constrained')
        axs[0,0].scatter(fit.fittedvalues,fit.resid,s=10)
        axs[0,0].axhline(0,color='black',lw=1)
        axs[0,0].set(xlabel='Fitted outcome',ylabel='Residual',title=y)
        stats.probplot(fit.resid,plot=axs[0,1]);axs[0,1].set_title('Residual normal Q-Q')
        influence=fit.get_influence()
        axs[0,2].scatter(influence.hat_matrix_diag,fit.resid,s=10)
        axs[0,2].set(xlabel='Leverage',ylabel='Residual')
        for ax,c in zip(axs[1],['amyloid','tau','age']):
            ax.scatter(X[c],fit.resid+fit.params[c]*X[c],s=10)
            ax.set(xlabel=c+' (standardized)',ylabel='Partial residual')
        fig.savefig(args.output/(y+'_diagnostics.png'),dpi=160);plt.close(fig)
    log=dict(status='Executed on supplied prepared data; inspect measurement evidence before interpreting',
        n=len(d),diagnostics=diagnostics,protocol_sha256=sha(args.protocol),prepared_data_sha256=sha(args.prepared_data),
        analysis_code_sha256=sha(Path(__file__).parent/'analysis.py'),
        scaling={c:{'mean':float(d[c].mean()),'sample_sd':float(d[c].std(ddof=1))} for c in ['amyloid','tau','age']})
    (args.output/'model_run.json').write_text(json.dumps(log,indent=2,allow_nan=False)+'\n')
    print('Models executed; inspect estimates, diagnostics and documented measurement assumptions.')

if __name__=='__main__':main()
