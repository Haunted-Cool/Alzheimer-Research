"""Verify the two completed runs and build an exploratory research record."""
from pathlib import Path
import hashlib,json,zipfile
import numpy as np
import pandas as pd
from pypdf import PdfReader

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
for f in sorted((HERE/'results').iterdir()):
    other=HERE/'repeat'/f.name
    if f.suffix=='.pdf':
        a,b=PdfReader(f),PdfReader(other)
        equal=len(a.pages)==len(b.pages)==136 and all(x.extract_text()==y.extract_text() for x,y in zip(a.pages,b.pages))
        mode='Page count and extracted labels; PDF timestamp metadata excluded'
    else:equal=f.read_bytes()==other.read_bytes();mode='byte comparison'
    if not equal:raise AssertionError(f.name)
    checks.append(dict(file=f.name,comparison=mode,match=equal,sha256=sha(f)))
prior=pd.read_csv(HERE.parent/'results/input_manifest.csv').set_index('file')
inputs=pd.read_csv(HERE/'results/input_manifest.csv')
assert all(row.sha256==prior.loc[row.file,'sha256'] for row in inputs.itertuples())
r=pd.read_csv(HERE/'results/regional_results.csv');s=pd.read_csv(HERE/'results/sensitivities.csv');d=pd.read_csv(HERE/'results/diagnostics.csv')
merged=r.merge(s,on=['region','outcome','predictor'],validate='one_to_one')
hit=merged.loc[merged.passes_Holm_0_05]
summary=dict(positive_holm_hits=int((hit.beta>0).sum()),hit_quadratic_sign_reversals=int((hit.beta*hit.quadratic_age_beta<0).sum()),
    hit_sex_contrast_sign_reversals=int((hit.beta*hit.numeric_sex_contrast_beta<0).sum()),
    hit_leave_one_out_ranges_crossing_zero=int(((hit.leave_one_out_min<=0)&(hit.leave_one_out_max>=0)).sum()),
    max_VIF_amyloid=float(d.VIF_amyloid.max()),max_VIF_tau=float(d.VIF_tau.max()),
    cooks_flag_count_range=[int(d.cooks_flag_count.min()),int(d.cooks_flag_count.max())],
    max_abs_studentized_residual=float(d.max_abs_studentized_residual.max()),max_leverage=float(d.max_leverage.max()))
validation=pd.read_csv(HERE/'results/independent_numeric_checks.csv')
verification=dict(status='PASS',scope='Two completed actual-data runs compared; this verifier does not refit',
    comparisons=checks,prior_source_hashes_match=True,numeric_check_models=len(validation),
    max_beta_discrepancy=float(validation.beta_error.max()),max_HC3_covariance_discrepancy=float(validation.covariance_error.max()),
    sensitivity_summary=summary,visual_review='Regional effect plot and first two diagnostic pages inspected. All 136 diagnostic pages generated and label/page-count checked; remaining diagnostic pages not visually reviewed.')
(HERE/'verification.json').write_text(json.dumps(verification,indent=2)+'\n')
lines=[]
for (y,p),g in r.groupby(['outcome','predictor']):
    lines.append(f'| {y} | {p} | {len(g)} | {int(g.passes_Holm_0_05.sum())} | {g.standardized_beta.min():.3f} to {g.standardized_beta.max():.3f} |')
