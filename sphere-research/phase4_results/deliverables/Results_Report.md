# SPHERE Phase 4 — Results and Figures

Research record for Chat 10, 2 November 2026. This is an evidence inventory and interpretation guide, not manuscript prose. Only existing executed analyses are presented. No new models, exclusion rules or hypothesis families were introduced.

## Confirmed scope and sample

The completed analysis is exploratory extension E1: 68 cortical regions, two outcomes, 136 mutually adjusted OLS models, and 272 focal slope tests on a common sample of 165 synthetic-release records. There are 90 readable male and 75 readable female labels. Original biological H1–H4 remain unassessed because their measurement mapping is unresolved.

The sequential linked sample is 644 roster records → 618 with blood → 270 also with amyloid → 165 also with tau. There are no further finite-value exclusions. The resulting sample is 25.62% of the roster. Table T1 and Figure 1 document these intersections. The source PET files individually contain 276 amyloid and 197 tau records; these standalone counts differ from the sequential overlap counts. Absence of additional cell-level exclusions does not remove missing-modality selection bias.

GFAP and NFL are outcomes on their released numeric scales. Every region's amyloid and tau fields are simultaneously included with standardized age and readable sex (female 0, male 1). All main models have 160 residual degrees of freedom. PET fields and age use common-sample means and sample SDs. Outcomes were not logged; five negative GFAP values were retained. No imputation or outlier removal was used. Synthetic sex encoding and clinical PET/plasma units remain unverified.

## Main findings: all completed regional tests

| Outcome | Predictor | Tests | Holm findings | Min standardized slope | Max standardized slope |
| --- | --- | --- | --- | --- | --- |
| GFAP | amyloid | 68 | 50 | 0.282 | 0.445 |
| GFAP | tau | 68 | 0 | -0.055 | 0.179 |
| NFL | amyloid | 68 | 0 | 0.077 | 0.160 |
| NFL | tau | 68 | 0 | 0.037 | 0.176 |

The significance rule is two-sided HC3 inference with a Student t reference and Holm p < .05 across the entire 272-test family. The 50 threshold-crossing results are all positive GFAP–amyloid coefficients. Across all 68 GFAP–amyloid tests, adjusted p ranges from 7.5467173e-06 to 0.24159955. All adjusted p-values in the other three combinations are 1.0. This does not mean the effects are exactly zero or that their null hypotheses have probability 1.

T3 contains all 272 test statistics, coefficients, HC3 SEs, n, residual degrees of freedom, raw and corrected p-values, 95% confidence bounds, standardized estimates and partial R². Its added t statistic is reconstructed as beta/HC3 SE from saved estimates, not a new test. Full precision is retained in machine-readable CSV; readable HTML values are rounded to six significant digits. No values are replaced with a generic “NS” label. The underlying numbers, not rounded display values, determine significance.

The 95% intervals are marginal: beta ± t(.975,160) × HC3 SE. They do not provide simultaneous 95% coverage across 272 coefficients. A nominal interval excluding zero does not guarantee Holm significance. Raw slopes are released outcome units per one sample SD of PET. Fully standardized slopes divide by the outcome SD, making those plotted effects unitless. Partial R² describes incremental model fit after the other variables; it is not causal variance explained and has no estimated interval here.

## Hypothesis evaluation

| hypothesis | association | original_status | regional_evidence |
| --- | --- | --- | --- |
| H1 | GFAP–amyloid | Unassessed as originally specified | 50/68 positive regional findings; direction consistent with expectation, not confirmation |
| H2 | GFAP–tau | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |
| H3 | NFL–amyloid | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |
| H4 | NFL–tau | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |

For the exploratory question itself, there is threshold-crossing evidence of positive GFAP–amyloid associations under the executed models. The direction is compatible with the original H1 expectation, but cannot confirm the originally defined burden hypothesis. For the other exploratory associations, evidence is inconclusive at the corrected threshold. None of H1–H4 is established as contradicted. No equivalence tests or direct tests comparing GFAP and NFL slopes were performed. A significant GFAP association and nonsignificant NFL association do not establish that their associations differ.

