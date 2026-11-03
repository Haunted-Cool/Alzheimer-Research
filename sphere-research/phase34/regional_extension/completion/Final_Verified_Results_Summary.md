# SPHERE statistical analysis: completed verification and reproducibility record

2 November 2026. Standalone research record for Chat 10; not final manuscript prose.

**The exploratory regional analysis and its planned sensitivity checks are complete and numerically verified.** It uses 165 shared synthetic-release records, 136 main regression models and 272 focal tests. Fifty GFAP–amyloid regional associations meet the prespecified exploratory Holm threshold. None of the other three outcome–predictor combinations do. The original biological H1–H4 analysis remains unexecuted because its measurement definitions remain unresolved. These two statements concern different analyses and must not be conflated.

The previously verified files have been preserved. This completion record adds independent sensitivity verification, summaries across all tests, an expanded graphical review and reproduction instructions. It does not change the model selection, data exclusions, estimates or significance threshold after seeing results.

## 1. Scope and sequence actually performed

1. The earlier Phase 3/4 work audited the local SPHERE exports, documented distributions and missing-modality patterns, specified continuous mutually adjusted H1–H4 models, and tested the software on an artificial 240-row fixture. Fixture findings are software checks, not SPHERE results.
2. The original plan required defined amyloid and tau summaries, documented sex coding, plasma scale and a qualification for synthetic-release inference. Those requirements remain unresolved. Its primary H1 and secondary H2–H4 were not run on SPHERE.
3. After the user supplied the cohort overview and requested execution, a distinct exploratory extension, E1, was specified before regional association results were inspected. All 68 exact shared cortical PET headers were selected by a fixed naming rule. The plan specified both outcomes, adjustment, scaling, all four sensitivity checks and one 272-test Holm family. E1 is prospectively specified within this project, not externally preregistered or a confirmatory analysis.
4. The regional runner read the original CSVs, joined them, formed a common sample, fitted every main model, calculated diagnostics and effect sizes, performed the sensitivities and independently checked the main-model arithmetic and all case deletions.
5. The entire regional analysis was executed again in a separate process and output directory. The two runs were compared. An initial methods/results report was saved.
6. In this completion work, the saved plan, code, outputs and source hashes were checked; the common sample and scaling were independently reconstructed; sensitivity estimates and intervals were independently recalculated using QR matrix algebra; and all diagnostic pages were visually reviewed at contact-sheet scale. No new hypothesis family or outcome-driven model selection was introduced.

## 2. Data, variables and transformations

The four inputs are `demographics_diagnosis.csv` (644 rows), `biomarkers.csv` (618), `imaging_amyloid.csv` (276), and `imaging_tau.csv` (197). Inputs are fingerprinted in `../results/input_manifest.csv`. Keys were validated and tables joined one-to-one by `adrc_id`.

The sequential intersection was **644 → 618 → 270 → 165**. No additional nonfinite-value exclusions occurred. Every main and sensitivity model uses the same 165 records, with 90 readable male and 75 readable female synthetic labels. This represents about 25.6% of the 644-row roster. Complete overlap is not evidence that missing modalities were missing at random.

The 68 regions are all exact shared headers beginning `Mean.ctx-lh-` or `Mean.ctx-rh-`. The fixed cortical scope excludes structural, subcortical and ventricular fields. `../results/field_mapping.csv` gives every exact source header. No average or global PET composite was constructed.

| Role | Executed representation |
| --- | --- |
| Dependent variables | GFAP and NFL, separately, on their released numeric scales |
| Focal independent variables | The regional amyloid and same-region tau fields, simultaneously |
| Main covariates | Age at visit and readable synthetic sex label |
| Main sex coding | female = 0, male = 1 |
| Age sensitivity | Add squared standardized age to the main model |
| Sex sensitivity | Replace readable sex with numeric `sex_orth_male` as a continuous nuisance field |

Each PET field and age was centered and divided by its sample standard deviation, using `ddof=1` in the common sample. All 137 means and standard deviations are saved in `../results/scaling.csv`. Outcomes were not normalized or logged. Five negative GFAP values were retained; NFL had no nonpositive values in this subset. There was no clipping, winsorization, imputation, positivity classification, genotype reconstruction, diagnosis-based exclusion or outlier deletion. Scaling was held fixed in sensitivity and deletion analyses.

The overview names Florbetaben and regional SUVRs at cohort level but does not map the exact exported fields to a verified normalization/reference region or identify the tau tracer. Accordingly, results concern **released PET numeric fields**, not certified SUVR, Centiloid or global pathology burden. GFAP/NFL units must not be relabeled as verified pg/mL. The continuous sex contrast is not rounded or interpreted as a probability.

