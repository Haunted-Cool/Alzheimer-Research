"""Consolidate previously verified aggregate evidence; no new statistical models."""
from pathlib import Path
import hashlib, html, json, re, shutil, zipfile
import numpy as np
import pandas as pd
from scipy import stats

ROOT=Path(__file__).resolve().parent.parent
HERE=ROOT/'chat10_final_results'
OLD=ROOT/'phase4_results/deliverables'
OUT=HERE/'deliverables'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return pd.read_csv(p,float_precision='round_trip')
def scalar(x):
    if isinstance(x,(float,np.floating)): return format(x,'.17g')
    return str(x)
def mdtable(df):
    return '| '+' | '.join(df.columns)+' |\n| '+' | '.join(['---']*len(df.columns))+' |\n'+'\n'.join('| '+' | '.join(scalar(x) for x in row)+' |' for row in df.itertuples(index=False,name=None))
def narrative_html(text):
    blocks=[]
    for para in text.split('\n\n'):
        lines=para.splitlines()
        if para.startswith('#'):
            level=min(len(para)-len(para.lstrip('#')),4)
            blocks.append(f'<h{level}>'+html.escape(para.lstrip('# '))+f'</h{level}>')
        elif para.startswith('|') and len(lines)>1:
            rows=[[html.escape(c.strip()) for c in l.strip('|').split('|')] for l in lines if not re.match(r'^\|[\s:|\-]+\|$',l)]
            blocks.append('<div class="scroll"><table>'+''.join('<tr>'+''.join(f'<{"th" if i==0 else "td"}>{c}</{"th" if i==0 else "td"}>' for c in row)+'</tr>' for i,row in enumerate(rows))+'</table></div>')
        else: blocks.append('<p>'+html.escape(para).replace('\n','<br>')+'</p>')
    return '\n'.join(blocks)

if OUT.exists(): raise ValueError('Final evidence already exists; use a new version')
inputs={str(p.relative_to(ROOT)):sha(p) for p in OLD.rglob('*') if p.is_file()}
prior=json.loads((OLD/'results_verification.json').read_text())
for name,digest in prior['input_sha256'].items(): assert sha(ROOT/name)==digest,name
r=read(OLD/'tables/T3_all_272_tests.csv');s=read(OLD/'tables/T4_all_sensitivities.csv')
d=read(OLD/'tables/T5_all_model_diagnostics.csv')
assert len(r)==272 and len(s)==272 and len(d)==136
assert r.n.eq(165).all() and r.df_resid.eq(160).all()
np.testing.assert_allclose(r.t_HC3,r.beta/r.se_HC3,rtol=1e-12,atol=1e-14)
p=2*stats.t.sf(abs(r.t_HC3),160)
np.testing.assert_allclose(p,r.p_raw,rtol=1e-12,atol=1e-14)
for col,sign in [('ci95_low',-1),('ci95_high',1)]:
    np.testing.assert_allclose(r[col],r.beta+sign*stats.t.ppf(.975,160)*r.se_HC3,rtol=1e-12,atol=1e-13)
order=np.argsort(p);holm=np.empty(272);holm[order]=np.minimum(1,np.maximum.accumulate(p[order]*np.arange(272,0,-1)))
np.testing.assert_allclose(holm,r.p_Holm_272,rtol=1e-12,atol=1e-13)
assert np.array_equal(holm<.05,r.passes_Holm_0_05)
keys=['region','outcome','predictor']; joined=r.merge(s,on=keys,validate='one_to_one',suffixes=('_canonical','_sensitivity'))
max_delta={}
for col in ['beta','p_raw','p_Holm_272','standardized_beta','partial_R2']:
    x=joined[col+'_canonical'];y=joined[col+'_sensitivity']
    np.testing.assert_allclose(x,y,rtol=1e-12,atol=1e-13)
    max_delta[col]=float(abs(x-y).max())