## Sensitivity findings, including nonsignificant results

All 136 models were separately refitted with quadratic age and with numeric sex_orth_male replacing the readable sex label. Original scaling and the sample were retained. The quadratic model has 159 residual degrees of freedom; the sex variant has 160. Alternative coefficients and marginal HC3 intervals are in T4. These descriptive checks were specified in E1; they do not create a new discovery family.

No slope changed sign with quadratic age. All 50 base-model GFAP–amyloid findings remained positive with either variant and after every single-record deletion. For those 50, median absolute coefficient changes were 1.93% with quadratic age (maximum 3.17%) and 1.15% with sex encoding (maximum 3.82%). Their largest absolute standardized deletion change was 0.0557. This supports limited coefficient stability, not preservation of corrected significance under all alternatives.

Across all 68 GFAP–tau slopes, 10 changed sign under alternate sex coding and 14 had single-deletion ranges spanning zero. Those findings qualify any broad claim that all estimates were robust. Neither NFL combination changed signs under these checks; neither had corrected main-model findings. Near-zero slopes can have misleadingly large percentage changes, so the figures emphasize absolute standardized changes. Figures 4–5 include all regions; T7 summarizes every combination, separately identifying the descriptive subset of 50 main-model findings.

All 22,440 case-deletion evaluations were checked against direct least-squares refits during the original execution. Conventional SEs were also compared with HC3 and are retained in T4. HC3/conventional ratios range from 0.7758 to 1.2732 across focal slopes; HC3 need not always be larger. No SE method was chosen based on favorable significance.

## Diagnostics and scientific concerns

All 136 models and deletion fits passed rank checks. Maximum PET VIFs were 1.586 for amyloid and 1.722 for tau. Maximum leverage was 0.235523; maximum absolute internally studentized residual was 5.315292. Cook's distance >4/165 flagged 4–12 records per model. No flags triggered deletion. T5 contains every model's R², diagnostic statistics and residual skewness.

Supplement S1 retains all 136 original diagnostic pages. Prior contact-sheet review found positive-tail residual departures; normality was not declared satisfied. Full-rank and low-VIF findings do not establish a correct linear conditional mean, independent synthetic observations or missing-at-random selection. HC3 provides approximate variance robustness, not protection against every misspecification or selection bias. Formal nonlinear PET checks, bootstrap inference, equivalence tests, multiple imputation and external validation were not performed.

The findings concern released regional fields; no field should be labeled certified SUVR, Centiloid or global pathology burden. The cohort overview does not establish normalization/reference regions for these exact exports or the tau tracer. Plasma units must not be silently labeled pg/mL. Synthetic-data generation uncertainty is not included in the intervals. The 50 regional findings are correlated observations of one dataset, not 50 replications. Only age, released sex and same-region PET were adjusted; residual confounding from diagnosis, APOE, renal function, vascular injury, timing or assay batch remains possible. These results establish neither causation, biomarker specificity nor clinical utility.

## Numerical verification and provenance

This presentation build rechecked all 272 sample sizes and t statistics, p-values, HC3 confidence limits, Holm values, and significance flags. Standardized coefficients and intervals were checked against the independently saved outcome SDs. Original partial R² verification used the reduced-model SSE and squared residual-correlation identity; it was reused, not incorrectly recomputed from a robust t statistic. All 136 main-model arithmetic checks and 544 alternative coefficient/CI checks are preserved in the prior verification records.

The previously executed repeat run agreed for all ten non-PDF output files; diagnostic PDFs matched page counts and extracted text, with different timestamp metadata. Completion verification independently rebuilt the sample and scales and verified sensitivity estimates using QR algebra. The current build checks source fingerprints before and after presentation generation. Validation results and input hashes are saved in `results_verification.json`; a package manifest fingerprints delivered outputs. Passing these checks verifies numerical consistency, not clinical validity.