## 3. Models, tests and rationale

For each region r and each outcome Y, the executed main model was:

`Y = intercept + bA*z(amyloid_r) + bT*z(tau_r) + bage*z(age) + bsex*sex_label + error`.

OLS was chosen because the outcomes and focal predictors are continuous and the question requires simultaneous adjustment. Simple correlations or group-comparison tests would answer a different question. Each main model has five parameters and 160 residual degrees of freedom. Mutual PET adjustment concerns the same region, not global amyloid or tau. The regional models are highly overlapping analyses, not independent replications.

There are 68 regions × 2 outcomes = 136 main models. Two focal slope tests per model yield 272 tests. Each is a two-sided test of a zero conditional slope, using HC3 robust standard errors and a Student t reference with n minus model rank degrees of freedom. HC3 reduces reliance on constant error variance, but its finite-sample inference remains approximate.

The decision threshold is **Holm-adjusted p < .05 across all 272 focal slopes together**. This controls familywise error under the validity of the component p-values; it does not repair uncertain synthetic-data calibration. Age and sex are nuisance adjustments, not separate discovery targets. There was no region selection based on p-values and no model selection to obtain significance.

Marginal 95% confidence intervals are coefficient ± t(.975, df) × HC3 SE. They are not simultaneous or multiplicity-adjusted confidence intervals. A marginal interval excluding zero can coexist with failure to meet the Holm threshold. A p-value is a model-based measure of compatibility with a zero slope, not the probability the hypothesis is true.

The raw slope measures change in released outcome units per one sample SD of a PET field. The fully standardized slope divides that coefficient and its interval by the outcome sample SD. Partial R² is `(SSE_reduced − SSE_full) / SSE_reduced`, omitting only the focal PET predictor from the reduced model. It describes incremental fit, not causal variance explained. No confidence interval for partial R² was calculated.

## 4. Verified main results

| Outcome | Regional predictor | Tests | Holm p < .05 | Standardized slope range across all 68 |
| --- | --- | ---: | ---: | ---: |
| GFAP | Amyloid | 68 | **50** | 0.282 to 0.445 |
| GFAP | Tau | 68 | 0 | −0.055 to 0.179 |
| NFL | Amyloid | 68 | 0 | 0.077 to 0.160 |
| NFL | Tau | 68 | 0 | 0.037 to 0.176 |

All 50 threshold-crossing associations are positive GFAP–amyloid slopes. Across all 68 GFAP–amyloid tests, Holm-adjusted p-values range from 0.00000755 to 0.2416. Adjusted p-values for the other three combinations are 1.0. Their absence of threshold-crossing results does not establish zero effects, equivalence, amyloid-specific biology or a statistically significant difference between biomarker slopes.

Exact coefficients, SEs, marginal intervals, raw and adjusted p-values, standardized estimates and partial R² are retained for all 272 tests in `../results/regional_results.csv`. `main_results_summary.csv` is the aggregate table. The effect plot uses all regions in alphabetical order; its panels have differing labeled x-axis scales.

## 5. Assumptions and diagnostics evaluated

Unique keys, finite model inputs, variable variation, full model rank and rank after every deletion were checked successfully. PET VIFs had maxima 1.586 for amyloid and 1.722 for tau, below the recorded flag threshold of 5. This does not prove an absence of all confounding or measurement dependence.

Every main model has residual-versus-fitted, residual Q-Q and residual-versus-leverage plots in the 136-page diagnostic PDF. All pages were reviewed in contact sheets during completion; the first two had earlier been reviewed separately. The plots show conspicuous positive-tail residual departures. Normality is not declared satisfied. Graphical review alone cannot establish a correct linear conditional mean or constant variance, especially for subtle curvature.

The maximum leverage was 0.235523. Cook's distance above 4/165 flagged 4–12 records per model. The maximum absolute internally studentized residual was 5.315292. These flags prompted reporting and influence checks, not removal of observations. Diagnostic details are in `../results/diagnostics.csv`, `diagnostic_page_index.csv` and `Diagnostic_Review.md`.

There was no Shapiro–Wilk test, heteroskedasticity pretest, formal nonlinear-PET model comparison, bootstrap, post-hoc power test, or independent assessment of synthetic-record dependence. HC3 does not fix mean misspecification, influential outcome values, measurement error, selection bias, temporal mismatch or synthesis uncertainty.

## 6. All planned sensitivity analyses

**Age adjustment:** Each of the 136 main models was refitted with squared standardized age, retaining linear age and all other terms. This assesses a limited departure from linear age adjustment; it is not a test of whether age should be excluded. The resulting models have six parameters and 159 residual degrees of freedom.