shutil.copytree(OLD,OUT)
scales=read(ROOT/'phase34/regional_extension/results/scaling.csv')
scales.to_csv(OUT/'tables/T10_predictor_descriptives_and_scaling.csv',index=False)
sample=pd.DataFrame([
 ['Main regional OLS','136',165,160,'272 focal tests'],
 ['Quadratic-age sensitivity','136',165,159,'272 focal estimates and intervals; descriptive'],
 ['Numeric-sex sensitivity','136',165,160,'272 focal estimates and intervals; descriptive'],
 ['Conventional SE comparison','136',165,160,'272 focal SE comparisons; same fitted main models'],
 ['Single-record deletion','22440',164,159,'One record omitted from each main model; original scaling'],
 ['Reduced models for partial R2','272',165,161,'Omit one PET predictor; descriptive fit comparison'],
 ['Blood descriptive audit','3 variables',618,'not applicable','GFAP, NFL, PTAU217'],
 ['Common-core descriptive audit','3 variables',165,'not applicable','GFAP, NFL, PTAU217']
],columns=['analysis','model_or_variable_count','records_per_analysis','residual_df','purpose'])
sample.to_csv(OUT/'tables/T11_analysis_sample_sizes.csv',index=False)
demographics=pd.DataFrame([
 ['Common sample','Records',165,'count'],['Readable male label','Records',90,'count'],['Readable female label','Records',75,'count'],
 ['Age at visit','Mean',float(scales.iloc[0]['mean']),'released age scale'],['Age at visit','Sample SD',float(scales.iloc[0]['sd']),'released age scale']
],columns=['variable','statistic','value','units'])
demographics.to_csv(OUT/'tables/T12_available_demographic_descriptives.csv',index=False)
inventory=pd.DataFrame([
 ['F1_sample_flow.png; F1_sample_flow.svg','Sequential linked sample counts','Synthetic records (count)','Document selection from 644 to 165'],
 ['F2_lh_regional_effects.png; F2_lh_regional_effects.svg','Left hemisphere: all GFAP/NFL and amyloid/tau slopes and marginal CIs','Standardized slopes and CIs (unitless)','Show all 136 left-hemisphere tests with Holm markers'],
 ['F3_rh_regional_effects.png; F3_rh_regional_effects.svg','Right hemisphere: all GFAP/NFL and amyloid/tau slopes and marginal CIs','Standardized slopes and CIs (unitless)','Show all 136 right-hemisphere tests with Holm markers'],
 ['F4_age_sex_sensitivity.png; F4_age_sex_sensitivity.svg','Main versus quadratic-age/alternate-sex slopes','Standardized slopes (unitless)','Assess coefficient stability, not alternate significance'],
 ['F5_single_record_influence.png; F5_single_record_influence.svg','Main slope versus maximum absolute single-deletion change','Standardized slopes/changes (unitless)','Assess individual-record influence for all 272 slopes'],
 ['S1_original_model_diagnostics.pdf','136 pages: residual versus fitted; Q-Q; residual versus leverage','Fitted/residual values: released GFAP or NFL units; leverage and theoretical normal quantiles: unitless','Identify residual departures and influential observations']
],columns=['filenames_in_figures_folder','variables','measurement_units','scientific_purpose'])
inventory.to_csv(OUT/'tables/T13_final_figure_inventory.csv',index=False)
front='''# Final authoritative results record for Chat 10

Date: 2 November 2026. Status: final consolidation of the actually executed exploratory regional analysis. This record is designed to audit independently written Results and Discussion sections. It is research documentation, not manuscript prose. It incorporates every reported focal main-model result, every saved sensitivity coefficient and interval, model diagnostics and saved descriptive summaries. The original biological H1–H4 remain UNASSESSED, not rejected or confirmed.

## How to audit this document

The exact numerical appendices below are part of this standalone report: it is not necessary to consult another chat to find individual results. Canonical main results are T3. Numeric values are displayed with up to 17 significant digits to preserve floating-point round trips; this is computational precision, not justified laboratory measurement precision. Routine manuscript rounding should be consistent and must not affect threshold decisions. Every significant and nonsignificant regional test is retained.

The included HTML version uses horizontally scrollable exact tables and embeds every final PNG figure with its caption. CSV files support independent calculation. The unchanged SVGs are scalable figure files. Previous numerical verification, methodology and graphical-review records are preserved alongside this report. The following overview is followed by exact appendices, a complete table inventory, figure inventory, and an explicit missing-results ledger.

## Final sample sizes and descriptive coverage

There are 165 synthetic records in every main, quadratic-age and alternate-sex model, not 165 newly studied real participants. Each leave-one-record-out model uses 164 records. The reduced models used to obtain partial R² retain 165. Counts of 136 models, 272 tests and 22,440 deletion evaluations do not represent additional participants. T11 lists the residual degrees of freedom and purpose for every model category.

Age at visit has common-sample mean 71.94553389115767 and sample SD 8.800217312696915 on the released age scale. Readable synthetic sex labels comprise 90 male and 75 female records. T12 records these available demographic summaries. T8 gives all saved blood biomarker descriptive statistics for both the 618-row blood sample and 165-row common core: n, mean, SD, range, quartiles, median, skewness, excess kurtosis, nonpositive and missing counts. PTAU217 is descriptive only. T9 enumerates all eight modality-availability patterns across the 644-record roster. T10 supplies means and SDs for age and all 136 selected PET fields used in standardization.

There is no completed original primary H1 test or original secondary H2–H4 test to report. E1 instead has one 272-test exploratory family. Region-level findings must not be placed into the original primary/secondary inferential hierarchy retrospectively.
'''
overview=(OLD/'Results_Report.md').read_text()
overview=overview.replace('# SPHERE Phase 4 — Results and Figures','# Preserved Results & Figures overview')
missing='''## Missing results and interpretation ledger

Original H1–H4 coefficients, p-values and confidence intervals: unexecuted because exact measurement definitions remain unresolved. Clinical PET positivity groups, global composites, clinical cutoffs and genotype analyses: not performed. Direct statistical comparisons of biomarker slopes, equivalence tests, causal effects and diagnostic accuracy: not performed. Sensitivity-adjusted Holm p-values: not computed or claimed. Confidence intervals for partial R²: not calculated. Covariate/intercept coefficient tables and every individual deleted-fit coefficient vector were not exported in the existing reporting outputs; only focal coefficients and deletion ranges were retained. No missing coefficient is fabricated here.

Age quartiles/range, diagnosis-specific summaries and every PET field's full distribution are not included in the saved summary outputs used here; T10 provides only recorded means and SDs. New distribution calculations from raw records were not commissioned in this consolidation. The negative synthetic measurements should be described as released values, not interpreted as physiologically negative concentrations. Correct source-person sex coding, exact PET units/reference regions, tau tracer, plasma scale, timing, synthesis uncertainty and external validity remain unverified.

Observed findings: positive regional GFAP–amyloid associations pass the exploratory correction in 50 regions; other combinations do not. Some small GFAP–tau coefficients are sensitive to encoding or individual observations. Proposed biological explanations, such as astrocytic responses to amyloid, are hypotheses for Discussion and were not measured or tested by these models. The numerical pattern cannot establish GFAP specificity, causation, the absence of tau-related biology or clinical usefulness.

Unexpected or cautionary observations include retained negative GFAP values, positive-tail residual departures, numerous Cook's-distance flags, and sex-sensitive GFAP–tau estimates. The 50 positive associations are correlated tests on one selected synthetic sample. No independent biological replication, fresh-environment installation or independent-investigator reproduction has been established. Main findings are compatible with H1's expected direction at a regional exploratory level, but do not constitute its original formal test.

## Agreement across outputs, tables and figures

The final consolidation rechecked n, degrees of freedom, t statistics, two-sided p-values, HC3 marginal confidence intervals and Holm decisions for all 272 main tests. It matched copied tables to their preserved source hashes and compared the duplicated main results in sensitivity tables with canonical T3 values. Tiny floating-point serialization differences, where present, are documented in final_verification.json; they do not change any conclusion. T3 is the authoritative full-precision main table.

Figures are unchanged, fingerprinted copies of the previously reviewed Matplotlib outputs. Their values were drawn from the checked tables using the preserved builder; labels, common axes and interval limits were visually checked during the Results & Figures phase. This is source-linked numerical verification plus graphical review, not independent extraction of coordinates from rendered pixels. SVG XML was checked; SVGs were not separately rendered. The diagnostic PDF review scope is recorded in provenance/Diagnostic_Review.md. No model assumptions are declared universally satisfied.

The preceding methodology package contains the original independent OLS/HC3 and partial-R² arithmetic checks, 544 sensitivity coefficient/CI checks and 22,440 direct deletion-fit comparisons. They are reused here, not misrepresented as new analyses. No model was refitted and no p-value selection was introduced in this consolidation.

## Exact numerical appendices

Tables are included in full below. To keep wide results readable, T3 is split into test statistics/decisions and interval/effect-size panels; T4 is split into alternative-model estimates and influence/SE panels. Join panels using region, outcome and predictor. T3 and T4 CSVs retain all original columns together. Region headers beginning ctx-lh and ctx-rh indicate left and right hemisphere. All raw outcomes and PET summaries retain their released scale unless explicitly standardized. CI means confidence interval; SE means standard error; df means residual degrees of freedom.
'''
parts=[front,overview,missing]
html_parts=[narrative_html(front),narrative_html(overview),narrative_html(missing)]
table_records=[]
def append_table(title,df,source):
    parts.append('## '+title+'\n\nSource: '+source+'\n\n'+mdtable(df))
    html_parts.append('<h2>'+html.escape(title)+'</h2><p>Source: '+html.escape(source)+'</p><div class="scroll">'+df.to_html(index=False,float_format=lambda x:format(x,'.17g'),escape=True)+'</div>')
    table_records.append(dict(panel=title,rows=len(df),columns=list(df.columns),source=source))
