"""Present and verify frozen SPHERE outputs; no model refits or new tests."""
from pathlib import Path
import argparse, hashlib, json, shutil, platform, html
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent.parent
SRC=ROOT/'phase34/regional_extension'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return pd.read_csv(p,float_precision='round_trip')
def mdtable(frame):
    return '| '+' | '.join(frame.columns)+' |\n| '+' | '.join(['---']*len(frame.columns))+' |\n'+'\n'.join('| '+' | '.join(str(x) for x in row)+' |' for row in frame.itertuples(index=False,name=None))

def build(out):
    if out.exists(): raise ValueError('Use a new output directory to preserve evidence')
    frozen=json.loads((SRC/'completion/completion_verification.json').read_text())
    for name,expected in frozen['baseline_sha256'].items(): assert sha(SRC/name)==expected,name
    inputs=[p for folder in [SRC/'results',SRC/'completion'] for p in folder.iterdir() if p.is_file()]
    inputs += [ROOT/'phase34/results/biomarker_distributions.csv',ROOT/'phase34/results/availability_patterns.csv',ROOT/'phase34/sources/hypotheses.txt']
    before={str(p.relative_to(ROOT)):sha(p) for p in inputs}
    r=read(SRC/'results/regional_results.csv')
    d=read(SRC/'results/diagnostics.csv')
    s=read(SRC/'results/sensitivities.csv')
    a=read(SRC/'completion/all_tests_with_sensitivity_changes.csv')
    summary=read(SRC/'completion/main_results_summary.csv')
    ss=read(SRC/'completion/sensitivity_summary.csv')
    assert len(r)==272 and len(d)==136 and len(s)==272
    assert not r.duplicated(['region','outcome','predictor']).any()
    assert (r.n==165).all() and (d.n==165).all() and (d.df_resid==160).all()
    t=r.beta/r.se_HC3; calculated_p=2*stats.t.sf(abs(t),160)
    np.testing.assert_allclose(calculated_p,r.p_raw,rtol=1e-10,atol=1e-14)
    critical=stats.t.ppf(.975,160)
    for column,sign in [('ci95_low',-1),('ci95_high',1)]:
        np.testing.assert_allclose(r[column],r.beta+sign*critical*r.se_HC3,rtol=1e-10,atol=1e-12)
    order=np.argsort(calculated_p); adjusted=np.empty(272)
    adjusted[order]=np.minimum(1,np.maximum.accumulate(calculated_p[order]*np.arange(272,0,-1)))
    np.testing.assert_allclose(adjusted,r.p_Holm_272,rtol=1e-10,atol=1e-13)
    assert np.array_equal(adjusted<.05,r.passes_Holm_0_05)
    distributions=read(ROOT/'phase34/results/biomarker_distributions.csv')
    core=distributions.loc[distributions.population!='all_blood'].set_index('field')
    for y in ['GFAP','NFL']:
        sub=r[r.outcome==y]; sd=core.loc[y,'sd']
        assert core.loc[y,'n']==165
        for raw,standard in [('beta','standardized_beta'),('ci95_low','standardized_ci95_low'),('ci95_high','standardized_ci95_high')]:
            np.testing.assert_allclose(sub[raw]/sd,sub[standard],rtol=1e-10,atol=1e-12)
    assert r.partial_R2.between(0,1).all()
    # Partial R2 is not reconstructed from robust t; its independent SSE/correlation
    # check belongs to the preserved original model execution.
    assert json.loads((SRC/'verification.json').read_text())['status']=='PASS'
    assert frozen['status']=='PASS'
    assert len(read(SRC/'completion/independent_sensitivity_checks.csv'))==544
    out.mkdir(parents=True);(out/'tables').mkdir();(out/'figures').mkdir();(out/'provenance').mkdir()
    exact=r.copy();exact.insert(4,'df_resid',160);exact.insert(7,'t_HC3',t)
    flow=read(SRC/'results/sample_flow.csv');flow['excluded_since_previous']=flow.n.shift(1,fill_value=flow.n.iloc[0])-flow.n
    flow.to_csv(out/'tables/T1_sample_flow.csv',index=False)
    summary.to_csv(out/'tables/T2_results_summary.csv',index=False)
    exact.to_csv(out/'tables/T3_all_272_tests.csv',index=False)
    a.to_csv(out/'tables/T4_all_sensitivities.csv',index=False)
    d.to_csv(out/'tables/T5_all_model_diagnostics.csv',index=False)
    hypotheses=pd.DataFrame([
      ['H1','GFAP–amyloid','Unassessed as originally specified','50/68 positive regional findings; direction consistent with expectation, not confirmation'],
      ['H2','GFAP–tau','Unassessed as originally specified','0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence'],
      ['H3','NFL–amyloid','Unassessed as originally specified','0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence'],
      ['H4','NFL–tau','Unassessed as originally specified','0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence']
    ],columns=['hypothesis','association','original_status','regional_evidence'])
    hypotheses.to_csv(out/'tables/T6_hypothesis_assessment.csv',index=False)
    ss.to_csv(out/'tables/T7_sensitivity_summary.csv',index=False)
    shutil.copy2(ROOT/'phase34/results/biomarker_distributions.csv',out/'tables/T8_prior_distribution_audit.csv')
    shutil.copy2(ROOT/'phase34/results/availability_patterns.csv',out/'tables/T9_prior_availability_audit.csv')
    for name in ['plan.json','verification.json']:
        shutil.copy2(SRC/name,out/'provenance'/name)
    for name in ['completion_verification.json','Final_Verified_Results_Summary.md','Diagnostic_Review.md']:
        shutil.copy2(SRC/'completion'/name,out/'provenance'/name)
    shutil.copy2(SRC/'results/all_model_diagnostics.pdf',out/'figures/S1_original_model_diagnostics.pdf')
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','savefig.facecolor':'white'})
    figures=[]
    def save(fig,name,caption):
        fig.savefig(out/'figures'/f'{name}.png',dpi=180,bbox_inches='tight')
        fig.savefig(out/'figures'/f'{name}.svg',bbox_inches='tight')
        plt.close(fig);figures.append((name,caption))
    fig,ax=plt.subplots(figsize=(11,4.8),layout='constrained')
    stages=['Roster','With blood','Also amyloid','Also tau','Finite analysis sample']
    ax.barh(np.arange(5),flow.n,color=['#9da9b1']*4+['#007f86'])
    for i,row in enumerate(flow.itertuples()): ax.text(row.n+8,i,str(row.n),va='center')
    ax.set(yticks=np.arange(5),yticklabels=stages,xlim=(0,715),xlabel='Number of synthetic records',title='Figure 1. Common-sample selection');ax.invert_yaxis()
    save(fig,'F1_sample_flow','Sequential one-to-one intersections: 644 → 618 → 270 → 165; no additional finite-value exclusions. These are overlapping stages, not independent groups. Source: T1.')
    combos=[('GFAP','amyloid'),('GFAP','tau'),('NFL','amyloid'),('NFL','tau')]
    lim=(np.floor(r.standardized_ci95_low.min()*10)/10-.02,np.ceil(r.standardized_ci95_high.max()*10)/10+.02)
    for hemi,label,num in [('lh','Left',2),('rh','Right',3)]:
        subset=r[r.region.str.startswith('ctx-'+hemi+'-')];regions=sorted(subset.region.unique())
        assert len(regions)==34
        fig,axes=plt.subplots(1,4,figsize=(13,11),sharey=True,sharex=True,layout='constrained')
        for ax,(outcome,predictor) in zip(axes,combos):
            sub=subset[(subset.outcome==outcome)&(subset.predictor==predictor)].set_index('region').loc[regions]
            for j,row in enumerate(sub.itertuples()):
                color='#007f86' if row.passes_Holm_0_05 else '#68737d'
                ax.plot([row.standardized_ci95_low,row.standardized_ci95_high],[j,j],color=color,lw=1)
                ax.plot(row.standardized_beta,j,'o',ms=4,mec=color,mfc=color if row.passes_Holm_0_05 else 'white')
            ax.axvline(0,color='#a5a5a5',ls='--',lw=.8);ax.set(xlim=lim,title=f'{outcome} / {predictor}',xlabel='Standardized slope')
            ax.set_yticks(range(34),[x.replace('ctx-'+hemi+'-','') for x in regions],fontsize=8);ax.grid(axis='x',alpha=.15)
        axes[0].invert_yaxis()
        fig.suptitle(f'Figure {num}. {label} hemisphere: exploratory regional associations\n165 synthetic records; marginal 95% HC3 intervals',fontsize=14)
        save(fig,f'F{num}_{hemi}_regional_effects',f'{label} hemisphere, all 34 regions in alphabetical order, identical axes across all eight hemisphere panels. Filled teal points: Holm p < .05 in the full 272-test family; hollow gray points: threshold not met. Bars are marginal 95% intervals, not simultaneous intervals. Models mutually adjust same-region PET fields, age and readable sex. Source: T3. Standardized slopes are unitless; clinical PET normalization remains unverified.')
    fig,axes=plt.subplots(2,4,figsize=(13,7),layout='constrained')
    for col,(outcome,predictor) in enumerate(combos):
        sub=a[(a.outcome==outcome)&(a.predictor==predictor)]
        for row,(variant,label) in enumerate([('quadratic_age','Quadratic age'),('numeric_sex_contrast','Numeric sex contrast')]):
            ax=axes[row,col];base=sub.standardized_beta;alt=base+sub[variant+'_standardized_change']
            ax.scatter(base,alt,s=14,c='#007f86',alpha=.75)
            ax.plot([-.1,.5],[-.1,.5],ls='--',color='gray',lw=.8)
            ax.set(xlim=(-.1,.5),ylim=(-.1,.5),xlabel='Main standardized slope',ylabel=label+' slope',title=f'{outcome} / {predictor}')
            ax.set_aspect('equal');ax.grid(alpha=.15)
    fig.suptitle('Figure 4. Sensitivity to age specification and sex encoding\nAll 68 regions per panel; dashed line denotes unchanged coefficient',fontsize=13)
    save(fig,'F4_age_sex_sensitivity','Each point is one regional slope. Alternative estimates use the original sample and scaling. Identical axes and identity lines prevent visual exaggeration. These are descriptive comparisons, not alternative corrected significance tests. Source: T4.')
    fig,axes=plt.subplots(1,4,figsize=(13,4),sharex=True,sharey=True,layout='constrained')
    for ax,(outcome,predictor) in zip(axes,combos):
        sub=a[(a.outcome==outcome)&(a.predictor==predictor)]
        ax.scatter(sub.standardized_beta,sub.leave_one_out_max_standardized_change,s=20,color='#007f86',alpha=.8)
        ax.set(title=f'{outcome} / {predictor}',xlabel='Main standardized slope',xlim=(-.1,.5),ylim=(0,.08));ax.grid(alpha=.15)
    axes[0].set_ylabel('Largest absolute standardized change')
    fig.suptitle('Figure 5. Influence of individual records\nAll 68 regions per panel; 165 deletions per model',fontsize=13)
    save(fig,'F5_single_record_influence','Each point shows the largest absolute slope change across single-record deletions for one regional association. Original scaling is held fixed. These maxima are not confidence limits. All 22,440 case-deletion fits were previously checked independently. Source: T4.')
    captions='\n\n'.join(f'**{name}.** {cap}' for name,cap in figures)
    (out/'Figure_Captions.md').write_text(captions+'\n')
    display=summary[['outcome','predictor','tests','Holm_passes','standardized_beta_min','standardized_beta_max']].copy()
    display.columns=['Outcome','Predictor','Tests','Holm findings','Min standardized slope','Max standardized slope']
    for col in display.columns[-2:]: display[col]=display[col].map(lambda x:f'{x:.3f}')
    report=f'''# SPHERE Phase 4 — Results and Figures

Research record for Chat 10, 2 November 2026. This is an evidence inventory and interpretation guide, not manuscript prose. Only existing executed analyses are presented. No new models, exclusion rules or hypothesis families were introduced.

## Confirmed scope and sample

The completed analysis is exploratory extension E1: 68 cortical regions, two outcomes, 136 mutually adjusted OLS models, and 272 focal slope tests on a common sample of 165 synthetic-release records. There are 90 readable male and 75 readable female labels. Original biological H1–H4 remain unassessed because their measurement mapping is unresolved.

The sequential linked sample is 644 roster records → 618 with blood → 270 also with amyloid → 165 also with tau. There are no further finite-value exclusions. The resulting sample is {165/644*100:.2f}% of the roster. Table T1 and Figure 1 document these intersections. The source PET files individually contain 276 amyloid and 197 tau records; these standalone counts differ from the sequential overlap counts. Absence of additional cell-level exclusions does not remove missing-modality selection bias.

GFAP and NFL are outcomes on their released numeric scales. Every region's amyloid and tau fields are simultaneously included with standardized age and readable sex (female 0, male 1). All main models have 160 residual degrees of freedom. PET fields and age use common-sample means and sample SDs. Outcomes were not logged; five negative GFAP values were retained. No imputation or outlier removal was used. Synthetic sex encoding and clinical PET/plasma units remain unverified.

## Main findings: all completed regional tests

{mdtable(display)}

The significance rule is two-sided HC3 inference with a Student t reference and Holm p < .05 across the entire 272-test family. The 50 threshold-crossing results are all positive GFAP–amyloid coefficients. Across all 68 GFAP–amyloid tests, adjusted p ranges from {summary.iloc[0].Holm_p_min:.8g} to {summary.iloc[0].Holm_p_max:.8g}. All adjusted p-values in the other three combinations are 1.0. This does not mean the effects are exactly zero or that their null hypotheses have probability 1.

T3 contains all 272 test statistics, coefficients, HC3 SEs, n, residual degrees of freedom, raw and corrected p-values, 95% confidence bounds, standardized estimates and partial R². Its added t statistic is reconstructed as beta/HC3 SE from saved estimates, not a new test. Full precision is retained in machine-readable CSV; readable HTML values are rounded to six significant digits. No values are replaced with a generic “NS” label. The underlying numbers, not rounded display values, determine significance.

The 95% intervals are marginal: beta ± t(.975,160) × HC3 SE. They do not provide simultaneous 95% coverage across 272 coefficients. A nominal interval excluding zero does not guarantee Holm significance. Raw slopes are released outcome units per one sample SD of PET. Fully standardized slopes divide by the outcome SD, making those plotted effects unitless. Partial R² describes incremental model fit after the other variables; it is not causal variance explained and has no estimated interval here.

## Hypothesis evaluation

{mdtable(hypotheses)}

For the exploratory question itself, there is threshold-crossing evidence of positive GFAP–amyloid associations under the executed models. The direction is compatible with the original H1 expectation, but cannot confirm the originally defined burden hypothesis. For the other exploratory associations, evidence is inconclusive at the corrected threshold. None of H1–H4 is established as contradicted. No equivalence tests or direct tests comparing GFAP and NFL slopes were performed. A significant GFAP association and nonsignificant NFL association do not establish that their associations differ.

## Sensitivity findings, including nonsignificant results

All 136 models were separately refitted with quadratic age and with numeric sex_orth_male replacing the readable sex label. Original scaling and the sample were retained. The quadratic model has 159 residual degrees of freedom; the sex variant has 160. Alternative coefficients and marginal HC3 intervals are in T4. These descriptive checks were specified in E1; they do not create a new discovery family.

No slope changed sign with quadratic age. All 50 base-model GFAP–amyloid findings remained positive with either variant and after every single-record deletion. For those 50, median absolute coefficient changes were 1.93% with quadratic age (maximum 3.17%) and 1.15% with sex encoding (maximum 3.82%). Their largest absolute standardized deletion change was 0.0557. This supports limited coefficient stability, not preservation of corrected significance under all alternatives.

Across all 68 GFAP–tau slopes, 10 changed sign under alternate sex coding and 14 had single-deletion ranges spanning zero. Those findings qualify any broad claim that all estimates were robust. Neither NFL combination changed signs under these checks; neither had corrected main-model findings. Near-zero slopes can have misleadingly large percentage changes, so the figures emphasize absolute standardized changes. Figures 4–5 include all regions; T7 summarizes every combination, separately identifying the descriptive subset of 50 main-model findings.

All 22,440 case-deletion evaluations were checked against direct least-squares refits during the original execution. Conventional SEs were also compared with HC3 and are retained in T4. HC3/conventional ratios range from {a.HC3_to_conventional_SE_ratio.min():.4f} to {a.HC3_to_conventional_SE_ratio.max():.4f} across focal slopes; HC3 need not always be larger. No SE method was chosen based on favorable significance.

## Diagnostics and scientific concerns

All 136 models and deletion fits passed rank checks. Maximum PET VIFs were {d.VIF_amyloid.max():.3f} for amyloid and {d.VIF_tau.max():.3f} for tau. Maximum leverage was {d.max_leverage.max():.6f}; maximum absolute internally studentized residual was {d.max_abs_studentized_residual.max():.6f}. Cook's distance >4/165 flagged {int(d.cooks_flag_count.min())}–{int(d.cooks_flag_count.max())} records per model. No flags triggered deletion. T5 contains every model's R², diagnostic statistics and residual skewness.

Supplement S1 retains all 136 original diagnostic pages. Prior contact-sheet review found positive-tail residual departures; normality was not declared satisfied. Full-rank and low-VIF findings do not establish a correct linear conditional mean, independent synthetic observations or missing-at-random selection. HC3 provides approximate variance robustness, not protection against every misspecification or selection bias. Formal nonlinear PET checks, bootstrap inference, equivalence tests, multiple imputation and external validation were not performed.

The findings concern released regional fields; no field should be labeled certified SUVR, Centiloid or global pathology burden. The cohort overview does not establish normalization/reference regions for these exact exports or the tau tracer. Plasma units must not be silently labeled pg/mL. Synthetic-data generation uncertainty is not included in the intervals. The 50 regional findings are correlated observations of one dataset, not 50 replications. Only age, released sex and same-region PET were adjusted; residual confounding from diagnosis, APOE, renal function, vascular injury, timing or assay batch remains possible. These results establish neither causation, biomarker specificity nor clinical utility.

## Numerical verification and provenance

This presentation build rechecked all 272 sample sizes and t statistics, p-values, HC3 confidence limits, Holm values, and significance flags. Standardized coefficients and intervals were checked against the independently saved outcome SDs. Original partial R² verification used the reduced-model SSE and squared residual-correlation identity; it was reused, not incorrectly recomputed from a robust t statistic. All 136 main-model arithmetic checks and 544 alternative coefficient/CI checks are preserved in the prior verification records.

The previously executed repeat run agreed for all ten non-PDF output files; diagnostic PDFs matched page counts and extracted text, with different timestamp metadata. Completion verification independently rebuilt the sample and scales and verified sensitivity estimates using QR algebra. The current build checks source fingerprints before and after presentation generation. Validation results and input hashes are saved in `results_verification.json`; a package manifest fingerprints delivered outputs. Passing these checks verifies numerical consistency, not clinical validity.

The earlier distribution audit is included unchanged as T8 (GFAP, NFL and PTAU217 in available blood records and the common core), and modality availability as T9. PTAU217 remains descriptive only. The artificial 240-row software fixture is not a scientific result and is not included as evidence for hypotheses. No unperformed original H1–H4 result is substituted with a fixture estimate.

## Figures, tables and handoff

{captions}

PNG files are for viewing; SVG files provide scalable, editable vector figures. Hemisphere panels use identical axes, include all 34 regions per hemisphere in alphabetical order, and distinguish Holm decisions from marginal confidence bars. Regions are named as exported, with hemisphere stated in the figure title. A forest plot avoids unsupported clinical units; a regional brain map was not created because anatomical localization and measurement equivalence were not independently verified. Figures 4–5 are descriptive sensitivity plots, not additional significance plots.

T1: sample flow. T2: exact group summary. T3: all 272 main results. T4: all 272 rows of alternative estimates, intervals, deletion ranges and SE comparisons. T5: all 136 model diagnostics. T6: hypothesis assessment. T7: sensitivity summary. T8–T9: preserved earlier descriptive audits. `Results_Tables.html` offers readable tables and all main estimates. The preceding comprehensive methodology record is included in `provenance/Final_Verified_Results_Summary.md`.

For a future Results section, organize the evidence as sample selection, complete regional associations, diagnostic qualifications and sensitivity estimates, with T1–T7 and Figures 1–5. For a future Discussion section, evaluate the limited positive GFAP–amyloid pattern, inconclusive remaining combinations, unstable small GFAP–tau coefficients, selection and measurement limitations, and the distinction between synthetic associations and source-cohort biology. These are organizational notes, not drafted manuscript prose.

Remaining tasks: resolve the original measurement contract if retaining biological H1–H4; seek scientific/mentor review; and obtain independent reproduction and external validation. Publication acceptance is not determined by these numerical checks. No planned E1 sensitivity remains unfinished. Any new outcome-driven analysis must be documented as a new exploratory extension.

## Reproduce this presentation

From the project root, run `phase34/.venv/bin/python phase4_results/build_results.py --output phase4_results/new_build` using a new output directory. The script consumes the frozen phase34 outputs and does not refit models or read individual records. It requires NumPy, pandas, SciPy and Matplotlib from the recorded environment. `environment.json` records exact versions. For the original model reproduction instructions and requirements, use the existing verified methodology package. A fresh environment installation has not been tested.
'''
    (out/'Results_Report.md').write_text(report)
    tables_html=''.join(f'<h2>{title}</h2>'+frame.to_html(index=False,float_format=lambda x:format(x,'.6g'),escape=True) for title,frame in [('T1. Sample flow',flow),('T2. Main results summary',summary),('T6. Hypothesis assessment',hypotheses),('T7. Sensitivity summary',ss),('T3. All 272 main tests (rounded for display)',exact)])
    figure_html=''.join(f'<figure><img src="figures/{name}.png"><figcaption>{html.escape(cap)}</figcaption></figure>' for name,cap in figures)
    (out/'Results_Tables.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><title>SPHERE verified results</title><style>body{font:15px system-ui;margin:32px;color:#192c38}table{border-collapse:collapse;font-size:12px}th,td{padding:7px;border-bottom:1px solid #ddd;text-align:left}th{background:#e5f0f1}img{max-width:1200px;width:100%}figure{margin:35px 0}figcaption{max-width:1000px}</style><h1>SPHERE exploratory results and figures</h1><p>165 synthetic records. Original H1–H4 unassessed. See Results_Report.md for scope and limitations. Tables here are rounded; CSV files retain numeric precision.</p>'+figure_html+tables_html+'</html>')
    for name,expected in before.items(): assert sha(ROOT/name)==expected,name
    # Round-trip verifies all exact result columns survive export.
    back=read(out/'tables/T3_all_272_tests.csv')
    pd.testing.assert_frame_equal(exact,back,check_exact=True)
    verification=dict(status='PASS',main_tests_checked=272,models=136,n=165,df=160,
      max_p_discrepancy=float(np.max(abs(calculated_p-r.p_raw))),
      checks=['source fingerprints','t=beta/HC3_SE','two-sided t p','marginal CI','Holm','standardized effects and CIs versus saved SD','CSV round trip'],
      prior_checks_reused=['partial R2 reduced SSE identity','136 independent OLS/HC3 checks','544 sensitivity coefficients and intervals','22440 deletion fits','two complete model runs'],
      original_files_unchanged=True,input_sha256=before,
      visual_review='Pending; recorded separately after inspecting the generated figures',
      build_script_sha256=sha(Path(__file__)))
    (out/'results_verification.json').write_text(json.dumps(verification,indent=2)+'\n')
    import scipy
    (out/'environment.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__,matplotlib=matplotlib.__version__),indent=2)+'\n')
    print(json.dumps({'status':'PASS','output':str(out),'tests':272,'figures':5,'tables':9}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    build(parser.parse_args().output.resolve())