**Sex coding:** Each model was separately refitted with numeric `sex_orth_male` replacing the readable sex label, retaining five parameters and 160 residual degrees of freedom. This evaluates dependence on the released encoding. Neither representation is certified here as correct adjustment for source-person sex.

**Standard errors:** Conventional OLS standard errors were compared with HC3. Ratios vary across the models; HC3 is not necessarily larger. No alternative method was selected on the basis of the smaller p-value.

**Individual observations:** Each record was omitted from every main model, for 136 × 165 = 22,440 deletion evaluations. The exact OLS case-deletion formula was checked against a direct least-squares refit for every deletion. These provide coefficient ranges using the original scaling, not bootstrap intervals or corrected significance tests.

| All 68 tests per row | Largest absolute standardized change: quadratic age | Largest absolute standardized change: sex encoding | Sex sign reversals | Deletion ranges spanning zero | Largest absolute standardized change: deletion |
| --- | ---: | ---: | ---: | ---: | ---: |
| GFAP–amyloid | 0.0134 | 0.0131 | 0 | 0 | 0.0620 |
| GFAP–tau | 0.0086 | 0.0557 | 10 | 14 | 0.0443 |
| NFL–amyloid | 0.0172 | 0.0035 | 0 | 0 | 0.0729 |
| NFL–tau | 0.0130 | 0.0109 | 0 | 0 | 0.0523 |

There were no sign reversals with quadratic age in any of the 272 slopes. Among the 50 original Holm-threshold GFAP–amyloid findings, all slopes stayed positive with quadratic age, alternate sex encoding and every single deletion. Their median absolute coefficient changes were 1.93% for quadratic age and 1.15% for alternate sex encoding; maxima were 3.17% and 3.82%, respectively. Their largest absolute standardized deletion change was 0.0557.

These checks support limited coefficient and directional stability for GFAP–amyloid. They **do not establish that all 50 would retain corrected significance under every alternative specification**. Alternate multiplicity-adjusted tests were not part of E1 and were not used to search for new discoveries. The less stable GFAP–tau estimates must also be reported: ten changed sign with sex coding and fourteen had deletion ranges spanning zero. Relative percentage changes for near-zero slopes can be misleading, so standardized absolute changes are emphasized.

All estimates and sensitivity marginal intervals remain in `../results/sensitivities.csv`. The new `all_tests_with_sensitivity_changes.csv` merges all 272 tests with those results, and `sensitivity_summary.csv` reports every outcome–predictor group as well as the descriptive subset of 50 base-model findings.

## 7. Missing data and confounding

The analysis uses a common complete-modality, finite sample so comparisons are not confounded by changing sample membership across regions or outcomes. No missing value was imputed. Zero additional finite-value exclusions does not remove the substantial selection involved in reaching 165 common records from the 644-record roster. No inverse-probability weighting, multiple imputation, missingness-mechanism test or selection-bias correction was performed.

Age and released sex were adjusted, alongside same-region mutual PET adjustment. Diagnosis, APOE, renal function, vascular injury, assay batch and measurement intervals were not adjusted. Their potential confounding cannot be dismissed, but adding covariates after inspecting results would require a documented new analysis and a defensible causal/measurement rationale. The models are cross-sectional associations; temporal ordering and causal effects are unestablished.

## 8. Independent numerical and reproducibility checks

The original run independently checked all 136 main-model coefficient vectors, HC3 covariance matrices, t probabilities and confidence intervals with NumPy/SciPy calculations against statsmodels. Maximum absolute discrepancies were 9.95 × 10⁻¹⁴ for coefficients and 1.54 × 10⁻¹³ for HC3 covariance elements. Partial R² was checked against squared partial-residual correlation, and Holm values against a separate sorting/cumulative-maximum calculation. All assertions passed.

Two complete analysis runs had already succeeded. All ten non-PDF output files agree byte-for-byte. The 136-page PDFs agree in page count and extracted labels; timestamp metadata prevents a claim of byte-identical PDFs. This is local repeatability, not independent reproduction on a different computer.

Completion verification used separately constructed indexed intersections and QR-based OLS/HC3 calculations without statsmodels fitting. It rechecked the four source hashes, rebuilt all 165 records, verified all 137 scaling fields, checked 272 alternative models and **544 focal coefficient/CI triples**, and checked 272 conventional SEs. The maximum absolute sensitivity discrepancy was 6.75 × 10⁻¹⁴. No new hypothesis tests were performed by this verifier. The recorded result is PASS in `completion_verification.json`.