for number in [1,2,6,7,8,9,10,11,12,13]:
    path=next((OUT/'tables').glob(f'T{number}_*.csv'))
    append_table(path.stem.replace('_',' '),read(path),'tables/'+path.name)
append_table('T3A — All 272 main tests and decisions',r[keys+['n','df_resid','beta','se_HC3','t_HC3','p_raw','p_Holm_272','passes_Holm_0_05']],'tables/T3_all_272_tests.csv')
append_table('T3B — All 272 intervals and effect sizes',r[keys+['ci95_low','ci95_high','standardized_beta','standardized_ci95_low','standardized_ci95_high','partial_R2']],'tables/T3_all_272_tests.csv')
append_table('T4A — All alternative-model focal coefficients and marginal intervals',s[keys+['quadratic_age_beta','quadratic_age_ci_low','quadratic_age_ci_high','numeric_sex_contrast_beta','numeric_sex_contrast_ci_low','numeric_sex_contrast_ci_high']],'tables/T4_all_sensitivities.csv')
append_table('T4B — All deletion ranges and standard-error comparisons',s[keys+['base_beta','leave_one_out_min','leave_one_out_max','conventional_se','HC3_se','HC3_to_conventional_SE_ratio','quadratic_age_standardized_change','numeric_sex_contrast_standardized_change','leave_one_out_max_standardized_change']],'tables/T4_all_sensitivities.csv')
append_table('T5 — All 136 model diagnostics',d,'tables/T5_all_model_diagnostics.csv')
index=pd.DataFrame([dict(filename=p.name,rows=len(read(p)),columns=', '.join(read(p).columns)) for p in sorted((OUT/'tables').glob('*.csv'))])
append_table('Complete CSV table inventory',index,'All numerical contents embedded above; no significant-only subset')
parts.append('## Final figures\n\n'+(OUT/'Figure_Captions.md').read_text())
for name in ['F1_sample_flow','F2_lh_regional_effects','F3_rh_regional_effects','F4_age_sex_sensitivity','F5_single_record_influence']:
    html_parts.append('<figure><img src="figures/'+name+'.png" alt="'+name+'"><figcaption>'+html.escape(name)+'</figcaption></figure>')