The earlier distribution audit is included unchanged as T8 (GFAP, NFL and PTAU217 in available blood records and the common core), and modality availability as T9. PTAU217 remains descriptive only. The artificial 240-row software fixture is not a scientific result and is not included as evidence for hypotheses. No unperformed original H1–H4 result is substituted with a fixture estimate.

## Figures, tables and handoff

**F1_sample_flow.** Sequential one-to-one intersections: 644 → 618 → 270 → 165; no additional finite-value exclusions. These are overlapping stages, not independent groups. Source: T1.

**F2_lh_regional_effects.** Left hemisphere, all 34 regions in alphabetical order, identical axes across all eight hemisphere panels. Filled teal points: Holm p < .05 in the full 272-test family; hollow gray points: threshold not met. Bars are marginal 95% intervals, not simultaneous intervals. Models mutually adjust same-region PET fields, age and readable sex. Source: T3. Standardized slopes are unitless; clinical PET normalization remains unverified.

**F3_rh_regional_effects.** Right hemisphere, all 34 regions in alphabetical order, identical axes across all eight hemisphere panels. Filled teal points: Holm p < .05 in the full 272-test family; hollow gray points: threshold not met. Bars are marginal 95% intervals, not simultaneous intervals. Models mutually adjust same-region PET fields, age and readable sex. Source: T3. Standardized slopes are unitless; clinical PET normalization remains unverified.

**F4_age_sex_sensitivity.** Each point is one regional slope. Alternative estimates use the original sample and scaling. Identical axes and identity lines prevent visual exaggeration. These are descriptive comparisons, not alternative corrected significance tests. Source: T4.

**F5_single_record_influence.** Each point shows the largest absolute slope change across single-record deletions for one regional association. Original scaling is held fixed. These maxima are not confidence limits. All 22,440 case-deletion fits were previously checked independently. Source: T4.

PNG files are for viewing; SVG files provide scalable, editable vector figures. Hemisphere panels use identical axes, include all 34 regions per hemisphere in alphabetical order, and distinguish Holm decisions from marginal confidence bars. Regions are named as exported, with hemisphere stated in the figure title. A forest plot avoids unsupported clinical units; a regional brain map was not created because anatomical localization and measurement equivalence were not independently verified. Figures 4–5 are descriptive sensitivity plots, not additional significance plots.

T1: sample flow. T2: exact group summary. T3: all 272 main results. T4: all 272 rows of alternative estimates, intervals, deletion ranges and SE comparisons. T5: all 136 model diagnostics. T6: hypothesis assessment. T7: sensitivity summary. T8–T9: preserved earlier descriptive audits. `Results_Tables.html` offers readable tables and all main estimates. The preceding comprehensive methodology record is included in `provenance/Final_Verified_Results_Summary.md`.

For a future Results section, organize the evidence as sample selection, complete regional associations, diagnostic qualifications and sensitivity estimates, with T1–T7 and Figures 1–5. For a future Discussion section, evaluate the limited positive GFAP–amyloid pattern, inconclusive remaining combinations, unstable small GFAP–tau coefficients, selection and measurement limitations, and the distinction between synthetic associations and source-cohort biology. These are organizational notes, not drafted manuscript prose.

Remaining tasks: resolve the original measurement contract if retaining biological H1–H4; seek scientific/mentor review; and obtain independent reproduction and external validation. Publication acceptance is not determined by these numerical checks. No planned E1 sensitivity remains unfinished. Any new outcome-driven analysis must be documented as a new exploratory extension.

## Reproduce this presentation

From the project root, run `phase34/.venv/bin/python phase4_results/build_results.py --output phase4_results/new_build` using a new output directory. The script consumes the frozen phase34 outputs and does not refit models or read individual records. It requires NumPy, pandas, SciPy and Matplotlib from the recorded environment. `environment.json` records exact versions. For the original model reproduction instructions and requirements, use the existing verified methodology package. A fresh environment installation has not been tested.