Hashes before and after verification confirm that the earlier plan, runner, reports and both runs' output files were unchanged. The new packaging manifest allows byte-level verification of the delivered files. Numerical verification checks implementation consistency, not the scientific validity of the measurements or synthetic inference.

## 9. Software and file references

Recorded environment: Python 3.12.14; NumPy 2.3.5; pandas 2.2.3; SciPy 1.18.1; statsmodels 0.15.0; Matplotlib 3.11.2; patsy 1.0.3; formulaic 1.2.2; pypdf 6.10.0. The last package is needed for PDF comparison and was missing from the earlier top-level requirements list. `../requirements-complete.txt` adds it without modifying the original requirements. A fresh installation in a separate environment has not been verified.

| File relative to `phase34/` | Purpose |
| --- | --- |
| `analysis.py` | Earlier audit/statistical helpers; supplies strict CSV reader and hashing to regional runner |
| `protocol.json` | Preserved original H1–H4 specification with unresolved measurement contract |
| `regional_extension/plan.json` | E1 prospective exploratory specification |
| `regional_extension/run.py` | Main models, all planned sensitivities, numerical checks and plots |
| `regional_extension/verify_and_report.py` | Earlier repeat comparison and report writer; rerunning overwrites its earlier report, so preserve evidence first |
| `regional_extension/complete_verification.py` | Independent sensitivity verification and new summary outputs; requires a new output directory |
| `regional_extension/results/` | Verified first-run results and diagnostics |
| `regional_extension/repeat/` | Verified second-run outputs |
| `regional_extension/completion/` | Completion summaries, checks and this report |
| `regional_extension/requirements-complete.txt` | Original package versions plus PDF-verification dependency |
| `regional_extension/package_completed.py` | Reproducibility archive creation, integrity verification and extracted-package check |

The model specification is implemented explicitly in the runner. Editing the JSON alone does not automatically reconfigure every model option. Any methodological change requires review of both plan and code, a new version and a new output directory.

## 10. Reproduction instructions

Keep the original results intact. From the extracted package's `phase34` directory, use Python 3.12 and install the complete requirements:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r regional_extension/requirements-complete.txt
```

Use the four original CSVs whose SHA-256 hashes match `regional_extension/results/input_manifest.csv`. No source or merged record table is included in the archive. With their folder path substituted below, check saved results and independently recalculate sensitivities without overwriting evidence:

```sh
.venv/bin/python regional_extension/complete_verification.py \
  --data-dir '/path/to/ADRC_SPHERE_all_data' \
  --output regional_extension/completion_rerun
```

To reproduce every main model, diagnostic and case-deletion check in a fresh output directory:

```sh
.venv/bin/python regional_extension/run.py \
  --data-dir '/path/to/ADRC_SPHERE_all_data' \
  --output regional_extension/new_run
```

Do not use Python `-O`: assertions enforce numerical checks. The runner refuses a nonempty output directory; the completion verifier refuses any existing output directory. Compare new numeric tables with the archived `results/` tables, allowing small floating-point differences across numerical-library builds. PDF binary identity is not expected. The archived results/repeat pair supports immediate repeat checks without rerunning the full analysis. The source path can differ, but source content must match.

## 11. Changes from the original plan and remaining tasks

The major change was a separately labeled exploratory regional question, replacing an earlier blanket restriction on all modeling with a narrower, defensible released-field analysis. The clinical global-burden questions were not silently redefined as regional findings. The original single primary H1 and three-test secondary family were **not** applied to E1; all 272 regional slopes were corrected together. This broader family and the all-region rule were specified before examining regional associations.

The sensitivity verification and graphical review added here do not change E1. The separate requirements addition repairs reproduction instructions. Earlier reports remain historical snapshots: their statements that regional analyses had not yet been performed are superseded for E1 by this record, while their statement that original H1–H4 are unexecuted remains true.

No programmed E1 sensitivity remains unfinished. Remaining scientific work is to resolve exact PET normalization and tau tracer/reference region, plasma-scale and negative-value interpretation, source-compatible sex coding, temporal alignment and release-specific inferential validity. If the project retains the original H1–H4 claims, those require a documented new measurement mapping and execution; this analysis cannot be presented as their confirmation. Because these data have now been explored, later analyses on them cannot be described as independent confirmation.

The synthetic release's dependence structure and fidelity to real-person associations are not established by this code. Standard errors and intervals do not incorporate synthesis uncertainty. The selected common sample, residual tails, limited confounder adjustment, correlated regional tests and absence of external validation constrain interpretation. An independent investigator's reproduction, a clean-environment installation check and scientific/mentor review remain outstanding. Nothing in these outputs establishes clinical utility, causation or acceptance by NHSJS.