html_parts.append(narrative_html((OUT/'Figure_Captions.md').read_text()))
(OUT/'Chat10_Final_Results_Report.md').write_text('\n\n'.join(parts)+'\n')
(OUT/'Chat10_Final_Results_Report.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Chat 10 — Final verified SPHERE results</title><style>body{font:15px system-ui;color:#19303c;margin:32px;line-height:1.55}p{max-width:1100px}h1,h2{color:#006f77}table{border-collapse:collapse;font-size:12px;white-space:nowrap}td,th{padding:7px;border-bottom:1px solid #ddd;text-align:left}th{background:#e7f0f2;position:sticky;top:0}.scroll{overflow-x:auto;margin:20px 0}img{width:100%;max-width:1400px}figure{margin:40px 0}@media print{.scroll{overflow:visible}body{font-size:10px}}</style></head><body>'+''.join(html_parts)+'</body></html>')
for name,digest in inputs.items(): assert sha(ROOT/name)==digest,name
receipt=dict(status='PASS',main_tests=272,main_sample=165,main_df=160,table_files=13,
    embedded_table_panels=table_records,main_sensitivity_serialization_max_discrepancies=max_delta,
    original_phase4_files_unchanged=True,figure_files_byte_identical_to_reviewed_versions=True,
    new_model_fits=0,input_sha256=inputs,script_sha256=sha(Path(__file__)))
(OUT/'final_verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
files=[p for p in OUT.rglob('*') if p.is_file()]+[Path(__file__)]
archive=HERE/'Chat10_Final_Results_Report_and_Evidence.zip'
manifest={str(p.relative_to(HERE)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in files}
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED) as z:
    for p in files:z.write(p,str(p.relative_to(HERE)))
    z.writestr('Manifest.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for name,item in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==item['sha256']
(HERE/'package_receipt.json').write_text(json.dumps(dict(status='PASS',sha256=sha(archive),bytes=archive.stat().st_size,files=len(files)),indent=2)+'\n')
print(json.dumps(dict(status='PASS',tests=272,tables=13,archive=str(archive),main_sensitivity_differences=max_delta)))