report=f'''# Executed exploratory regional analysis: Chat 10 update

2 November 2026. Research notes, not manuscript prose. Read this addendum after the earlier Phase 3/4 report. The earlier report correctly describes the work completed at that time; this extension adds actual-data model results.

## What changed and what was executed

The user supplied a cohort overview naming Florbetaben amyloid imaging, FreeSurfer outputs and regional SUVRs and requested that the code and analysis proceed. This supports the cohort context. It still does not identify the scale/reference region of the exact Mean.* columns or the tau tracer. No field is relabeled as validated SUVR, Centiloid, or global pathology burden.

The previous blanket restriction on all modeling was broader than necessary: mathematical associations between documented released regional fields can be estimated without claiming a clinically validated burden scale. We therefore specified a new exploratory question before examining association results, saved it in plan.json, and ran that question on the actual SPHERE CSVs. This does not fill the unresolved original measurement contract or complete H1-H4 as originally framed.

The extension asks: within the linked synthetic release, how does each cortical amyloid field relate to plasma GFAP/NFL conditional on the same-region tau field, age and readable synthetic sex label, and vice versa? It is an exploratory field-level association study, not a confirmed clinical replication. The 68 regions were selected by an exhaustive header rule, not by p-values. No arbitrary composite was formed.

## Executed sequence

1. Reviewed the new overview, original plan and available schema. Found 68 matching left/right cortical Mean.ctx-* fields in both PET tables, with no unmatched cortical fields.
2. Saved extension E1 with all regions, both outcomes, common sample, model formula, four sensitivity checks and a single Holm family of 272 tests before association execution. This is not an external preregistration; existing descriptive results and literature were already known.
3. Read original files, validated keys and joined by adrc_id one-to-one. Selected a common finite sample across all chosen fields and sensitivity covariates. No raw or merged records were exported.
4. Fitted 136 main OLS models on actual data, calculated HC3 inference, diagnostics, effect sizes and sensitivity estimates, and verified arithmetic independently.
5. Repeated the entire run in a fresh process into a separate directory. Compared outputs and assembled this report.

## Data and processing

The four inputs are demographics_diagnosis.csv, biomarkers.csv, imaging_amyloid.csv and imaging_tau.csv from the previously verified local folder. Their hashes match the earlier audit. Source counts remain 644, 618, 276 and 197. Sequential intersection was 644 to 618 to 270 to 165. Finite-value exclusions were zero. Every model uses the same 165 rows, including 90 readable male and 75 readable female labels.

All 68 exact shared headers starting Mean.ctx-lh- or Mean.ctx-rh- are included, preserving hemisphere and region. The cortical-only scope excludes subcortical/ventricular uptake and all structural volume/thickness fields by a fixed naming rule. It does not assert that each cortical field has identical biological validity or tracer specificity.

GFAP and NFL remain on their released numeric scales. Five negative GFAP values are retained; NFL has no nonpositive values in this subset. No logarithms, clipping, winsorization, imputation, positivity thresholds, ratio normalization, genotype reconstruction, clinical diagnosis exclusion or outlier deletion was applied. PET fields and age are centered and divided by their common-sample SD (ddof=1). All 137 means/SDs are saved in scaling.csv. Readable sex is coded female=0/male=1 solely as a synthetic-label covariate.

## Model and testing

For each region r and each outcome Y, fit Y = intercept + bA*z(amyloid_r) + bT*z(tau_r) + bage*z(age) + bsex*sex_label + error. Each main model has five parameters and 160 residual degrees of freedom. Mutual adjustment is for the same region; it is not adjustment for global amyloid or global tau. Diagnosis, APOE, renal function, vascular injury, measurement intervals and assay batch are not adjusted. Residual confounding remains possible.

OLS estimates use HC3 covariance and a two-sided t reference with n-rank(X) degrees of freedom. Reported 95% CIs are marginal approximate intervals for a synthetic-release model. They are not simultaneous intervals and do not include SPHERE synthesis uncertainty. HC3 does not establish independence, correct misspecification, or certify real-cohort inference.

The entire inferential family contains 68 regions x 2 outcomes x 2 focal PET slopes = 272 tests. Holm correction is applied once across that full family, with alpha=.05. All results are retained in alphabetical region order; no subset was selected for publication. Age/sex coefficients are nuisance adjustments and do not enter a separate discovery search. Sensitivity analyses are descriptive, with no significance-based model selection or new claims based on their marginal intervals.

## Actual results

| Outcome | Regional predictor | Tests | Holm-adjusted p < .05 | Standardized slope range across all 68 |
| --- | --- | --- | --- | --- |
{chr(10).join(lines)}

All 50 adjusted-threshold GFAP-amyloid slopes are positive. These are correlated regional tests from the same 165 synthetic records, not 50 independent replications. The pattern is an association between released regional amyloid fields and GFAP. It cannot by itself establish amyloid-specific biology, a global-burden H1 result, causal direction or clinical utility. No adjusted-threshold finding for the other combinations does not establish absence, equivalence or that their coefficients differ significantly from the GFAP-amyloid slopes.

Exact coefficients, HC3 SEs, raw and Holm p-values, marginal CIs, standardized slopes/intervals and partial R-squared for every focal association are in regional_results.csv. Slopes use released outcome units per one sample SD of that regional PET field. Fully standardized slopes divide by the outcome sample SD. Partial R-squared compares the full model with a reduced model omitting only that PET field; it is descriptive incremental fit, not causal variance explained.

The four-panel regional_effects.png displays every standardized slope and marginal interval in alphabetical order. The panels use labeled, differing x-axis ranges. Whether a marginal interval crosses zero is not the Holm decision. The CSV's p_Holm_272 column determines that decision.

## Sensitivity and diagnostic findings

Every model was refitted with a quadratic standardized-age term, and separately with sex_orth_male replacing the readable sex label. The numeric contrast is used as a continuous nuisance field without rounding or probability interpretation. This is an encoding sensitivity; it does not certify either representation as correct adjustment for source-person sex. Both analyses retain original PET/age scaling and the same sample.

Every row was omitted in turn from every main model, giving 22,440 case-deletion coefficient evaluations. The exact OLS deletion formula was independently checked against a fresh least-squares fit for every deletion. These are influence checks, not resampled patient-cohort uncertainty. Conventional OLS SEs are also exported alongside HC3 SEs.

Among the 50 base-model Holm findings, {summary['hit_quadratic_sign_reversals']} reversed sign with quadratic age, {summary['hit_sex_contrast_sign_reversals']} reversed sign with the numeric sex contrast, and {summary['hit_leave_one_out_ranges_crossing_zero']} had a leave-one-out slope range crossing zero. This establishes sign stability under these limited checks, not preservation of multiplicity-adjusted significance in alternate models. All 272 sensitivity rows are available, including those without base-model findings.

The largest PET VIFs were {summary['max_VIF_amyloid']:.3f} for amyloid and {summary['max_VIF_tau']:.3f} for tau. No severe PET collinearity flag (>5) occurred. The largest leverage was {summary['max_leverage']:.3f}. Cook's distance >4/n flagged {summary['cooks_flag_count_range'][0]} to {summary['cooks_flag_count_range'][1]} rows per model. The largest absolute internally studentized residual was {summary['max_abs_studentized_residual']:.3f}. Flags did not trigger deletion. The first two visually inspected diagnostic pages show upper-tail residual departures; normality is not declared satisfied. The full 136-page diagnostic PDF contains residual-versus-fitted, residual Q-Q and residual-versus-leverage plots for every model. The remaining pages were generated and label-checked, not individually visually interpreted.

Thus model rank and finite values were checked, and collinearity/influence summaries were evaluated. Independence, clinical validity, temporal alignment, missing-at-random selection and complete correctness of the conditional mean remain unestablished. There was no Shapiro-Wilk or heteroskedasticity pretest, no post-hoc power test and no bootstrap. Model-based p-values remain conditional on assumptions.

## Verification and reproducibility

All 136 main models were independently checked using NumPy least squares, an explicit HC3 sandwich covariance, and SciPy t probabilities and quantiles. Largest absolute coefficient discrepancy: {verification['max_beta_discrepancy']:.3g}; largest HC3 covariance discrepancy: {verification['max_HC3_covariance_discrepancy']:.3g}. Checks used rtol=1e-8 and atol=1e-9 for coefficients/covariances/CIs. p-values used atol=1e-10. Partial R-squared was independently checked against squared partial residual correlation, and Holm against a separate sorting/cumulative-maximum implementation. All assertions passed.

Two actual-data runs completed. CSV, JSON and PNG artifacts match byte-for-byte. The diagnostic PDFs match in page count and extracted labels; timestamp metadata is excluded from binary comparison. Details are in verification.json. This is repeatability in the installed environment, not independent reproduction by another investigator or inferential calibration under repeated synthesis.

Code: run.py performs selection, fits, sensitivities, numerical checks and plots. plan.json records the prospective exploratory specification. verify_and_report.py checks repeat outputs and writes this record. The unchanged parent analysis.py supplies strict CSV parsing and hashing; it does not impose the former biological-model gate on this distinct exploratory extension.

Versions: Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, SciPy 1.18.1, statsmodels 0.15.0, Matplotlib 3.11.2. Original requirements.txt is included. No raw data are included.

## Reproduce from the package

From the extracted phase34 directory, create a Python 3.12 environment and install requirements.txt. Use the original input files whose hashes match results/input_manifest.csv. Preserve supplied evidence first. Run without Python -O because assertions enforce numerical checks.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python regional_extension/run.py --data-dir '/path/to/ADRC_SPHERE_all_data' --output regional_extension/new_run
```

The runner requires an empty output directory. To repeat the exact comparison workflow, use a separate package copy without supplied results/ and repeat/ directories, run once to each of those names, then execute verify_and_report.py. That verifier also needs the preserved parent results/input_manifest.csv, included in this package. The included completed results allow checking the verifier immediately without a new model run. Missing/duplicate/padded keys, unexpected region schema, unknown sex labels, rank deficiency and insufficient rows are rejected. Source data are never modified.

## Limits and remaining work

This update makes substantive progress: actual released-field models, effect sizes, uncertainty calculations, multiplicity correction, sensitivity checks and repeatable outputs now exist. The original biological H1-H4 analysis remains incomplete because the clinical measurement mapping is still unresolved. The new overview provides cohort-level context, not verification that the exported Mean.* values are particular SUVRs.

For a manuscript using this exploratory extension, the research question, Methods and interpretation must explicitly concern the synthetic regional fields. The earlier original-burden hypotheses cannot be retroactively relabeled as confirmed. A later validated composite would be a new, documented analysis, not an independent confirmation using data already explored. Mentor/scientific review and NHSJS suitability remain separate; this result does not guarantee publication.

Sources: user-supplied Stanford cohort overview; exact local source headers; earlier Stanford public dictionary snapshot; [Stanford SPHERE portal](https://adrc-sphere.stanford.edu/); [statsmodels robust covariance API](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html); [Holm API](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html). The code, not a generic software citation, establishes which options were actually executed.
'''
(HERE/'Exploratory_Regional_Results_and_Methods.md').write_text(report)
(HERE.parent/'CURRENT_STATUS.md').write_text('''# Current analysis status - 2 November 2026

The earlier Chat 10 report is a historical record of the audit/software phase. Actual exploratory regional analyses have now been executed on the 165-record synthetic-release subset. Read regional_extension/Exploratory_Regional_Results_and_Methods.md and regional_extension/verification.json for the new scope, results and checks. Original biological H1-H4 remain unresolved; the regional extension is not their completed test.
''')
print(json.dumps({'verification':'PASS','repeat_artifacts':len(checks),'numeric_models':len(validation),'summary':summary},indent=2))
