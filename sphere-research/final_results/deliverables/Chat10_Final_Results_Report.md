# Final authoritative results record for Chat 10

Date: 2 November 2026. Status: final consolidation of the actually executed exploratory regional analysis. This record is designed to audit independently written Results and Discussion sections. It is research documentation, not manuscript prose. It incorporates every reported focal main-model result, every saved sensitivity coefficient and interval, model diagnostics and saved descriptive summaries. The original biological H1–H4 remain UNASSESSED, not rejected or confirmed.

## How to audit this document

The exact numerical appendices below are part of this standalone report: it is not necessary to consult another chat to find individual results. Canonical main results are T3. Numeric values are displayed with up to 17 significant digits to preserve floating-point round trips; this is computational precision, not justified laboratory measurement precision. Routine manuscript rounding should be consistent and must not affect threshold decisions. Every significant and nonsignificant regional test is retained.

The included HTML version uses horizontally scrollable exact tables and embeds every final PNG figure with its caption. CSV files support independent calculation. The unchanged SVGs are scalable figure files. Previous numerical verification, methodology and graphical-review records are preserved alongside this report. The following overview is followed by exact appendices, a complete table inventory, figure inventory, and an explicit missing-results ledger.

## Final sample sizes and descriptive coverage

There are 165 synthetic records in every main, quadratic-age and alternate-sex model, not 165 newly studied real participants. Each leave-one-record-out model uses 164 records. The reduced models used to obtain partial R² retain 165. Counts of 136 models, 272 tests and 22,440 deletion evaluations do not represent additional participants. T11 lists the residual degrees of freedom and purpose for every model category.

Age at visit has common-sample mean 71.94553389115767 and sample SD 8.800217312696915 on the released age scale. Readable synthetic sex labels comprise 90 male and 75 female records. T12 records these available demographic summaries. T8 gives all saved blood biomarker descriptive statistics for both the 618-row blood sample and 165-row common core: n, mean, SD, range, quartiles, median, skewness, excess kurtosis, nonpositive and missing counts. PTAU217 is descriptive only. T9 enumerates all eight modality-availability patterns across the 644-record roster. T10 supplies means and SDs for age and all 136 selected PET fields used in standardization.

There is no completed original primary H1 test or original secondary H2–H4 test to report. E1 instead has one 272-test exploratory family. Region-level findings must not be placed into the original primary/secondary inferential hierarchy retrospectively.


# Preserved Results & Figures overview

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


## Missing results and interpretation ledger

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


## T1 sample flow

Source: tables/T1_sample_flow.csv

| stage | n | excluded_since_previous |
| --- | --- | --- |
| roster | 644 | 0 |
| blood | 618 | 26 |
| amyloid | 270 | 348 |
| tau | 165 | 105 |
| common_finite | 165 | 0 |

## T2 results summary

Source: tables/T2_results_summary.csv

| outcome | predictor | tests | Holm_passes | standardized_beta_min | standardized_beta_max | Holm_p_min | Holm_p_max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GFAP | amyloid | 68 | 50 | 0.28248001237068932 | 0.44536027873816592 | 7.5467172608604817e-06 | 0.24159954599423061 |
| GFAP | tau | 68 | 0 | -0.054821902881866003 | 0.17921797110924981 | 1 | 1 |
| NFL | amyloid | 68 | 0 | 0.0770398383133655 | 0.15989152456006689 | 1 | 1 |
| NFL | tau | 68 | 0 | 0.036882610026631499 | 0.17591369078238039 | 1 | 1 |

## T6 hypothesis assessment

Source: tables/T6_hypothesis_assessment.csv

| hypothesis | association | original_status | regional_evidence |
| --- | --- | --- | --- |
| H1 | GFAP–amyloid | Unassessed as originally specified | 50/68 positive regional findings; direction consistent with expectation, not confirmation |
| H2 | GFAP–tau | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |
| H3 | NFL–amyloid | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |
| H4 | NFL–tau | Unassessed as originally specified | 0/68 adjusted findings; exploratory evidence inconclusive, not evidence of absence |

## T7 sensitivity summary

Source: tables/T7_sensitivity_summary.csv

| scope | outcome | predictor | n_tests | quadratic_age_sign_reversals | quadratic_age_median_abs_standardized_change | quadratic_age_max_abs_standardized_change | quadratic_age_median_abs_percent_change | quadratic_age_max_abs_percent_change | numeric_sex_contrast_sign_reversals | numeric_sex_contrast_median_abs_standardized_change | numeric_sex_contrast_max_abs_standardized_change | numeric_sex_contrast_median_abs_percent_change | numeric_sex_contrast_max_abs_percent_change | loo_ranges_crossing_zero | loo_max_abs_standardized_change | SE_ratio_min | SE_ratio_max |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_272 | GFAP | amyloid | 68 | 0 | 0.00750832671993849 | 0.013401574685530606 | 2.0566949066458888 | 4.1800685384103584 | 0 | 0.0051431181613530788 | 0.013085262762055599 | 1.3979817068262403 | 3.8536714090972417 | 0 | 0.061955260343277148 | 0.96334341944771329 | 1.2424264440421982 |
| all_272 | GFAP | tau | 68 | 0 | 0.0021314701777495107 | 0.0085587780748216987 | 2.9815930293221382 | 72.718520708946727 | 10 | 0.040370603136252556 | 0.055743170947215398 | 49.398188714001563 | 1104.2247139683845 | 14 | 0.044287766079917378 | 0.77581726838952636 | 1.1076895827872357 |
| all_272 | NFL | amyloid | 68 | 0 | 0.011763358982125792 | 0.017221541984645025 | 10.50602679075055 | 19.69230450799251 | 0 | 0.00080316441265776298 | 0.0034784183357768127 | 0.75838623313842446 | 4.0615398772885394 | 0 | 0.072879037190558243 | 0.99581472739046162 | 1.2731687714101174 |
| all_272 | NFL | tau | 68 | 0 | 0.0033330133838654213 | 0.012997458008330005 | 3.6576093187824235 | 17.989214027475292 | 0 | 0.0057793033453451305 | 0.010915519822730022 | 6.2049116192742275 | 15.946041380638565 | 0 | 0.052266550657978847 | 0.78959524640935563 | 1.0958026038551563 |
| base_Holm_pass_50 | GFAP | amyloid | 50 | 0 | 0.0071825313378224053 | 0.013401574685530606 | 1.93221742851004 | 3.1724127253201444 | 0 | 0.0045411329732879969 | 0.013085262762055599 | 1.151206067149662 | 3.8184906124135907 | 0 | 0.055749280587130051 | 0.96334341944771329 | 1.2152840405787737 |

## T8 prior distribution audit

Source: tables/T8_prior_distribution_audit.csv

| population | field | n | mean | sd | minimum | q1 | median | q3 | maximum | skewness | excess_kurtosis | nonpositive | missing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all_blood | GFAP | 618 | 73.499601537741498 | 35.416409449319673 | -35.312267303466797 | 49.857119560241699 | 72.034271240234375 | 93.801137924194336 | 239.27882385253903 | 0.464686731263177 | 1.2465963960977557 | 8 | 0 |
| all_blood | NFL | 618 | 25.627918515004772 | 12.413634110059812 | -48.479907989501953 | 18.472152709960938 | 24.911463737487793 | 32.761792182922363 | 82.226715087890625 | 0.15653711739706133 | 3.765073533653454 | 8 | 0 |
| all_blood | PTAU217 | 618 | 0.34184345013961576 | 0.41848946554247674 | -1.2501749992370603 | 0.11964067444205277 | 0.27732779085636139 | 0.52892588078975677 | 2.5257136821746826 | 0.90633402736203617 | 3.7314640578095375 | 85 | 0 |
| dual_PET_blood | GFAP | 165 | 74.251702900366354 | 36.23404123717151 | -23.427310943603516 | 48.987495422363281 | 74.06488037109375 | 97.040740966796875 | 239.27882385253903 | 0.36166076054084378 | 2.0973555171770339 | 5 | 0 |
| dual_PET_blood | NFL | 165 | 25.923891913529598 | 11.544251177796944 | 0.77875125408172607 | 19.108316421508789 | 25.254194259643555 | 32.610683441162109 | 78.296760559082031 | 0.87853966334519162 | 2.7483994220324082 | 0 | 0 |
| dual_PET_blood | PTAU217 | 165 | 0.3468530647188538 | 0.42894902429133108 | -1.2501749992370603 | 0.099387817084789207 | 0.30309993028640742 | 0.56375914812088013 | 2.0314860343933105 | 0.46224007462011069 | 2.6417576850622293 | 27 | 0 |

## T9 prior availability audit

Source: tables/T9_prior_availability_audit.csv

| biomarkers | imaging_amyloid | imaging_tau | n |
| --- | --- | --- | --- |
| True | False | False | 321 |
| True | True | True | 165 |
| True | True | False | 105 |
| True | False | True | 27 |
| False | False | False | 19 |
| False | True | True | 4 |
| False | True | False | 2 |
| False | False | True | 1 |

## T10 predictor descriptives and scaling

Source: tables/T10_predictor_descriptives_and_scaling.csv

| field | mean | sd |
| --- | --- | --- |
| age_at_visit | 71.945533891157666 | 8.8002173126969154 |
| amy__Mean.ctx-lh-bankssts | 16356.152558297821 | 6283.7950194701762 |
| amy__Mean.ctx-lh-caudalanteriorcingulate | 14602.038059269298 | 5765.4936988021136 |
| amy__Mean.ctx-lh-caudalmiddlefrontal | 14367.492106489703 | 5585.0982933398636 |
| amy__Mean.ctx-lh-cuneus | 13633.56073922822 | 5116.1559598245658 |
| amy__Mean.ctx-lh-entorhinal | 11155.453050648082 | 3902.1227241623055 |
| amy__Mean.ctx-lh-frontalpole | 12472.804426713423 | 5755.0552217269478 |
| amy__Mean.ctx-lh-fusiform | 13521.641976651279 | 5204.8228602095696 |
| amy__Mean.ctx-lh-inferiorparietal | 14883.737367572206 | 5978.5360244642961 |
| amy__Mean.ctx-lh-inferiortemporal | 14361.16434585109 | 5644.2746017819773 |
| amy__Mean.ctx-lh-insula | 13310.020266261245 | 4848.4277142670926 |
| amy__Mean.ctx-lh-isthmuscingulate | 14262.615350896662 | 5450.0597906707635 |
| amy__Mean.ctx-lh-lateraloccipital | 14268.033570815578 | 5265.3597297447805 |
| amy__Mean.ctx-lh-lateralorbitofrontal | 14503.192396314216 | 5432.5881932014872 |
| amy__Mean.ctx-lh-lingual | 12349.4059477835 | 4633.2584223912772 |
| amy__Mean.ctx-lh-medialorbitofrontal | 12931.143306107955 | 5365.7722027718373 |
| amy__Mean.ctx-lh-middletemporal | 13814.238179154829 | 5413.3292710745582 |
| amy__Mean.ctx-lh-paracentral | 14296.859765809955 | 5235.1915004113234 |
| amy__Mean.ctx-lh-parahippocampal | 11807.705324554443 | 4196.7803334988148 |
| amy__Mean.ctx-lh-parsopercularis | 14026.190990471117 | 5467.7475753812741 |
| amy__Mean.ctx-lh-parsorbitalis | 14178.970722360322 | 5558.3943993076109 |
| amy__Mean.ctx-lh-parstriangularis | 14421.203506747159 | 5546.9143179170997 |
| amy__Mean.ctx-lh-pericalcarine | 15050.685758463542 | 5696.0468530711969 |
| amy__Mean.ctx-lh-postcentral | 13353.096074884588 | 4845.1715087546136 |
| amy__Mean.ctx-lh-posteriorcingulate | 15003.335206557766 | 6101.23743910753 |
| amy__Mean.ctx-lh-precentral | 13717.014920691288 | 4683.51966486529 |
| amy__Mean.ctx-lh-precuneus | 15375.566180974787 | 6634.1932903542547 |
| amy__Mean.ctx-lh-rostralanteriorcingulate | 13694.43391677394 | 5734.0706999004869 |
| amy__Mean.ctx-lh-rostralmiddlefrontal | 14357.276187411222 | 6145.2174118341454 |
| amy__Mean.ctx-lh-superiorfrontal | 13661.440685665246 | 5505.8631781788326 |
| amy__Mean.ctx-lh-superiorparietal | 14603.716098484849 | 5813.5055653596582 |
| amy__Mean.ctx-lh-superiortemporal | 13291.219166888613 | 4998.8608293308362 |
| amy__Mean.ctx-lh-supramarginal | 14442.662948330966 | 5715.2297789985887 |
| amy__Mean.ctx-lh-temporalpole | 11442.717093542851 | 4003.8504114574966 |
| amy__Mean.ctx-lh-transversetemporal | 13218.332758123224 | 4977.4178433002671 |
| amy__Mean.ctx-rh-bankssts | 16843.818325343276 | 6781.3588598194265 |
| amy__Mean.ctx-rh-caudalanteriorcingulate | 14792.022916666667 | 5883.7553157667253 |
| amy__Mean.ctx-rh-caudalmiddlefrontal | 14712.502506510416 | 5822.5236795482697 |
| amy__Mean.ctx-rh-cuneus | 13170.886861257843 | 4984.6490791090318 |
| amy__Mean.ctx-rh-entorhinal | 11308.306604171521 | 3948.2363254415523 |
| amy__Mean.ctx-rh-frontalpole | 12465.04770267371 | 5692.6493031761147 |
| amy__Mean.ctx-rh-fusiform | 13486.363988517993 | 5347.0103948764381 |
| amy__Mean.ctx-rh-inferiorparietal | 15111.829741506866 | 6420.9735636718415 |
| amy__Mean.ctx-rh-inferiortemporal | 14426.97392504143 | 5911.6848908735392 |
| amy__Mean.ctx-rh-insula | 13432.372586706913 | 5035.9588399952936 |
| amy__Mean.ctx-rh-isthmuscingulate | 14196.184860229492 | 5516.7549169893846 |
| amy__Mean.ctx-rh-lateraloccipital | 14305.723501124527 | 5488.5350517730749 |
| amy__Mean.ctx-rh-lateralorbitofrontal | 14332.380539772726 | 5529.231713243591 |
| amy__Mean.ctx-rh-lingual | 12082.316661487926 | 4554.9394811422799 |
| amy__Mean.ctx-rh-medialorbitofrontal | 13404.619805168382 | 5621.2347969321536 |
| amy__Mean.ctx-rh-middletemporal | 14148.64980764678 | 5815.8673615333273 |
| amy__Mean.ctx-rh-paracentral | 14543.832739396528 | 5499.4820189916709 |
| amy__Mean.ctx-rh-parahippocampal | 11974.211082504735 | 4448.2106506645232 |
| amy__Mean.ctx-rh-parsopercularis | 14530.191586766099 | 5779.93765998865 |
| amy__Mean.ctx-rh-parsorbitalis | 14320.664213423295 | 5790.4168230364567 |
| amy__Mean.ctx-rh-parstriangularis | 14790.536131332859 | 5797.7104666874311 |
| amy__Mean.ctx-rh-pericalcarine | 14314.995990360145 | 5635.8816472378239 |
| amy__Mean.ctx-rh-postcentral | 13483.620631362453 | 4992.6854806249039 |
| amy__Mean.ctx-rh-posteriorcingulate | 15008.744296727036 | 6214.1515915050968 |
| amy__Mean.ctx-rh-precentral | 13871.995474520596 | 4832.881829223792 |
| amy__Mean.ctx-rh-precuneus | 15118.257215835109 | 6619.3086071073831 |
| amy__Mean.ctx-rh-rostralanteriorcingulate | 14372.270588452888 | 5958.1333763249922 |
| amy__Mean.ctx-rh-rostralmiddlefrontal | 14747.101191850143 | 6268.1061267908053 |
| amy__Mean.ctx-rh-superiorfrontal | 14062.95234079072 | 5701.3365638005507 |
| amy__Mean.ctx-rh-superiorparietal | 14220.33310546875 | 5711.281128029982 |
| amy__Mean.ctx-rh-superiortemporal | 13521.251528468276 | 5340.2390835195556 |
| amy__Mean.ctx-rh-supramarginal | 14754.622351444128 | 6030.3790951559067 |
| amy__Mean.ctx-rh-temporalpole | 11994.634256813742 | 4274.8712695591794 |
| amy__Mean.ctx-rh-transversetemporal | 12962.816814630682 | 5101.8585755957292 |
| tau__Mean.ctx-lh-bankssts | 4429.4831192478987 | 2160.2907092834093 |
| tau__Mean.ctx-lh-caudalanteriorcingulate | 3473.6269496108548 | 1189.467143425431 |
| tau__Mean.ctx-lh-caudalmiddlefrontal | 3911.6921612363872 | 1569.7040979275691 |
| tau__Mean.ctx-lh-cuneus | 4482.051258526426 | 1990.3591880314782 |
| tau__Mean.ctx-lh-entorhinal | 4982.0224637118254 | 2036.4267419620376 |
| tau__Mean.ctx-lh-frontalpole | 3448.8853830048533 | 1159.8187796443972 |
| tau__Mean.ctx-lh-fusiform | 4616.1218909061317 | 1941.9563713426492 |
| tau__Mean.ctx-lh-inferiorparietal | 4607.4123875473488 | 2121.9353480481491 |
| tau__Mean.ctx-lh-inferiortemporal | 4991.8890937573979 | 2124.9657248419749 |
| tau__Mean.ctx-lh-insula | 3403.6951087720468 | 1226.720039984953 |
| tau__Mean.ctx-lh-isthmuscingulate | 4079.1754899458451 | 1678.5775708276497 |
| tau__Mean.ctx-lh-lateraloccipital | 4967.2962232185137 | 2057.9855119953804 |
| tau__Mean.ctx-lh-lateralorbitofrontal | 4020.0954837683475 | 1338.8825513457416 |
| tau__Mean.ctx-lh-lingual | 4406.3533804228809 | 1777.0472042508163 |
| tau__Mean.ctx-lh-medialorbitofrontal | 3356.6643336440579 | 1196.990958438518 |
| tau__Mean.ctx-lh-middletemporal | 4769.9995365027225 | 1955.0539549838243 |
| tau__Mean.ctx-lh-paracentral | 3740.8157208067 | 1299.0431740775948 |
| tau__Mean.ctx-lh-parahippocampal | 4399.9280023748224 | 1627.0311897131073 |
| tau__Mean.ctx-lh-parsopercularis | 3802.1767130533854 | 1315.1274474561831 |
| tau__Mean.ctx-lh-parsorbitalis | 4431.0994815710819 | 1411.0964974178703 |
| tau__Mean.ctx-lh-parstriangularis | 4028.1399497292259 | 1293.5635176651472 |
| tau__Mean.ctx-lh-pericalcarine | 4042.3171246152938 | 1573.0713835415265 |
| tau__Mean.ctx-lh-postcentral | 3779.2242575905539 | 1290.6994359653754 |
| tau__Mean.ctx-lh-posteriorcingulate | 3784.1092621774383 | 1446.3366296089091 |
| tau__Mean.ctx-lh-precentral | 3759.1454342004026 | 1308.4852093349891 |
| tau__Mean.ctx-lh-precuneus | 4131.1979887991238 | 2043.8652908860849 |
| tau__Mean.ctx-lh-rostralanteriorcingulate | 3290.0428470495976 | 1168.7369667846622 |
| tau__Mean.ctx-lh-rostralmiddlefrontal | 3774.9058349609377 | 1383.0242428090467 |
| tau__Mean.ctx-lh-superiorfrontal | 3587.8643909801135 | 1229.6684096306387 |
| tau__Mean.ctx-lh-superiorparietal | 4316.016203169389 | 1932.0674151837418 |
| tau__Mean.ctx-lh-superiortemporal | 4088.8655905983665 | 1505.6326540833568 |
| tau__Mean.ctx-lh-supramarginal | 4177.8806607333099 | 1658.7314292703602 |
| tau__Mean.ctx-lh-temporalpole | 4014.3875088778409 | 1433.5765160979461 |
| tau__Mean.ctx-lh-transversetemporal | 3381.3522414698746 | 1314.7003939124056 |
| tau__Mean.ctx-rh-bankssts | 4533.5420635338987 | 2484.5792961971456 |
| tau__Mean.ctx-rh-caudalanteriorcingulate | 3508.9157964533024 | 1226.7856785260572 |
| tau__Mean.ctx-rh-caudalmiddlefrontal | 3977.5410374034536 | 1596.3534178292339 |
| tau__Mean.ctx-rh-cuneus | 4511.2397632945667 | 1982.2641695649859 |
| tau__Mean.ctx-rh-entorhinal | 5206.5472558223837 | 2091.9714036720175 |
| tau__Mean.ctx-rh-frontalpole | 3489.8101680871214 | 1147.1810728453279 |
| tau__Mean.ctx-rh-fusiform | 4670.9113826867306 | 2022.5957960821099 |
| tau__Mean.ctx-rh-inferiorparietal | 4731.6163871996332 | 2219.9235652351813 |
| tau__Mean.ctx-rh-inferiortemporal | 5046.5131851369688 | 2385.4793106179745 |
| tau__Mean.ctx-rh-insula | 3425.0482063062263 | 1231.6083273850329 |
| tau__Mean.ctx-rh-isthmuscingulate | 4111.0989766438806 | 1740.6511976807255 |
| tau__Mean.ctx-rh-lateraloccipital | 5046.305255589341 | 2139.8599003214076 |
| tau__Mean.ctx-rh-lateralorbitofrontal | 4086.0428629557291 | 1410.8990447556334 |
| tau__Mean.ctx-rh-lingual | 4426.2050347530485 | 1746.3115535660977 |
| tau__Mean.ctx-rh-medialorbitofrontal | 3359.8017851858426 | 1208.8037816654312 |
| tau__Mean.ctx-rh-middletemporal | 4791.2855221835052 | 2219.3893994278988 |
| tau__Mean.ctx-rh-paracentral | 3791.9384881684273 | 1269.7019635795759 |
| tau__Mean.ctx-rh-parahippocampal | 4372.1218478578512 | 1729.0612465082729 |
| tau__Mean.ctx-rh-parsopercularis | 3852.9823338364108 | 1354.3333469721222 |
| tau__Mean.ctx-rh-parsorbitalis | 4372.9450032552086 | 1422.4002401447931 |
| tau__Mean.ctx-rh-parstriangularis | 4076.8529755563445 | 1338.3265620185755 |
| tau__Mean.ctx-rh-pericalcarine | 3959.6017167524856 | 1557.5081718041511 |
| tau__Mean.ctx-rh-postcentral | 3728.0717992609198 | 1245.6587974119923 |
| tau__Mean.ctx-rh-posteriorcingulate | 3825.0545911384352 | 1475.3398658705714 |
| tau__Mean.ctx-rh-precentral | 3748.1363026936847 | 1251.0407757697046 |
| tau__Mean.ctx-rh-precuneus | 4096.2907608494615 | 1926.5768117899825 |
| tau__Mean.ctx-rh-rostralanteriorcingulate | 3393.8597278941761 | 1235.6885231765557 |
| tau__Mean.ctx-rh-rostralmiddlefrontal | 3808.503875547467 | 1339.1469007441015 |
| tau__Mean.ctx-rh-superiorfrontal | 3636.7530145818537 | 1211.0830129515889 |
| tau__Mean.ctx-rh-superiorparietal | 4247.6556620279944 | 1822.3765282840682 |
| tau__Mean.ctx-rh-superiortemporal | 4041.5053017356181 | 1559.3060890710108 |
| tau__Mean.ctx-rh-supramarginal | 4189.7641884543682 | 1666.2131399086049 |
| tau__Mean.ctx-rh-temporalpole | 4159.3110895330256 | 1555.1913671195741 |
| tau__Mean.ctx-rh-transversetemporal | 3252.2769224224667 | 1172.9956382341361 |

## T11 analysis sample sizes

Source: tables/T11_analysis_sample_sizes.csv

| analysis | model_or_variable_count | records_per_analysis | residual_df | purpose |
| --- | --- | --- | --- | --- |
| Main regional OLS | 136 | 165 | 160 | 272 focal tests |
| Quadratic-age sensitivity | 136 | 165 | 159 | 272 focal estimates and intervals; descriptive |
| Numeric-sex sensitivity | 136 | 165 | 160 | 272 focal estimates and intervals; descriptive |
| Conventional SE comparison | 136 | 165 | 160 | 272 focal SE comparisons; same fitted main models |
| Single-record deletion | 22440 | 164 | 159 | One record omitted from each main model; original scaling |
| Reduced models for partial R2 | 272 | 165 | 161 | Omit one PET predictor; descriptive fit comparison |
| Blood descriptive audit | 3 variables | 618 | not applicable | GFAP, NFL, PTAU217 |
| Common-core descriptive audit | 3 variables | 165 | not applicable | GFAP, NFL, PTAU217 |

## T12 available demographic descriptives

Source: tables/T12_available_demographic_descriptives.csv

| variable | statistic | value | units |
| --- | --- | --- | --- |
| Common sample | Records | 165 | count |
| Readable male label | Records | 90 | count |
| Readable female label | Records | 75 | count |
| Age at visit | Mean | 71.945533891157666 | released age scale |
| Age at visit | Sample SD | 8.8002173126969154 | released age scale |

## T13 final figure inventory

Source: tables/T13_final_figure_inventory.csv

| filenames_in_figures_folder | variables | measurement_units | scientific_purpose |
| --- | --- | --- | --- |
| F1_sample_flow.png; F1_sample_flow.svg | Sequential linked sample counts | Synthetic records (count) | Document selection from 644 to 165 |
| F2_lh_regional_effects.png; F2_lh_regional_effects.svg | Left hemisphere: all GFAP/NFL and amyloid/tau slopes and marginal CIs | Standardized slopes and CIs (unitless) | Show all 136 left-hemisphere tests with Holm markers |
| F3_rh_regional_effects.png; F3_rh_regional_effects.svg | Right hemisphere: all GFAP/NFL and amyloid/tau slopes and marginal CIs | Standardized slopes and CIs (unitless) | Show all 136 right-hemisphere tests with Holm markers |
| F4_age_sex_sensitivity.png; F4_age_sex_sensitivity.svg | Main versus quadratic-age/alternate-sex slopes | Standardized slopes (unitless) | Assess coefficient stability, not alternate significance |
| F5_single_record_influence.png; F5_single_record_influence.svg | Main slope versus maximum absolute single-deletion change | Standardized slopes/changes (unitless) | Assess individual-record influence for all 272 slopes |
| S1_original_model_diagnostics.pdf | 136 pages: residual versus fitted; Q-Q; residual versus leverage | Fitted/residual values: released GFAP or NFL units; leverage and theoretical normal quantiles: unitless | Identify residual departures and influential observations |

## T3A — All 272 main tests and decisions

Source: tables/T3_all_272_tests.csv

| region | outcome | predictor | n | df_resid | beta | se_HC3 | t_HC3 | p_raw | p_Holm_272 | passes_Holm_0_05 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctx-lh-bankssts | GFAP | amyloid | 165 | 160 | 11.520263335693542 | 3.1000994501454646 | 3.7160947643640858 | 0.00027926310227439113 | 0.061996408704914831 | False |
| ctx-lh-bankssts | GFAP | tau | 165 | 160 | 4.594947777022691 | 2.9811256525465879 | 1.5413465625300016 | 0.12520790555155029 | 1 | False |
| ctx-lh-bankssts | NFL | amyloid | 165 | 160 | 1.1182234402902655 | 1.0908873493926268 | 1.0250585827334588 | 0.30688280685104408 | 1 | False |
| ctx-lh-bankssts | NFL | tau | 165 | 160 | 1.1419347556943751 | 0.83247709178017493 | 1.3717311466823112 | 0.17206757813954057 | 1 | False |
| ctx-lh-caudalanteriorcingulate | GFAP | amyloid | 165 | 160 | 15.214439088626271 | 2.9807045168957842 | 5.1043097369715635 | 9.3199913125708356e-07 | 0.00023859177760181339 | True |
| ctx-lh-caudalanteriorcingulate | GFAP | tau | 165 | 160 | -0.14760706120525335 | 2.5152237687839523 | -0.058685458938954632 | 0.95327587213377851 | 1 | False |
| ctx-lh-caudalanteriorcingulate | NFL | amyloid | 165 | 160 | 1.6145907364635508 | 1.1571204795731749 | 1.3953523120246927 | 0.16484327729897272 | 1 | False |
| ctx-lh-caudalanteriorcingulate | NFL | tau | 165 | 160 | 0.78795863253168841 | 0.98209838904713187 | 0.80232147951713373 | 0.423557111642755 | 1 | False |
| ctx-lh-caudalmiddlefrontal | GFAP | amyloid | 165 | 160 | 13.807702457297829 | 3.1298156718862047 | 4.4116663423109905 | 1.8768939757971339e-05 | 0.0044857766021551499 | True |
| ctx-lh-caudalmiddlefrontal | GFAP | tau | 165 | 160 | 4.1536826827891993 | 2.8012487033314 | 1.4827968248050984 | 0.14009541559667935 | 1 | False |
| ctx-lh-caudalmiddlefrontal | NFL | amyloid | 165 | 160 | 1.5464421699185047 | 1.1461052682307289 | 1.349302034276298 | 0.17914622382747217 | 1 | False |
| ctx-lh-caudalmiddlefrontal | NFL | tau | 165 | 160 | 1.413505198397313 | 0.86765389919466529 | 1.6291117918207862 | 0.10525665229568582 | 1 | False |
| ctx-lh-cuneus | GFAP | amyloid | 165 | 160 | 11.409331061088983 | 3.2196090563470716 | 3.543700760375506 | 0.00051740122499775785 | 0.11124126337451794 | False |
| ctx-lh-cuneus | GFAP | tau | 165 | 160 | 2.3111659190100431 | 2.989624578006147 | 0.77306225537904016 | 0.44062610110711919 | 1 | False |
| ctx-lh-cuneus | NFL | amyloid | 165 | 160 | 1.3818536408612667 | 1.0480448806135203 | 1.3185061693658924 | 0.18921851712869173 | 1 | False |
| ctx-lh-cuneus | NFL | tau | 165 | 160 | 1.3194883602568681 | 0.8070158051915246 | 1.6350217080862763 | 0.10401036579410049 | 1 | False |
| ctx-lh-entorhinal | GFAP | amyloid | 165 | 160 | 10.244394729481941 | 3.1011619587386838 | 3.3034052609263207 | 0.0011785343707035639 | 0.24159954599423061 | False |
| ctx-lh-entorhinal | GFAP | tau | 165 | 160 | 4.7098856862589757 | 2.9569606911957091 | 1.5928130868572468 | 0.11317578322316998 | 1 | False |
| ctx-lh-entorhinal | NFL | amyloid | 165 | 160 | 1.3116913147858669 | 1.0690112803391507 | 1.227013539435921 | 0.22161992028832239 | 1 | False |
| ctx-lh-entorhinal | NFL | tau | 165 | 160 | 0.50988902907574163 | 0.88487311609352104 | 0.57622841038132766 | 0.56527048974317751 | 1 | False |
| ctx-lh-frontalpole | GFAP | amyloid | 165 | 160 | 15.306747634784694 | 2.7488064064789541 | 5.5685069704096266 | 1.0629894625786163e-07 | 2.8594416543364777e-05 | True |
| ctx-lh-frontalpole | GFAP | tau | 165 | 160 | 1.1226646283864132 | 2.3103619052196471 | 0.48592587414554039 | 0.62768453872626984 | 1 | False |
| ctx-lh-frontalpole | NFL | amyloid | 165 | 160 | 1.5618671880484698 | 0.96648095119355693 | 1.6160351490835281 | 0.10805678138650712 | 1 | False |
| ctx-lh-frontalpole | NFL | tau | 165 | 160 | 0.86494199756621004 | 0.96192659458391583 | 0.89917671726327852 | 0.36990977715441697 | 1 | False |
| ctx-lh-fusiform | GFAP | amyloid | 165 | 160 | 11.231378860424245 | 3.1145910914564325 | 3.6060524578114919 | 0.00041499637188921847 | 0.089639216328071189 | False |
| ctx-lh-fusiform | GFAP | tau | 165 | 160 | 5.0367129754820033 | 2.9213326276621556 | 1.7241148535395352 | 0.086618527950977936 | 1 | False |
| ctx-lh-fusiform | NFL | amyloid | 165 | 160 | 1.1021510445708551 | 1.1719044580360543 | 0.94047858339740764 | 0.34838984039634996 | 1 | False |
| ctx-lh-fusiform | NFL | tau | 165 | 160 | 1.5358255898728563 | 0.98015529930666334 | 1.5669206614087174 | 0.11910886059131866 | 1 | False |
| ctx-lh-inferiorparietal | GFAP | amyloid | 165 | 160 | 10.976396511669533 | 3.1307191156007743 | 3.5060304378545948 | 0.00059033413228881258 | 0.12633150430980589 | False |
| ctx-lh-inferiorparietal | GFAP | tau | 165 | 160 | 6.4937913556147695 | 2.9145914913166102 | 2.2280279671993846 | 0.02727302460290407 | 1 | False |
| ctx-lh-inferiorparietal | NFL | amyloid | 165 | 160 | 0.98293657686037483 | 1.0930610536156511 | 0.89925130312620316 | 0.36987017823195623 | 1 | False |
| ctx-lh-inferiorparietal | NFL | tau | 165 | 160 | 1.5631225842402485 | 0.83882005969713513 | 1.863477829565295 | 0.064227779206829025 | 1 | False |
| ctx-lh-inferiortemporal | GFAP | amyloid | 165 | 160 | 11.720116016544756 | 3.3816249443733777 | 3.4658237413482644 | 0.00067877386478796176 | 0.1439000593350479 | False |
| ctx-lh-inferiortemporal | GFAP | tau | 165 | 160 | 5.1202363409841114 | 3.3000601397796197 | 1.551558494120669 | 0.12274367030997013 | 1 | False |
| ctx-lh-inferiortemporal | NFL | amyloid | 165 | 160 | 1.1091576266743313 | 1.2342875039507222 | 0.89862177420100775 | 0.37020448949596241 | 1 | False |
| ctx-lh-inferiortemporal | NFL | tau | 165 | 160 | 1.5286750761143866 | 1.0238960570329627 | 1.4929983035037446 | 0.1374069201214797 | 1 | False |
| ctx-lh-insula | GFAP | amyloid | 165 | 160 | 14.144620912752261 | 2.9275940705542962 | 4.8314829760787799 | 3.150627529130157e-06 | 0.0007876568822825392 | True |
| ctx-lh-insula | GFAP | tau | 165 | 160 | -0.65977027255522103 | 2.6989750199278189 | -0.2444521596842589 | 0.80719385285742162 | 1 | False |
| ctx-lh-insula | NFL | amyloid | 165 | 160 | 1.4358049395749857 | 1.1796667907947977 | 1.2171275404028417 | 0.22534786703056425 | 1 | False |
| ctx-lh-insula | NFL | tau | 165 | 160 | 0.90315406405808618 | 0.98707320825227085 | 0.91498184380591852 | 0.36157804054508752 | 1 | False |
| ctx-lh-isthmuscingulate | GFAP | amyloid | 165 | 160 | 12.236352810149182 | 3.1825417296475762 | 3.8448365644852656 | 0.00017376640641862952 | 0.038891159032960386 | True |
| ctx-lh-isthmuscingulate | GFAP | tau | 165 | 160 | 4.0439201543291583 | 2.9072051733077053 | 1.3909992289013928 | 0.16615700951169934 | 1 | False |
| ctx-lh-isthmuscingulate | NFL | amyloid | 165 | 160 | 1.2389043091104681 | 1.1951713190526809 | 1.0365913985389568 | 0.30149041068934679 | 1 | False |
| ctx-lh-isthmuscingulate | NFL | tau | 165 | 160 | 1.3998940628139962 | 0.93298672195070964 | 1.5004437146619474 | 0.13547023691330667 | 1 | False |
| ctx-lh-lateraloccipital | GFAP | amyloid | 165 | 160 | 10.763647090833901 | 3.1797223286297083 | 3.3850902621023713 | 0.00089515156081969695 | 0.18529637308967728 | False |
| ctx-lh-lateraloccipital | GFAP | tau | 165 | 160 | 4.4658868202198851 | 3.0409516044175335 | 1.4685820102274483 | 0.14390947853203448 | 1 | False |
| ctx-lh-lateraloccipital | NFL | amyloid | 165 | 160 | 1.0763710873902796 | 0.99733322999203622 | 1.0792491967793698 | 0.28210091633993351 | 1 | False |
| ctx-lh-lateraloccipital | NFL | tau | 165 | 160 | 1.5580918234750818 | 0.9984702383655446 | 1.5604789843567246 | 0.12062250982565732 | 1 | False |
| ctx-lh-lateralorbitofrontal | GFAP | amyloid | 165 | 160 | 15.27540641734036 | 2.7964219584126786 | 5.4624826455057143 | 1.7638565397701146e-07 | 4.6565812649931023e-05 | True |
| ctx-lh-lateralorbitofrontal | GFAP | tau | 165 | 160 | -0.14508964948556491 | 2.7874677600587598 | -0.052050700483260985 | 0.95855322279364641 | 1 | False |
| ctx-lh-lateralorbitofrontal | NFL | amyloid | 165 | 160 | 1.7871567788183422 | 1.173149773141124 | 1.5233833051283865 | 0.12963688331211912 | 1 | False |
| ctx-lh-lateralorbitofrontal | NFL | tau | 165 | 160 | 0.77630743069898522 | 1.0072963459827056 | 0.77068425175475996 | 0.44203063865879405 | 1 | False |
| ctx-lh-lingual | GFAP | amyloid | 165 | 160 | 11.101420785166351 | 3.294193721819155 | 3.3699963398132531 | 0.00094217331502387063 | 0.19408770289491736 | False |
| ctx-lh-lingual | GFAP | tau | 165 | 160 | 2.1172263717373063 | 3.002982444171431 | 0.70504120856473462 | 0.48180967957226911 | 1 | False |
| ctx-lh-lingual | NFL | amyloid | 165 | 160 | 1.2574130522430318 | 1.1657551900315906 | 1.0786253091517075 | 0.28237820142508646 | 1 | False |
| ctx-lh-lingual | NFL | tau | 165 | 160 | 1.3971838774019469 | 0.89607676526814917 | 1.559223418747882 | 0.1209193016593971 | 1 | False |
| ctx-lh-medialorbitofrontal | GFAP | amyloid | 165 | 160 | 15.804177148438484 | 2.8141942441321213 | 5.6158799917211777 | 8.4608166902049874e-08 | 2.2928813230455515e-05 | True |
| ctx-lh-medialorbitofrontal | GFAP | tau | 165 | 160 | -0.64622903842542945 | 2.6342836049377736 | -0.24531490732968916 | 0.80652697784449234 | 1 | False |
| ctx-lh-medialorbitofrontal | NFL | amyloid | 165 | 160 | 1.8307500714608547 | 1.0873127242166989 | 1.6837382941321952 | 0.094182245605691661 | 1 | False |
| ctx-lh-medialorbitofrontal | NFL | tau | 165 | 160 | 0.64325645623896621 | 0.94697726765018087 | 0.67927338724311281 | 0.4979461271723139 | 1 | False |
| ctx-lh-middletemporal | GFAP | amyloid | 165 | 160 | 11.191464320106839 | 3.2925595398930612 | 3.3990165354672146 | 0.00085372324555045597 | 0.1784281583200453 | False |
| ctx-lh-middletemporal | GFAP | tau | 165 | 160 | 5.6148722741568928 | 3.4069579616635131 | 1.6480603333935246 | 0.101302624406957 | 1 | False |
| ctx-lh-middletemporal | NFL | amyloid | 165 | 160 | 1.15400061814837 | 1.1793240591854934 | 0.97852715643347998 | 0.32929089128055844 | 1 | False |
| ctx-lh-middletemporal | NFL | tau | 165 | 160 | 1.3538807076516182 | 0.98632692197839644 | 1.372649045142126 | 0.17178245335929776 | 1 | False |
| ctx-lh-paracentral | GFAP | amyloid | 165 | 160 | 14.608100213393723 | 3.2183179803734046 | 4.5390481308807225 | 1.105137275283983e-05 | 0.0026965349516929185 | True |
| ctx-lh-paracentral | GFAP | tau | 165 | 160 | 0.84668873560206492 | 2.8961439598202383 | 0.29235036218801025 | 0.77039751004558976 | 1 | False |
| ctx-lh-paracentral | NFL | amyloid | 165 | 160 | 1.4381175357490117 | 1.065829505572135 | 1.34929416781067 | 0.17914874427175628 | 1 | False |
| ctx-lh-paracentral | NFL | tau | 165 | 160 | 1.5840818529434404 | 0.88784941551845709 | 1.7841785163742214 | 0.076289828515941585 | 1 | False |
| ctx-lh-parahippocampal | GFAP | amyloid | 165 | 160 | 10.235392416916275 | 3.0015244684669891 | 3.4100646269740196 | 0.00082214110984242994 | 0.17264963306691028 | False |
| ctx-lh-parahippocampal | GFAP | tau | 165 | 160 | 5.6352024714790314 | 2.8975921862102987 | 1.9447879857963024 | 0.053553948993284375 | 1 | False |
| ctx-lh-parahippocampal | NFL | amyloid | 165 | 160 | 1.0147218523567147 | 1.1466060419363249 | 0.88497863716391079 | 0.37749616477016834 | 1 | False |
| ctx-lh-parahippocampal | NFL | tau | 165 | 160 | 1.3511908244989128 | 0.93780333289345774 | 1.4408040333254173 | 0.15159413767136426 | 1 | False |
| ctx-lh-parsopercularis | GFAP | amyloid | 165 | 160 | 14.26009275495316 | 2.8789469091169528 | 4.9532322773284827 | 1.8396184897501099e-06 | 0.00046542347790677781 | True |
| ctx-lh-parsopercularis | GFAP | tau | 165 | 160 | 2.5805159563853399 | 2.7254733564979539 | 0.94681386271232004 | 0.34516138059144713 | 1 | False |
| ctx-lh-parsopercularis | NFL | amyloid | 165 | 160 | 1.3527540591884981 | 1.1322980883271578 | 1.194697821301667 | 0.23397308805414416 | 1 | False |
| ctx-lh-parsopercularis | NFL | tau | 165 | 160 | 1.5594892576424537 | 1.0322556765358211 | 1.510758713263745 | 0.13282237348031212 | 1 | False |
| ctx-lh-parsorbitalis | GFAP | amyloid | 165 | 160 | 13.683987153562375 | 2.6294509293834989 | 5.2041234162794296 | 5.9037201089009493e-07 | 0.00015231597880964448 | True |
| ctx-lh-parsorbitalis | GFAP | tau | 165 | 160 | 2.3713624522824723 | 2.7960151067368733 | 0.84812218881392332 | 0.39763692440547549 | 1 | False |
| ctx-lh-parsorbitalis | NFL | amyloid | 165 | 160 | 1.7840878765879156 | 1.0901817244966598 | 1.6365050307659801 | 0.10369942691771511 | 1 | False |
| ctx-lh-parsorbitalis | NFL | tau | 165 | 160 | 0.91325420118032519 | 1.0228105377730683 | 0.89288696924136457 | 0.37325867557643772 | 1 | False |
| ctx-lh-parstriangularis | GFAP | amyloid | 165 | 160 | 14.373923149398371 | 2.5831782972364716 | 5.5644332273834287 | 1.083996843978775e-07 | 2.9051115418631169e-05 | True |
| ctx-lh-parstriangularis | GFAP | tau | 165 | 160 | 2.263226025148962 | 2.822051256612411 | 0.801979063932998 | 0.42375458175259872 | 1 | False |
| ctx-lh-parstriangularis | NFL | amyloid | 165 | 160 | 1.5969553349064796 | 1.1090089547763615 | 1.4399841660688082 | 0.15182565330872122 | 1 | False |
| ctx-lh-parstriangularis | NFL | tau | 165 | 160 | 1.1176920080387376 | 1.0235244031680877 | 1.0920032825589459 | 0.27647323681332986 | 1 | False |
| ctx-lh-pericalcarine | GFAP | amyloid | 165 | 160 | 12.60781812716516 | 3.2548380599805382 | 3.8735623385332252 | 0.00015606106064533083 | 0.035113738645199441 | True |
| ctx-lh-pericalcarine | GFAP | tau | 165 | 160 | -0.72436389509624988 | 3.1142138302861606 | -0.23259928013025655 | 0.81636985379616533 | 1 | False |
| ctx-lh-pericalcarine | NFL | amyloid | 165 | 160 | 1.5605016136113166 | 1.1729281469494994 | 1.3304324034424455 | 0.1852689615677697 | 1 | False |
| ctx-lh-pericalcarine | NFL | tau | 165 | 160 | 0.83789269659273935 | 0.8028608475400324 | 1.0436337743458841 | 0.29822911038214339 | 1 | False |
| ctx-lh-postcentral | GFAP | amyloid | 165 | 160 | 13.226100290820895 | 2.9249769209972905 | 4.5217793671723632 | 1.1881370205904439e-05 | 0.0028871729600347786 | True |
| ctx-lh-postcentral | GFAP | tau | 165 | 160 | 1.4842017833003389 | 2.7241555649925617 | 0.54483003921414874 | 0.58662901028922865 | 1 | False |
| ctx-lh-postcentral | NFL | amyloid | 165 | 160 | 1.3368578752832305 | 1.1407123935802201 | 1.171949987399884 | 0.24295925472801461 | 1 | False |
| ctx-lh-postcentral | NFL | tau | 165 | 160 | 1.4091677406532339 | 0.95689136579803635 | 1.4726517460819644 | 0.14280938194796627 | 1 | False |
| ctx-lh-posteriorcingulate | GFAP | amyloid | 165 | 160 | 14.088863112091046 | 3.1556836538794681 | 4.4645993253381953 | 1.5080257292181148e-05 | 0.0036192617501234754 | True |
| ctx-lh-posteriorcingulate | GFAP | tau | 165 | 160 | 4.4306926868357843 | 2.9749737559412375 | 1.489321604262011 | 0.13837121027761565 | 1 | False |
| ctx-lh-posteriorcingulate | NFL | amyloid | 165 | 160 | 1.1741414383081943 | 1.100517591956709 | 1.0668992907424433 | 0.28762450544356177 | 1 | False |
| ctx-lh-posteriorcingulate | NFL | tau | 165 | 160 | 2.0307918320051028 | 0.88895096594681799 | 2.2844812703950605 | 0.023657519373117192 | 1 | False |
| ctx-lh-precentral | GFAP | amyloid | 165 | 160 | 13.39830300716021 | 3.0851144760126474 | 4.3428868235958724 | 2.4873158942554045e-05 | 0.0058700655104427547 | True |
| ctx-lh-precentral | GFAP | tau | 165 | 160 | 1.1736802241320552 | 2.7934247150789595 | 0.42015817279646273 | 0.67493360859113105 | 1 | False |
| ctx-lh-precentral | NFL | amyloid | 165 | 160 | 1.3259319977711674 | 1.1639217921993839 | 1.1391933776457985 | 0.25632518118266323 | 1 | False |
| ctx-lh-precentral | NFL | tau | 165 | 160 | 1.2124119798486757 | 0.95028025369874747 | 1.2758467569221192 | 0.20385878260506207 | 1 | False |
| ctx-lh-precuneus | GFAP | amyloid | 165 | 160 | 13.467474054424668 | 3.1562258226447435 | 4.2669551582147776 | 3.3819147812537501e-05 | 0.0079136805881337754 | True |
| ctx-lh-precuneus | GFAP | tau | 165 | 160 | 4.3825229320678343 | 3.0011456808419332 | 1.4602833044873627 | 0.14617302511892899 | 1 | False |
| ctx-lh-precuneus | NFL | amyloid | 165 | 160 | 1.4845759518033415 | 1.0636178949699908 | 1.3957794042617415 | 0.16471481007955943 | 1 | False |
| ctx-lh-precuneus | NFL | tau | 165 | 160 | 1.3482429973759626 | 0.8320664834351581 | 1.6203548925679441 | 0.10712527530268684 | 1 | False |
| ctx-lh-rostralanteriorcingulate | GFAP | amyloid | 165 | 160 | 16.137202705196902 | 2.8870393847601838 | 5.589533274253327 | 9.6072814581427453e-08 | 2.5939659936985413e-05 | True |
| ctx-lh-rostralanteriorcingulate | GFAP | tau | 165 | 160 | -1.4162105315631819 | 2.6295008409742047 | -0.53858531227489148 | 0.59092154340858927 | 1 | False |
| ctx-lh-rostralanteriorcingulate | NFL | amyloid | 165 | 160 | 1.8458279207223016 | 1.0426872194440155 | 1.7702604254673218 | 0.078588220511574464 | 1 | False |
| ctx-lh-rostralanteriorcingulate | NFL | tau | 165 | 160 | 0.72332921843064635 | 0.92685210775254911 | 0.78041492529438228 | 0.43629971382400445 | 1 | False |
| ctx-lh-rostralmiddlefrontal | GFAP | amyloid | 165 | 160 | 14.249264093757873 | 2.6497312695072015 | 5.3776261229720701 | 2.6337204593718421e-07 | 6.9266848081479444e-05 | True |
| ctx-lh-rostralmiddlefrontal | GFAP | tau | 165 | 160 | 4.6566948255160936 | 2.6918832922746612 | 1.7299021985389094 | 0.085576115467419375 | 1 | False |
| ctx-lh-rostralmiddlefrontal | NFL | amyloid | 165 | 160 | 1.6038780299291049 | 1.0612409463486532 | 1.5113231688312347 | 0.1326786530819892 | 1 | False |
| ctx-lh-rostralmiddlefrontal | NFL | tau | 165 | 160 | 1.3561709217182265 | 0.97345725654229232 | 1.3931489159938344 | 0.16550725793295737 | 1 | False |
| ctx-lh-superiorfrontal | GFAP | amyloid | 165 | 160 | 15.096604548866672 | 2.9795494954187074 | 5.066740650584558 | 1.1050922963767624e-06 | 0.00028179853557607442 | True |
| ctx-lh-superiorfrontal | GFAP | tau | 165 | 160 | 3.0672883619876314 | 2.4696099905383546 | 1.2420132627172389 | 0.2160491268698212 | 1 | False |
| ctx-lh-superiorfrontal | NFL | amyloid | 165 | 160 | 1.6431084001758007 | 1.1067115917438857 | 1.4846762358264407 | 0.13959706981025863 | 1 | False |
| ctx-lh-superiorfrontal | NFL | tau | 165 | 160 | 1.4077437830853505 | 0.93747827459636868 | 1.5016281670009417 | 0.13516411174630036 | 1 | False |
| ctx-lh-superiorparietal | GFAP | amyloid | 165 | 160 | 12.416737361568583 | 3.0173061681795987 | 4.1151731609191815 | 6.1780970951612156e-05 | 0.014086061376967572 | True |
| ctx-lh-superiorparietal | GFAP | tau | 165 | 160 | 5.7269555404702448 | 2.7410423102456396 | 2.0893349654121249 | 0.03826003125383038 | 1 | False |
| ctx-lh-superiorparietal | NFL | amyloid | 165 | 160 | 1.129472389962014 | 1.0397600925216457 | 1.0862817279539903 | 0.27898821930366446 | 1 | False |
| ctx-lh-superiorparietal | NFL | tau | 165 | 160 | 1.6598004905678836 | 0.82193594499975331 | 2.0193793697249509 | 0.045117136870420502 | 1 | False |
| ctx-lh-superiortemporal | GFAP | amyloid | 165 | 160 | 13.037434290874049 | 3.1519987269257901 | 4.1362435141557716 | 5.6876289029824999e-05 | 0.013138422765889574 | True |
| ctx-lh-superiortemporal | GFAP | tau | 165 | 160 | 2.7410362530904737 | 2.9181491905027448 | 0.93930641449426455 | 0.34898929493467279 | 1 | False |
| ctx-lh-superiortemporal | NFL | amyloid | 165 | 160 | 1.2663522489251011 | 1.2031898268704173 | 1.0524958079299704 | 0.29415904661382281 | 1 | False |
| ctx-lh-superiortemporal | NFL | tau | 165 | 160 | 1.0375538358491738 | 1.0736215343769955 | 0.96640557461549881 | 0.33529974074886804 | 1 | False |
| ctx-lh-supramarginal | GFAP | amyloid | 165 | 160 | 12.467270956771692 | 3.0261938663541628 | 4.1197859447754945 | 6.0673840163056612e-05 | 0.013894309397339964 | True |
| ctx-lh-supramarginal | GFAP | tau | 165 | 160 | 5.0015894333915654 | 3.1739166366971481 | 1.5758414621110957 | 0.11703753258919818 | 1 | False |
| ctx-lh-supramarginal | NFL | amyloid | 165 | 160 | 1.1161404642415738 | 1.1454784316010891 | 0.97438802289929782 | 0.33133475501315446 | 1 | False |
| ctx-lh-supramarginal | NFL | tau | 165 | 160 | 1.436687119640814 | 0.91078260134015632 | 1.5774204706225436 | 0.11667389282909536 | 1 | False |
| ctx-lh-temporalpole | GFAP | amyloid | 165 | 160 | 14.746700393022525 | 3.2291577620571652 | 4.5667327147336403 | 9.8361059426914875e-06 | 0.0024196820619021061 | True |
| ctx-lh-temporalpole | GFAP | tau | 165 | 160 | 1.5039373500238948 | 2.879550403220537 | 0.52228200219793564 | 0.60219635881889078 | 1 | False |
| ctx-lh-temporalpole | NFL | amyloid | 165 | 160 | 1.2970243533767518 | 1.1796480524856072 | 1.0995011186970758 | 0.27320115015449981 | 1 | False |
| ctx-lh-temporalpole | NFL | tau | 165 | 160 | 0.8657035726050516 | 1.0343158958523491 | 0.83698179258054517 | 0.40385118762292532 | 1 | False |
| ctx-lh-transversetemporal | GFAP | amyloid | 165 | 160 | 13.33999710707138 | 3.2825601538091389 | 4.0639002735689154 | 7.5460809366913564e-05 | 0.01712960372628938 | True |
| ctx-lh-transversetemporal | GFAP | tau | 165 | 160 | 0.21158335244170257 | 2.8639823960672581 | 0.073877322965477374 | 0.94120027998060352 | 1 | False |
| ctx-lh-transversetemporal | NFL | amyloid | 165 | 160 | 1.318657559152838 | 1.1440959554954622 | 1.1525760167395926 | 0.25080354778015085 | 1 | False |
| ctx-lh-transversetemporal | NFL | tau | 165 | 160 | 0.75434249398082787 | 1.0943273020322457 | 0.68932072934665778 | 0.49161991538104288 | 1 | False |
| ctx-rh-bankssts | GFAP | amyloid | 165 | 160 | 12.653240943129294 | 3.1351892461034447 | 4.0358778848375154 | 8.4113588843403412e-05 | 0.01900967107860917 | True |
| ctx-rh-bankssts | GFAP | tau | 165 | 160 | 2.8193163982432221 | 2.5678335461006494 | 1.0979358076088923 | 0.27388204116626297 | 1 | False |
| ctx-rh-bankssts | NFL | amyloid | 165 | 160 | 1.0009119466254974 | 1.0164778237049725 | 0.98468645678590527 | 0.32626478675292553 | 1 | False |
| ctx-rh-bankssts | NFL | tau | 165 | 160 | 0.93076751939518609 | 1.0586274811704812 | 0.87922100639790157 | 0.38060000198348576 | 1 | False |
| ctx-rh-caudalanteriorcingulate | GFAP | amyloid | 165 | 160 | 15.153857404418416 | 2.7700670091705586 | 5.4705743053327565 | 1.6973499183570936e-07 | 4.4979772836462982e-05 | True |
| ctx-rh-caudalanteriorcingulate | GFAP | tau | 165 | 160 | -0.44726246631644084 | 2.4130611828146153 | -0.18535065314620414 | 0.85318876494175555 | 1 | False |
| ctx-rh-caudalanteriorcingulate | NFL | amyloid | 165 | 160 | 1.4705608852258532 | 1.092786000229417 | 1.3456988696022159 | 0.18030347902985985 | 1 | False |
| ctx-rh-caudalanteriorcingulate | NFL | tau | 165 | 160 | 0.69354887733753579 | 0.98505552953204822 | 0.70407084326201086 | 0.4824120993581042 | 1 | False |
| ctx-rh-caudalmiddlefrontal | GFAP | amyloid | 165 | 160 | 14.156362311122665 | 2.9607890773599159 | 4.7812802402478622 | 3.9229007652309498e-06 | 0.00097287938977727551 | True |
| ctx-rh-caudalmiddlefrontal | GFAP | tau | 165 | 160 | 5.4737643285272064 | 2.5605677234214217 | 2.1377151162450732 | 0.034058661871990352 | 1 | False |
| ctx-rh-caudalmiddlefrontal | NFL | amyloid | 165 | 160 | 1.2324386273752117 | 1.10845496485272 | 1.1118526836486906 | 0.26786935872586842 | 1 | False |
| ctx-rh-caudalmiddlefrontal | NFL | tau | 165 | 160 | 1.2375431921447997 | 0.87821161156822092 | 1.4091628667206084 | 0.16072757783804642 | 1 | False |
| ctx-rh-cuneus | GFAP | amyloid | 165 | 160 | 11.625263359941524 | 3.3184793422009218 | 3.5031899135557905 | 0.0005962083272174674 | 0.12699237369732055 | False |
| ctx-rh-cuneus | GFAP | tau | 165 | 160 | 2.385202443092485 | 2.7226008740972771 | 0.8760749567757844 | 0.3823026478461794 | 1 | False |
| ctx-rh-cuneus | NFL | amyloid | 165 | 160 | 1.3260058821270322 | 1.0347738160229749 | 1.2814451444310522 | 0.2018913627189341 | 1 | False |
| ctx-rh-cuneus | NFL | tau | 165 | 160 | 1.2436511769265151 | 1.0409690303737822 | 1.194705260808725 | 0.23397018861117197 | 1 | False |
| ctx-rh-entorhinal | GFAP | amyloid | 165 | 160 | 11.137021775328767 | 2.8964489898031762 | 3.8450605602018788 | 0.00017362124568285887 | 0.038891159032960386 | True |
| ctx-rh-entorhinal | GFAP | tau | 165 | 160 | 4.0182492462680219 | 3.0227257339230813 | 1.3293462920477699 | 0.18562607646918353 | 1 | False |
| ctx-rh-entorhinal | NFL | amyloid | 165 | 160 | 0.9886825239413799 | 1.0833005789185661 | 0.91265761616075081 | 0.36279576470797503 | 1 | False |
| ctx-rh-entorhinal | NFL | tau | 165 | 160 | 0.50650493980388056 | 0.97865664993683321 | 0.51755121659529169 | 0.60548623570048821 | 1 | False |
| ctx-rh-frontalpole | GFAP | amyloid | 165 | 160 | 15.152015261187156 | 2.8177181841713734 | 5.377406209855943 | 2.6364445818104474e-07 | 6.9266848081479444e-05 | True |
| ctx-rh-frontalpole | GFAP | tau | 165 | 160 | 1.3369205484701265 | 2.5878007884965974 | 0.5166242140481071 | 0.60613184163530154 | 1 | False |
| ctx-rh-frontalpole | NFL | amyloid | 165 | 160 | 1.4972895137366631 | 1.0711554564451604 | 1.3978265290322212 | 0.16410010146494114 | 1 | False |
| ctx-rh-frontalpole | NFL | tau | 165 | 160 | 0.97905963113414207 | 0.9120767489368744 | 1.0734399624541944 | 0.28469003125619846 | 1 | False |
| ctx-rh-fusiform | GFAP | amyloid | 165 | 160 | 10.878607291830706 | 2.9579315680800633 | 3.6777751754722985 | 0.00032088514009068366 | 0.070273845679859726 | False |
| ctx-rh-fusiform | GFAP | tau | 165 | 160 | 5.8508931245372349 | 2.7268691551905926 | 2.1456449838819975 | 0.033409439106533365 | 1 | False |
| ctx-rh-fusiform | NFL | amyloid | 165 | 160 | 0.99441860630979151 | 1.0839555087045725 | 0.91739799126830779 | 0.36031490232836072 | 1 | False |
| ctx-rh-fusiform | NFL | tau | 165 | 160 | 1.3934466869737747 | 1.1389982405723313 | 1.223396698377327 | 0.22297860015796489 | 1 | False |
| ctx-rh-inferiorparietal | GFAP | amyloid | 165 | 160 | 11.583153361089089 | 3.1211286997732275 | 3.7112065779058354 | 0.00028427308141723123 | 0.0628243509932081 | False |
| ctx-rh-inferiorparietal | GFAP | tau | 165 | 160 | 5.9630265116749825 | 2.7897860221901176 | 2.1374494187886555 | 0.03408060185359061 | 1 | False |
| ctx-rh-inferiorparietal | NFL | amyloid | 165 | 160 | 0.90092243968453511 | 1.0484493605122993 | 0.859290370728369 | 0.3914659207193994 | 1 | False |
| ctx-rh-inferiorparietal | NFL | tau | 165 | 160 | 1.4690614085394271 | 0.91730182392667692 | 1.6015027662878105 | 0.11123812089749445 | 1 | False |
| ctx-rh-inferiortemporal | GFAP | amyloid | 165 | 160 | 13.051798104990137 | 3.1440461717580837 | 4.1512743108641592 | 5.3607389763555541e-05 | 0.012436914425144885 | True |
| ctx-rh-inferiortemporal | GFAP | tau | 165 | 160 | 3.151899870285285 | 2.8874543352889095 | 1.0915843176338633 | 0.27665686710712567 | 1 | False |
| ctx-rh-inferiortemporal | NFL | amyloid | 165 | 160 | 1.3924970843895108 | 1.1176240202350323 | 1.2459441271642262 | 0.2146062059040936 | 1 | False |
| ctx-rh-inferiortemporal | NFL | tau | 165 | 160 | 0.85748306632331217 | 1.133612891038122 | 0.75641612150163529 | 0.45051205835872721 | 1 | False |
| ctx-rh-insula | GFAP | amyloid | 165 | 160 | 15.476596009773811 | 3.0017754982630027 | 5.1558139570162549 | 7.3690203505726711e-07 | 0.00018938382300971764 | True |
| ctx-rh-insula | GFAP | tau | 165 | 160 | -1.1818125473082559 | 2.6694720354572326 | -0.44271396426366111 | 0.65857057140736386 | 1 | False |
| ctx-rh-insula | NFL | amyloid | 165 | 160 | 1.4249407260295957 | 1.1453552009439825 | 1.2441037722229606 | 0.21528087827505368 | 1 | False |
| ctx-rh-insula | NFL | tau | 165 | 160 | 0.88947155672739964 | 0.9527798573635945 | 0.93355411520624165 | 0.35194063439349643 | 1 | False |
| ctx-rh-isthmuscingulate | GFAP | amyloid | 165 | 160 | 11.401637300009549 | 3.0922633754783391 | 3.6871494809997682 | 0.00031019277338883912 | 0.068242410145544607 | False |
| ctx-rh-isthmuscingulate | GFAP | tau | 165 | 160 | 5.4943905778173709 | 2.8494709417177777 | 1.9282142861597766 | 0.055599214678453315 | 1 | False |
| ctx-rh-isthmuscingulate | NFL | amyloid | 165 | 160 | 1.1636977666974431 | 1.0875307766035154 | 1.0700366295212409 | 0.28621437654219051 | 1 | False |
| ctx-rh-isthmuscingulate | NFL | tau | 165 | 160 | 1.5014559622109047 | 0.90118417938421502 | 1.6660922334842354 | 0.097651624354995067 | 1 | False |
| ctx-rh-lateraloccipital | GFAP | amyloid | 165 | 160 | 11.0561963785296 | 3.0169251162958499 | 3.6647235023533784 | 0.00033635300812883827 | 0.07298860276395791 | False |
| ctx-rh-lateraloccipital | GFAP | tau | 165 | 160 | 5.423662203576078 | 2.6940901643029527 | 2.0131702626141887 | 0.045773418614199521 | 1 | False |
| ctx-rh-lateraloccipital | NFL | amyloid | 165 | 160 | 1.0240472488910457 | 0.96504926616025977 | 1.061134684828607 | 0.29022781857898666 | 1 | False |
| ctx-rh-lateraloccipital | NFL | tau | 165 | 160 | 1.3620281067746249 | 1.0748054269522023 | 1.267232256760084 | 0.20691359629002193 | 1 | False |
| ctx-rh-lateralorbitofrontal | GFAP | amyloid | 165 | 160 | 16.039572278616674 | 2.8867701791420353 | 5.5562345747189781 | 1.1275120331817146e-07 | 2.9991820082633608e-05 | True |
| ctx-rh-lateralorbitofrontal | GFAP | tau | 165 | 160 | -1.9864190897217473 | 2.7666425215622281 | -0.71798906950945174 | 0.47381107960366636 | 1 | False |
| ctx-rh-lateralorbitofrontal | NFL | amyloid | 165 | 160 | 1.6555180481588023 | 1.0703724363506311 | 1.5466747759342432 | 0.12391734418595551 | 1 | False |
| ctx-rh-lateralorbitofrontal | NFL | tau | 165 | 160 | 0.42578211424016721 | 0.90682180257765632 | 0.4695322863101376 | 0.6393284553652907 | 1 | False |
| ctx-rh-lingual | GFAP | amyloid | 165 | 160 | 10.984364456792658 | 3.2323328806749969 | 3.3982776101014793 | 0.00085587555232793271 | 0.1784281583200453 | False |
| ctx-rh-lingual | GFAP | tau | 165 | 160 | 3.5106974255433139 | 2.7790070771972677 | 1.2632920061088808 | 0.20832198568436922 | 1 | False |
| ctx-rh-lingual | NFL | amyloid | 165 | 160 | 1.1524315116592647 | 1.0645032645096679 | 1.0826002606860001 | 0.28061473534962356 | 1 | False |
| ctx-rh-lingual | NFL | tau | 165 | 160 | 1.2030850612627657 | 0.98991814546447143 | 1.2153379213978102 | 0.22602752512497004 | 1 | False |
| ctx-rh-medialorbitofrontal | GFAP | amyloid | 165 | 160 | 15.296225252322117 | 2.7514833147844784 | 5.5592651316950681 | 1.1112318341801912e-07 | 2.9669889972611106e-05 | True |
| ctx-rh-medialorbitofrontal | GFAP | tau | 165 | 160 | -1.5053083245707439 | 2.6604788836430688 | -0.56580352275131862 | 0.5723199953122563 | 1 | False |
| ctx-rh-medialorbitofrontal | NFL | amyloid | 165 | 160 | 1.4877488414924629 | 1.0646164712683519 | 1.3974505201107812 | 0.1642128780722599 | 1 | False |
| ctx-rh-medialorbitofrontal | NFL | tau | 165 | 160 | 0.79383590381694924 | 0.92952865106218163 | 0.85401983350359889 | 0.3943708238089973 | 1 | False |
| ctx-rh-middletemporal | GFAP | amyloid | 165 | 160 | 13.537510570291683 | 3.1925071176862718 | 4.2404010613773728 | 3.7621103609578563e-05 | 0.0087657171410318053 | True |
| ctx-rh-middletemporal | GFAP | tau | 165 | 160 | 2.6339372146097952 | 2.9232723260085609 | 0.90102355198845807 | 0.36893004302539606 | 1 | False |
| ctx-rh-middletemporal | NFL | amyloid | 165 | 160 | 1.2901364874450798 | 1.0920154691511361 | 1.1814269338583183 | 0.23918621111900767 | 1 | False |
| ctx-rh-middletemporal | NFL | tau | 165 | 160 | 0.91106148591518443 | 1.1219807243086655 | 0.8120117094494258 | 0.41799135123792469 | 1 | False |
| ctx-rh-paracentral | GFAP | amyloid | 165 | 160 | 13.918998365476114 | 3.1169341348928881 | 4.4656055479832695 | 1.5017395172264344e-05 | 0.003619192236515707 | True |
| ctx-rh-paracentral | GFAP | tau | 165 | 160 | 0.5330049499513736 | 2.595730517299776 | 0.20533909294476191 | 0.83756821442677409 | 1 | False |
| ctx-rh-paracentral | NFL | amyloid | 165 | 160 | 1.2798723809812402 | 1.0398793650332849 | 1.230789285774772 | 0.22020794549711428 | 1 | False |
| ctx-rh-paracentral | NFL | tau | 165 | 160 | 1.5236863291918439 | 0.85367209132848998 | 1.7848613591439699 | 0.076178505103337235 | 1 | False |
| ctx-rh-parahippocampal | GFAP | amyloid | 165 | 160 | 10.607649300047992 | 3.105404950045346 | 3.4158666810565546 | 0.00080599676998939832 | 0.17006531846776304 | False |
| ctx-rh-parahippocampal | GFAP | tau | 165 | 160 | 4.6705337711982118 | 2.8893781944950305 | 1.6164494423390876 | 0.10796716386408919 | 1 | False |
| ctx-rh-parahippocampal | NFL | amyloid | 165 | 160 | 0.88936724418635671 | 1.0012445277300979 | 0.88826177777233306 | 0.37573335200850566 | 1 | False |
| ctx-rh-parahippocampal | NFL | tau | 165 | 160 | 1.1437828657157529 | 1.1407094749756364 | 1.0026942800139205 | 0.3175224006825812 | 1 | False |
| ctx-rh-parsopercularis | GFAP | amyloid | 165 | 160 | 14.652106317204829 | 2.9938529448222049 | 4.8940634651228567 | 2.3920776616969693e-06 | 0.00060280357074763628 | True |
| ctx-rh-parsopercularis | GFAP | tau | 165 | 160 | 3.2875981906112597 | 2.4498526670303833 | 1.3419575123251632 | 0.18151104146662228 | 1 | False |
| ctx-rh-parsopercularis | NFL | amyloid | 165 | 160 | 1.3335888685128969 | 1.1338602438842509 | 1.1761492438825072 | 0.24128223138102856 | 1 | False |
| ctx-rh-parsopercularis | NFL | tau | 165 | 160 | 1.186066917870102 | 1.0515769360282106 | 1.127893620746246 | 0.26105333671418873 | 1 | False |
| ctx-rh-parsorbitalis | GFAP | amyloid | 165 | 160 | 15.020579868200272 | 2.9679729652171924 | 5.0608883720411804 | 1.1347254918915502e-06 | 0.00028822027494045376 | True |
| ctx-rh-parsorbitalis | GFAP | tau | 165 | 160 | 1.0467850925310829 | 2.6076827823911457 | 0.40142347819285784 | 0.68864399889386596 | 1 | False |
| ctx-rh-parsorbitalis | NFL | amyloid | 165 | 160 | 1.5963644238841326 | 1.1324066579529088 | 1.4097095002690434 | 0.16056630212158171 | 1 | False |
| ctx-rh-parsorbitalis | NFL | tau | 165 | 160 | 0.69616021246497783 | 1.0193509964960974 | 0.68294455477843163 | 0.49562955429342059 | 1 | False |
| ctx-rh-parstriangularis | GFAP | amyloid | 165 | 160 | 15.491282153878927 | 2.9225587525031331 | 5.3005887873463102 | 3.776857769960223e-07 | 9.8575987795961818e-05 | True |
| ctx-rh-parstriangularis | GFAP | tau | 165 | 160 | 1.3189728070413453 | 2.5756069242646746 | 0.51210174759795957 | 0.60928593650469287 | 1 | False |
| ctx-rh-parstriangularis | NFL | amyloid | 165 | 160 | 1.5770243195216691 | 1.0511822691967467 | 1.5002386985910072 | 0.13552327875719469 | 1 | False |
| ctx-rh-parstriangularis | NFL | tau | 165 | 160 | 0.5301486652515297 | 1.0359467634490691 | 0.51175280811386381 | 0.60952960259186884 | 1 | False |
| ctx-rh-pericalcarine | GFAP | amyloid | 165 | 160 | 12.744692287219323 | 3.4722801785407893 | 3.6704101143633014 | 0.00032952902997584164 | 0.071837328534733472 | False |
| ctx-rh-pericalcarine | GFAP | tau | 165 | 160 | 0.19946990249143948 | 3.037437882813673 | 0.065670446668250643 | 0.94772218392576624 | 1 | False |
| ctx-rh-pericalcarine | NFL | amyloid | 165 | 160 | 1.3112920305159055 | 1.1072710435935884 | 1.1842556870810763 | 0.23806813075557173 | 1 | False |
| ctx-rh-pericalcarine | NFL | tau | 165 | 160 | 1.0785522467651489 | 0.95505249771660228 | 1.1293120004856461 | 0.26045652512143691 | 1 | False |
| ctx-rh-postcentral | GFAP | amyloid | 165 | 160 | 14.571716964814666 | 3.0470143582647653 | 4.7822935016010453 | 3.9056409355591843e-06 | 0.00097250459295423694 | True |
| ctx-rh-postcentral | GFAP | tau | 165 | 160 | 0.63731180709484114 | 2.6516304820925796 | 0.24034714165447957 | 0.81036882431519508 | 1 | False |
| ctx-rh-postcentral | NFL | amyloid | 165 | 160 | 1.4245555966337615 | 1.0899685999021684 | 1.3069693904591604 | 0.19309838354997691 | 1 | False |
| ctx-rh-postcentral | NFL | tau | 165 | 160 | 1.3391169592275025 | 0.88545900681876799 | 1.5123421286758534 | 0.13241951564034465 | 1 | False |
| ctx-rh-posteriorcingulate | GFAP | amyloid | 165 | 160 | 13.51218537354063 | 3.064529860069849 | 4.4092196814922371 | 1.8958896893960485e-05 | 0.0045122174607625954 | True |
| ctx-rh-posteriorcingulate | GFAP | tau | 165 | 160 | 4.2091433018829321 | 2.7930377691334103 | 1.5070126685715723 | 0.13377926811654958 | 1 | False |
| ctx-rh-posteriorcingulate | NFL | amyloid | 165 | 160 | 1.1573390939628838 | 1.0836661802249281 | 1.0679848786299337 | 0.28713603560324591 | 1 | False |
| ctx-rh-posteriorcingulate | NFL | tau | 165 | 160 | 1.6151867847409223 | 0.87006917551634688 | 1.856388928825552 | 0.065237065596126118 | 1 | False |
| ctx-rh-precentral | GFAP | amyloid | 165 | 160 | 13.724774530305567 | 3.0386078258429277 | 4.5167969402231867 | 1.2131798281335501e-05 | 0.0029358951840831914 | True |
| ctx-rh-precentral | GFAP | tau | 165 | 160 | 2.0363872961915401 | 2.5383886554692903 | 0.80223621067793438 | 0.42360628086095709 | 1 | False |
| ctx-rh-precentral | NFL | amyloid | 165 | 160 | 1.3772851847311576 | 1.1246120452377184 | 1.2246758253776568 | 0.22249740526983033 | 1 | False |
| ctx-rh-precentral | NFL | tau | 165 | 160 | 1.2195584681098879 | 0.92909890484642932 | 1.3126250195198201 | 0.19118906271110453 | 1 | False |
| ctx-rh-precuneus | GFAP | amyloid | 165 | 160 | 13.279666031566107 | 3.0950494587564279 | 4.2906151286195584 | 3.0744282940877822e-05 | 0.0072249064911062881 | True |
| ctx-rh-precuneus | GFAP | tau | 165 | 160 | 5.0424834704334751 | 2.7005971140672167 | 1.8671735388324087 | 0.063706781724688397 | 1 | False |
| ctx-rh-precuneus | NFL | amyloid | 165 | 160 | 1.2257070878765741 | 1.0169553083765448 | 1.2052713406189679 | 0.229878114595857 | 1 | False |
| ctx-rh-precuneus | NFL | tau | 165 | 160 | 1.564631071172373 | 0.82212907116068512 | 1.9031452919715155 | 0.058817407575348118 | 1 | False |
| ctx-rh-rostralanteriorcingulate | GFAP | amyloid | 165 | 160 | 15.390826369708225 | 2.6336549632228725 | 5.8439038464150475 | 2.7745284047281183e-08 | 7.5467172608604817e-06 | True |
| ctx-rh-rostralanteriorcingulate | GFAP | tau | 165 | 160 | -1.7081177084131074 | 2.4893775908749123 | -0.68616256315409963 | 0.49360371927199742 | 1 | False |
| ctx-rh-rostralanteriorcingulate | NFL | amyloid | 165 | 160 | 1.8258911912614333 | 1.0791104351607477 | 1.6920336712242459 | 0.09258612006491794 | 1 | False |
| ctx-rh-rostralanteriorcingulate | NFL | tau | 165 | 160 | 0.59465675543633856 | 0.91811608210698803 | 0.64769234198758241 | 0.51811224630247943 | 1 | False |
| ctx-rh-rostralmiddlefrontal | GFAP | amyloid | 165 | 160 | 14.454160104815143 | 2.7670143635436064 | 5.2237387327127092 | 5.393429334524731e-07 | 0.00013968981976419053 | True |
| ctx-rh-rostralmiddlefrontal | GFAP | tau | 165 | 160 | 4.915920665668958 | 2.6854619258412051 | 1.8305679996297377 | 0.06902558700848066 | 1 | False |
| ctx-rh-rostralmiddlefrontal | NFL | amyloid | 165 | 160 | 1.3669674163766876 | 1.1033810555451515 | 1.238889692284326 | 0.21720072834134208 | 1 | False |
| ctx-rh-rostralmiddlefrontal | NFL | tau | 165 | 160 | 1.2214212914069282 | 0.95120247920198386 | 1.2840812740854564 | 0.20096981119381058 | 1 | False |
| ctx-rh-superiorfrontal | GFAP | amyloid | 165 | 160 | 14.729919867765036 | 2.8131128448579283 | 5.2361638796999435 | 5.0926779786838994e-07 | 0.00013240962744578139 | True |
| ctx-rh-superiorfrontal | GFAP | tau | 165 | 160 | 3.4696064144190188 | 2.2923282792908872 | 1.5135730976072559 | 0.13210698891814365 | 1 | False |
| ctx-rh-superiorfrontal | NFL | amyloid | 165 | 160 | 1.4152359321478289 | 1.0939433311864826 | 1.2937013205362977 | 0.19763306783287785 | 1 | False |
| ctx-rh-superiorfrontal | NFL | tau | 165 | 160 | 1.4000080330589157 | 0.93084315573100807 | 1.5040214073008509 | 0.13454721844672546 | 1 | False |
| ctx-rh-superiorparietal | GFAP | amyloid | 165 | 160 | 13.004769512771519 | 2.9693161782435014 | 4.3797186732955087 | 2.1399869273536565e-05 | 0.0050717690178281654 | True |
| ctx-rh-superiorparietal | GFAP | tau | 165 | 160 | 5.2095666919560637 | 2.4722855150318814 | 2.1071865123510558 | 0.036660675003725371 | 1 | False |
| ctx-rh-superiorparietal | NFL | amyloid | 165 | 160 | 1.0438551789824355 | 0.99965372829135579 | 1.044216761704706 | 0.2979602008702113 | 1 | False |
| ctx-rh-superiorparietal | NFL | tau | 165 | 160 | 1.5267582173476399 | 0.94326475038781621 | 1.6185892844187433 | 0.10750523078432322 | 1 | False |
| ctx-rh-superiortemporal | GFAP | amyloid | 165 | 160 | 14.249112590637203 | 3.1343644716356769 | 4.5460930659417738 | 1.0729066974415143e-05 | 0.0026286214087317102 | True |
| ctx-rh-superiortemporal | GFAP | tau | 165 | 160 | 0.67954354122233251 | 2.6872375666591375 | 0.25287810413694217 | 0.80068700886895616 | 1 | False |
| ctx-rh-superiortemporal | NFL | amyloid | 165 | 160 | 1.2159085608012234 | 1.100768392769498 | 1.1045998129924828 | 0.27099138684009938 | 1 | False |
| ctx-rh-superiortemporal | NFL | tau | 165 | 160 | 0.85406142485004866 | 1.0867912809423808 | 0.78585597789252881 | 0.43311411280677264 | 1 | False |
| ctx-rh-supramarginal | GFAP | amyloid | 165 | 160 | 12.599628426520979 | 3.0516143296859535 | 4.1288403662128657 | 5.8555549241651228e-05 | 0.013467776325579783 | True |
| ctx-rh-supramarginal | GFAP | tau | 165 | 160 | 5.2505760116423135 | 2.7477701916446811 | 1.9108497601466354 | 0.057812141412644062 | 1 | False |
| ctx-rh-supramarginal | NFL | amyloid | 165 | 160 | 1.1735726258026655 | 1.0511214755195335 | 1.1164957173219285 | 0.26588389320988159 | 1 | False |
| ctx-rh-supramarginal | NFL | tau | 165 | 160 | 1.2858411922129682 | 0.92903654359756038 | 1.3840587876486894 | 0.16826800572099893 | 1 | False |
| ctx-rh-temporalpole | GFAP | amyloid | 165 | 160 | 14.662256501170194 | 2.996626128092398 | 4.8929215305560794 | 2.4041819034563075e-06 | 0.00060344965776753319 | True |
| ctx-rh-temporalpole | GFAP | tau | 165 | 160 | 1.1658478603292188 | 2.8321300368776692 | 0.41165054045842048 | 0.68114649497347168 | 1 | False |
| ctx-rh-temporalpole | NFL | amyloid | 165 | 160 | 0.93647197282875172 | 1.1313910688438911 | 0.82771731067815757 | 0.40906346881684219 | 1 | False |
| ctx-rh-temporalpole | NFL | tau | 165 | 160 | 1.1582720611742527 | 1.0212246597506689 | 1.134199071786069 | 0.25840749317277134 | 1 | False |
| ctx-rh-transversetemporal | GFAP | amyloid | 165 | 160 | 13.736613065088825 | 2.8833440924821394 | 4.7641254822498835 | 4.2265604702353831e-06 | 0.0010439604361481395 | True |
| ctx-rh-transversetemporal | GFAP | tau | 165 | 160 | -0.97512619252648847 | 2.8134600723016541 | -0.34659322239065959 | 0.72935233141990763 | 1 | False |
| ctx-rh-transversetemporal | NFL | amyloid | 165 | 160 | 1.2269771856581011 | 1.113497474047495 | 1.101912859485989 | 0.27215436128278764 | 1 | False |
| ctx-rh-transversetemporal | NFL | tau | 165 | 160 | 0.88414507681058574 | 1.0133477255935195 | 0.87249919694914246 | 0.38424356732818815 | 1 | False |

## T3B — All 272 intervals and effect sizes

Source: tables/T3_all_272_tests.csv

| region | outcome | predictor | ci95_low | ci95_high | standardized_beta | standardized_ci95_low | standardized_ci95_high | partial_R2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctx-lh-bankssts | GFAP | amyloid | 5.3978720954436463 | 17.642654575943439 | 0.31794033848687075 | 0.14897240029373585 | 0.48690827668000564 | 0.093099864957974732 |
| ctx-lh-bankssts | GFAP | tau | -1.2924819247499642 | 10.482377478795346 | 0.12681300843442381 | -0.035670377374965354 | 0.28929639424381298 | 0.015553940933730052 |
| ctx-lh-bankssts | NFL | amyloid | -1.0361716878103695 | 3.2726185683909006 | 0.096864094783466276 | -0.089756509266121831 | 0.28348469883305438 | 0.0083610530686519541 |
| ctx-lh-bankssts | NFL | tau | -0.50212555152722049 | 2.7859950629159709 | 0.098918044843883654 | -0.043495723004793797 | 0.24133181269256113 | 0.0084348362047383715 |
| ctx-lh-caudalanteriorcingulate | GFAP | amyloid | 9.327841088307359 | 21.101037088945183 | 0.41989351916446449 | 0.25743308694858419 | 0.58235395138034474 | 0.17174553155064476 |
| ctx-lh-caudalanteriorcingulate | GFAP | tau | -5.1149264059277684 | 4.8197122835172621 | -0.0040737123479847263 | -0.14116356418672135 | 0.13301613949075189 | 1.6116071870508869e-05 |
| ctx-lh-caudalanteriorcingulate | NFL | amyloid | -0.6706083037543844 | 3.899789776681486 | 0.139861019272423 | -0.058090238459482336 | 0.33781227700432837 | 0.01934356895306175 |
| ctx-lh-caudalanteriorcingulate | NFL | tau | -1.1515890080717637 | 2.7275062731351403 | 0.068255499676511622 | -0.099754327096296586 | 0.23626532644931983 | 0.0038642244650623813 |
| ctx-lh-caudalmiddlefrontal | GFAP | amyloid | 7.6266246043748156 | 19.988780310220843 | 0.3810698996261252 | 0.21048230735441317 | 0.55165749189783719 | 0.14215421761112867 |
| ctx-lh-caudalmiddlefrontal | GFAP | tau | -1.3785077513701971 | 9.6858731169485957 | 0.1146348169005242 | -0.038044548835916868 | 0.26731418263696527 | 0.013114425234171376 |
| ctx-lh-caudalmiddlefrontal | NFL | amyloid | -0.71700291223549573 | 3.8098872520725049 | 0.13395777223669356 | -0.062109087994768095 | 0.33002463246815522 | 0.0172641251658428 |
| ctx-lh-caudalmiddlefrontal | NFL | tau | -0.30002584066300719 | 3.1270362374576335 | 0.12244234611907155 | -0.025989198956450875 | 0.27087389119459399 | 0.0128390043096767 |
| ctx-lh-cuneus | GFAP | amyloid | 5.0509201131164518 | 17.767742009061514 | 0.31487878998670626 | 0.13939709567738889 | 0.49036048429602369 | 0.094116398420831054 |
| ctx-lh-cuneus | GFAP | tau | -3.5930483239110256 | 8.2153801619311118 | 0.063784381760847622 | -0.099162229804635085 | 0.22673099332633034 | 0.0037986661719383069 |
| ctx-lh-cuneus | NFL | amyloid | -0.68793182881322545 | 3.4516391105357589 | 0.11970058686170873 | -0.059590857667435763 | 0.29899203139085323 | 0.01378967249615462 |
| ctx-lh-cuneus | NFL | tau | -0.27428841236117441 | 2.9132651328749106 | 0.11429830657138157 | -0.023759740509519855 | 0.25235635365228298 | 0.011274477061994068 |
| ctx-lh-entorhinal | GFAP | amyloid | 4.119905139353782 | 16.3688843196101 | 0.28272846140530683 | 0.11370261220344598 | 0.45175431060716764 | 0.070108222934901168 |
| ctx-lh-entorhinal | GFAP | tau | -1.1298205956444702 | 10.549591968162421 | 0.12998510586854534 | -0.031181191969429516 | 0.29115140370652015 | 0.013419366167621457 |
| ctx-lh-entorhinal | NFL | amyloid | -0.79950073041437308 | 3.4228833599861068 | 0.11362290152770084 | -0.069255313151194473 | 0.29650111620659614 | 0.010843798818827131 |
| ctx-lh-entorhinal | NFL | tau | -1.2376482683001209 | 2.2574263264516041 | 0.044168220287549791 | -0.10720905576625787 | 0.19554549634135746 | 0.0014119058822542969 |
| ctx-lh-frontalpole | GFAP | amyloid | 9.8781255744892178 | 20.73536969508017 | 0.42244108336118802 | 0.27262003456450007 | 0.57226213215787591 | 0.17789486314619365 |
| ctx-lh-frontalpole | GFAP | tau | -3.4400727023982851 | 5.685401959171112 | 0.030983699031470503 | -0.094940354013540409 | 0.15690775207648144 | 0.00097078106614373978 |
| ctx-lh-frontalpole | NFL | amyloid | -0.3468375501747416 | 3.4705719262716812 | 0.13529393669573028 | -0.030044179118504814 | 0.30063205250996539 | 0.018351657999090339 |
| ctx-lh-frontalpole | NFL | tau | -1.034768334683821 | 2.7646523298162409 | 0.07492404524511323 | -0.089634946324971737 | 0.23948303681519817 | 0.0047632608194611683 |
| ctx-lh-fusiform | GFAP | amyloid | 5.0803680551423467 | 17.382389665706143 | 0.30996760165140735 | 0.14020981048977049 | 0.47972539281304416 | 0.082490816072825116 |
| ctx-lh-fusiform | GFAP | tau | -0.73263138816921991 | 10.806057339133226 | 0.13900500202320731 | -0.020219422486543771 | 0.29822942653295836 | 0.016082962979927465 |
| ctx-lh-fusiform | NFL | amyloid | -1.2122448977764391 | 3.4165469869181493 | 0.095471852404824822 | -0.10500853447367373 | 0.29595223928332337 | 0.0075112098352892436 |
| ctx-lh-fusiform | NFL | tau | -0.39988463977092281 | 3.4715358195166353 | 0.13303813008042559 | -0.034639287868235301 | 0.30071554802908645 | 0.013111074246914954 |
| ctx-lh-inferiorparietal | GFAP | amyloid | 4.7935344463452427 | 17.159258576993821 | 0.30293050780129788 | 0.13229367419904814 | 0.47356734140354756 | 0.084733816831151484 |
| ctx-lh-inferiorparietal | GFAP | tau | 0.73776007264854204 | 12.249822638580998 | 0.17921797110924981 | 0.02036096575094953 | 0.33807497646755008 | 0.029826112549548485 |
| ctx-lh-inferiorparietal | NFL | amyloid | -1.1757514031012912 | 3.1416245568220411 | 0.085145113504707548 | -0.10184735111815771 | 0.27213757812757283 | 0.0063334587508567432 |
| ctx-lh-inferiorparietal | NFL | tau | -0.093464460215586742 | 3.2197096286960836 | 0.13540268313345447 | -0.008096190803206612 | 0.27890155707011555 | 0.015062759855978256 |
| ctx-lh-inferiortemporal | GFAP | amyloid | 5.0417396385641586 | 18.398492394525352 | 0.32345594408943296 | 0.13914372966468824 | 0.50776815851417767 | 0.0830169949633634 |
| ctx-lh-inferiortemporal | GFAP | tau | -1.3970575771631131 | 11.637530259131335 | 0.14131010966923008 | -0.038556493547562395 | 0.32117671288602251 | 0.015813594687740622 |
| ctx-lh-inferiortemporal | NFL | amyloid | -1.3284386903674417 | 3.5467539437161042 | 0.09607878498066412 | -0.11507361282318833 | 0.30723118278451655 | 0.0069142344523572758 |
| ctx-lh-inferiortemporal | NFL | tau | -0.49341884419867821 | 3.5507689964274514 | 0.13241872968378293 | -0.04274152013841058 | 0.30757897950597646 | 0.012148541617302021 |
| ctx-lh-insula | GFAP | amyloid | 8.3629108157654937 | 19.92633100973903 | 0.39036829538742374 | 0.23080259695642816 | 0.54993399381841934 | 0.1395445638238606 |
| ctx-lh-insula | GFAP | tau | -5.9899802498138568 | 4.6704397047034147 | -0.018208575417703637 | -0.16531361242888082 | 0.12889646159347357 | 0.00028352681447494174 |
| ctx-lh-insula | NFL | amyloid | -0.89392084584679599 | 3.7655307249967676 | 0.12437402110034376 | -0.077434285869149619 | 0.32618232806983716 | 0.014385000943790589 |
| ctx-lh-insula | NFL | tau | -1.0462183547543167 | 2.852526482870489 | 0.078234096794006183 | -0.090626783724743282 | 0.24709497731275565 | 0.0046201292756794764 |
| ctx-lh-isthmuscingulate | GFAP | amyloid | 5.9511461835005433 | 18.521559436797819 | 0.33770323133584784 | 0.1642418560090235 | 0.51116460666267216 | 0.10814011321536082 |
| ctx-lh-isthmuscingulate | GFAP | tau | -1.6975238776786208 | 9.7853641863369383 | 0.11160555147187423 | -0.046848869729087174 | 0.27005997267283566 | 0.011920021582174166 |
| ctx-lh-isthmuscingulate | NFL | amyloid | -1.1214413933548837 | 3.5992500115758199 | 0.10731785804290644 | -0.097142844181331706 | 0.31177856026714457 | 0.010760862880429387 |
| ctx-lh-isthmuscingulate | NFL | tau | -0.44266286982649161 | 3.242450995454484 | 0.12126330597400825 | -0.038344875125193474 | 0.28087148707320997 | 0.012493785677963378 |
| ctx-lh-lateraloccipital | GFAP | amyloid | 4.4840085036537181 | 17.043285678014083 | 0.29705897336650844 | 0.1237512667798616 | 0.47036667995315529 | 0.080083813912064233 |
| ctx-lh-lateraloccipital | GFAP | tau | -1.5396932472312335 | 10.471466887671003 | 0.1232511380938225 | -0.042493003668928442 | 0.28899527985657342 | 0.013151062172208256 |
| ctx-lh-lateraloccipital | NFL | amyloid | -0.89326386436162797 | 3.0460060391421875 | 0.093238709970245942 | -0.077377376029347147 | 0.26385479596983907 | 0.0077880354395602853 |
| ctx-lh-lateraloccipital | NFL | tau | -0.41378860788740157 | 3.5299722548375652 | 0.13496690252822627 | -0.035843694104927395 | 0.30577749916137997 | 0.014414414064291423 |
| ctx-lh-lateralorbitofrontal | GFAP | amyloid | 9.7527483292506716 | 20.798064505430048 | 0.42157611725820243 | 0.26915982861016324 | 0.57399240590624168 | 0.16319900836685131 |
| ctx-lh-lateralorbitofrontal | GFAP | tau | -5.6500640772775412 | 5.3598847783064123 | -0.004004235921018973 | -0.15593248460183612 | 0.14792401275979819 | 1.4283347231970436e-05 |
| ctx-lh-lateralorbitofrontal | NFL | amyloid | -0.52969853827264668 | 4.1040120959093311 | 0.15480924239205573 | -0.045884183401294638 | 0.3555026681854061 | 0.022175361129440498 |
| ctx-lh-lateralorbitofrontal | NFL | tau | -1.2130036943653641 | 2.7656185557633348 | 0.067246235268343516 | -0.10507426386376049 | 0.23956673440044754 | 0.0034617796318548626 |
| ctx-lh-lingual | GFAP | amyloid | 4.5957124650008643 | 17.607129105331836 | 0.30638097231555023 | 0.12683411256612051 | 0.48592783206497997 | 0.083595993070404176 |
| ctx-lh-lingual | GFAP | tau | -3.8133683419118638 | 8.0478210853864773 | 0.058431968928856375 | -0.10524270028151962 | 0.2221066381392324 | 0.0028807957380749794 |
| ctx-lh-lingual | NFL | amyloid | -1.0448386911293839 | 3.5596647956154475 | 0.10892114463529812 | -0.090507272844073394 | 0.30834956211466963 | 0.010695544122811578 |
| ctx-lh-lingual | NFL | tau | -0.37247952420659036 | 3.1668472790104842 | 0.12102854103600502 | -0.032265369010939411 | 0.27432245108294945 | 0.011489335792359161 |
| ctx-lh-medialorbitofrontal | GFAP | amyloid | 10.246420545556688 | 21.361933751320279 | 0.4361693205842414 | 0.28278437060024003 | 0.58955427056824283 | 0.18262357399672255 |
| ctx-lh-medialorbitofrontal | GFAP | tau | -5.8486798393015658 | 4.5562217624507078 | -0.01783485960606792 | -0.16141395327721728 | 0.12574423406508145 | 0.00030767736435743958 |
| ctx-lh-medialorbitofrontal | NFL | amyloid | -0.31658552380342231 | 3.9780856667251316 | 0.15858543298000441 | -0.02742365173172177 | 0.34459451769173061 | 0.024486062959334653 |
| ctx-lh-medialorbitofrontal | NFL | tau | -1.2269304269286698 | 2.513443339406602 | 0.055720933851139784 | -0.10628064202972512 | 0.21772250973200469 | 0.0025465581894822046 |
| ctx-lh-middletemporal | GFAP | amyloid | 4.68898334837652 | 17.693945291837156 | 0.3088660259244233 | 0.1294082356887705 | 0.48832381616007609 | 0.077945925490711054 |
| ctx-lh-middletemporal | GFAP | tau | -1.1135343191895206 | 12.343278867503306 | 0.15496124866129338 | -0.030731717500149452 | 0.34065421482273622 | 0.018928887939717604 |
| ctx-lh-middletemporal | NFL | amyloid | -1.1750483060835351 | 3.4830495423802752 | 0.099963228482749827 | -0.10178644660326736 | 0.30171290356876701 | 0.0076781169646864484 |
| ctx-lh-middletemporal | NFL | tau | -0.594017869234303 | 3.3017792845375391 | 0.11727748182190773 | -0.051455729790146745 | 0.28601069343396218 | 0.0095644225621697374 |
| ctx-lh-paracentral | GFAP | amyloid | 8.2522390133756662 | 20.963961413411781 | 0.40315956251679907 | 0.22774823706139408 | 0.57857088797220413 | 0.15979106092916598 |
| ctx-lh-paracentral | GFAP | tau | -4.8729104886338144 | 6.5662879598379442 | 0.023367217861789871 | -0.13448432253907217 | 0.18121875826265191 | 0.00053368385739369876 |
| ctx-lh-paracentral | NFL | amyloid | -0.66679081750027769 | 3.5430258889983008 | 0.12457434558552767 | -0.0577595555771271 | 0.30690824674818246 | 0.015698751365352953 |
| ctx-lh-paracentral | NFL | tau | -0.16933334280975787 | 3.3374970486966387 | 0.13721824209699321 | -0.014668196334417656 | 0.2891046805284041 | 0.015915726861933981 |
| ctx-lh-parahippocampal | GFAP | amyloid | 4.3076770617602502 | 16.163107772072301 | 0.28248001237068932 | 0.11888480872349183 | 0.44607521601788686 | 0.068792567918215086 |
| ctx-lh-parahippocampal | GFAP | tau | -0.087256857313811942 | 11.357661800271874 | 0.15552232870171909 | -0.0024081458853200599 | 0.31345280328875819 | 0.01885705187652784 |
| ctx-lh-parahippocampal | NFL | amyloid | -1.2497122085696746 | 3.2791559132831041 | 0.087898455839936065 | -0.1082540728993532 | 0.28405098457922534 | 0.0063638130433844777 |
| ctx-lh-parahippocampal | NFL | tau | -0.50087844060632514 | 3.203260089604151 | 0.11704447553061369 | -0.043387694263761725 | 0.27747664532498911 | 0.0096527977744214396 |
| ctx-lh-parsopercularis | GFAP | amyloid | 8.5744560129786116 | 19.945729496927708 | 0.39355512849403396 | 0.23664089679796224 | 0.55046936019010573 | 0.14901584977227975 |
| ctx-lh-parsopercularis | GFAP | tau | -2.8020256271030819 | 7.9630575398737617 | 0.071218000208545865 | -0.077331303145633135 | 0.21976730356272486 | 0.0046547052018253762 |
| ctx-lh-parsopercularis | NFL | amyloid | -0.88342320183472811 | 3.5889313202117243 | 0.11717988792467107 | -0.076524946332925919 | 0.31088472218226804 | 0.013234180971492177 |
| ctx-lh-parsopercularis | NFL | tau | -0.47911408826781932 | 3.5980926035527268 | 0.13508795275018087 | -0.04150239637797376 | 0.31167830187833551 | 0.014327867515208717 |
| ctx-lh-parsorbitalis | GFAP | amyloid | 8.4910804111773537 | 18.876893895947397 | 0.37765556052644628 | 0.23433986718728428 | 0.52097125386560827 | 0.13646312883804299 |
| ctx-lh-parsorbitalis | GFAP | tau | -3.1504921437979778 | 7.8932170483629225 | 0.065445707166932196 | -0.08694840642191394 | 0.21783982075577835 | 0.0037018523752884425 |
| ctx-lh-parsorbitalis | NFL | amyloid | -0.36891371180489863 | 3.9370894649807298 | 0.15454340425468663 | -0.03195648692350269 | 0.34104329543287593 | 0.022729955634733196 |
| ctx-lh-parsorbitalis | NFL | tau | -1.1066959254529634 | 2.9332043278136135 | 0.079109003010674847 | -0.095865544538867212 | 0.25408355056021686 | 0.0047488922494765776 |
| ctx-lh-parstriangularis | GFAP | amyloid | 9.2724003004258559 | 19.475445998370887 | 0.39669666033974033 | 0.25590301230086238 | 0.53749030837861833 | 0.15224841157283259 |
| ctx-lh-parstriangularis | GFAP | tau | -3.3100474039371028 | 7.8364994542350264 | 0.062461319462957958 | -0.091351869427730742 | 0.21627450835364664 | 0.0035016949384557004 |
| ctx-lh-parstriangularis | NFL | amyloid | -0.5932281799362118 | 3.7871388497491711 | 0.13833338432361061 | -0.051387324374678134 | 0.32805409302189942 | 0.018478095968515938 |
| ctx-lh-parstriangularis | NFL | tau | -0.9036679324768051 | 3.1390519485542803 | 0.096818060420271704 | -0.078278609721766035 | 0.27191473056230947 | 0.0072256824943456466 |
| ctx-lh-pericalcarine | GFAP | amyloid | 6.179833364959622 | 19.0358028893707 | 0.34795506371039686 | 0.17055324644880904 | 0.52535688097198474 | 0.11056767183554699 |
| ctx-lh-pericalcarine | GFAP | tau | -6.8746296467044505 | 5.4259018565119508 | -0.019991253262502357 | -0.18972848216698379 | 0.14974597564197908 | 0.00034751807465291975 |
| ctx-lh-pericalcarine | NFL | amyloid | -0.75591601356809579 | 3.8769192407907287 | 0.13517564626561737 | -0.065479865426174094 | 0.33583115795740881 | 0.017079531635591012 |
| ctx-lh-pericalcarine | NFL | tau | -0.74767844367763403 | 2.423463836863113 | 0.0725809481869433 | -0.064766300746785868 | 0.20992819712067251 | 0.0042261609292563677 |
| ctx-lh-postcentral | GFAP | amyloid | 7.4495588065770137 | 19.002641775064777 | 0.36501863549386815 | 0.20559558228174438 | 0.52444168870599195 | 0.12791571681618941 |
| ctx-lh-postcentral | GFAP | tau | -3.8957372916883282 | 6.864140858289006 | 0.040961530445512019 | -0.10751594795039859 | 0.18943900884142265 | 0.0015007933695452341 |
| ctx-lh-postcentral | NFL | amyloid | -0.91593681031059138 | 3.5896525608770524 | 0.11580290957757475 | -0.079341379202854861 | 0.31094719835800438 | 0.013106358853840584 |
| ctx-lh-postcentral | NFL | tau | -0.48059851041260293 | 3.2989339917190708 | 0.12206662164138335 | -0.041630981777054356 | 0.28576422505982108 | 0.01186501634430564 |
| ctx-lh-posteriorcingulate | GFAP | amyloid | 7.8566985411754642 | 20.321027683006626 | 0.38882947170788301 | 0.21683196996297208 | 0.56082697345279386 | 0.14920310790020494 |
| ctx-lh-posteriorcingulate | GFAP | tau | -1.4445876247340008 | 10.305972998405569 | 0.12227983784183748 | -0.039868244761283707 | 0.28442792044495863 | 0.014918208566446333 |
| ctx-lh-posteriorcingulate | NFL | amyloid | -0.9992724708554328 | 3.3475553474718214 | 0.10170789081291129 | -0.086560180947667972 | 0.28997596257349056 | 0.010126209341158753 |
| ctx-lh-posteriorcingulate | NFL | tau | 0.27520118259251514 | 3.7863824814176903 | 0.17591369078238042 | 0.023838807589513424 | 0.32798857397524739 | 0.026025886152490654 |
| ctx-lh-precentral | GFAP | amyloid | 7.3055056157017866 | 19.491100398618634 | 0.36977114750907936 | 0.20161995091530857 | 0.53792234410285011 | 0.12913807607639297 |
| ctx-lh-precentral | GFAP | tau | -4.3430586034221683 | 6.6904190516862787 | 0.032391645647519132 | -0.11986128113600378 | 0.18464457243104204 | 0.00092915457173629466 |
| ctx-lh-precentral | NFL | amyloid | -0.97269896536232126 | 3.6245629609046564 | 0.11485647508444133 | -0.084258298817433283 | 0.31397124898631595 | 0.012624462806267542 |
| ctx-lh-precentral | NFL | tau | -0.66429797561893533 | 3.0891219353162866 | 0.10502300765774286 | -0.057543617631655435 | 0.26758963294714116 | 0.0086615797240445821 |
| ctx-lh-precuneus | GFAP | amyloid | 7.2342387535687607 | 19.700709355280576 | 0.37168015475482641 | 0.19965310262293773 | 0.54370720688671503 | 0.13924923210182516 |
| ctx-lh-precuneus | GFAP | tau | -1.5444443548165587 | 10.309490218952227 | 0.12095043176061532 | -0.042624126431477248 | 0.28452498995270786 | 0.016089625655713997 |
| ctx-lh-precuneus | NFL | amyloid | -0.61596468821765882 | 3.5851165918243417 | 0.12859872233710801 | -0.05335683352094274 | 0.31055427819515874 | 0.016399278715146008 |
| ctx-lh-precuneus | NFL | tau | -0.29500639878450974 | 2.991492393536435 | 0.11678912530671871 | -0.025554398829427363 | 0.25913264944286479 | 0.012956055845606509 |
| ctx-lh-rostralanteriorcingulate | GFAP | amyloid | 10.435584120450269 | 21.838821289943535 | 0.44536027873816592 | 0.28800497444222944 | 0.60271558303410233 | 0.19231353441196841 |
| ctx-lh-rostralanteriorcingulate | GFAP | tau | -6.6092158444265507 | 3.7767947813001865 | -0.03908508361773156 | -0.18240349734012934 | 0.10423333010466622 | 0.0014530640684769511 |
| ctx-lh-rostralanteriorcingulate | NFL | amyloid | -0.21337669555057981 | 3.9050325369951828 | 0.15989152456006689 | -0.018483372569107568 | 0.33826642168924137 | 0.025327529103556831 |
| ctx-lh-rostralanteriorcingulate | NFL | tau | -1.1071124550598912 | 2.5537708919211841 | 0.062657092893285721 | -0.095901625667085294 | 0.22121581145365676 | 0.0031564638575481566 |
| ctx-lh-rostralmiddlefrontal | GFAP | amyloid | 9.0163056760252047 | 19.482222511490541 | 0.39325627523821283 | 0.2488352214705663 | 0.53767732900585929 | 0.15621087168742764 |
| ctx-lh-rostralmiddlefrontal | GFAP | tau | -0.65950968773722085 | 9.9728993387694089 | 0.12851712551287042 | -0.018201383704908078 | 0.27523563473064894 | 0.016038414506659215 |
| ctx-lh-rostralmiddlefrontal | NFL | amyloid | -0.49196837055157427 | 3.699724430409784 | 0.13893305033191264 | -0.042615875466897053 | 0.32048197613072232 | 0.019040158132209418 |
| ctx-lh-rostralmiddlefrontal | NFL | tau | -0.56631133282124413 | 3.2786531762576971 | 0.11747586749728293 | -0.049055700893829345 | 0.28400743588839522 | 0.011310986544013094 |
| ctx-lh-superiorfrontal | GFAP | amyloid | 9.2122876022646736 | 20.980921495468671 | 0.4166414794875124 | 0.25424400060609414 | 0.57903895836893071 | 0.17064791399874008 |
| ctx-lh-superiorfrontal | GFAP | tau | -1.8099482609201223 | 7.9445249848953852 | 0.084652118760658257 | -0.049951597975865465 | 0.219255835497182 | 0.0069205854389347166 |
| ctx-lh-superiorfrontal | NFL | amyloid | -0.5425380488301661 | 3.8287548491817676 | 0.14233131061250559 | -0.046996382915994526 | 0.33165900414100574 | 0.019786976054669898 |
| ctx-lh-superiorfrontal | NFL | tau | -0.44368352388187504 | 3.2591710900525763 | 0.12194327387755245 | -0.038433287447453619 | 0.28231983520255854 | 0.01201080499402422 |
| ctx-lh-superiorparietal | GFAP | amyloid | 6.4578547030306606 | 18.375620020106503 | 0.34268154855524624 | 0.17822617854741868 | 0.50713691856307375 | 0.1138272075731131 |
| ctx-lh-superiorparietal | GFAP | tau | 0.31366680593793816 | 11.140244275002551 | 0.15805456264136272 | 0.0086566884407074073 | 0.30745243684201806 | 0.024976033437032544 |
| ctx-lh-superiorparietal | NFL | amyloid | -0.92395143878555874 | 3.1828962187095868 | 0.097838514821500758 | -0.08003563198300763 | 0.27571266162600916 | 0.0089466621224346642 |
| ctx-lh-superiorparietal | NFL | tau | 0.036557910567140084 | 3.2830430705686271 | 0.14377723292786432 | 0.0031667632663305093 | 0.28438770258939816 | 0.017947628390711231 |
| ctx-lh-superiortemporal | GFAP | amyloid | 6.8125470879477756 | 19.262321493800322 | 0.35981176390281588 | 0.18801510555656625 | 0.53160842224906546 | 0.11572415317972383 |
| ctx-lh-superiortemporal | GFAP | tau | -3.022021135548465 | 8.504093641729412 | 0.075648096637879844 | -0.083402817692006609 | 0.23469901096776627 | 0.0049824163816503059 |
| ctx-lh-superiortemporal | NFL | amyloid | -1.1098292171383768 | 3.6425337149885788 | 0.10969548647388026 | -0.096136960296992743 | 0.31552793324475326 | 0.010561195669648041 |
| ctx-lh-superiortemporal | NFL | tau | -1.0827430072424056 | 3.1578506789407532 | 0.089876235354675996 | -0.093790666069778941 | 0.27354313677913089 | 0.0061642284279660722 |
| ctx-lh-supramarginal | GFAP | amyloid | 6.4908359692440074 | 18.443705944299378 | 0.34407619274832257 | 0.17913640730157465 | 0.5090159781950705 | 0.11082382323817033 |
| ctx-lh-supramarginal | GFAP | tau | -1.2665834837341201 | 11.269762350517251 | 0.13803564997493495 | -0.034955622958080836 | 0.3110269229079507 | 0.017560765628429054 |
| ctx-lh-supramarginal | NFL | amyloid | -1.146066677274685 | 3.3783476057578326 | 0.096683660728748372 | -0.099275965120969881 | 0.29264328657846661 | 0.0084314277881508658 |
| ctx-lh-supramarginal | NFL | tau | -0.36201886056744614 | 3.2353930998490741 | 0.12445043836225547 | -0.031359232833024012 | 0.28026010955753494 | 0.012398410156218309 |
| ctx-lh-temporalpole | GFAP | amyloid | 8.3694316912471418 | 21.123969094797907 | 0.40698469973297624 | 0.23098256240491252 | 0.58298683706103993 | 0.14019627597429557 |
| ctx-lh-temporalpole | GFAP | tau | -4.1828912333972728 | 7.1907659334450624 | 0.041506199658487078 | -0.11544092490313113 | 0.19845332422010528 | 0.0014110106878578231 |
| ctx-lh-temporalpole | NFL | amyloid | -1.0326644257289779 | 3.6267131324824815 | 0.11235240236900929 | -0.089452698994898952 | 0.31415750373291751 | 0.010387792891299132 |
| ctx-lh-temporalpole | NFL | tau | -1.1769685036473758 | 2.9083756488574792 | 0.074990015313427943 | -0.1019527802644349 | 0.25193281089129083 | 0.0038810407326952141 |
| ctx-lh-transversetemporal | GFAP | amyloid | 6.8572639385172494 | 19.82273027562551 | 0.36816200047225872 | 0.18924921715556725 | 0.54707478378895025 | 0.13037082476781567 |
| ctx-lh-transversetemporal | GFAP | tau | -5.4444999493663504 | 5.8676666542497555 | 0.0058393528631480668 | -0.15025925244521129 | 0.16193795817150744 | 3.1866930017541585e-05 |
| ctx-lh-transversetemporal | NFL | amyloid | -0.94081932814575464 | 3.5781344464514309 | 0.11422633991964863 | -0.081496782567866521 | 0.30994946240716381 | 0.012731897397076749 |
| ctx-lh-transversetemporal | NFL | tau | -1.4068462019541192 | 2.9155311899157752 | 0.065343562121348717 | -0.12186552252604362 | 0.25255264676874106 | 0.0035533778471092581 |
| ctx-rh-bankssts | GFAP | amyloid | 6.4615508101018735 | 18.844931076156715 | 0.34920865879427992 | 0.17832818502930733 | 0.52008913255925249 | 0.10770633774294396 |
| ctx-rh-bankssts | GFAP | tau | -2.251902077773333 | 7.8905348742597772 | 0.077808500017683996 | -0.062148797122391311 | 0.21776579715775932 | 0.0056996420477553687 |
| ctx-rh-bankssts | NFL | amyloid | -1.0065316931156696 | 3.0083555863666644 | 0.086702197588229113 | -0.087188998022802167 | 0.26059339319926039 | 0.0064774469444346524 |
| ctx-rh-bankssts | NFL | tau | -1.1599175446281131 | 3.0214525834184851 | 0.080626062709492227 | -0.10047577159954577 | 0.26172789701853022 | 0.0053640576002492819 |
| ctx-rh-caudalanteriorcingulate | GFAP | amyloid | 9.683247746700733 | 20.624467062136098 | 0.41822156422542478 | 0.26724172673201446 | 0.56920140171883515 | 0.16632152681853099 |
| ctx-rh-caudalanteriorcingulate | GFAP | tau | -5.212820760634397 | 4.3182958280015153 | -0.012343709148777105 | -0.14386528752102615 | 0.11917786922347193 | 0.00014154868512262898 |
| ctx-rh-caudalanteriorcingulate | NFL | amyloid | -0.68758389137425557 | 3.6287056618259621 | 0.12738469239600247 | -0.059560718212428143 | 0.31433010300443309 | 0.015608137324154314 |
| ctx-rh-caudalanteriorcingulate | NFL | tau | -1.251838824622719 | 2.6389365792977904 | 0.060077424395567389 | -0.10843828719097694 | 0.2285931359821117 | 0.0028646017187805711 |
| ctx-rh-caudalmiddlefrontal | GFAP | amyloid | 8.3090953434112418 | 20.00362927883409 | 0.39069233868950948 | 0.22931737834661314 | 0.55206729903240592 | 0.14898666015600226 |
| ctx-rh-caudalmiddlefrontal | GFAP | tau | 0.4168951370545475 | 10.530633519999865 | 0.15106690122414007 | 0.011505620759377682 | 0.29062818168890242 | 0.022750984722225639 |
| ctx-rh-caudalmiddlefrontal | NFL | amyloid | -0.95665081190305545 | 3.4215280666534786 | 0.10675777998884504 | -0.082868156380985686 | 0.29638371635867578 | 0.010481260583606005 |
| ctx-rh-caudalmiddlefrontal | NFL | tau | -0.4968382895520953 | 2.9719246738416949 | 0.10719995373324569 | -0.043037723443480183 | 0.25743763090997157 | 0.0094099791314203596 |
| ctx-rh-cuneus | GFAP | amyloid | 5.0715933301984997 | 18.178933389684548 | 0.32083816662480047 | 0.13996764249955346 | 0.50170869075004743 | 0.095498821178060425 |
| ctx-rh-cuneus | GFAP | tau | -2.9916662704217654 | 7.7620711566067353 | 0.065827668172038487 | -0.082565073292258026 | 0.21422040963633499 | 0.0039192233270877322 |
| ctx-rh-cuneus | NFL | amyloid | -0.71757054138472043 | 3.3695823056387848 | 0.11486287518391308 | -0.06215825784913824 | 0.29188400821696442 | 0.012326698474892737 |
| ctx-rh-cuneus | NFL | tau | -0.81216018507118592 | 3.299462538924216 | 0.10772904693189879 | -0.070351915647262883 | 0.28581000951106045 | 0.0096252271100533953 |
| ctx-rh-entorhinal | GFAP | amyloid | 5.4168201469037376 | 16.857223403753796 | 0.30736350114608807 | 0.14949533537944892 | 0.46523166691272716 | 0.083287742358565287 |
| ctx-rh-entorhinal | GFAP | tau | -1.9513365211112301 | 9.987835013647274 | 0.11089707659066773 | -0.053853681634313741 | 0.2756478348156492 | 0.0097449039701254809 |
| ctx-rh-entorhinal | NFL | amyloid | -1.1507294793146645 | 3.1280945271974243 | 0.085642845838534126 | -0.099679871963273117 | 0.27096556364034136 | 0.0062204683693323276 |
| ctx-rh-entorhinal | NFL | tau | -1.4262456048615269 | 2.439255484469288 | 0.043875079639469496 | -0.1235459609198927 | 0.21129612019883171 | 0.0013650239975169084 |
| ctx-rh-frontalpole | GFAP | amyloid | 9.5872992236244929 | 20.716731298749821 | 0.41817072409916889 | 0.26459370515340547 | 0.57174774304493237 | 0.17748042033919764 |
| ctx-rh-frontalpole | GFAP | tau | -3.773731265703101 | 6.4475723626433536 | 0.036896810370095193 | -0.10414878210801763 | 0.177942402848208 | 0.0013586914602063281 |
| ctx-rh-frontalpole | NFL | amyloid | -0.61813706820025183 | 3.6127160956735782 | 0.12970001177871107 | -0.053545012030673293 | 0.31294503558809544 | 0.017223533821878849 |
| ctx-rh-frontalpole | NFL | tau | -0.82220216318174788 | 2.7803214254500319 | 0.084809280052496355 | -0.07122178394412354 | 0.24084034404911625 | 0.0060323040396588349 |
| ctx-rh-fusiform | GFAP | amyloid | 5.0369836236537804 | 16.720230960007633 | 0.3002316860165915 | 0.13901247146803147 | 0.46145090056515159 | 0.078056174810447951 |
| ctx-rh-fusiform | GFAP | tau | 0.46559497603327404 | 11.236191273041197 | 0.16147503631295104 | 0.012849656293806746 | 0.31010041633209534 | 0.020893781615846679 |
| ctx-rh-fusiform | NFL | amyloid | -1.1462868188023279 | 3.1351240314219107 | 0.086139723659370518 | -0.099295034484954803 | 0.27157448180369581 | 0.0060705488628680724 |
| ctx-rh-fusiform | NFL | tau | -0.85596271517068745 | 3.6428560891182369 | 0.12070481363518755 | -0.074146231053683259 | 0.31555585832405836 | 0.010341574469157649 |
| ctx-rh-inferiorparietal | GFAP | amyloid | 5.4192314229436773 | 17.747075299234499 | 0.31967599984972828 | 0.149561882636051 | 0.48979011706340558 | 0.093091607849278793 |
| ctx-rh-inferiorparietal | GFAP | tau | 0.45347374438329702 | 11.472579278966668 | 0.16456973354541743 | 0.012515130217329739 | 0.31662433687350511 | 0.024428758627847075 |
| ctx-rh-inferiorparietal | NFL | amyloid | -1.1696618379730448 | 2.9715067173421148 | 0.078040786345439095 | -0.10131985348886509 | 0.25740142617974326 | 0.0052279803681281141 |
| ctx-rh-inferiorparietal | NFL | tau | -0.34251939452494495 | 3.2806422116037992 | 0.1272548029243224 | -0.029670126650025806 | 0.28417973249867062 | 0.012699316507269616 |
| ctx-rh-inferiortemporal | GFAP | amyloid | 6.8426164156705589 | 19.260979794309716 | 0.36020818157044693 | 0.18884496959314895 | 0.53157139354774496 | 0.10544395256999076 |
| ctx-rh-inferiortemporal | GFAP | tau | -2.5505382009078517 | 8.8543379414784216 | 0.0869872573598508 | -0.070390663415465904 | 0.2443651781351675 | 0.0061427286992206762 |
| ctx-rh-inferiortemporal | NFL | amyloid | -0.81470033666701869 | 3.5996945054460401 | 0.12062255601885204 | -0.070571951711682401 | 0.31181706374938645 | 0.011316593141289596 |
| ctx-rh-inferiortemporal | NFL | tau | -1.3812908006248905 | 3.0962569332715146 | 0.074277928738462395 | -0.11965183183830291 | 0.2682076893152277 | 0.0038873040563140557 |
| ctx-rh-insula | GFAP | amyloid | 9.5483848954820321 | 21.404807124065591 | 0.42712861942368147 | 0.26351973363894626 | 0.59073750520841672 | 0.16653887655565774 |
| ctx-rh-insula | GFAP | tau | -6.453757034511252 | 4.0901319398947393 | -0.0326160844045148 | -0.17811308962938749 | 0.11288092082035787 | 0.0009319276592375113 |
| ctx-rh-insula | NFL | amyloid | -0.83702304706970332 | 3.6869044991288948 | 0.12343292813744243 | -0.072505616360769201 | 0.31937147263565407 | 0.014105777803461011 |
| ctx-rh-insula | NFL | tau | -0.99217486991730164 | 2.7711179833721009 | 0.077048874199663983 | -0.085945364028942053 | 0.24004311242827001 | 0.0044433829973845101 |
| ctx-rh-isthmuscingulate | GFAP | amyloid | 5.294721535844042 | 17.508553064175054 | 0.31466645482295585 | 0.14612561434114427 | 0.48320729530476741 | 0.095423520493441424 |
| ctx-rh-isthmuscingulate | GFAP | tau | -0.13303403015801329 | 11.121815185792755 | 0.15163615181242401 | -0.0036715206368296929 | 0.30694382426167771 | 0.021215409847019182 |
| ctx-rh-isthmuscingulate | NFL | amyloid | -0.98406846056571928 | 3.3114639939606052 | 0.10080322653890124 | -0.085243160895388151 | 0.28684961397319064 | 0.0095025545391295169 |
| ctx-rh-isthmuscingulate | NFL | tau | -0.2782940795030211 | 3.2812060039248303 | 0.13006092288589965 | -0.024106724222898408 | 0.28422856999469764 | 0.013934364767393074 |
| ctx-rh-lateraloccipital | GFAP | amyloid | 5.0980662599513353 | 17.014326497107866 | 0.30513285300308574 | 0.14069825186160489 | 0.46956745414456652 | 0.085426938319332277 |
| ctx-rh-lateraloccipital | GFAP | tau | 0.10309933531136917 | 10.744225071840788 | 0.14968416490104591 | 0.002845372246405747 | 0.29652295755568608 | 0.019698644273535168 |
| ctx-rh-lateraloccipital | NFL | amyloid | -0.88183005232647727 | 2.9299245501085687 | 0.088706251546275719 | -0.076386942621492912 | 0.25379944571404434 | 0.0069587344954886816 |
| ctx-rh-lateraloccipital | NFL | tau | -0.76060680761060362 | 3.4846630211598537 | 0.11798323562070558 | -0.065886197025362581 | 0.30185266826677376 | 0.010960622565495737 |
| ctx-rh-lateralorbitofrontal | GFAP | amyloid | 10.338485348465284 | 21.740659208768065 | 0.44266583938647497 | 0.2853252078837763 | 0.60000647088917369 | 0.17511050195505456 |
| ctx-rh-lateralorbitofrontal | GFAP | tau | -7.4502657215195347 | 3.4774275420760405 | -0.054821902881866086 | -0.20561509197258712 | 0.095971286208854978 | 0.0026300706121098077 |
| ctx-rh-lateralorbitofrontal | NFL | amyloid | -0.45836214617191451 | 3.7693982424895189 | 0.14340627405464457 | -0.039704796708987265 | 0.32651734481827638 | 0.018578233949246313 |
| ctx-rh-lateralorbitofrontal | NFL | tau | -1.3651016783131824 | 2.2166659067935166 | 0.036882610026631589 | -0.11824947822849541 | 0.19201469828175857 | 0.0010131040412427355 |
| ctx-rh-lingual | GFAP | amyloid | 4.6008252083057313 | 17.367903705279584 | 0.30315040999412729 | 0.12697521588030514 | 0.47932560410794939 | 0.083344943839824492 |
| ctx-rh-lingual | GFAP | tau | -1.9775679864668296 | 8.9989628375534565 | 0.096889480324976435 | -0.054577626975764904 | 0.24835658762571775 | 0.0079058717266895766 |
| ctx-rh-lingual | NFL | amyloid | -0.9498576460468211 | 3.2547206693653505 | 0.099827307454617389 | -0.082279710603809619 | 0.28193432551304443 | 0.0089629240679076454 |
| ctx-rh-lingual | NFL | tau | -0.75190582848811638 | 3.1580759510136476 | 0.10421508010642204 | -0.065132490354528713 | 0.27356265056737278 | 0.0083859359728519992 |
| ctx-rh-medialorbitofrontal | GFAP | amyloid | 9.8623165616380817 | 20.730133943006152 | 0.42215068289512619 | 0.27218373178646715 | 0.57211763400378524 | 0.17135456074247615 |
| ctx-rh-medialorbitofrontal | GFAP | tau | -6.7594922222266236 | 3.7488755730851357 | -0.041544036303256433 | -0.18655087844003018 | 0.10346280583351732 | 0.0016122419753727374 |
| ctx-rh-medialorbitofrontal | NFL | amyloid | -0.61476388841795049 | 3.5902615714028761 | 0.12887356820110166 | -0.053252816397509235 | 0.31099995279971254 | 0.016318659736970043 |
| ctx-rh-medialorbitofrontal | NFL | tau | -1.0418916792311914 | 2.6295634868650897 | 0.06876460773339145 | -0.090251993237557171 | 0.22778120870434004 | 0.0037940503109060125 |
| ctx-rh-middletemporal | GFAP | amyloid | 7.2326232832594117 | 19.842397857323956 | 0.37361304751190499 | 0.19960851829686779 | 0.54761757672694211 | 0.11284984413877992 |
| ctx-rh-middletemporal | GFAP | tau | -3.139237862331675 | 8.4071122915512646 | 0.072692339156133406 | -0.086637806745972809 | 0.23202248505823961 | 0.004221262614107611 |
| ctx-rh-middletemporal | NFL | amyloid | -0.8664865661265031 | 3.4467595410166627 | 0.11175575336808323 | -0.075057840719285146 | 0.29856934745545161 | 0.0097024196474443328 |
| ctx-rh-middletemporal | NFL | tau | -1.304739996812825 | 3.1268629686431941 | 0.078919062993659445 | -0.11302075610778731 | 0.27085888209510622 | 0.0042826928168924272 |
| ctx-rh-paracentral | GFAP | amyloid | 7.7633602800564088 | 20.074636450895817 | 0.38414148381541813 | 0.21425598732531634 | 0.55402698030551989 | 0.14183912484147465 |
| ctx-rh-paracentral | GFAP | tau | -4.5933072980056338 | 5.6593171979083809 | 0.014710060808910777 | -0.12676773390911433 | 0.15618785552693587 | 0.00020273157331254684 |
| ctx-rh-paracentral | NFL | amyloid | -0.77378699923563432 | 3.333531761198115 | 0.11086664360203963 | -0.067027907424940525 | 0.28876119462901978 | 0.012120647921046061 |
| ctx-rh-paracentral | NFL | tau | -0.16223201570193524 | 3.209604674085623 | 0.13198658845212491 | -0.014053056642942421 | 0.27802623354719225 | 0.014339782331572159 |
| ctx-rh-parahippocampal | GFAP | amyloid | 4.4747802197692366 | 16.740518380326748 | 0.29275369066936691 | 0.12349658130815069 | 0.46201080003058309 | 0.073073729748911562 |
| ctx-rh-parahippocampal | GFAP | tau | -1.0357037325423146 | 10.376771274938738 | 0.12889905767416412 | -0.028583721196403965 | 0.2863818365447322 | 0.012464400698576144 |
| ctx-rh-parahippocampal | NFL | amyloid | -1.0879921355700766 | 2.8667266239427898 | 0.077039838313365569 | -0.094245362372451791 | 0.2483250389991829 | 0.0048663179660114369 |
| ctx-rh-parahippocampal | NFL | tau | -1.1090060559213233 | 3.3965717873528289 | 0.099078134051309455 | -0.096065655436731512 | 0.29422192353935039 | 0.0066352993800896463 |
| ctx-rh-parsopercularis | GFAP | amyloid | 8.7395414660624731 | 20.564671168347186 | 0.40437405867313619 | 0.24119698404208958 | 0.56755113330418283 | 0.15636243604365063 |
| ctx-rh-parsopercularis | GFAP | tau | -1.5506196632791611 | 8.1258160445016809 | 0.090732308027474534 | -0.042794554798056113 | 0.22425917085300517 | 0.0077564209612429862 |
| ctx-rh-parsopercularis | NFL | amyloid | -0.90567349595699609 | 3.5728512329827899 | 0.11551973774425386 | -0.07845233805193684 | 0.30949181354044458 | 0.012437334815564121 |
| ctx-rh-parsopercularis | NFL | tau | -0.89069401355287114 | 3.2628278492930751 | 0.10274091403617967 | -0.077154767324011678 | 0.28263659539637104 | 0.0082763151966453331 |
| ctx-rh-parsorbitalis | GFAP | amyloid | 9.1591254291526418 | 20.882034307247903 | 0.41454332322145371 | 0.2527768119818925 | 0.57630983446101491 | 0.16410258219789145 |
| ctx-rh-parsorbitalis | GFAP | tau | -4.1031317024004137 | 6.1967018874625799 | 0.028889548523701923 | -0.11323969290488976 | 0.17101878995229361 | 0.00077521363231222772 |
| ctx-rh-parsorbitalis | NFL | amyloid | -0.64002725146235795 | 3.8327560992306231 | 0.13828219771884553 | -0.055441209793955462 | 0.33200560523164652 | 0.018251512908991852 |
| ctx-rh-parsorbitalis | NFL | tau | -1.3169576607035336 | 2.7092780856334895 | 0.060303626605414003 | -0.11407908927314729 | 0.23468634248397532 | 0.0028685305458009129 |
| ctx-rh-parstriangularis | GFAP | amyloid | 9.7195163143665013 | 21.263047993391353 | 0.42753393286937164 | 0.26824267960471149 | 0.58682518613403178 | 0.17440611130453243 |
| ctx-rh-parstriangularis | GFAP | tau | -3.7675973256378192 | 6.4055429397205099 | 0.036401482197581853 | -0.10397949544123011 | 0.17678245983639382 | 0.0012368262020793271 |
| ctx-rh-parstriangularis | NFL | amyloid | -0.4989571837601654 | 3.6530058228035038 | 0.13660689595482464 | -0.043221268844168048 | 0.31643506075381733 | 0.017659619521437728 |
| ctx-rh-parstriangularis | NFL | tau | -1.5157442139618154 | 2.576041544464875 | 0.045923174841445279 | -0.13129861700142539 | 0.22314496668431597 | 0.0016401327294234861 |
| ctx-rh-pericalcarine | GFAP | amyloid | 5.8872807458592664 | 19.602103828579381 | 0.35173256562243166 | 0.1624792748709373 | 0.54098585637392604 | 0.11502250061838104 |
| ctx-rh-pericalcarine | GFAP | tau | -5.7991709106828067 | 6.1981107156656856 | 0.0055050415487966266 | -0.16004758819818299 | 0.17105767129577623 | 2.5720651315199593e-05 |
| ctx-rh-pericalcarine | NFL | amyloid | -0.87545928082078439 | 3.4980433418525951 | 0.1135883142457878 | -0.075835085995404783 | 0.30301171448698039 | 0.012227930921717053 |
| ctx-rh-pericalcarine | NFL | tau | -0.80758242085802801 | 2.9646869143883259 | 0.093427648979045777 | -0.069955375053797425 | 0.25681067301188898 | 0.0067204410983127622 |
| ctx-rh-postcentral | GFAP | amyloid | 8.5541635553327495 | 20.589270374296582 | 0.40215544463933384 | 0.23608085831058964 | 0.568230030968078 | 0.15311619612300653 |
| ctx-rh-postcentral | GFAP | tau | -4.5993973685354641 | 5.8740209827251464 | 0.017588758673736906 | -0.12693580984880781 | 0.16211332719628163 | 0.00027885164398550857 |
| ctx-rh-postcentral | NFL | amyloid | -0.72802509166491736 | 3.5771362849324406 | 0.12339956699604811 | -0.063063864468327555 | 0.30986299846042381 | 0.014673586980709509 |
| ctx-rh-postcentral | NFL | tau | -0.40957741465564013 | 3.0878113331106452 | 0.11599859866207915 | -0.035478907063576391 | 0.26747610438773467 | 0.01050180469549453 |
| ctx-rh-posteriorcingulate | GFAP | amyloid | 7.4600405722196559 | 19.564330174861603 | 0.37291411369479949 | 0.2058848617903157 | 0.53994336559928324 | 0.13501381219281344 |
| ctx-rh-posteriorcingulate | GFAP | tau | -1.3068313455197904 | 9.7251179492856537 | 0.1161654388571178 | -0.036066397809890106 | 0.26839727552412568 | 0.012735830304328554 |
| ctx-rh-posteriorcingulate | NFL | amyloid | -0.98279493588343336 | 3.2974731238092012 | 0.10025241794710718 | -0.085132844109771497 | 0.28563768000398587 | 0.0095579045406616395 |
| ctx-rh-posteriorcingulate | NFL | tau | -0.10311418729491995 | 3.3334877567767647 | 0.13991265088266708 | -0.0089320810598126476 | 0.28875738282514679 | 0.015756117379423958 |
| ctx-rh-precentral | GFAP | amyloid | 7.7238231948177338 | 19.7257258657934 | 0.3787812251045764 | 0.2131648287382881 | 0.54439762147086479 | 0.13366628259886359 |
| ctx-rh-precentral | GFAP | tau | -2.9766804193830909 | 7.0494550117661712 | 0.056200943274924198 | -0.082151488427666633 | 0.19455337497751501 | 0.0027517838165838832 |
| ctx-rh-precentral | NFL | amyloid | -0.84371289780450143 | 3.5982832672668166 | 0.11930485256420006 | -0.073085112651326764 | 0.31169481777972691 | 0.013283079103445308 |
| ctx-rh-precentral | NFL | tau | -0.61532040846635905 | 3.0544373446861348 | 0.10564205935292401 | -0.053301023945996999 | 0.26458514265184502 | 0.0085019708059931448 |
| ctx-rh-precuneus | GFAP | amyloid | 7.1672480271884096 | 19.392084035943803 | 0.3664969619216214 | 0.19780426865098685 | 0.53518965519225592 | 0.13490990342238199 |
| ctx-rh-precuneus | GFAP | tau | -0.29092998307152573 | 10.375896923938477 | 0.13916425820205033 | -0.0080291894897185426 | 0.2863577058938192 | 0.020355784261550821 |
| ctx-rh-precuneus | NFL | amyloid | -0.78267953708735738 | 3.2340937128405054 | 0.10617467248408248 | -0.067798207526243423 | 0.28014755249440837 | 0.011008676236865383 |
| ctx-rh-precuneus | NFL | tau | -0.05899291398487172 | 3.1882550563296177 | 0.13553335310146641 | -0.0051101550959262538 | 0.2761768612988591 | 0.016485278861941476 |
| ctx-rh-rostralanteriorcingulate | GFAP | amyloid | 10.18961707433553 | 20.592035665080921 | 0.42476151829068404 | 0.28121668813144368 | 0.56830634844992434 | 0.17164885150197604 |
| ctx-rh-rostralanteriorcingulate | GFAP | tau | -6.6243933960630015 | 3.2081579792367867 | -0.047141242050053093 | -0.18282237282622557 | 0.088539888726119384 | 0.0020174868629631469 |
| ctx-rh-rostralanteriorcingulate | NFL | amyloid | -0.30524569055066797 | 3.9570280730735345 | 0.15816454121971715 | -0.026441359066904823 | 0.34277044150633912 | 0.024294791932192979 |
| ctx-rh-rostralanteriorcingulate | NFL | tau | -1.2185321273785736 | 2.4078456382512505 | 0.051511072158585886 | -0.10555315443258685 | 0.20857529874975858 | 0.0020874669723146264 |
| ctx-rh-rostralmiddlefrontal | GFAP | amyloid | 8.9895791217082568 | 19.918741087922029 | 0.39891106846748897 | 0.24809761248728981 | 0.54972452444768816 | 0.15999578844089679 |
| ctx-rh-rostralmiddlefrontal | GFAP | tau | -0.3876022809975872 | 10.219443612335503 | 0.13567133275285478 | -0.010697186064908394 | 0.28203985157061795 | 0.017720237984461075 |
| ctx-rh-rostralmiddlefrontal | NFL | amyloid | -0.81210155149475982 | 3.5460363842481351 | 0.11841109443337265 | -0.070346836619136835 | 0.30716902548588215 | 0.013596043586194066 |
| ctx-rh-rostralmiddlefrontal | NFL | tau | -0.65710996864569693 | 3.0999525514595536 | 0.10580342307139742 | -0.056920969452701815 | 0.26852781559549666 | 0.0089301735920724757 |
| ctx-rh-superiorfrontal | GFAP | amyloid | 9.1742989219968294 | 20.285540813533242 | 0.40652158480887346 | 0.25319557545199145 | 0.55984759416575536 | 0.16246627909493722 |
| ctx-rh-superiorfrontal | GFAP | tau | -1.0575162803865004 | 7.9967291092245381 | 0.09575543593684617 | -0.029185711675506494 | 0.22069658354919883 | 0.0085443492855325851 |
| ctx-rh-superiorfrontal | NFL | amyloid | -0.74519445916482563 | 3.5756663234604833 | 0.12259226781809388 | -0.064551130054936595 | 0.30973566569112432 | 0.014569695628195043 |
| ctx-rh-superiorfrontal | NFL | tau | -0.43831556731031851 | 3.23833163342815 | 0.121273178441539 | -0.037968297861824998 | 0.280514654744903 | 0.011452768049008325 |
| ctx-rh-superiorparietal | GFAP | amyloid | 7.1406623602228185 | 18.868876665320219 | 0.3589102697004794 | 0.19707054792710807 | 0.5207499914738507 | 0.12285410884741881 |
| ctx-rh-superiorparietal | GFAP | tau | 0.32704617155222326 | 10.092087212359903 | 0.14377548057244335 | 0.0090259369472902064 | 0.27852502419759645 | 0.020146939130963076 |
| ctx-rh-superiorparietal | NFL | amyloid | -0.9303625284807775 | 3.0180728864456485 | 0.090422077872844772 | -0.080590981099765341 | 0.26143513684545489 | 0.0074866673015775561 |
| ctx-rh-superiorparietal | NFL | tau | -0.33609680968702227 | 3.3896132443823022 | 0.13225268523991002 | -0.029113781787201334 | 0.29361915226702134 | 0.014547233573008226 |
| ctx-rh-superiortemporal | GFAP | amyloid | 8.0590513059928259 | 20.439173875281583 | 0.39325209400102545 | 0.22241657377497451 | 0.56408761422707643 | 0.13642467769611064 |
| ctx-rh-superiortemporal | GFAP | tau | -4.627486121265548 | 5.9865732037102131 | 0.018754285142370691 | -0.12771101326998371 | 0.1652195835547251 | 0.00030827675268759271 |
| ctx-rh-superiortemporal | NFL | amyloid | -0.95800065527883005 | 3.3898177768812769 | 0.10532589269538591 | -0.08298508413619346 | 0.29363686952696527 | 0.0097413146229962441 |
| ctx-rh-superiortemporal | NFL | tau | -1.2922443712783251 | 3.0003672209784225 | 0.073981535198460055 | -0.11193834501485019 | 0.25990141541177031 | 0.0041482317770209056 |
| ctx-rh-supramarginal | GFAP | amyloid | 6.5729905263033981 | 18.626266326738559 | 0.34772904142956501 | 0.18140373808374285 | 0.51405434477538714 | 0.11277796938068149 |
| ctx-rh-supramarginal | GFAP | tau | -0.1759996263604604 | 10.677151649645086 | 0.14490727041111526 | -0.0048573004928831182 | 0.29467184131511359 | 0.01885752497796072 |
| ctx-rh-supramarginal | NFL | amyloid | -0.90228881595120236 | 3.2494340675565336 | 0.10165861845242914 | -0.078159146232591861 | 0.28147638313745016 | 0.0091714398476568076 |
| ctx-rh-supramarginal | NFL | tau | -0.54891452703560373 | 3.1205969114615399 | 0.11138368114217977 | -0.047548733874686548 | 0.27031609615904606 | 0.0095824004860124781 |
| ctx-rh-temporalpole | GFAP | amyloid | 8.7442148860613642 | 20.580298116279025 | 0.40465418707225476 | 0.24132596275490556 | 0.56798241138960404 | 0.13980761755297305 |
| ctx-rh-temporalpole | GFAP | tau | -4.4273301676256098 | 6.7590258882840475 | 0.032175485276348573 | -0.1221870378367769 | 0.18653800838947404 | 0.00083889234936442068 |
| ctx-rh-temporalpole | NFL | amyloid | -1.2979140140020196 | 3.1708579596595232 | 0.081120200730721098 | -0.11242946762093128 | 0.27466986908237351 | 0.0055242900756634714 |
| ctx-rh-temporalpole | NFL | tau | -0.858546112478628 | 3.1750902348271337 | 0.10033323455417853 | -0.074370013200151894 | 0.27503648230850897 | 0.0068954434095671157 |
| ctx-rh-transversetemporal | GFAP | amyloid | 8.0422923188267603 | 19.43093381135089 | 0.37910794921204677 | 0.22195405326680462 | 0.53626184515728892 | 0.13672629557313787 |
| ctx-rh-transversetemporal | GFAP | tau | -6.5314328783149849 | 4.5811804932620079 | -0.026911880630254768 | -0.1802568152849196 | 0.12643305402441007 | 0.0006487908213190952 |
| ctx-rh-transversetemporal | NFL | amyloid | -0.97207071289524549 | 3.4260250842114477 | 0.10628469242058297 | -0.084203877577164007 | 0.29677326241832996 | 0.010973043850076296 |
| ctx-rh-transversetemporal | NFL | tau | -1.1171169272873174 | 2.8854070809084886 | 0.07658747745467126 | -0.096768245084260462 | 0.24994319999360295 | 0.0046642667413801051 |

## T4A — All alternative-model focal coefficients and marginal intervals

Source: tables/T4_all_sensitivities.csv

| region | outcome | predictor | quadratic_age_beta | quadratic_age_ci_low | quadratic_age_ci_high | numeric_sex_contrast_beta | numeric_sex_contrast_ci_low | numeric_sex_contrast_ci_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctx-lh-bankssts | GFAP | amyloid | 11.780623723686629 | 5.5518550218025373 | 18.00939242557072 | 11.949079552325614 | 5.6478111151337922 | 18.250347989517437 |
| ctx-lh-bankssts | GFAP | tau | 4.6359287824977029 | -1.2046384747450336 | 10.476496039740439 | 5.2721834518579467 | -0.72975754316778385 | 11.274124446883675 |
| ctx-lh-bankssts | NFL | amyloid | 1.2470800739888928 | -0.92050756769258024 | 3.4146677156703658 | 1.11333809888821 | -1.0458025041852901 | 3.2724787019617096 |
| ctx-lh-bankssts | NFL | tau | 1.1622169286155328 | -0.52677574146030737 | 2.8512095986913728 | 1.1613465459253338 | -0.39962728214714049 | 2.7223203739978081 |
| ctx-lh-caudalanteriorcingulate | GFAP | amyloid | 15.421454951185687 | 9.3990659846828564 | 21.443843917688518 | 15.426086138252142 | 9.4076110017616159 | 21.444561274742668 |
| ctx-lh-caudalanteriorcingulate | GFAP | tau | -0.14705103656397961 | -5.135932466557402 | 4.8418303934294427 | 1.482306588185593 | -3.3939416603390482 | 6.3585548367102342 |
| ctx-lh-caudalanteriorcingulate | NFL | amyloid | 1.7225966799230616 | -0.5562592797731849 | 4.0014526396193082 | 1.6010637555570004 | -0.69657308330527812 | 3.898700594419279 |
| ctx-lh-caudalanteriorcingulate | NFL | tau | 0.78824872607923291 | -1.1315377205020636 | 2.7080351726605292 | 0.87039465796409365 | -1.0897674018334391 | 2.8305567177616262 |
| ctx-lh-caudalmiddlefrontal | GFAP | amyloid | 14.078197304520558 | 7.7613935025827985 | 20.395001106458317 | 14.069911174570986 | 7.7751434137009312 | 20.364678935441042 |
| ctx-lh-caudalmiddlefrontal | GFAP | tau | 4.1485229783995017 | -1.4056947914992532 | 9.7027407482982575 | 5.2067937861193254 | -0.21140022213803619 | 10.624987794376686 |
| ctx-lh-caudalmiddlefrontal | NFL | amyloid | 1.6796476311920874 | -0.58868110765172754 | 3.9479763700359021 | 1.5463019474445696 | -0.72036259590859641 | 3.8129664907977361 |
| ctx-lh-caudalmiddlefrontal | NFL | tau | 1.4109642967486389 | -0.33207149999586361 | 3.1540000934931411 | 1.4633178108311491 | -0.21398105660223621 | 3.1406166782645344 |
| ctx-lh-cuneus | GFAP | amyloid | 11.708669746676147 | 5.1755409025332062 | 18.241798590819087 | 11.839152404889475 | 5.2158272016696134 | 18.462477608109339 |
| ctx-lh-cuneus | GFAP | tau | 2.291245137716432 | -3.6423909239150878 | 8.2248811993479514 | 3.4599964518805173 | -2.3535108113960899 | 9.2735037151571245 |
| ctx-lh-cuneus | NFL | amyloid | 1.5379608613888944 | -0.5139722553170758 | 3.5898939780948647 | 1.3756197109811701 | -0.75921582351438777 | 3.5104552454767282 |
| ctx-lh-cuneus | NFL | tau | 1.309099533325305 | -0.29637017129779769 | 2.9145692379484078 | 1.3965302742306192 | -0.23402993282724899 | 3.0270904812884876 |
| ctx-lh-entorhinal | GFAP | amyloid | 10.585905988138547 | 4.3712570698725681 | 16.800554906404528 | 10.273877408057182 | 4.1241671060748635 | 16.423587710039499 |
| ctx-lh-entorhinal | GFAP | tau | 4.6017118184447305 | -1.2419487246471812 | 10.44537236153664 | 6.4071402518546243 | 0.45856383442643178 | 12.355716669282817 |
| ctx-lh-entorhinal | NFL | amyloid | 1.4885884842017272 | -0.63999393717573749 | 3.6171709055791919 | 1.2746443745647011 | -0.86166534925512273 | 3.4109540983845248 |
| ctx-lh-entorhinal | NFL | tau | 0.45385675916939228 | -1.303066124703715 | 2.2107796430424997 | 0.55733471258561862 | -1.2077402973109432 | 2.3224097224821807 |
| ctx-lh-frontalpole | GFAP | amyloid | 15.792340844583244 | 10.225011145354578 | 21.359670543811912 | 15.431738943391323 | 9.9382097721591514 | 20.925268114623496 |
| ctx-lh-frontalpole | GFAP | tau | 1.432783746089302 | -3.151511854934995 | 6.017079347113599 | 2.6903258766317313 | -1.9640057928470211 | 7.3446575461104837 |
| ctx-lh-frontalpole | NFL | amyloid | 1.7525096342555355 | -0.1660365808996935 | 3.6710558494107648 | 1.5494651941052231 | -0.3541016829047936 | 3.4530320711152398 |
| ctx-lh-frontalpole | NFL | tau | 0.98669383845168002 | -0.94232167750565243 | 2.915709354409012 | 0.92906031138421241 | -0.98597526483331877 | 2.8440958876017435 |
| ctx-lh-fusiform | GFAP | amyloid | 11.5863403634376 | 5.2826574461247642 | 17.890023280750434 | 11.380723357523078 | 5.1851050615383087 | 17.576341653507846 |
| ctx-lh-fusiform | GFAP | tau | 4.8011301217328182 | -1.0532621439810541 | 10.655522387446691 | 6.2708348311862157 | 0.50380683018953043 | 12.037862832182901 |
| ctx-lh-fusiform | NFL | amyloid | 1.2928989458533702 | -1.020568025076549 | 3.6063659167832895 | 1.0881528271490644 | -1.2464502672537332 | 3.4227559215518619 |
| ctx-lh-fusiform | NFL | tau | 1.4092289461542489 | -0.5328312217867075 | 3.3512891140952048 | 1.6034395115790816 | -0.349080917962514 | 3.555959941120677 |
| ctx-lh-inferiorparietal | GFAP | amyloid | 11.295395092497897 | 4.965226069259761 | 17.625564115736029 | 11.393900202385501 | 5.0851092006685592 | 17.70269120410244 |
| ctx-lh-inferiorparietal | GFAP | tau | 6.3899973536469705 | 0.67160303709935132 | 12.108391670194589 | 7.3272819246144794 | 1.5970644955766715 | 13.057499353652286 |
| ctx-lh-inferiorparietal | NFL | amyloid | 1.1450735918596071 | -1.0141970686047896 | 3.3043442523240039 | 0.98461644608910182 | -1.1753484222743384 | 3.1445813144525419 |
| ctx-lh-inferiorparietal | NFL | tau | 1.510367334952992 | -0.20049409627448811 | 3.2212287661804719 | 1.5952462288327125 | -0.018081243555327 | 3.208573701220752 |
| ctx-lh-inferiortemporal | GFAP | amyloid | 12.106110760586381 | 5.2398340057847861 | 18.972387515387975 | 11.908845337862664 | 5.2036159084677944 | 18.614074767257534 |
| ctx-lh-inferiortemporal | GFAP | tau | 4.8907364576785248 | -1.7199910784317129 | 11.501463993788764 | 6.1055317384526759 | -0.53087212991127419 | 12.741935606816623 |
| ctx-lh-inferiortemporal | NFL | amyloid | 1.3079674330140492 | -1.1507997047534122 | 3.7667345707815105 | 1.1025899200992599 | -1.3437234713374815 | 3.5489033115360016 |
| ctx-lh-inferiortemporal | NFL | tau | 1.4104692506225032 | -0.63685158076544157 | 3.4577900820104479 | 1.5739846251513745 | -0.40598848989919678 | 3.5539577402019455 |
| ctx-lh-insula | GFAP | amyloid | 14.382552698476465 | 8.4729749719984149 | 20.292130424954511 | 14.113828042465858 | 8.288452844698277 | 19.939203240233439 |
| ctx-lh-insula | GFAP | tau | -0.57501714279261407 | -5.9183585987243923 | 4.7683243131391642 | 0.93443062854073222 | -4.3636405846623472 | 6.2325018417438116 |
| ctx-lh-insula | NFL | amyloid | 1.5571546405746559 | -0.77129096927729357 | 3.8856002504266058 | 1.4083977579476989 | -0.93185012362031316 | 3.7486456395157113 |
| ctx-lh-insula | NFL | tau | 0.94637975970935917 | -0.98689574597808361 | 2.8796552653968019 | 0.98661029148710078 | -0.98152154049462204 | 2.954742123468824 |
| ctx-lh-isthmuscingulate | GFAP | amyloid | 12.604750836800902 | 6.1412582760538257 | 19.068243397547977 | 12.574754022813153 | 6.1485275972248505 | 19.00098044840145 |
| ctx-lh-isthmuscingulate | GFAP | tau | 4.1113262434012929 | -1.5772678880454505 | 9.7999203748480355 | 5.1403179805588817 | -0.7523091972812681 | 11.032945158399031 |
| ctx-lh-isthmuscingulate | NFL | amyloid | 1.4060067091658224 | -0.95331934314226019 | 3.7653327614739052 | 1.2399250138423623 | -1.1301308867388569 | 3.6099809144235815 |
| ctx-lh-isthmuscingulate | NFL | tau | 1.4304689259984475 | -0.46689387941174981 | 3.327831731408645 | 1.4522864525540209 | -0.3397912249111501 | 3.244364130019191 |
| ctx-lh-lateraloccipital | GFAP | amyloid | 11.106170746814303 | 4.6634665379031723 | 17.548874955725438 | 11.096383628548232 | 4.7658218065485398 | 17.426945450547922 |
| ctx-lh-lateraloccipital | GFAP | tau | 4.3166792673821348 | -1.763341812711448 | 10.396700347475718 | 5.7190809425487226 | -0.33470598609577701 | 11.772867871193222 |
| ctx-lh-lateraloccipital | NFL | amyloid | 1.2541755980780325 | -0.6899800908757816 | 3.1983312870318468 | 1.0787350293780531 | -0.90773367888578005 | 3.0652037376418866 |
| ctx-lh-lateraloccipital | NFL | tau | 1.4806379733247874 | -0.49018170444965392 | 3.4514576510992288 | 1.6268635741487678 | -0.35974301688164489 | 3.613470165179181 |
| ctx-lh-lateralorbitofrontal | GFAP | amyloid | 15.597054443708458 | 9.9469856021903968 | 21.247123285226522 | 15.284986545214576 | 9.7328389142769236 | 20.83713417615223 |
| ctx-lh-lateralorbitofrontal | GFAP | tau | -0.091508055678447706 | -5.6557633293390985 | 5.472747217982203 | 1.371756133380917 | -4.4276315558569497 | 7.1711438226187845 |
| ctx-lh-lateralorbitofrontal | NFL | amyloid | 1.9370123360165821 | -0.37670889204984997 | 4.2507335640830144 | 1.7696951566181991 | -0.5514794810473731 | 4.0908697942837717 |
| ctx-lh-lateralorbitofrontal | NFL | tau | 0.80127105222716144 | -1.1872216470459267 | 2.7897637515002498 | 0.85116112370261598 | -1.1309291168215023 | 2.8332513642267347 |
| ctx-lh-lingual | GFAP | amyloid | 11.40898705582998 | 4.7368730825566265 | 18.08110102910333 | 11.387186671393463 | 4.7515643266376903 | 18.022809016149239 |
| ctx-lh-lingual | GFAP | tau | 2.1439689753026299 | -3.8213011397659602 | 8.1092390903712186 | 3.4907468038533298 | -2.3641956172908989 | 9.3456892249975567 |
| ctx-lh-lingual | NFL | amyloid | 1.4166272448169437 | -0.86930501113896375 | 3.7025595007728511 | 1.2590161783225655 | -1.0907891033862496 | 3.6088214600313808 |
| ctx-lh-lingual | NFL | tau | 1.4110274046027378 | -0.34561745033852559 | 3.167672259544001 | 1.487785918112372 | -0.34111799328225079 | 3.3166898295069949 |
| ctx-lh-medialorbitofrontal | GFAP | amyloid | 16.147895368343384 | 10.46868217897145 | 21.82710855771532 | 15.950446168593166 | 10.277498117411325 | 21.623394219775008 |
| ctx-lh-medialorbitofrontal | GFAP | tau | -0.57565480392788637 | -5.8356529418019463 | 4.684343333946174 | 0.81567158829247144 | -4.4853858183336328 | 6.1167289949185761 |
| ctx-lh-medialorbitofrontal | NFL | amyloid | 1.9858968667207064 | -0.16727626489416769 | 4.1390699983355805 | 1.8119848451864771 | -0.34271124917961421 | 3.966680939552568 |
| ctx-lh-medialorbitofrontal | NFL | tau | 0.67511210332465033 | -1.1803347796314716 | 2.5305589862807718 | 0.71920282639254651 | -1.1380551431267478 | 2.5764607959118409 |
| ctx-lh-middletemporal | GFAP | amyloid | 11.453953734563919 | 4.842792727440659 | 18.065114741687182 | 11.39025575820494 | 4.8592881724175676 | 17.921223343992313 |
| ctx-lh-middletemporal | GFAP | tau | 5.5560578801798686 | -1.2265186706125537 | 12.338634430972292 | 6.686924702141134 | -0.2479889760001352 | 13.621838380282403 |
| ctx-lh-middletemporal | NFL | amyloid | 1.2929366741713624 | -1.0457222034250837 | 3.6315955517678078 | 1.1375764429294295 | -1.2033732748915646 | 3.4785261607504241 |
| ctx-lh-middletemporal | NFL | tau | 1.322750157288465 | -0.66830845759059376 | 3.3138087721675236 | 1.4084082571416925 | -0.46866690758285928 | 3.2854834218662443 |
| ctx-lh-paracentral | GFAP | amyloid | 14.80937322130749 | 8.3489901678367939 | 21.269756274778189 | 14.849018811488399 | 8.4130203302980213 | 21.285017292678777 |
| ctx-lh-paracentral | GFAP | tau | 0.97196323977235721 | -4.7133495937472532 | 6.6572760732919676 | 2.1985736698697664 | -3.590385182012259 | 7.9875325217517918 |
| ctx-lh-paracentral | NFL | amyloid | 1.5448655940298637 | -0.54679903127365859 | 3.6365302193333857 | 1.4474778936596642 | -0.65456062263240877 | 3.5495164099517371 |
| ctx-lh-paracentral | NFL | tau | 1.6505230027572448 | -0.098691438038806603 | 3.3997374435532963 | 1.664628050641243 | -0.16378742439261451 | 3.4930435256751005 |
| ctx-lh-parahippocampal | GFAP | amyloid | 10.663238835118634 | 4.5993366002841309 | 16.727141069953134 | 10.298697697890534 | 4.401303683291184 | 16.196091712489881 |
| ctx-lh-parahippocampal | GFAP | tau | 5.5769964230914271 | -0.17189456588942059 | 11.325887412072277 | 7.2577350822322106 | 1.4201984656587081 | 13.095271698805714 |
| ctx-lh-parahippocampal | NFL | amyloid | 1.2120630939348025 | -1.0637435184364812 | 3.4878697063060864 | 0.99923348325376482 | -1.2765655275774028 | 3.2750324940849325 |
| ctx-lh-parahippocampal | NFL | tau | 1.3243436817685239 | -0.52241781661842612 | 3.1711051801554739 | 1.4296508872816456 | -0.47253184221381428 | 3.3318336167771054 |
| ctx-lh-parsopercularis | GFAP | amyloid | 14.526607008646142 | 8.7045952935831323 | 20.348618723709151 | 14.388084979178396 | 8.6389976961433881 | 20.137172262213404 |
| ctx-lh-parsopercularis | GFAP | tau | 2.6582093041624564 | -2.7559809943477882 | 8.0723996026727001 | 4.1843351939679003 | -1.5112918622150904 | 9.8799622501508928 |
| ctx-lh-parsopercularis | NFL | amyloid | 1.480682608866833 | -0.7509381370389614 | 3.7123033547726272 | 1.3491661968867457 | -0.88985817521304766 | 3.5881905689865388 |
| ctx-lh-parsopercularis | NFL | tau | 1.5967825624584491 | -0.4403279242747084 | 3.6338930491916068 | 1.6525810207131315 | -0.3650114946104166 | 3.6701735360366801 |
| ctx-lh-parsorbitalis | GFAP | amyloid | 13.944724676058511 | 8.6073694823108209 | 19.282079869806203 | 13.733751517114188 | 8.496526520983922 | 18.970976513244452 |
| ctx-lh-parsorbitalis | GFAP | tau | 2.4882844520292617 | -3.061840373887986 | 8.0384092779465099 | 4.3411616516767531 | -1.8307376382070499 | 10.513060941560555 |
| ctx-lh-parsorbitalis | NFL | amyloid | 1.9119853537873504 | -0.23834309996499839 | 4.0623138075396996 | 1.7698279008090183 | -0.38928494290048338 | 3.92894074451852 |
| ctx-lh-parsorbitalis | NFL | tau | 0.97060700814714518 | -1.0603168463634989 | 3.0015308626577895 | 1.0258950246797358 | -0.92615564092598601 | 2.9779456902854577 |
| ctx-lh-parstriangularis | GFAP | amyloid | 14.595062442386196 | 9.3713773734264443 | 19.818747511345951 | 14.49864185079166 | 9.3651174266100607 | 19.632166274973255 |
| ctx-lh-parstriangularis | GFAP | tau | 2.3650979916992201 | -3.2398056410224818 | 7.970001624420922 | 4.2830263799410657 | -1.9632889332476049 | 10.529341693129735 |
| ctx-lh-parstriangularis | NFL | amyloid | 1.707802539051493 | -0.47717452434097818 | 3.892779602443964 | 1.591428695523712 | -0.60303673806002811 | 3.7858941291074522 |
| ctx-lh-parstriangularis | NFL | tau | 1.1687558534561622 | -0.84604157141794012 | 3.1835532783302645 | 1.2373021466978491 | -0.77515624916147607 | 3.2497605425571745 |
| ctx-lh-pericalcarine | GFAP | amyloid | 12.806437559968291 | 6.2510089716135804 | 19.361866148323003 | 12.891783179669062 | 6.263519132244749 | 19.520047227093375 |
| ctx-lh-pericalcarine | GFAP | tau | -0.60038590591977226 | -6.700881737826772 | 5.5001099259872275 | 0.71514819389288409 | -5.2504202213318498 | 6.680716609117618 |
| ctx-lh-pericalcarine | NFL | amyloid | 1.6733705902641769 | -0.62418339352925867 | 3.9709245740576118 | 1.5485280868232276 | -0.82459070213146624 | 3.9216468757779217 |
| ctx-lh-pericalcarine | NFL | tau | 0.90834536362707963 | -0.66022853552766181 | 2.4769192627818213 | 0.92906699586666519 | -0.69744737981368288 | 2.5555813715470137 |
| ctx-lh-postcentral | GFAP | amyloid | 13.446907453659186 | 7.5590855776336916 | 19.334729329684681 | 13.465363626064864 | 7.5962263031798107 | 19.334500948949916 |
| ctx-lh-postcentral | GFAP | tau | 1.6060333180477473 | -3.7832454735380461 | 6.9953121096335407 | 3.027041341830488 | -2.665851132876619 | 8.7199338165375941 |
| ctx-lh-postcentral | NFL | amyloid | 1.4524379249754504 | -0.78972702630522273 | 3.6946028762561234 | 1.339555997625214 | -0.92130090260421238 | 3.6004128978546408 |
| ctx-lh-postcentral | NFL | tau | 1.4729396521219671 | -0.40651309126116492 | 3.3523923955050998 | 1.4968528639118923 | -0.39447884765944807 | 3.3881845754832325 |
| ctx-lh-posteriorcingulate | GFAP | amyloid | 14.3318356252769 | 7.9570234388702783 | 20.706647811683524 | 14.379105755574267 | 8.0906814365203186 | 20.667530074628218 |
| ctx-lh-posteriorcingulate | GFAP | tau | 4.3868639020584865 | -1.5452530018509725 | 10.318980805967946 | 5.8063334832068438 | -0.15128732825990979 | 11.763954294673598 |
| ctx-lh-posteriorcingulate | NFL | amyloid | 1.2958769476733398 | -0.8732496397634637 | 3.4650035351101431 | 1.1833749389796111 | -0.99711237161214161 | 3.3638622495713646 |
| ctx-lh-posteriorcingulate | NFL | tau | 2.0088324779622959 | 0.232041597059716 | 3.7856233588648762 | 2.1176086975563178 | 0.3528032825023843 | 3.8824141126102512 |
| ctx-lh-precentral | GFAP | amyloid | 13.627839631846827 | 7.4336006913029484 | 19.822078572390705 | 13.593859339159598 | 7.428375568204121 | 19.759343110115076 |
| ctx-lh-precentral | GFAP | tau | 1.2504504329876929 | -4.2489797037023402 | 6.7498805696777255 | 2.6763863243520207 | -2.9521895383364605 | 8.3049621870405019 |
| ctx-lh-precentral | NFL | amyloid | 1.4445150809965921 | -0.84428242163433542 | 3.7333125836275194 | 1.3209545571213634 | -0.98521524178532904 | 3.6271243560280562 |
| ctx-lh-precentral | NFL | tau | 1.2520729623972828 | -0.60701762884545118 | 3.1111635536400168 | 1.2891281428817891 | -0.58520494635919484 | 3.1634612321227733 |
| ctx-lh-precuneus | GFAP | amyloid | 13.753905108123655 | 7.3892421823659413 | 20.11856803388137 | 13.839382060464096 | 7.4791349998507242 | 20.199629121077468 |
| ctx-lh-precuneus | GFAP | tau | 4.4163043994035185 | -1.4440759932830949 | 10.276684792090132 | 5.1429485146768936 | -1.0121923267495596 | 11.298089356103349 |
| ctx-lh-precuneus | NFL | amyloid | 1.6215154632383562 | -0.47218580832668211 | 3.7152167348033944 | 1.4957026320634541 | -0.59994202770772653 | 3.5913472918346345 |
| ctx-lh-precuneus | NFL | tau | 1.3643935424120754 | -0.35715085037428701 | 3.0859379351984382 | 1.369279772209429 | -0.207268203171111 | 2.945827747589969 |
| ctx-lh-rostralanteriorcingulate | GFAP | amyloid | 16.41631235329146 | 10.556300462312525 | 22.276324244270395 | 16.294675571900271 | 10.46714074986998 | 22.122210393930558 |
| ctx-lh-rostralanteriorcingulate | GFAP | tau | -1.4384034550193068 | -6.6800260957616491 | 3.8032191857230351 | 0.3070879635409724 | -4.7755772421130169 | 5.3897531691949618 |
| ctx-lh-rostralanteriorcingulate | NFL | amyloid | 1.9800018027785375 | -0.081708883201246404 | 4.0417124887583222 | 1.8326112291455909 | -0.2360823776119462 | 3.9013048359031282 |
| ctx-lh-rostralanteriorcingulate | NFL | tau | 0.71266061304700801 | -1.1015847766820626 | 2.5269060027760784 | 0.82092745245524146 | -1.0271832345148508 | 2.669038139425334 |
| ctx-lh-rostralmiddlefrontal | GFAP | amyloid | 14.50084533293359 | 9.1621856594540567 | 19.839505006413127 | 14.51245420313114 | 9.1813811178962901 | 19.843527288365987 |
| ctx-lh-rostralmiddlefrontal | GFAP | tau | 4.6768532051543819 | -0.61696720319213227 | 9.970673613500896 | 6.3275095175942866 | 0.44863030570373658 | 12.206388729484836 |
| ctx-lh-rostralmiddlefrontal | NFL | amyloid | 1.7269463176143098 | -0.36759994321789469 | 3.8214925784465144 | 1.6039617320041279 | -0.49582479204676039 | 3.7037482560550159 |
| ctx-lh-rostralmiddlefrontal | NFL | tau | 1.3660319800098606 | -0.59946890254442775 | 3.3315328625641492 | 1.4522789407786141 | -0.41030127237595709 | 3.3148591539331855 |
| ctx-lh-superiorfrontal | GFAP | amyloid | 15.396625446911838 | 9.3762867975766309 | 21.416964096247039 | 15.267930482505225 | 9.3039300020957203 | 21.231930962914731 |
| ctx-lh-superiorfrontal | GFAP | tau | 3.0964794247079261 | -1.8382358698175061 | 8.0311947192333584 | 4.4960280752901305 | -0.62600360552145862 | 9.6180597561017205 |
| ctx-lh-superiorfrontal | NFL | amyloid | 1.7825197731956743 | -0.40122791140211023 | 3.9662674577934589 | 1.6408128044514758 | -0.5497823472352914 | 3.8314079561382428 |
| ctx-lh-superiorfrontal | NFL | tau | 1.4213080586416882 | -0.43894800587215621 | 3.2815641231555324 | 1.4819230729389574 | -0.40974271569354531 | 3.3735888615714602 |
| ctx-lh-superiorparietal | GFAP | amyloid | 12.676504112436316 | 6.5895432814768258 | 18.763464943395807 | 12.890869312088132 | 6.8581724430500755 | 18.923566181126191 |
| ctx-lh-superiorparietal | GFAP | tau | 5.7044687003331926 | 0.33987403132926541 | 11.069063369337121 | 6.7942446131802958 | 1.3299149847365117 | 12.25857424162408 |
| ctx-lh-superiorparietal | NFL | amyloid | 1.2600277262286843 | -0.77872530776850857 | 3.2987807602258772 | 1.1441132298626968 | -0.91365970963363041 | 3.2018861693590241 |
| ctx-lh-superiorparietal | NFL | tau | 1.6484989018700968 | -0.013348717733902799 | 3.3103465214740968 | 1.709041905708341 | 0.091640378460764199 | 3.3264434329559176 |
| ctx-lh-superiortemporal | GFAP | amyloid | 13.328442480873925 | 6.9913716911731658 | 19.665513270574682 | 13.231101342718116 | 6.9730009619370268 | 19.489201723499207 |
| ctx-lh-superiortemporal | GFAP | tau | 2.850795803393086 | -2.959369117098773 | 8.6609607238849442 | 4.2047158239894937 | -1.9280668753398231 | 10.337498523318811 |
| ctx-lh-superiortemporal | NFL | amyloid | 1.401699519951378 | -0.9803375367347692 | 3.7837365766375255 | 1.2555206861847801 | -1.1241904064006081 | 3.6352317787701689 |
| ctx-lh-superiortemporal | NFL | tau | 1.0886027620066672 | -1.0238056910100026 | 3.2010112150233372 | 1.1017508953459665 | -0.96102504064999805 | 3.1645268313419308 |
| ctx-lh-supramarginal | GFAP | amyloid | 12.740890149533779 | 6.6369509883177882 | 18.844829310749773 | 12.765238906056783 | 6.7280105906450505 | 18.802467221468518 |
| ctx-lh-supramarginal | GFAP | tau | 5.0061836262575063 | -1.2535215769643449 | 11.265888829479358 | 6.1255093278765873 | -0.33392605356519489 | 12.58494470931837 |
| ctx-lh-supramarginal | NFL | amyloid | 1.2491860993024304 | -1.0128233431903191 | 3.5111955417951801 | 1.1092275343966858 | -1.1614961369962029 | 3.3799512057895744 |
| ctx-lh-supramarginal | NFL | tau | 1.4389210174214186 | -0.4052372319094541 | 3.2830792667522912 | 1.4880827481378429 | -0.231920973855259 | 3.2080864701309446 |
| ctx-lh-temporalpole | GFAP | amyloid | 15.158559843780113 | 8.6846181410216516 | 21.63250154653857 | 14.514270689903832 | 8.3091521793228811 | 20.719389200484784 |
| ctx-lh-temporalpole | GFAP | tau | 1.3051015310850911 | -4.4174409483438017 | 7.0276440105139839 | 3.518541170015276 | -2.5029262116324689 | 9.5400085516630195 |
| ctx-lh-temporalpole | NFL | amyloid | 1.4805879696127231 | -0.87241769853284756 | 3.8335936377582942 | 1.283025813038837 | -1.0491092195541969 | 3.6151608456318702 |
| ctx-lh-temporalpole | NFL | tau | 0.7770834817111516 | -1.2745014278967548 | 2.828668391319058 | 0.92517857312914564 | -1.1577049763752731 | 3.0080621226335644 |
| ctx-lh-transversetemporal | GFAP | amyloid | 13.494364986118542 | 6.9205079064954553 | 20.068222065741629 | 13.618566277112411 | 6.994099833901406 | 20.243032720323416 |
| ctx-lh-transversetemporal | GFAP | tau | 0.3654436364037057 | -5.26856639887301 | 5.9994536716804214 | 1.7109391221221366 | -4.2010778107994184 | 7.6229560550436926 |
| ctx-lh-transversetemporal | NFL | amyloid | 1.4047345895089127 | -0.83802011620819261 | 3.6474892952260181 | 1.305320417018468 | -0.96856746271776639 | 3.5792082967547021 |
| ctx-lh-transversetemporal | NFL | tau | 0.84013648438180777 | -1.2603585091896514 | 2.940631477953267 | 0.81383437929895752 | -1.354949855657166 | 2.982618614255081 |
| ctx-rh-bankssts | GFAP | amyloid | 12.912168847353691 | 6.5918017260526858 | 19.232535968654695 | 12.998955221038235 | 6.6784057732579765 | 19.319504668818496 |
| ctx-rh-bankssts | GFAP | tau | 2.7884897113848215 | -2.2296031700749017 | 7.8065825928445447 | 3.5814702983392643 | -1.5781873632748025 | 8.7411279599533316 |
| ctx-rh-bankssts | NFL | amyloid | 1.1304674590865229 | -0.89103820080424589 | 3.151973118977291 | 0.99341839278027999 | -1.0067345782626216 | 2.9935713638231816 |
| ctx-rh-bankssts | NFL | tau | 0.91534327523974157 | -1.2152174650011871 | 3.0459040154806707 | 0.93903255707378019 | -1.1374795059382341 | 3.015544620085794 |
| ctx-rh-caudalanteriorcingulate | GFAP | amyloid | 15.327775798191537 | 9.7353558869792316 | 20.920195709403838 | 15.272230619500087 | 9.7218372383827418 | 20.822624000617441 |
| ctx-rh-caudalanteriorcingulate | GFAP | tau | -0.50107352171171349 | -5.2873728135178624 | 4.2852257700944349 | 1.1913973985019952 | -3.4349527091920535 | 5.817747506196044 |
| ctx-rh-caudalanteriorcingulate | NFL | amyloid | 1.5667773482504932 | -0.58198807363380189 | 3.7155427701347881 | 1.4523687776374623 | -0.71034236649065474 | 3.61507992176558 |
| ctx-rh-caudalanteriorcingulate | NFL | tau | 0.66377911400525647 | -1.252487701350766 | 2.5800459293612787 | 0.76037417194535273 | -1.1939933156122866 | 2.7147416595029918 |
| ctx-rh-caudalmiddlefrontal | GFAP | amyloid | 14.439580232910568 | 8.4914749844819042 | 20.387685481339233 | 14.367421801483111 | 8.4886876789927186 | 20.246155923973504 |
| ctx-rh-caudalmiddlefrontal | GFAP | tau | 5.3003029993975561 | 0.29512491871645791 | 10.305481080078652 | 6.6729837852198974 | 1.5152536676220765 | 11.83071390281772 |
| ctx-rh-caudalmiddlefrontal | NFL | amyloid | 1.3780373554876697 | -0.80324045878970218 | 3.5593151697650418 | 1.2301577265440933 | -0.95620394680156395 | 3.4165193998897507 |
| ctx-rh-caudalmiddlefrontal | NFL | tau | 1.1483689310721248 | -0.62677601647166914 | 2.9235138786159185 | 1.2766929073496265 | -0.4239147209823399 | 2.9773005356815925 |
| ctx-rh-cuneus | GFAP | amyloid | 11.864084364492506 | 5.1507073802423786 | 18.577461348742631 | 12.073262810275848 | 5.3175786812105885 | 18.828946939341108 |
| ctx-rh-cuneus | GFAP | tau | 2.354337989394522 | -3.0250421039638602 | 7.7337180827529037 | 3.6765442023004953 | -1.600824450638501 | 8.9539128552394907 |
| ctx-rh-cuneus | NFL | amyloid | 1.4572035852004654 | -0.56324807690890366 | 3.4776552473098343 | 1.321110118025187 | -0.78944485816448084 | 3.4316650942148548 |
| ctx-rh-cuneus | NFL | tau | 1.2266956103949911 | -0.80503497465193674 | 3.2584261954419187 | 1.3272212762822475 | -0.79882627152265373 | 3.4532688240871487 |
| ctx-rh-entorhinal | GFAP | amyloid | 11.383136475542573 | 5.601736936103177 | 17.164536014981969 | 11.228038818624279 | 5.5100382294360175 | 16.946039407812545 |
| ctx-rh-entorhinal | GFAP | tau | 3.8621219616340303 | -2.0966742260477407 | 9.8209181493157995 | 5.7042645400287624 | -0.4837607846011211 | 11.892289864658649 |
| ctx-rh-entorhinal | NFL | amyloid | 1.132315653130469 | -1.010806348192109 | 3.275437654453047 | 0.94852678897171805 | -1.2128336162220656 | 3.1098871941655015 |
| ctx-rh-entorhinal | NFL | tau | 0.41538868212282559 | -1.5376477527493353 | 2.3684251169949864 | 0.54888771666177538 | -1.3814765864932654 | 2.4792520198168164 |
| ctx-rh-frontalpole | GFAP | amyloid | 15.36486778496039 | 9.7232677158215353 | 21.006467854099245 | 15.21821288478897 | 9.6087351369409326 | 20.827690632637008 |
| ctx-rh-frontalpole | GFAP | tau | 1.5717824225540815 | -3.6120420413672969 | 6.7556068864754604 | 2.6751869125117969 | -2.6247974755927519 | 7.9751713006163456 |
| ctx-rh-frontalpole | NFL | amyloid | 1.6003908712786414 | -0.50439537238911591 | 3.705177114946399 | 1.4799615916204534 | -0.63971499295710199 | 3.5996381761980087 |
| ctx-rh-frontalpole | NFL | tau | 1.0928218624840784 | -0.6859854154527969 | 2.8716291404209535 | 1.03504804410681 | -0.81591046828431169 | 2.8860065564979314 |
| ctx-rh-fusiform | GFAP | amyloid | 11.171512181600209 | 5.2165494238944614 | 17.12647493930595 | 11.03143758957067 | 5.1614667733796784 | 16.901408405761661 |
| ctx-rh-fusiform | GFAP | tau | 5.6595241209179736 | 0.29206265625043049 | 11.026985585585518 | 7.1427285068787629 | 1.6653672856033743 | 12.620089728154152 |
| ctx-rh-fusiform | NFL | amyloid | 1.1611497396752437 | -0.97516052067217962 | 3.2974600000226664 | 0.96966399826425498 | -1.1963812275985384 | 3.1357092241270483 |
| ctx-rh-fusiform | NFL | tau | 1.2845131321616201 | -0.96043664085502023 | 3.52946290517826 | 1.4600568512686505 | -0.80963976355928136 | 3.7297534660965823 |
| ctx-rh-inferiorparietal | GFAP | amyloid | 11.867532560090156 | 5.5555602547032263 | 18.179504865477085 | 11.886812369699172 | 5.6366909126954612 | 18.136933826702883 |
| ctx-rh-inferiorparietal | GFAP | tau | 5.765985341578773 | 0.27298614625706458 | 11.25898453690048 | 6.8429024346147003 | 1.2658155266411653 | 12.419989342588234 |
| ctx-rh-inferiorparietal | NFL | amyloid | 1.0610220849501084 | -1.0038770815954905 | 3.1259212514957069 | 0.88095678682401202 | -1.2008787290141294 | 2.9627923026621534 |
| ctx-rh-inferiorparietal | NFL | tau | 1.3581312788185178 | -0.50395914229543326 | 3.2202216999324689 | 1.51048575750935 | -0.2716504952627003 | 3.2926220102814003 |
| ctx-rh-inferiortemporal | GFAP | amyloid | 13.395329655990722 | 7.0594382031242757 | 19.731221108857167 | 13.235780694764454 | 6.9695668965635367 | 19.501994492965373 |
| ctx-rh-inferiortemporal | GFAP | tau | 2.8781834585322001 | -2.7918311115813457 | 8.5481980286457464 | 4.2246384016949641 | -1.5841295012820249 | 10.033406304671953 |
| ctx-rh-inferiortemporal | NFL | amyloid | 1.5808142819650814 | -0.64168554780432907 | 3.8033141117344922 | 1.3601306236919537 | -0.8656794665552745 | 3.5859407139391815 |
| ctx-rh-inferiortemporal | NFL | tau | 0.70743714640228217 | -1.5573456483660333 | 2.9722199411705974 | 0.91975064061066703 | -1.3070067757309796 | 3.1465080569523138 |
| ctx-rh-insula | GFAP | amyloid | 15.734002951748014 | 9.6976779287963009 | 21.770327974699725 | 15.433573771960084 | 9.497515886264086 | 21.369631657656083 |
| ctx-rh-insula | GFAP | tau | -1.1892050519447781 | -6.4774688683977981 | 4.0990587645082428 | 0.3289988843844493 | -4.8794462840204993 | 5.5374440527893984 |
| ctx-rh-insula | NFL | amyloid | 1.5507490901065371 | -0.69787845746909305 | 3.7993766376821672 | 1.4049143616483126 | -0.86413751270647166 | 3.6739662360030971 |
| ctx-rh-insula | NFL | tau | 0.8858584493744307 | -0.97263352937922076 | 2.7443504281280822 | 0.95573069936173005 | -0.96015286964253277 | 2.8716142683659927 |
| ctx-rh-isthmuscingulate | GFAP | amyloid | 11.758339796888084 | 5.4829391846076172 | 18.033740409168551 | 11.750863419699046 | 5.4857830265472893 | 18.015943812850804 |
| ctx-rh-isthmuscingulate | GFAP | tau | 5.4511203421059955 | -0.14957942276172079 | 11.051820106973713 | 6.7039943327836422 | 0.77580566218394598 | 12.632183003383339 |
| ctx-rh-isthmuscingulate | NFL | amyloid | 1.3334936303021698 | -0.8098927680269723 | 3.476880028631312 | 1.1562487750727397 | -1.0150849280686345 | 3.3275824782141132 |
| ctx-rh-isthmuscingulate | NFL | tau | 1.4808586658496881 | -0.33790983310691369 | 3.2996271648062896 | 1.5671454238951597 | -0.1758412119983179 | 3.3101320597886374 |
| ctx-rh-lateraloccipital | GFAP | amyloid | 11.410296363964358 | 5.2783950006121669 | 17.542197727316548 | 11.480542231635695 | 5.4262286748091251 | 17.534855788462266 |
| ctx-rh-lateraloccipital | GFAP | tau | 5.2840068714767252 | -0.041047766561960401 | 10.60906150951541 | 6.6069023270329446 | 1.3035343826766397 | 11.910270271389249 |
| ctx-rh-lateraloccipital | NFL | amyloid | 1.201504274057299 | -0.68407460983596957 | 3.0870831579505675 | 1.0161805384454572 | -0.90577100120380682 | 2.9381320780947213 |
| ctx-rh-lateraloccipital | NFL | tau | 1.2920399090837136 | -0.82754005228185612 | 3.4116198704492833 | 1.4194849205624942 | -0.72852259710637113 | 3.5674924382313593 |
| ctx-rh-lateralorbitofrontal | GFAP | amyloid | 16.412623052850236 | 10.605813002033884 | 22.219433103666589 | 16.010858885249348 | 10.318935309741878 | 21.702782460756818 |
| ctx-rh-lateralorbitofrontal | GFAP | tau | -2.0226542791585218 | -7.5228747353653418 | 3.4775661770482991 | -0.54045930673445308 | -6.1783359539954974 | 5.097417340526591 |
| ctx-rh-lateralorbitofrontal | NFL | amyloid | 1.820078230249792 | -0.28775956625319621 | 3.9279160267527802 | 1.6374731280561281 | -0.47933517117513502 | 3.754281427287391 |
| ctx-rh-lateralorbitofrontal | NFL | tau | 0.40979804509014728 | -1.3740349646738974 | 2.1936310548541922 | 0.47121261819309979 | -1.3196188173007566 | 2.2620440536869562 |
| ctx-rh-lingual | GFAP | amyloid | 11.254070413697169 | 4.719957222250347 | 17.788183605143992 | 11.370584349419024 | 4.8443809045553872 | 17.896787794282659 |
| ctx-rh-lingual | GFAP | tau | 3.5583607994490118 | -1.9034119066873216 | 9.0201335055853455 | 4.9548202613023653 | -0.43192813423293241 | 10.341568656837662 |
| ctx-rh-lingual | NFL | amyloid | 1.2906426491300431 | -0.78871387457158026 | 3.3699991728316672 | 1.1449390478510022 | -1.0027871461579865 | 3.2926652418599907 |
| ctx-rh-lingual | NFL | tau | 1.2275102137466358 | -0.69160670647396749 | 3.1466271339672391 | 1.2820969993874065 | -0.74493483556253537 | 3.3091288343373479 |
| ctx-rh-medialorbitofrontal | GFAP | amyloid | 15.552776767854017 | 10.01684288691964 | 21.088710648788393 | 15.37342812043825 | 9.8335733860581769 | 20.913282854818323 |
| ctx-rh-medialorbitofrontal | GFAP | tau | -1.5048943423648369 | -6.7821373460991889 | 3.7723486613695161 | 0.063894254465820005 | -5.223325781680499 | 5.3511142906121396 |
| ctx-rh-medialorbitofrontal | NFL | amyloid | 1.6136208745158711 | -0.4870365623187678 | 3.7142783113505105 | 1.4625549137684444 | -0.65123872931935756 | 3.5763485568562463 |
| ctx-rh-medialorbitofrontal | NFL | tau | 0.79403901616958372 | -1.0129654183501675 | 2.601043450689335 | 0.87265124485838186 | -0.99422244535154358 | 2.7395249350683075 |
| ctx-rh-middletemporal | GFAP | amyloid | 13.87901957016102 | 7.4577123379183909 | 20.300326802403649 | 13.659874900341039 | 7.3416143465239623 | 19.978135454158121 |
| ctx-rh-middletemporal | GFAP | tau | 2.4129530843518361 | -3.3508778842404161 | 8.1767840529440878 | 3.8360805321660743 | -2.1036007218181512 | 9.7757617861502997 |
| ctx-rh-middletemporal | NFL | amyloid | 1.4648075500914679 | -0.70384760392999168 | 3.6334627041129282 | 1.2576313625525604 | -0.91095904544039685 | 3.4262217705455176 |
| ctx-rh-middletemporal | NFL | tau | 0.79803508580592564 | -1.4557449212535705 | 3.0518150928654215 | 0.97490472079643198 | -1.2034033014368055 | 3.1532127430296697 |
| ctx-rh-paracentral | GFAP | amyloid | 14.08747745774318 | 7.825975625455766 | 20.348979290030595 | 14.050868263239296 | 7.8228992580948322 | 20.278837268383761 |
| ctx-rh-paracentral | GFAP | tau | 0.64408528606531767 | -4.4445656631946475 | 5.7327362353252829 | 2.0978613254180987 | -3.1447761291021026 | 7.3404987799382999 |
| ctx-rh-paracentral | NFL | amyloid | 1.373720812443455 | -0.66773010937775923 | 3.4151717342646695 | 1.281189965665551 | -0.77812063766894868 | 3.3405005690000507 |
| ctx-rh-paracentral | NFL | tau | 1.5855617534377444 | -0.091728612061013001 | 3.2628521189365021 | 1.6385193990574234 | -0.1461418086065546 | 3.4231806067214015 |
| ctx-rh-parahippocampal | GFAP | amyloid | 10.953118635117306 | 4.6996884989135381 | 17.206548771321074 | 10.629181173886444 | 4.552601490521071 | 16.705760857251818 |
| ctx-rh-parahippocampal | GFAP | tau | 4.5258620050392953 | -1.1862383620168453 | 10.237962372095437 | 6.4408387545820744 | 0.67715524811959682 | 12.204522261044552 |
| ctx-rh-parahippocampal | NFL | amyloid | 1.0645041501058754 | -0.9206684661117952 | 3.0496767663235458 | 0.85639460493258313 | -1.1392889703841225 | 2.8520781802492889 |
| ctx-rh-parahippocampal | NFL | tau | 1.0704410002390352 | -1.1730176945336002 | 3.3138996950116706 | 1.2242463883806445 | -1.1045620887056613 | 3.55305486546695 |
| ctx-rh-parsopercularis | GFAP | amyloid | 14.952750880700457 | 8.9158837646326798 | 20.989617996768231 | 14.660691837710582 | 8.7793632748587971 | 20.542020400562365 |
| ctx-rh-parsopercularis | GFAP | tau | 3.1439467737406361 | -1.6497047268024354 | 7.9375982742837081 | 4.6416317235126785 | -0.31128675685093471 | 9.5945502038762918 |
| ctx-rh-parsopercularis | NFL | amyloid | 1.4787981869272722 | -0.74999027357131798 | 3.7075866474258623 | 1.3263466870375054 | -0.90865289150975437 | 3.5613462655847652 |
| ctx-rh-parsopercularis | NFL | tau | 1.1166842418938401 | -0.97677219378338365 | 3.2101406775710633 | 1.2345298659215111 | -0.85260857665394774 | 3.32166830849697 |
| ctx-rh-parsorbitalis | GFAP | amyloid | 15.338655501581922 | 9.3769280152662624 | 21.300382987897581 | 15.071834441142199 | 9.2660529110329204 | 20.877615971251483 |
| ctx-rh-parsorbitalis | GFAP | tau | 1.0036862685888459 | -4.1534571303112493 | 6.160829667488942 | 2.7756469827582153 | -2.7366269088575308 | 8.2879208743739614 |
| ctx-rh-parsorbitalis | NFL | amyloid | 1.7439034923689944 | -0.47824302306976518 | 3.9660500078077541 | 1.6011741674208662 | -0.62761524734830831 | 3.82996358219004 |
| ctx-rh-parsorbitalis | NFL | tau | 0.67616886553397593 | -1.3540166854846472 | 2.7063544165525988 | 0.73362643215758627 | -1.2817137809118062 | 2.7489666452269788 |
| ctx-rh-parstriangularis | GFAP | amyloid | 15.810257276705579 | 9.9136899785017594 | 21.706824574909401 | 15.586704596749604 | 9.8200957656217582 | 21.353313427877453 |
| ctx-rh-parstriangularis | GFAP | tau | 1.3038116937137043 | -3.7657685950805257 | 6.3733919825079344 | 3.1435553149204769 | -2.0772162655521158 | 8.3643268953930701 |
| ctx-rh-parstriangularis | NFL | amyloid | 1.7208094679620822 | -0.34161734452611392 | 3.7832362804502786 | 1.5783139734870892 | -0.488107487019799 | 3.6447354339939775 |
| ctx-rh-parstriangularis | NFL | tau | 0.52331445538895682 | -1.5279224159940794 | 2.5745513267719931 | 0.5569365415361287 | -1.4957653679901055 | 2.6096384510623629 |
| ctx-rh-pericalcarine | GFAP | amyloid | 12.994866184268524 | 5.9868075286030544 | 20.002924839933993 | 13.024031907819126 | 6.0274702309422503 | 20.020593584696002 |
| ctx-rh-pericalcarine | GFAP | tau | 0.27076486536755778 | -5.6917863904746193 | 6.233316121209735 | 2.0295028910085957 | -3.6747796999641902 | 7.733785481981382 |
| ctx-rh-pericalcarine | NFL | amyloid | 1.4416984321796118 | -0.720669964333577 | 3.6040668286928006 | 1.298730340661034 | -0.97052639522620321 | 3.5679870765482713 |
| ctx-rh-pericalcarine | NFL | tau | 1.1157156745850911 | -0.72912975556100346 | 2.9605611047311857 | 1.1950925487301407 | -0.7998665334221533 | 3.1900516308824347 |
| ctx-rh-postcentral | GFAP | amyloid | 14.763293645274876 | 8.6455726262911234 | 20.881014664258629 | 14.76443753372245 | 8.6823339420276184 | 20.846541125417279 |
| ctx-rh-postcentral | GFAP | tau | 0.74208334278276133 | -4.4689809397583282 | 5.9531476253238509 | 2.4815083694880418 | -2.7533470972699412 | 7.7163638362460247 |
| ctx-rh-postcentral | NFL | amyloid | 1.5262539545667453 | -0.60616865902066275 | 3.6586765681541538 | 1.4288922130391213 | -0.73491420209122227 | 3.5926986281694648 |
| ctx-rh-postcentral | NFL | tau | 1.3947348617403876 | -0.33006301494723123 | 3.1195327384280063 | 1.4651284617973193 | -0.3783146586849413 | 3.3085715822795798 |
| ctx-rh-posteriorcingulate | GFAP | amyloid | 13.732423036342464 | 7.5343576452823413 | 19.930488427402587 | 13.669946638737271 | 7.5934913771977453 | 19.746401900276791 |
| ctx-rh-posteriorcingulate | GFAP | tau | 4.1025226876887162 | -1.4291730391762645 | 9.6342184145536969 | 5.746829922350118 | -0.033373715467589202 | 11.527033560167826 |
| ctx-rh-posteriorcingulate | NFL | amyloid | 1.2761526038583588 | -0.85835912730733166 | 3.4106643350240491 | 1.1482854469078307 | -1.0049157916762446 | 3.301486685491906 |
| ctx-rh-posteriorcingulate | NFL | tau | 1.5576672431762983 | -0.1863658249661248 | 3.3017003113187213 | 1.7022341369592813 | 0.0038194515238178998 | 3.4006488223947446 |
| ctx-rh-precentral | GFAP | amyloid | 13.95049133273602 | 7.8487737708366536 | 20.052208894635388 | 13.954510359914666 | 7.8716794503891458 | 20.037341269440187 |
| ctx-rh-precentral | GFAP | tau | 2.106117642016911 | -2.894588335331127 | 7.106823619364949 | 3.7930224087242479 | -1.395026401300572 | 8.9810712187490687 |
| ctx-rh-precentral | NFL | amyloid | 1.4924483151535013 | -0.70796693453027149 | 3.6928635648372738 | 1.3786108339938501 | -0.84670814593479471 | 3.6039298139224942 |
| ctx-rh-precentral | NFL | tau | 1.2551356374841347 | -0.55721540121381485 | 3.0674866761820843 | 1.3167301863074661 | -0.58006154248231812 | 3.2135219150972505 |
| ctx-rh-precuneus | GFAP | amyloid | 13.556839208612381 | 7.2825922686061659 | 19.831086148618596 | 13.623009344768604 | 7.4048980169378718 | 19.841120672599335 |
| ctx-rh-precuneus | GFAP | tau | 4.9819685196975785 | -0.31634633134239371 | 10.28028337073755 | 6.0860296207178219 | 0.53535916289533514 | 11.636700078540308 |
| ctx-rh-precuneus | NFL | amyloid | 1.361958158418805 | -0.63758149244161966 | 3.3614978092792298 | 1.2266292814368198 | -0.79227386516165477 | 3.2455324280352942 |
| ctx-rh-precuneus | NFL | tau | 1.5348835071784737 | -0.12981920370164229 | 3.1995862180585899 | 1.6118615298448875 | 0.0066117414497524002 | 3.2171113182400228 |
| ctx-rh-rostralanteriorcingulate | GFAP | amyloid | 15.580644588344772 | 10.260678135870032 | 20.900611040819513 | 15.4729023567709 | 10.1548192794748 | 20.790985434066997 |
| ctx-rh-rostralanteriorcingulate | GFAP | tau | -1.7516527303679852 | -6.7099647328469523 | 3.2066592721109815 | -0.0320784347178125 | -4.806814600856077 | 4.7426577314204525 |
| ctx-rh-rostralanteriorcingulate | NFL | amyloid | 1.9299217158558628 | -0.1936169642703453 | 4.0534603959820714 | 1.8021561082726001 | -0.34460491152374217 | 3.9489171280689419 |
| ctx-rh-rostralanteriorcingulate | NFL | tau | 0.57079723760539713 | -1.2222417753741956 | 2.3638362505849901 | 0.68948096773097978 | -1.1393459857578998 | 2.5183079212198596 |
| ctx-rh-rostralmiddlefrontal | GFAP | amyloid | 14.760659323785816 | 9.1903179294556647 | 20.33100071811597 | 14.62621336664 | 9.1372950657514753 | 20.115131667528523 |
| ctx-rh-rostralmiddlefrontal | GFAP | tau | 4.7953813609225655 | -0.42692274638016592 | 10.017685468225295 | 6.5195279802131765 | 0.77810117538524803 | 12.260954785041104 |
| ctx-rh-rostralmiddlefrontal | NFL | amyloid | 1.5129616333716702 | -0.65332312582810625 | 3.6792463925714465 | 1.3638864208702817 | -0.81634761654842203 | 3.5441204582889858 |
| ctx-rh-rostralmiddlefrontal | NFL | tau | 1.1640050230305534 | -0.74738746594757166 | 3.0753975120086787 | 1.2871922977780683 | -0.55163917746965874 | 3.1260237730257954 |
| ctx-rh-superiorfrontal | GFAP | amyloid | 14.991111240078263 | 9.3094008426071646 | 20.672821637549365 | 14.870667682902877 | 9.2628713285036248 | 20.478464037302125 |
| ctx-rh-superiorfrontal | GFAP | tau | 3.3720517720861971 | -1.1608320555103586 | 7.9049355996827533 | 5.1727856443475151 | 0.27746740596884839 | 10.068103882726181 |
| ctx-rh-superiorfrontal | NFL | amyloid | 1.5449745449054926 | -0.60391193916328234 | 3.693861028974267 | 1.4098234255887878 | -0.76004461476890461 | 3.57969146594648 |
| ctx-rh-superiorfrontal | NFL | tau | 1.3515508277070023 | -0.48380641427026672 | 3.1869080696842715 | 1.4900353371496915 | -0.40233808749788902 | 3.3824087617972718 |
| ctx-rh-superiorparietal | GFAP | amyloid | 13.23068934288356 | 7.2278582835791374 | 19.233520402187981 | 13.360006324155997 | 7.4521105549430828 | 19.26790209336891 |
| ctx-rh-superiorparietal | GFAP | tau | 5.0575922192265992 | 0.18753780895501301 | 9.9276466294981844 | 6.3608871699967313 | 1.4757296800632069 | 11.246044659930256 |
| ctx-rh-superiorparietal | NFL | amyloid | 1.1721088836025353 | -0.7803535366695924 | 3.1245713038746628 | 1.0486164517645602 | -0.92501305769572895 | 3.0222459612248493 |
| ctx-rh-superiorparietal | NFL | tau | 1.4404829703913546 | -0.44289001358176172 | 3.323855954364471 | 1.5738213852309155 | -0.3386136378991253 | 3.4862564083609566 |
| ctx-rh-superiortemporal | GFAP | amyloid | 14.539674777633923 | 8.2436928291485181 | 20.835656726119328 | 14.327109802501557 | 8.1763325911308673 | 20.477887013872248 |
| ctx-rh-superiortemporal | GFAP | tau | 0.69960650767952592 | -4.5580884160237014 | 5.9573014313827537 | 2.1616097502622384 | -3.2398696737351012 | 7.5630891742595781 |
| ctx-rh-superiortemporal | NFL | amyloid | 1.3524980057925184 | -0.81776126874577248 | 3.5227572803308096 | 1.2105695428886434 | -0.95844429554329158 | 3.3795833813205785 |
| ctx-rh-superiortemporal | NFL | tau | 0.86349276029528033 | -1.2661269909667561 | 2.9931125115573169 | 0.89495380346491504 | -1.3009940719111204 | 3.0909016788409507 |
| ctx-rh-supramarginal | GFAP | amyloid | 12.846973618044156 | 6.6963504049965898 | 18.997596831091723 | 12.7718369169199 | 6.7430531086978931 | 18.800620725141908 |
| ctx-rh-supramarginal | GFAP | tau | 5.2240348807562444 | -0.1347955759915668 | 10.582865337504057 | 6.7040787937763113 | 1.1834997176923228 | 12.2246578698603 |
| ctx-rh-supramarginal | NFL | amyloid | 1.2984878001239351 | -0.77180760460911091 | 3.3687832048569808 | 1.1642622630405042 | -0.91552229215464365 | 3.2440468182356517 |
| ctx-rh-supramarginal | NFL | tau | 1.272437293107832 | -0.56543320455782653 | 3.1103077907734908 | 1.3487688473517707 | -0.46693518504358961 | 3.1644728797471311 |
| ctx-rh-temporalpole | GFAP | amyloid | 14.992802199454104 | 9.0128791723502282 | 20.97272522655798 | 14.517569424524703 | 8.7363737967426687 | 20.298765052306742 |
| ctx-rh-temporalpole | GFAP | tau | 0.92394749560008238 | -4.6491844897226198 | 6.4970794809227854 | 3.101008766133603 | -2.9780203568824715 | 9.1800378891496806 |
| ctx-rh-temporalpole | NFL | amyloid | 1.0941173147863732 | -1.1512453125704374 | 3.3394799421431842 | 0.92091044665227717 | -1.3127937880838696 | 3.1546146813884244 |
| ctx-rh-temporalpole | NFL | tau | 1.0429038506200636 | -0.97547175460260205 | 3.0612794558427292 | 1.2376266218375018 | -0.85526394104494341 | 3.3305171847199473 |
| ctx-rh-transversetemporal | GFAP | amyloid | 13.89021614095078 | 8.0843351969344521 | 19.696097084967107 | 13.806329105444178 | 8.0865029886879487 | 19.526155222200408 |
| ctx-rh-transversetemporal | GFAP | tau | -0.82384443161963405 | -6.3340032434162907 | 4.6863143801770217 | 0.71638776191169606 | -4.7712808299005101 | 6.2040563537239031 |
| ctx-rh-transversetemporal | NFL | amyloid | 1.313927708838905 | -0.86850791136053118 | 3.4963633290383411 | 1.2087960183515096 | -0.99720345958144696 | 3.4147954962844662 |
| ctx-rh-transversetemporal | NFL | tau | 0.9697815667359968 | -0.98592035146710322 | 2.9254834849390967 | 0.96453792116976478 | -1.0901138367386405 | 3.0191896790781696 |

## T4B — All deletion ranges and standard-error comparisons

Source: tables/T4_all_sensitivities.csv

| region | outcome | predictor | base_beta | leave_one_out_min | leave_one_out_max | conventional_se | HC3_se | HC3_to_conventional_SE_ratio | quadratic_age_standardized_change | numeric_sex_contrast_standardized_change | leave_one_out_max_standardized_change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctx-lh-bankssts | GFAP | amyloid | 11.520263335693542 | 10.317678234615473 | 12.296816010742877 | 2.8425467951524572 | 3.1000994501454646 | 1.0906063025707178 | 0.0071855188961365514 | 0.011834622967535867 | 0.033189372756036124 |
| ctx-lh-bankssts | GFAP | tau | 4.594947777022691 | 3.4611529786048147 | 5.8999971887745151 | 2.8899899215509168 | 2.9811256525465879 | 1.0315349649893459 | 0.0011310084129663859 | 0.018690591822269557 | 0.036017219365887615 |
| ctx-lh-bankssts | NFL | amyloid | 1.1182234402902655 | 0.79341037940398995 | 1.7660478209538972 | 0.96275303897127895 | 1.0908873493926268 | 1.1330915668240964 | 0.011161974190795253 | -0.00042318391438428838 | 0.056116622090620488 |
| ctx-lh-bankssts | NFL | tau | 1.1419347556943751 | 0.78401320798192287 | 1.4948712790386776 | 0.97882173279060658 | 0.83247709178017493 | 0.85048897454166128 | 0.0017569067589387212 | 0.0016815114234774644 | 0.031004310474536678 |
| ctx-lh-caudalanteriorcingulate | GFAP | amyloid | 15.214439088626271 | 13.435082925109118 | 15.889745490979204 | 2.6414057874533841 | 2.9807045168957842 | 1.1284538449389567 | 0.0057132976474907841 | 0.0058411108007667594 | 0.049107306355101257 |
| ctx-lh-caudalanteriorcingulate | GFAP | tau | -0.1476070612052533 | -1.0272014358324819 | 0.67845516025543984 | 2.9067925941878507 | 2.5152237687839523 | 0.865291790619378 | 1.5345366464485852e-05 | 0.044982938522429086 | 0.024275359429819184 |
| ctx-lh-caudalanteriorcingulate | NFL | amyloid | 1.6145907364635508 | 1.2731047308195806 | 2.3941172688256693 | 0.90885081817675162 | 1.1571204795731749 | 1.2731687714101174 | 0.0093558206414668683 | -0.0011717503975109962 | 0.067525084161489973 |
| ctx-lh-caudalanteriorcingulate | NFL | tau | 0.78795863253168841 | 0.54027957319460929 | 1.1772622496792908 | 1.000164700193523 | 0.98209838904713198 | 0.98193666388856227 | 2.5128831924797152e-05 | 0.0071408724708757572 | 0.033722725809738958 |
| ctx-lh-caudalmiddlefrontal | GFAP | amyloid | 13.807702457297829 | 11.973263543001726 | 14.701787501846145 | 2.6815516350328292 | 3.1298156718862047 | 1.167165916552596 | 0.0074652133183873348 | 0.007236529747175007 | 0.050627499767103033 |
| ctx-lh-caudalmiddlefrontal | GFAP | tau | 4.1536826827891993 | 2.9401916395655348 | 4.9880226081553696 | 2.8486040951100402 | 2.8012487033314 | 0.98337593073746843 | -0.00014239936296160075 | 0.02906413602713926 | 0.03349035883910121 |
| ctx-lh-caudalmiddlefrontal | NFL | amyloid | 1.5464421699185047 | 1.2434866461420642 | 2.3338803324308373 | 0.92240109483045341 | 1.1461052682307289 | 1.2425237509517424 | 0.011538683559638472 | -1.2146519663810751e-05 | 0.068210414896967247 |
| ctx-lh-caudalmiddlefrontal | NFL | tau | 1.413505198397313 | 1.1585076305983282 | 1.7128507628298693 | 0.97986386006542281 | 0.86765389919466529 | 0.88548413157796679 | -0.00022010103639819181 | 0.0043149279816122365 | 0.02593027125122567 |
| ctx-lh-cuneus | GFAP | amyloid | 11.409331061088984 | 9.7869376823983032 | 12.400396478266211 | 2.7983610032665536 | 3.2196090563470716 | 1.1505338491312562 | 0.0082612558623485627 | 0.011862362825804504 | 0.044775391408074912 |
| ctx-lh-cuneus | GFAP | tau | 2.3111659190100431 | 0.86823550953115891 | 3.1386875662377935 | 2.9588920988460532 | 2.989624578006147 | 1.0103864818768076 | -0.00054978083077233172 | 0.031705835000593874 | 0.039822508343304017 |
| ctx-lh-cuneus | NFL | amyloid | 1.3818536408612667 | 1.0364557210414005 | 2.0242596611626311 | 0.92386784732779181 | 1.0480448806135203 | 1.1344099522944757 | 0.013522507274258608 | -0.00054000296633239825 | 0.05564726636725504 |
| ctx-lh-cuneus | NFL | tau | 1.3194883602568681 | 1.0069983206335973 | 1.5321156727080272 | 0.97686655533189903 | 0.8070158051915246 | 0.82612696768734584 | -0.00089991345229423745 | 0.0066736172651826672 | 0.02706888777890443 |
| ctx-lh-entorhinal | GFAP | amyloid | 10.24439472948194 | 9.1890291644808553 | 10.93321312472116 | 2.9495654458202183 | 3.1011619587386838 | 1.0513962194442203 | 0.0094251495829910572 | 0.00081367348406604268 | 0.029126355464827745 |
| ctx-lh-entorhinal | GFAP | tau | 4.7098856862589757 | 4.1172384087344156 | 6.0053964779459665 | 3.1926452635368978 | 2.9569606911957091 | 0.92617890404770775 | -0.0029854210052416841 | 0.046841437158118636 | 0.035753969125529445 |
| ctx-lh-entorhinal | NFL | amyloid | 1.3116913147858669 | 1.0423097309286731 | 1.9444448423034315 | 0.99040623276288564 | 1.0690112803391507 | 1.0793664710257169 | 0.015323399213288652 | -0.0032091245807625954 | 0.054811136536472738 |
| ctx-lh-entorhinal | NFL | tau | 0.50988902907574163 | 0.2126859384028246 | 0.69241194017049867 | 1.0720276685125567 | 0.88487311609352104 | 0.82542003540009978 | -0.0048536946263016342 | 0.0041098970196637137 | 0.025744683314282667 |
| ctx-lh-frontalpole | GFAP | amyloid | 15.306747634784694 | 13.744661870406777 | 16.017773045174316 | 2.6013866533903029 | 2.7488064064789541 | 1.056669681493339 | 0.013401574685530606 | 0.003449554737449614 | 0.043111000347800459 |
| ctx-lh-frontalpole | GFAP | tau | 1.1226646283864132 | 0.36942051551516952 | 1.8252746380145211 | 2.8472034076668771 | 2.3103619052196471 | 0.81144954343562647 | 0.0085587780748216987 | 0.043264874541156545 | 0.020788299818418024 |
| ctx-lh-frontalpole | NFL | amyloid | 1.5618671880484698 | 1.3105820435490569 | 2.1593042298156586 | 0.90307625865534857 | 0.96648095119355681 | 1.0702096771236305 | 0.016514059099279499 | -0.001074300424708313 | 0.0517519094626284 |
| ctx-lh-frontalpole | NFL | tau | 0.86494199756621004 | 0.441325230627443 | 1.1681294321528288 | 0.98841200621812464 | 0.96192659458391583 | 0.97320407738110382 | 0.01054653428882726 | 0.0055541336402417417 | 0.036695040710263561 |
| ctx-lh-fusiform | GFAP | amyloid | 11.231378860424243 | 9.9671950337834527 | 11.890009369490578 | 2.9612528787962864 | 3.1145910914564325 | 1.0517815326607556 | 0.0097963542264010925 | 0.0041216627237710881 | 0.034889396365313484 |
| ctx-lh-fusiform | GFAP | tau | 5.0367129754820033 | 4.1058902432995552 | 5.972867912205821 | 3.1144647549535796 | 2.9213326276621556 | 0.93798866178072948 | -0.0065016996643340761 | 0.034059735363941704 | 0.025836338005914783 |
| ctx-lh-fusiform | NFL | amyloid | 1.1021510445708551 | 0.75935122504754726 | 1.8284754405317432 | 1.0015877011128582 | 1.1719044580360545 | 1.1700467734717173 | 0.016523193955566423 | -0.0012125704132905143 | 0.062916544761069254 |
| ctx-lh-fusiform | NFL | tau | 1.5358255898728563 | 1.1974676570121381 | 1.7651314042431701 | 1.0534087164413255 | 0.98015529930666323 | 0.93046059331829878 | -0.010966206622573384 | 0.005856934387937357 | 0.029309647516287753 |
| ctx-lh-inferiorparietal | GFAP | amyloid | 10.976396511669533 | 9.5969715819276686 | 11.713979773134264 | 2.8519710927692485 | 3.1307191156007743 | 1.0977387265734391 | 0.0088038366667505981 | 0.011522415840484896 | 0.038069861451908653 |
| ctx-lh-inferiorparietal | GFAP | tau | 6.4937913556147695 | 5.4725917516051474 | 8.0438925841119389 | 2.9279577379666057 | 2.9145914913166102 | 0.99543495916055191 | -0.0028645439046782214 | 0.023002970150198282 | 0.04278024684994184 |
| ctx-lh-inferiorparietal | NFL | amyloid | 0.98293657686037483 | 0.63615287341118809 | 1.6598258199220179 | 0.97334177872756344 | 1.0930610536156511 | 1.12299818779442 | 0.014044827377896137 | 0.00014551565128432707 | 0.058634313532912721 |
| ctx-lh-inferiorparietal | NFL | tau | 1.5631225842402483 | 1.2965506848357675 | 1.987764919588352 | 0.99927506275819522 | 0.83882005969713513 | 0.83942859274585235 | -0.0045698286077420448 | 0.0027826529497424301 | 0.036783878729598166 |
| ctx-lh-inferiortemporal | GFAP | amyloid | 11.720116016544756 | 10.198783834455179 | 12.514584128756203 | 3.0794209381691293 | 3.3816249443733777 | 1.0981366342153678 | 0.010652820686356219 | 0.0052086191568467806 | 0.041986268441094654 |
| ctx-lh-inferiortemporal | GFAP | tau | 5.1202363409841114 | 3.8763211637039392 | 6.2596193840312786 | 3.1934005486851902 | 3.3000601397796197 | 1.0334000039983535 | -0.0063338196753540401 | 0.027192533977076147 | 0.034330014947492903 |
| ctx-lh-inferiortemporal | NFL | amyloid | 1.1091576266743313 | 0.77710394333140609 | 1.8949199690289045 | 1.0508835794881533 | 1.2342875039507222 | 1.1745235419435311 | 0.017221541984645025 | -0.00056891577235455501 | 0.068065249989174667 |
| ctx-lh-inferiortemporal | NFL | tau | 1.5286750761143866 | 1.1875975524063482 | 1.8435072836486768 | 1.0897802758128194 | 1.0238960570329627 | 0.93954357567105296 | -0.010239367081619693 | 0.0039248582120364594 | 0.029545227183208955 |
| ctx-lh-insula | GFAP | amyloid | 14.144620912752259 | 12.719332845897174 | 14.686339986328289 | 2.7767645183963641 | 2.9275940705542962 | 1.054318452702298 | 0.0065665263271853227 | -0.00084983262244597586 | 0.039335608675990605 |
| ctx-lh-insula | GFAP | tau | -0.65977027255522103 | -1.3638497107758982 | 0.17511764775809099 | 3.0972346352431899 | 2.6989750199278189 | 0.87141445120637417 | 0.0023390471189192403 | 0.043997325351070864 | 0.023041534750388906 |
| ctx-lh-insula | NFL | amyloid | 1.4358049395749857 | 1.150779394879168 | 2.2255075254662859 | 0.93958084941248998 | 1.1796667907947975 | 1.2555245155671604 | 0.010511699644327046 | -0.0023740978262842155 | 0.068406566500401084 |
| ctx-lh-insula | NFL | tau | 0.90315406405808618 | 0.61062207817662051 | 1.2150410949546049 | 1.0480191352676247 | 0.98707320825227085 | 0.94184655130386474 | 0.0037443481595765132 | 0.0072292456343574646 | 0.027016653232248698 |
| ctx-lh-isthmuscingulate | GFAP | amyloid | 12.236352810149182 | 10.64519088470475 | 13.139328798505389 | 2.7780937968231187 | 3.1825417296475762 | 1.1455846931039415 | 0.010167180200528958 | 0.0093393174238818964 | 0.043913454616596903 |
| ctx-lh-isthmuscingulate | GFAP | tau | 4.0439201543291583 | 2.9127599926906234 | 5.32146737231123 | 2.9107178515652676 | 2.9072051733077053 | 0.99879319177031423 | 0.001860297299738804 | 0.030258778452373094 | 0.03525820400820958 |
| ctx-lh-isthmuscingulate | NFL | amyloid | 1.2389043091104679 | 0.92412355859800843 | 2.0695261327364229 | 0.93908492387466502 | 1.1951713190526809 | 1.2726978025814781 | 0.014474944929883583 | 8.8416712021784349e-05 | 0.071951121890304129 |
| ctx-lh-isthmuscingulate | NFL | tau | 1.3998940628139962 | 1.0819220342759324 | 1.9409299344658499 | 0.98391611369766641 | 0.93298672195070964 | 0.94823807534205484 | 0.0026484925452121117 | 0.0045383965519384187 | 0.046866259519060691 |
| ctx-lh-lateraloccipital | GFAP | amyloid | 10.763647090833899 | 9.2734155770800584 | 11.619451822277179 | 2.8840395718077043 | 3.1797223286297083 | 1.1025238210017594 | 0.009453090085602113 | 0.0091829817032108192 | 0.041127941098246946 |
| ctx-lh-lateraloccipital | GFAP | tau | 4.4658868202198851 | 3.1708604412273464 | 5.443891070634959 | 3.0583884485080963 | 3.0409516044175335 | 0.99429868233413299 | -0.0041178832871858187 | 0.034586098584091139 | 0.035740600131127703 |
| ctx-lh-lateraloccipital | NFL | amyloid | 1.0763710873902796 | 0.68362216958294031 | 1.5807271843833788 | 0.96048437124163055 | 0.99733322999203622 | 1.0383648707399276 | 0.015401996019432094 | 0.0002047722239723979 | 0.043688939994923799 |
| ctx-lh-lateraloccipital | NFL | tau | 1.5580918234750818 | 1.0989134230707158 | 1.9466378818337908 | 1.0185485437485624 | 0.9984702383655446 | 0.98028733583072669 | -0.0067093004957533616 | 0.005957229240295351 | 0.039775503264127134 |
| ctx-lh-lateralorbitofrontal | GFAP | amyloid | 15.27540641734036 | 13.964588565782558 | 15.907088254629665 | 2.7345452727238126 | 2.7964219584126786 | 1.0226277788508624 | 0.0088769570101975993 | 0.00026439578769336426 | 0.036176418826091912 |
| ctx-lh-lateralorbitofrontal | GFAP | tau | -0.14508964948556491 | -1.3249550746412906 | 0.59158916126983296 | 3.0349975268264791 | 2.7874677600587598 | 0.91844152603756923 | 0.0014787639462128038 | 0.041862451194386543 | 0.032562347032528464 |
| ctx-lh-lateralorbitofrontal | NFL | amyloid | 1.7871567788183422 | 1.519188798582324 | 2.6284906897421516 | 0.93820512077789275 | 1.173149773141124 | 1.2504192816262099 | 0.01298096817976873 | -0.001512581624499566 | 0.072879037190558243 |
| ctx-lh-lateralorbitofrontal | NFL | tau | 0.77630743069898522 | 0.40091303764930131 | 1.0925690581399781 | 1.0412883815160128 | 1.0072963459827056 | 0.9673557910212941 | 0.0021624288265824241 | 0.0064840665583920107 | 0.032517864283105671 |
| ctx-lh-lingual | GFAP | amyloid | 11.101420785166351 | 9.4817343310113031 | 11.996843963412337 | 2.9058241718716089 | 3.294193721819155 | 1.1336521162247066 | 0.0084883236912615175 | 0.0078866689022242774 | 0.044700684738788 |
| ctx-lh-lingual | GFAP | tau | 2.1172263717373063 | 0.77328520897855269 | 2.8309727184494591 | 3.1140430412720805 | 3.002982444171431 | 0.964335561317328 | 0.0007380519161602388 | 0.037906907019440231 | 0.037090567788503843 |
| ctx-lh-lingual | NFL | amyloid | 1.2574130522430318 | 0.89331762886095145 | 2.0284409901295359 | 0.95605199821367481 | 1.1657551900315906 | 1.2193428727827915 | 0.013791643140971196 | 0.00013886791398103109 | 0.066788908696773841 |
| ctx-lh-lingual | NFL | tau | 1.3971838774019469 | 1.0635466242262914 | 1.5854587667224651 | 1.0245585747929091 | 0.89607676526814917 | 0.87459788763104185 | 0.0011991706510523698 | 0.0078482388606270076 | 0.028900727127051766 |
| ctx-lh-medialorbitofrontal | GFAP | amyloid | 15.804177148438484 | 14.237731119979072 | 16.385484029013824 | 2.6432882949915535 | 2.8141942441321213 | 1.0646565679061177 | 0.0094860580870645295 | 0.004036784613597787 | 0.043231336471859991 |
| ctx-lh-medialorbitofrontal | GFAP | tau | -0.64622903842542945 | -1.7831941292515845 | 0.2587063236529113 | 2.9121375413044452 | 2.6342836049377736 | 0.90458763282100629 | 0.0019477329077260889 | 0.040346055168093621 | 0.031378368296931053 |
| ctx-lh-medialorbitofrontal | NFL | amyloid | 1.8307500714608549 | 1.5258466308138812 | 2.5526298532530727 | 0.91353738905417836 | 1.0873127242166989 | 1.1902224662555267 | 0.013439312162424645 | -0.0016255039833565797 | 0.062531538050784 |
| ctx-lh-medialorbitofrontal | NFL | tau | 0.64325645623896621 | 0.36469407497306339 | 1.0636841513142516 | 1.0064534130048115 | 0.94697726765018075 | 0.94090521768209612 | 0.0027594381476168908 | 0.0065787177517107323 | 0.036418793094513902 |
| ctx-lh-middletemporal | GFAP | amyloid | 11.19146432010684 | 9.8996955882073117 | 12.118305379187026 | 3.0430452459728969 | 3.2925595398930612 | 1.081994933940061 | 0.007244276528222255 | 0.0054863170463626144 | 0.03565069442417973 |
| ctx-lh-middletemporal | GFAP | tau | 5.6148722741568928 | 4.2254914547953151 | 6.6091435549911068 | 3.1957116363809122 | 3.4069579616635131 | 1.0661030622656034 | -0.001623180632600489 | 0.029586885464060575 | 0.038344627646342964 |
| ctx-lh-middletemporal | NFL | amyloid | 1.15400061814837 | 0.86020092106185464 | 1.8573085285277371 | 1.0371581219247623 | 1.1793240591854934 | 1.1370725777057977 | 0.012035086025346371 | -0.0014227146452365027 | 0.060922783084626481 |
| ctx-lh-middletemporal | NFL | tau | 1.3538807076516182 | 1.0309608517148043 | 1.6833745115036176 | 1.089191257799476 | 0.98632692197839644 | 0.90555897774198146 | -0.0026966279478591497 | 0.0047233509259524027 | 0.028541808279926788 |
| ctx-lh-paracentral | GFAP | amyloid | 14.608100213393724 | 12.588078481657009 | 15.291589081414791 | 2.6482022909152128 | 3.218317980373405 | 1.2152840405787737 | 0.005554804295671156 | 0.0066489574408146084 | 0.055749280587130051 |
| ctx-lh-paracentral | GFAP | tau | 0.84668873560206492 | -0.22843635594190359 | 2.2795587914134732 | 2.8967154676451399 | 2.8961439598202383 | 0.99980270488030842 | 0.003457370469672497 | 0.037309802829302956 | 0.039544859112802082 |
| ctx-lh-paracentral | NFL | amyloid | 1.4381175357490117 | 1.1647984562275613 | 2.1497307817233411 | 0.90025564440151551 | 1.065829505572135 | 1.1839187148675885 | 0.0092468585997297504 | 0.00081082417269777158 | 0.061642217846314268 |
| ctx-lh-paracentral | NFL | tau | 1.5840818529434404 | 1.3510880016737681 | 1.9391112653771376 | 0.98473763085201016 | 0.88784941551845709 | 0.90161012202841895 | 0.0057553451315742925 | 0.0069771695415564976 | 0.030753784456502918 |
| ctx-lh-parahippocampal | GFAP | amyloid | 10.235392416916277 | 9.1944051849585922 | 10.845914231840217 | 2.977124265996411 | 3.0015244684669891 | 1.0081958965399154 | 0.011807858124404876 | 0.0017471217345006982 | 0.028729537098659705 |
| ctx-lh-parahippocampal | GFAP | tau | 5.6352024714790314 | 4.6515376798602635 | 6.6535339538496814 | 3.2135035120457398 | 2.8975921862102987 | 0.90169255311181229 | -0.0016063912939385948 | 0.044779233984219999 | 0.028104275636965704 |
| ctx-lh-parahippocampal | NFL | amyloid | 1.0147218523567147 | 0.72980349940823486 | 1.730581231421336 | 1.0024022097958207 | 1.1466060419363249 | 1.1438582544324967 | 0.017094330202866173 | -0.0013416521231570829 | 0.062010031490083425 |
| ctx-lh-parahippocampal | NFL | tau | 1.3511908244989128 | 1.0351945706127104 | 1.5821927066906389 | 1.0819914568071185 | 0.93780333289345763 | 0.86673820481064612 | -0.0023255854638734824 | 0.0067964618557187122 | 0.027372607284737352 |
| ctx-lh-parsopercularis | GFAP | amyloid | 14.26009275495316 | 12.834633849542609 | 15.18242287673727 | 2.6940575131382833 | 2.8789469091169528 | 1.0686286001976599 | 0.0073553554776984807 | 0.003532375077553667 | 0.039340323539407238 |
| ctx-lh-parsopercularis | GFAP | tau | 2.5805159563853399 | 1.5950871536716209 | 3.3319443790233563 | 2.9832342124485445 | 2.7254733564979539 | 0.91359684235485195 | 0.0021442087364357517 | 0.044262775633683561 | 0.027196215742636917 |
| ctx-lh-parsopercularis | NFL | amyloid | 1.3527540591884979 | 1.0431441810249569 | 2.1215210498835364 | 0.9234584690777804 | 1.1322980883271578 | 1.2261494439029152 | 0.011081580581370236 | -0.00031079212038046829 | 0.066593058211831688 |
| ctx-lh-parsopercularis | NFL | tau | 1.5594892576424535 | 1.1523215448925379 | 1.9305132171043184 | 1.0225813240041193 | 1.0322556765358211 | 1.0094607170154644 | 0.0032304654707896322 | 0.0080639065831936644 | 0.035270170968994603 |
| ctx-lh-parsorbitalis | GFAP | amyloid | 13.683987153562375 | 12.760319852931543 | 14.646698219823261 | 2.7213565538344024 | 2.6294509293834989 | 0.96622801068775488 | 0.0071959271887302601 | 0.0013734146634673599 | 0.026569243545300887 |
| ctx-lh-parsorbitalis | GFAP | tau | 2.3713624522824723 | 1.3993892717756302 | 3.2558915451907517 | 3.0755519080954681 | 2.7960151067368733 | 0.90911003627583131 | 0.0032268550720432015 | 0.054363221217883853 | 0.026824862679399986 |
| ctx-lh-parsorbitalis | NFL | amyloid | 1.7840878765879156 | 1.5211130586601138 | 2.5347350200037471 | 0.92483498518252039 | 1.0901817244966598 | 1.1787851259557482 | 0.011078888983758422 | -0.0012352447602944976 | 0.065023459023444571 |
| ctx-lh-parsorbitalis | NFL | tau | 0.91325420118032519 | 0.57441491798808464 | 1.2524244127221309 | 1.0452059283976609 | 1.0228105377730683 | 0.97857322656127144 | 0.0049680837746433155 | 0.0097573087907211059 | 0.029380009696439353 |
| ctx-lh-parstriangularis | GFAP | amyloid | 14.373923149398371 | 13.478788109042368 | 15.213532446381723 | 2.6814718874785202 | 2.5831782972364716 | 0.96334341944771329 | 0.0061030811203295855 | 0.0034420312262973384 | 0.024704256268210798 |
| ctx-lh-parstriangularis | GFAP | tau | 2.263226025148962 | 1.082868817847578 | 3.0695687757372987 | 3.0183323964505218 | 2.822051256612411 | 0.93497033657759754 | 0.0028114988853561946 | 0.055743170947215398 | 0.032575919411674342 |
| ctx-lh-parstriangularis | NFL | amyloid | 1.5969553349064796 | 1.3013428954284021 | 2.3546647264839793 | 0.92014054328382477 | 1.1090089547763615 | 1.2052603951332235 | 0.0096019397393402057 | -0.00047873519881453405 | 0.065635213571478931 |
| ctx-lh-parstriangularis | NFL | tau | 1.1176920080387376 | 0.8180575223557518 | 1.4787559436823436 | 1.0357334059887289 | 1.0235244031680877 | 0.98821221489038846 | 0.004423313788913019 | 0.010361013184567367 | 0.031276514178593083 |
| ctx-lh-pericalcarine | GFAP | amyloid | 12.60781812716516 | 10.723438710582702 | 13.47762848052936 | 2.8269772715358097 | 3.2548380599805382 | 1.1513492141421728 | 0.0054815699828528307 | 0.0078369688505125941 | 0.052005775570220555 |
| ctx-lh-pericalcarine | GFAP | tau | -0.72436389509624988 | -1.919730001800537 | 0.65074996887804903 | 3.0713734772500132 | 3.1142138302861606 | 1.013948272117823 | 0.0034215887862183033 | 0.039728168314617306 | 0.037950883120473115 |
| ctx-lh-pericalcarine | NFL | amyloid | 1.5605016136113166 | 1.2314196528307175 | 2.3747328429701979 | 0.93589136803186757 | 1.1729281469494994 | 1.2532738168278101 | 0.009777072147385461 | -0.0010371852278402967 | 0.070531316134639546 |
| ctx-lh-pericalcarine | NFL | tau | 0.83789269659273935 | 0.60281580715144112 | 1.0294644495465242 | 1.0168005078437357 | 0.8028608475400324 | 0.78959524640935563 | 0.0061028355974999801 | 0.0078978097296844452 | 0.020363112844722361 |
| ctx-lh-postcentral | GFAP | amyloid | 13.226100290820897 | 11.725653923950478 | 13.882374084800549 | 2.7301662622372338 | 2.9249769209972905 | 1.0713548700145532 | 0.0060939148739437114 | 0.006603274905988497 | 0.041409854259677546 |
| ctx-lh-postcentral | GFAP | tau | 1.4842017833003389 | 0.33882719949173129 | 2.119473659916804 | 3.0265396552788459 | 2.7241555649925617 | 0.90008916957064466 | 0.003362350170933314 | 0.042579836690901381 | 0.031610456485146328 |
| ctx-lh-postcentral | NFL | amyloid | 1.3368578752832303 | 1.0335152948939608 | 2.1063833844898374 | 0.91710570570639804 | 1.1407123935802199 | 1.2438177916487712 | 0.010011913974508386 | 0.00023371999624999858 | 0.066658763513967476 |
| ctx-lh-postcentral | NFL | tau | 1.4091677406532339 | 1.1761920459292921 | 1.7960751491745428 | 1.0166621809062988 | 0.95689136579803635 | 0.94120877491972799 | 0.0055241271596191245 | 0.0075955661314181357 | 0.033515158546224964 |
| ctx-lh-posteriorcingulate | GFAP | amyloid | 14.088863112091046 | 12.266686709457208 | 14.92640854847437 | 2.6597448141871523 | 3.1556836538794681 | 1.1864610608683075 | 0.0067056421224303241 | 0.008010220046486825 | 0.050289074594431854 |
| ctx-lh-posteriorcingulate | GFAP | tau | 4.4306926868357843 | 2.8259679443938523 | 5.1637464592786833 | 2.8463574956349729 | 2.9749737559412375 | 1.0451862636733102 | -0.0012096024423666836 | 0.037965425588792102 | 0.044287766079917378 |
| ctx-lh-posteriorcingulate | NFL | amyloid | 1.1741414383081945 | 0.86831715617742911 | 1.906373905163864 | 0.91775526847514877 | 1.100517591956709 | 1.1991405876484043 | 0.010545119600245635 | 0.0007998353924571031 | 0.06342832077874154 |
| ctx-lh-posteriorcingulate | NFL | tau | 2.0307918320051028 | 1.7492874161965375 | 2.3020422286728515 | 0.98214669830310841 | 0.88895096594681799 | 0.90511017089676304 | -0.0019021895577810476 | 0.0075203548687670426 | 0.024384813832705118 |
| ctx-lh-precentral | GFAP | amyloid | 13.39830300716021 | 11.704086803069194 | 14.14245064237558 | 2.7506624530501722 | 3.085114476012647 | 1.1215896274701411 | 0.0063348336770986859 | 0.0053970334338189121 | 0.046757583373089696 |
| ctx-lh-precentral | GFAP | tau | 1.1736802241320552 | -0.31575314939530558 | 1.877909717969372 | 3.0425936496620336 | 2.7934247150789595 | 0.91810640418225042 | 0.0021187316190632698 | 0.041472219187032901 | 0.041105913739464199 |
| ctx-lh-precentral | NFL | amyloid | 1.3259319977711674 | 1.0166817900377914 | 2.1235455713696552 | 0.92703469423653884 | 1.1639217921993841 | 1.2555320738647586 | 0.010272046354422316 | -0.00043116184611238345 | 0.069091841585406391 |
| ctx-lh-precentral | NFL | tau | 1.2124119798486757 | 0.97949696076612236 | 1.6409718564899609 | 1.0254220289998739 | 0.95028025369874758 | 0.92672112244905214 | 0.0034355612969412105 | 0.0066453996756984657 | 0.037123228699799456 |
| ctx-lh-precuneus | GFAP | amyloid | 13.467474054424668 | 11.771560456066409 | 14.400252605422253 | 2.6470884992058057 | 3.1562258226447435 | 1.192338610360663 | 0.0079050264314747525 | 0.010264049864189528 | 0.046804428665783722 |
| ctx-lh-precuneus | GFAP | tau | 4.3825229320678343 | 3.0866065874504911 | 5.9075190620830238 | 2.7093742935545793 | 3.0011456808419332 | 1.1076895827872357 | 0.00093231299027801326 | 0.020986496582913846 | 0.042087387383407227 |
| ctx-lh-precuneus | NFL | amyloid | 1.4845759518033417 | 1.1942822431206157 | 2.1930900280161603 | 0.908948915280686 | 1.0636178949699908 | 1.1701624558752486 | 0.011862138940496219 | 0.00096382867011005199 | 0.061373757838490507 |
| ctx-lh-precuneus | NFL | tau | 1.3482429973759626 | 1.0375516988671898 | 1.9013136788249565 | 0.93033641525573396 | 0.8320664834351581 | 0.89437161632164741 | 0.0013990119226767288 | 0.0018222727927062392 | 0.047908753277364102 |
| ctx-lh-rostralanteriorcingulate | GFAP | amyloid | 16.137202705196902 | 14.361915859258795 | 16.721392094755227 | 2.614476490481477 | 2.8870393847601838 | 1.104251422902836 | 0.0077029676669967103 | 0.0043459923686851084 | 0.048994999876439078 |
| ctx-lh-rostralanteriorcingulate | GFAP | tau | -1.4162105315631821 | -2.1781442498194599 | -0.61053449928321313 | 2.9350106955391211 | 2.6295008409742047 | 0.89590843569011303 | -0.0006124882209759577 | 0.047560206818340479 | 0.022235334640328442 |
| ctx-lh-rostralanteriorcingulate | NFL | amyloid | 1.8458279207223016 | 1.5830725740062837 | 2.5195725466774279 | 0.90524087983243884 | 1.0426872194440155 | 1.151833995430054 | 0.011622571268571538 | -0.001144872142259893 | 0.058361916730548885 |
| ctx-lh-rostralanteriorcingulate | NFL | tau | 0.72332921843064635 | 0.49158354739994559 | 1.0541077605942399 | 1.0162231995661068 | 0.92685210775254923 | 0.91205564697625874 | -0.00092414875762208515 | 0.0084542715262732465 | 0.028653096426018505 |
| ctx-lh-rostralmiddlefrontal | GFAP | amyloid | 14.249264093757873 | 13.099543834809923 | 15.062614145945428 | 2.6181455057012659 | 2.6497312695072015 | 1.0120641743314702 | 0.0069432288142794018 | 0.0072636145565587113 | 0.031730389978374345 |
| ctx-lh-rostralmiddlefrontal | GFAP | tau | 4.6566948255160936 | 3.7725833168082441 | 5.4601702665497882 | 2.8835410694082833 | 2.6918832922746612 | 0.93353388333291498 | 0.00055633815467451449 | 0.046111740093847164 | 0.024400024908092881 |
| ctx-lh-rostralmiddlefrontal | NFL | amyloid | 1.6038780299291049 | 1.327270714001983 | 2.3034094558179397 | 0.91012634527730318 | 1.0612409463486532 | 1.1660369484473141 | 0.01066056912568761 | 7.2505417401213795e-06 | 0.060595651906313622 |
| ctx-lh-rostralmiddlefrontal | NFL | tau | 1.3561709217182265 | 1.004275333369985 | 1.733260314825448 | 1.0023838206252138 | 0.97345725654229243 | 0.97114222766995673 | 0.00085419644286671909 | 0.0083251843346264058 | 0.03266469061522824 |
| ctx-lh-superiorfrontal | GFAP | amyloid | 15.096604548866672 | 13.323617072039344 | 15.953439483819308 | 2.6311055240878729 | 2.9795494954187074 | 1.1324325338306718 | 0.0082800838052086243 | 0.0047283142533600161 | 0.048931541067201441 |
| ctx-lh-superiorfrontal | GFAP | tau | 3.067288361987631 | 2.1328674412774165 | 3.7212722070158941 | 2.9047929905190313 | 2.4696099905383546 | 0.85018450491960262 | 0.0008056253656395587 | 0.039430868446349132 | 0.025788482013196411 |
| ctx-lh-superiorfrontal | NFL | amyloid | 1.6431084001758007 | 1.3705947382669232 | 2.3920335999341997 | 0.9142747900177054 | 1.1067115917438857 | 1.2104802667942465 | 0.012076259505510712 | -0.00019885185179789188 | 0.064874298750429701 |
| ctx-lh-superiorfrontal | NFL | tau | 1.4077437830853503 | 1.1323629057861535 | 1.7622564709615631 | 1.0093776084379475 | 0.93747827459636879 | 0.92876864590562314 | 0.0011749809794875258 | 0.0064256475981981503 | 0.030709024120858262 |
| ctx-lh-superiorparietal | GFAP | amyloid | 12.416737361568584 | 10.95891083613513 | 13.238874196980127 | 2.7389472542240485 | 3.0173061681795987 | 1.1016298921150309 | 0.0071691354869145504 | 0.013085262762055599 | 0.04023361666702277 |
| ctx-lh-superiorparietal | GFAP | tau | 5.7269555404702448 | 4.6529301634873468 | 6.9889555617179102 | 2.8288487796322288 | 2.7410423102456396 | 0.96896035234587385 | -0.00062059983841889323 | 0.029455424685423948 | 0.034829126924793972 |
| ctx-lh-superiorparietal | NFL | amyloid | 1.129472389962014 | 0.76264075106872831 | 1.768575341554433 | 0.93979606851479303 | 1.0397600925216457 | 1.1063677827093179 | 0.011309121246232696 | 0.00126823642999396 | 0.055361143979750317 |
| ctx-lh-superiorparietal | NFL | tau | 1.6598004905678836 | 1.4116840999213858 | 2.0439728668427297 | 0.97064335847329442 | 0.82193594499975331 | 0.84679500232975369 | -0.00097897979901226395 | 0.0042654490431708056 | 0.033278241295868954 |
| ctx-lh-superiortemporal | GFAP | amyloid | 13.037434290874049 | 11.450087546948591 | 13.814667618634756 | 2.8491414889157798 | 3.1519987269257901 | 1.1062977178171873 | 0.008031347872434879 | 0.0053448924059121697 | 0.043808161875607814 |
| ctx-lh-superiortemporal | GFAP | tau | 2.7410362530904737 | 1.4258402588568546 | 3.5176938202966466 | 3.0623170798445347 | 2.9181491905027448 | 0.95292195890142473 | 0.003029183236398511 | 0.040395151104411484 | 0.036297248369977442 |
| ctx-lh-superiortemporal | NFL | amyloid | 1.2663522489251011 | 0.92515147263656761 | 2.0344196391379654 | 0.96901937259317361 | 1.2031898268704171 | 1.2416571442226016 | 0.011724213978173848 | -0.00093826464562321587 | 0.066532456578048821 |
| ctx-lh-superiortemporal | NFL | tau | 1.0375538358491738 | 0.68062326777687421 | 1.4956240412433293 | 1.0415223627667398 | 1.0736215343769957 | 1.0308194742213566 | 0.0044220214348485182 | 0.005560954843070536 | 0.039679507864066724 |
| ctx-lh-supramarginal | GFAP | amyloid | 12.467270956771692 | 11.219889785579516 | 13.254058740078042 | 2.7918285997001249 | 3.0261938663541628 | 1.083946867898413 | 0.0075514401214896451 | 0.0082234257927435959 | 0.034425670684298984 |
| ctx-lh-supramarginal | GFAP | tau | 5.0015894333915654 | 3.6608208641190623 | 6.155912175451113 | 2.9575300988055173 | 3.1739166366971481 | 1.0731646105576489 | 0.00012679217412900457 | 0.031018342313195342 | 0.03700300942134617 |
| ctx-lh-supramarginal | NFL | amyloid | 1.1161404642415738 | 0.78107118270231291 | 1.8507841185505616 | 0.95690687791116003 | 1.1454784316010891 | 1.1970636412412079 | 0.011524838901352325 | -0.00059882011733975783 | 0.063637185556212394 |
| ctx-lh-supramarginal | NFL | tau | 1.436687119640814 | 1.1436320141839418 | 1.7948291748266296 | 1.0137015193125596 | 0.91078260134015643 | 0.89847216758420423 | 0.00019350737836518417 | 0.0044520539015885357 | 0.031023411537911626 |
| ctx-lh-temporalpole | GFAP | amyloid | 14.746700393022524 | 12.94878246051683 | 15.457644477634473 | 2.8871296550536392 | 3.2291577620571652 | 1.1184664867422351 | 0.011366644091994737 | -0.0064146778880476811 | 0.049619580679321498 |
| ctx-lh-temporalpole | GFAP | tau | 1.5039373500238948 | 0.63559016575783955 | 2.4565432253176054 | 3.162991236400635 | 2.879550403220537 | 0.9103883596267428 | -0.0054875418846414385 | 0.055599755125427586 | 0.0262903568790019 |
| ctx-lh-temporalpole | NFL | amyloid | 1.2970243533767518 | 1.0036271571292037 | 2.0744504946133695 | 1.0008270160780597 | 1.1796480524856072 | 1.1786732707399261 | 0.015900868181820151 | -0.00121259838531911 | 0.067343141557058381 |
| ctx-lh-temporalpole | NFL | tau | 0.8657035726050516 | 0.53303424877965733 | 1.1342446638489925 | 1.096454769693773 | 1.0343158958523491 | 0.94332746269252987 | -0.0076765560216103907 | 0.0051519149755232538 | 0.02881688198756599 |
| ctx-lh-transversetemporal | GFAP | amyloid | 13.33999710707138 | 11.521351283844099 | 14.12330212008896 | 2.7237835225793501 | 3.2825601538091389 | 1.2051472250264008 | 0.0042602998113498028 | 0.0076880513608085926 | 0.050191636404100057 |
| ctx-lh-transversetemporal | GFAP | tau | 0.21158335244170251 | -1.1385385572268971 | 0.99516198532347799 | 2.9630874529064597 | 2.8639823960672581 | 0.96655344858553183 | 0.0042462910210567997 | 0.041379755569254197 | 0.037261146247290426 |
| ctx-lh-transversetemporal | NFL | amyloid | 1.318657559152838 | 1.0220377773642286 | 2.0537888356683713 | 0.91800072709235636 | 1.1440959554954622 | 1.2462909034061791 | 0.0074562679753214867 | -0.0011553059552291537 | 0.063679424953037328 |
| ctx-lh-transversetemporal | NFL | tau | 0.75434249398082787 | 0.47037859945634258 | 1.3149249674013812 | 0.99865367921401138 | 1.0943273020322457 | 1.0958026038551563 | 0.0074317501481592375 | 0.0051533775904452229 | 0.04855944874958381 |
| ctx-rh-bankssts | GFAP | amyloid | 12.653240943129294 | 11.238343702780488 | 13.351179471740206 | 2.879221397537715 | 3.1351892461034447 | 1.0889017596162043 | 0.0071459846979135622 | 0.0095411460081433717 | 0.039048838938155792 |
| ctx-rh-bankssts | GFAP | tau | 2.8193163982432221 | 2.06550386330525 | 3.6103817585772879 | 2.9438713911956813 | 2.5678335461006494 | 0.87226417355742547 | -0.00085076590426729349 | 0.021034195305661061 | 0.02183210410222014 |
| ctx-rh-bankssts | NFL | amyloid | 1.0009119466254974 | 0.6360235980302722 | 1.4713011586270719 | 0.97999264080644177 | 1.0164778237049723 | 1.0372300580425855 | 0.011222513306900281 | -0.00064911562732018399 | 0.040746619660032506 |
| ctx-rh-bankssts | NFL | tau | 0.93076751939518598 | 0.52840586069358064 | 1.3668112473294491 | 1.0019973807222995 | 1.0586274811704812 | 1.0565172140543515 | -0.0013360974148855886 | 0.00071594402714403468 | 0.037771503860978516 |
| ctx-rh-caudalanteriorcingulate | GFAP | amyloid | 15.153857404418416 | 13.667971790133778 | 15.85029245779387 | 2.6821821450900591 | 2.7700670091705586 | 1.0327661804182013 | 0.0047998618932602833 | 0.0032669062307142216 | 0.041008001413883353 |
| ctx-rh-caudalanteriorcingulate | GFAP | tau | -0.44726246631644079 | -1.0597688695196179 | 0.32572761027948488 | 2.9717947020694964 | 2.4130611828146153 | 0.81198784732142149 | -0.0014850967090049402 | 0.045224319696842971 | 0.021333255971540274 |
| ctx-rh-caudalanteriorcingulate | NFL | amyloid | 1.4705608852258532 | 1.1554218788170687 | 2.17159815536872 | 0.92327587493057295 | 1.092786000229417 | 1.1835963983263298 | 0.0083345780980314359 | -0.0015758586077354001 | 0.060726092957087731 |
| ctx-rh-caudalanteriorcingulate | NFL | tau | 0.69354887733753579 | 0.44539602692969688 | 1.0843071461821934 | 1.0229679437281944 | 0.98505552953204822 | 0.96293880523961006 | -0.0025787522182067119 | 0.0057886209836062828 | 0.033848732397316755 |
| ctx-rh-caudalmiddlefrontal | GFAP | amyloid | 14.156362311122663 | 12.675175279918909 | 14.886777383840627 | 2.6747683120852521 | 2.9607890773599159 | 1.1069329122759353 | 0.0078163492704026536 | 0.0058248951304920348 | 0.040878328241351264 |
| ctx-rh-caudalmiddlefrontal | GFAP | tau | 5.4737643285272064 | 4.6362148985458536 | 6.4179371661826075 | 2.8361462692236059 | 2.5605677234214217 | 0.90283345087218514 | -0.0047872476601285383 | 0.033096486501275064 | 0.026057618896972497 |
| ctx-rh-caudalmiddlefrontal | NFL | amyloid | 1.2324386273752117 | 0.88660966967949562 | 1.951490333216952 | 0.94669604477202385 | 1.10845496485272 | 1.170866796131645 | 0.012612228014623241 | -0.00019757893309747817 | 0.062286561056874107 |
| ctx-rh-caudalmiddlefrontal | NFL | tau | 1.2375431921447997 | 0.91595187577426218 | 1.5268985996562527 | 1.003813468006773 | 0.87821161156822092 | 0.87487530259187096 | -0.0077245600168665525 | 0.0033912736826207861 | 0.027857269511690284 |
| ctx-rh-cuneus | GFAP | amyloid | 11.625263359941524 | 9.8152402199145321 | 12.602454216589759 | 2.8284491287957851 | 3.3184793422009218 | 1.1732504956218772 | 0.0065910673056799865 | 0.012364048696691703 | 0.049953664516177089 |
| ctx-rh-cuneus | GFAP | tau | 2.385202443092485 | 1.2459778476853405 | 3.2169901836986523 | 3.0061630186379582 | 2.7226008740972771 | 0.90567306470653131 | -0.00085180820698244335 | 0.035638910679476131 | 0.03144072691065012 |
| ctx-rh-cuneus | NFL | amyloid | 1.3260058821270322 | 0.94680232453637836 | 1.8997980701658621 | 0.93835836524708405 | 1.0347738160229749 | 1.1027490715133159 | 0.011364765115797702 | -0.00042408676201200862 | 0.049703716525364955 |
| ctx-rh-cuneus | NFL | tau | 1.2436511769265151 | 0.75512204342127465 | 1.7702057536131672 | 0.99731622786383178 | 1.0409690303737822 | 1.0437702719461921 | -0.0014687454621686163 | 0.007239109585250778 | 0.045611843382217326 |
| ctx-rh-entorhinal | GFAP | amyloid | 11.137021775328767 | 10.087252891827708 | 11.744480131403108 | 2.9210235050863025 | 2.8964489898031762 | 0.99158701898826374 | 0.006792361321301451 | 0.0025119208398465937 | 0.028971896251642228 |
| ctx-rh-entorhinal | GFAP | tau | 4.0182492462680219 | 3.418435990410599 | 5.4394360850511614 | 3.2022972449718403 | 3.0227257339230813 | 0.94392415902967242 | -0.004308856514570197 | 0.046531251723340855 | 0.039222421520158306 |
| ctx-rh-entorhinal | NFL | amyloid | 0.98868252394138001 | 0.68787675392292391 | 1.6055121544151632 | 0.98793949357779964 | 1.0833005789185659 | 1.0965252284787383 | 0.01244196154232494 | -0.0034784183357768127 | 0.05343175758858499 |
| ctx-rh-entorhinal | NFL | tau | 0.50650493980388056 | 0.16934604292280769 | 0.7549505989173827 | 1.0830710238976975 | 0.97865664993683321 | 0.9035941580404363 | -0.0078927819810694026 | 0.0036713318347931997 | 0.02920578318059559 |
| ctx-rh-frontalpole | GFAP | amyloid | 15.152015261187156 | 13.52715608396694 | 15.827424964786328 | 2.5787444476867161 | 2.8177181841713734 | 1.0926705772256846 | 0.0058743799064531286 | 0.0018269456384540441 | 0.044843443395800896 |
| ctx-rh-frontalpole | GFAP | tau | 1.3369205484701263 | 0.46972070075485572 | 2.0377589706375558 | 2.8654309504521582 | 2.5878007884965974 | 0.90311050353115252 | 0.0064818018102550711 | 0.036933952668486224 | 0.023933290853177979 |
| ctx-rh-frontalpole | NFL | amyloid | 1.4972895137366631 | 1.2270176429537909 | 2.2298059819045921 | 0.89415340494288265 | 1.0711554564451604 | 1.1979549040732942 | 0.0089309697055338817 | -0.0015010000951414233 | 0.063452921881739524 |
| ctx-rh-frontalpole | NFL | tau | 0.97905963113414196 | 0.70366027154528499 | 1.3480223248822272 | 0.99355903345672802 | 0.9120767489368744 | 0.9179894885195039 | 0.0098544487293151864 | 0.0048498955982827609 | 0.031960729896254425 |
| ctx-rh-fusiform | GFAP | amyloid | 10.878607291830706 | 9.7670920816421205 | 11.568772728388826 | 2.9557105770617205 | 2.9579315680800633 | 1.0007514237136679 | 0.0080836936695048937 | 0.0042178650937555271 | 0.030675993409432688 |
| ctx-rh-fusiform | GFAP | tau | 5.8508931245372349 | 5.1822178974055886 | 6.7606732894325097 | 3.166420238177392 | 2.7268691551905926 | 0.86118359221964569 | -0.0052814700509569721 | 0.035652533866861902 | 0.02510843764128513 |
| ctx-rh-fusiform | NFL | amyloid | 0.99441860630979162 | 0.63384073060882073 | 1.5157581026678053 | 1.0059422531820483 | 1.0839555087045725 | 1.0775524194115007 | 0.014442784620463387 | -0.002144323409486028 | 0.045160096426237306 |
| ctx-rh-fusiform | NFL | tau | 1.3934466869737747 | 1.0448408099138389 | 1.8214799778121751 | 1.0776548738002132 | 1.1389982405723311 | 1.0569230170655641 | -0.0094361733069067717 | 0.0057699857070839782 | 0.037077614151503964 |
| ctx-rh-inferiorparietal | GFAP | amyloid | 11.583153361089089 | 10.390177871920612 | 12.381150507802239 | 2.8582042442103632 | 3.1211286997732275 | 1.0919893867261059 | 0.0078483986133274786 | 0.0083804896788207978 | 0.032924163257413201 |
| ctx-rh-inferiorparietal | GFAP | tau | 5.9630265116749825 | 5.0749979427108558 | 6.8565310886066575 | 2.9791031751293269 | 2.7897860221901176 | 0.9364516292957894 | -0.0054380125254720538 | 0.024283129700616368 | 0.024659258156803473 |
| ctx-rh-inferiorparietal | NFL | amyloid | 0.90092243968453523 | 0.4810581615722353 | 1.4610067458408429 | 0.98247660912250845 | 1.0484493605122993 | 1.0671494372254968 | 0.013868343888211024 | -0.0017294887778362914 | 0.048516295906097191 |
| ctx-rh-inferiorparietal | NFL | tau | 1.4690614085394271 | 1.1730179025040519 | 1.7417177693684045 | 1.0240343011371371 | 0.91730182392667681 | 0.89577255655211996 | -0.0096091230182396934 | 0.0035883097423931921 | 0.025644236380160852 |
| ctx-rh-inferiortemporal | GFAP | amyloid | 13.051798104990135 | 11.770174615029228 | 13.680070175461523 | 3.0054070117193388 | 3.1440461717580837 | 1.0461299116885443 | 0.0094809063320313962 | 0.005077617165859377 | 0.035370702416878765 |
| ctx-rh-inferiortemporal | GFAP | tau | 3.151899870285285 | 2.4952357096570603 | 4.0350761013603966 | 3.1695219477487391 | 2.8874543352889095 | 0.91100625989980044 | -0.0075541232058953071 | 0.02960582079122839 | 0.024374212782235435 |
| ctx-rh-inferiortemporal | NFL | amyloid | 1.3924970843895108 | 1.0339557284354219 | 1.9394789248660771 | 1.0289755959352631 | 1.1176240202350325 | 1.0861521154145493 | 0.016312638617718318 | -0.0028036864582267154 | 0.047381318376767151 |
| ctx-rh-inferiortemporal | NFL | tau | 0.85748306632331217 | 0.52980699949653354 | 1.2674573718458726 | 1.0851644127724616 | 1.133612891038122 | 1.0446462100078278 | -0.012997458008330005 | 0.0053938166563037068 | 0.03551328702125469 |
| ctx-rh-insula | GFAP | amyloid | 15.476596009773813 | 13.807128176856668 | 16.117485727156392 | 2.7371608091733157 | 3.0017754982630027 | 1.0966748786563281 | 0.0071040086389848947 | -0.0011873430714538418 | 0.046074568994100576 |
| ctx-rh-insula | GFAP | tau | -1.1818125473082559 | -1.9069547511446596 | -0.35498266798940231 | 3.0591096539144096 | 2.669472035457233 | 0.87263038513228852 | -0.00020402098093707589 | 0.041695913017364597 | 0.022819146059552181 |
| ctx-rh-insula | NFL | amyloid | 1.4249407260295957 | 1.1057718401333698 | 2.164998833260583 | 0.94178864368783921 | 1.1453552009439825 | 1.2161488765239523 | 0.01089792331605783 | -0.0017347478041537872 | 0.064106202804590812 |
| ctx-rh-insula | NFL | tau | 0.88947155672739964 | 0.60012834488450006 | 1.2617778823985022 | 1.0525631969436844 | 0.95277985736359438 | 0.90519966889415315 | -0.00031297892754776716 | 0.0057395790869282709 | 0.032250365999239444 |
| ctx-rh-isthmuscingulate | GFAP | amyloid | 11.401637300009549 | 9.9356910749516878 | 12.220696463415234 | 2.7752502993030292 | 3.0922633754783391 | 1.1142286431803732 | 0.0098444027963572479 | 0.009638067070786344 | 0.040457707034731387 |
| ctx-rh-isthmuscingulate | GFAP | tau | 5.4943905778173709 | 4.4582945501176114 | 6.5940290774270469 | 2.9503761318507924 | 2.8494709417177777 | 0.9657992114823285 | -0.001194187405929916 | 0.033383076070614276 | 0.030348215712731125 |
| ctx-rh-isthmuscingulate | NFL | amyloid | 1.1636977666974431 | 0.80937908243980738 | 1.8363859296237308 | 0.93926189548092676 | 1.0875307766035154 | 1.1578568041948205 | 0.014708261366600814 | -0.00064525550509763707 | 0.058270402520353044 |
| ctx-rh-isthmuscingulate | NFL | tau | 1.5014559622109047 | 1.212257050004347 | 1.9080711520461755 | 0.99853187248725161 | 0.90118417938421502 | 0.90250917793885499 | -0.0017842037602951179 | 0.0056902314989988653 | 0.035222309665031683 |
| ctx-rh-lateraloccipital | GFAP | amyloid | 11.0561963785296 | 9.6925890713905343 | 11.937484336428373 | 2.8599440335689357 | 3.0169251162958499 | 1.0548895645804008 | 0.0097725777568386726 | 0.011711248279719075 | 0.037633321058877053 |
| ctx-rh-lateraloccipital | GFAP | tau | 5.423662203576078 | 4.3479411658290417 | 6.1841335574600524 | 3.0247833549270005 | 2.6940901643029527 | 0.89067210711623723 | -0.0038542576905852884 | 0.032655483160487574 | 0.029688133065419255 |
| ctx-rh-lateraloccipital | NFL | amyloid | 1.0240472488910457 | 0.61605077080619641 | 1.4362689723371906 | 0.96711588886227517 | 0.96504926616025977 | 0.99786310748710105 | 0.015371895710962726 | -0.00068143964683638821 | 0.035707965557694274 |
| ctx-rh-lateraloccipital | NFL | tau | 1.3620281067746249 | 0.95059056376851758 | 1.965406295767381 | 1.0228577932224523 | 1.0748054269522025 | 1.0507867604607013 | -0.0060626017758102519 | 0.0049770931784970107 | 0.052266550657978847 |
| ctx-rh-lateralorbitofrontal | GFAP | amyloid | 16.039572278616674 | 14.587051985148248 | 16.72365344107633 | 2.7521657278895892 | 2.8867701791420353 | 1.0489085558650799 | 0.010295588388602353 | -0.00079244247638239563 | 0.040087173383749578 |
| ctx-rh-lateralorbitofrontal | GFAP | tau | -1.9864190897217473 | -2.8343105891634881 | -1.2339493995318356 | 3.0581256093520168 | 2.7666425215622281 | 0.90468570457066644 | -0.0010000316884223727 | 0.039906114074405918 | 0.023400412167437514 |
| ctx-rh-lateralorbitofrontal | NFL | amyloid | 1.6555180481588023 | 1.3452573242755204 | 2.3439635993624588 | 0.95126070563297438 | 1.0703724363506311 | 1.1252146020668425 | 0.014254729870005617 | -0.0015631087564501377 | 0.059635357945757757 |
| ctx-rh-lateralorbitofrontal | NFL | tau | 0.42578211424016721 | 0.1291424557062823 | 0.71090492249321668 | 1.0570129173497125 | 0.90682180257765643 | 0.85790985870954561 | -0.0013845912483922806 | 0.0039353357141352786 | 0.0256958770183736 |
| ctx-rh-lingual | GFAP | amyloid | 10.984364456792658 | 9.2633581889060164 | 12.011369069403049 | 2.879905802552484 | 3.2323328806749969 | 1.1223745157949798 | 0.0074434412418736039 | 0.010659034417341057 | 0.047496945113621736 |
| ctx-rh-lingual | GFAP | tau | 3.5106974255433139 | 2.5201912230425099 | 4.4222358302735367 | 3.1091019796446706 | 2.7790070771972677 | 0.8938295029855764 | 0.0013154308014862394 | 0.03985541734929543 | 0.027336343633805629 |
| ctx-rh-lingual | NFL | amyloid | 1.1524315116592647 | 0.76890913757168444 | 1.7734456964039031 | 0.95802143496970638 | 1.0645032645096679 | 1.1111476483230551 | 0.011972291259271959 | -0.00064902120482901221 | 0.053794237077848306 |
| ctx-rh-lingual | NFL | tau | 1.2030850612627657 | 0.80357372365520563 | 1.5907897288135469 | 1.0342651962319038 | 0.98991814546447143 | 0.95712216660775185 | 0.0021157849138666528 | 0.0068442670648577392 | 0.034606951239586688 |
| ctx-rh-medialorbitofrontal | GFAP | amyloid | 15.296225252322117 | 13.835637531611731 | 15.776536758321154 | 2.6592600992540776 | 2.7514833147844784 | 1.0346800283117359 | 0.0070804002747756065 | 0.0021306723037267262 | 0.040309821119594275 |
| ctx-rh-medialorbitofrontal | GFAP | tau | -1.5053083245707439 | -2.5554731088077434 | -0.66677224343151387 | 2.961419853591027 | 2.6604788836430688 | 0.89837949874515899 | 1.1425228646104085e-05 | 0.043307412738349538 | 0.028982822461427905 |
| ctx-rh-medialorbitofrontal | NFL | amyloid | 1.4877488414924629 | 1.2067071762947827 | 2.1921669885816981 | 0.91317623898831501 | 1.0646164712683519 | 1.1658389977906276 | 0.010903438524059304 | -0.0021823786866725483 | 0.061018955343248457 |
| ctx-rh-medialorbitofrontal | NFL | tau | 0.79383590381694924 | 0.53510198927760522 | 1.1753151480369839 | 1.0169363443335746 | 0.92952865106218163 | 0.91404801907372724 | 1.7594242320812316e-05 | 0.0068272371960355583 | 0.033044953574271972 |
| ctx-rh-middletemporal | GFAP | amyloid | 13.537510570291683 | 12.168199249445111 | 14.177829744663796 | 3.0007298757403977 | 3.1925071176862718 | 1.063910198480813 | 0.0094250872441739141 | 0.0033770544458018052 | 0.03779074246462559 |
| ctx-rh-middletemporal | GFAP | tau | 2.6339372146097952 | 1.9366311896758233 | 3.5473051615728508 | 3.1982003445255796 | 2.9232723260085609 | 0.9140366490837204 | -0.0060987988839417001 | 0.033177180256753508 | 0.025207454531073845 |
| ctx-rh-middletemporal | NFL | amyloid | 1.2901364874450798 | 0.91054492979695645 | 1.8077372726953895 | 1.0304300096054499 | 1.0920154691511359 | 1.0597667565691986 | 0.015130566717253423 | -0.0028156979947765288 | 0.044836237299289809 |
| ctx-rh-middletemporal | NFL | tau | 0.91106148591518443 | 0.56109550228395544 | 1.3004483601026378 | 1.0982400109961621 | 1.1219807243086657 | 1.0216170537175835 | -0.0097907086712252442 | 0.0055303054219781028 | 0.033729937801107529 |
| ctx-rh-paracentral | GFAP | amyloid | 13.918998365476114 | 11.979156052682368 | 14.691933710859644 | 2.706663873081828 | 3.1169341348928881 | 1.1515778393805225 | 0.0046497461093086244 | 0.0036393924955823364 | 0.053536460371516992 |
| ctx-rh-paracentral | GFAP | tau | 0.5330049499513736 | -0.21355732085400331 | 1.6094980492041633 | 2.9591469222809734 | 2.595730517299776 | 0.8771887930792337 | 0.0030656347545354617 | 0.0431874646613081 | 0.029709440694361326 |
| ctx-rh-paracentral | NFL | amyloid | 1.2798723809812402 | 0.97367143290955283 | 1.9557348199563591 | 0.91347299334992083 | 1.0398793650332849 | 1.1383799768614966 | 0.0081294516220084875 | 0.00011413340406564157 | 0.058545368475263676 |
| ctx-rh-paracentral | NFL | tau | 1.5236863291918441 | 1.3005591878678291 | 1.8814371683787452 | 0.99868359116953664 | 0.85367209132848998 | 0.85479735411370195 | 0.0053598473641066728 | 0.0099472081902061936 | 0.030989523155470069 |
| ctx-rh-parahippocampal | GFAP | amyloid | 10.607649300047992 | 9.4655147692514312 | 11.350915234044839 | 2.9867654561119088 | 3.105404950045346 | 1.0397217309751128 | 0.0095343859882487132 | 0.000594244337735169 | 0.03152103634592314 |
| ctx-rh-parahippocampal | GFAP | tau | 4.6705337711982118 | 3.791844701096688 | 5.6186049231480988 | 3.2866026757906597 | 2.8893781944950305 | 0.87913827119365173 | -0.0039927030278505537 | 0.048857508655914296 | 0.026165205965965693 |
| ctx-rh-parahippocampal | NFL | amyloid | 0.88936724418635671 | 0.5193402433339156 | 1.287389462985093 | 1.0054526210451469 | 1.0012445277300981 | 0.99581472739046162 | 0.015170919553133029 | -0.0028561955856599734 | 0.034477959000428916 |
| ctx-rh-parahippocampal | NFL | tau | 1.1437828657157529 | 0.83961492973042295 | 1.6202608129449467 | 1.1063886077648195 | 1.1407094749756364 | 1.0310206259988102 | -0.0063531072173634018 | 0.006970007965492556 | 0.041274045400675585 |
| ctx-rh-parsopercularis | GFAP | amyloid | 14.652106317204829 | 12.990183682838689 | 15.445121935469739 | 2.6906165579768846 | 2.9938529448222049 | 1.1127014497648555 | 0.0082972959468623712 | 0.00023694625861784061 | 0.045866333912023584 |
| ctx-rh-parsopercularis | GFAP | tau | 3.2875981906112597 | 2.7395176915362995 | 4.011630564333136 | 2.9396606862169961 | 2.4498526670303833 | 0.8333794027715018 | -0.0039645430640857003 | 0.037369100621112969 | 0.019982103817310651 |
| ctx-rh-parsopercularis | NFL | amyloid | 1.3335888685128969 | 1.0101598636216609 | 2.077935530189214 | 0.93946507375559363 | 1.1338602438842509 | 1.2069211251798277 | 0.012578496099743243 | -0.00062734094778884046 | 0.064477691121960223 |
| ctx-rh-parsopercularis | NFL | tau | 1.186066917870102 | 0.72266972616441061 | 1.5261244733755228 | 1.0264221913024425 | 1.0515769360282106 | 1.0245072105210906 | -0.0060101495460966395 | 0.0041980157313813412 | 0.040140948474591667 |
| ctx-rh-parsorbitalis | GFAP | amyloid | 15.020579868200272 | 13.385340415008304 | 15.64012206547466 | 2.6800660169886834 | 2.9679729652171924 | 1.1074253195270169 | 0.0087783648337669985 | 0.0014145419939895155 | 0.045129921956218906 |
| ctx-rh-parsorbitalis | GFAP | tau | 1.0467850925310829 | 0.4410208611831869 | 1.9545542782634029 | 2.9711079840018799 | 2.6076827823911457 | 0.877680244687295 | -0.0011894567227577989 | 0.047713747382214171 | 0.025052937920738039 |
| ctx-rh-parsorbitalis | NFL | amyloid | 1.5963644238841326 | 1.3035876643858144 | 2.3745561920015268 | 0.92559869728378485 | 1.1324066579529088 | 1.2234315597850474 | 0.012780306510362811 | 0.00041663538523695301 | 0.06740946260889491 |
| ctx-rh-parsorbitalis | NFL | tau | 0.69616021246497783 | 0.32112673029874728 | 1.0540094496220562 | 1.0261141561622975 | 1.0193509964960974 | 0.99340895978718924 | -0.0017317144804897572 | 0.0032454439110496144 | 0.032486601026797852 |
| ctx-rh-parstriangularis | GFAP | amyloid | 15.491282153878927 | 13.9755008280633 | 16.255273627490148 | 2.6645861006774663 | 2.9225587525031331 | 1.0968152809023801 | 0.0088031892644484851 | 0.0026335026293668007 | 0.041833073928850883 |
| ctx-rh-parstriangularis | GFAP | tau | 1.3189728070413451 | 0.72560253131468722 | 2.0650588734105919 | 2.9631441019138962 | 2.5756069242646742 | 0.86921419805438704 | -0.00041842181578375629 | 0.050355479145598105 | 0.020590749496742791 |
| ctx-rh-parstriangularis | NFL | amyloid | 1.5770243195216691 | 1.2841103922680941 | 2.2328866414272062 | 0.92986248481974321 | 1.0511822691967467 | 1.1304706731990826 | 0.012455129936617721 | 0.00011171395576531854 | 0.056812894297289446 |
| ctx-rh-parstriangularis | NFL | tau | 0.5301486652515297 | 0.1336652986200127 | 0.93372526762266961 | 1.0340504804044752 | 1.0359467634490691 | 1.0018338399145197 | -0.00059200114042191974 | 0.0023204516145767956 | 0.034959097489782501 |
| ctx-rh-pericalcarine | GFAP | amyloid | 12.744692287219324 | 10.499802829081323 | 13.728606872171474 | 2.7947571425184958 | 3.4722801785407893 | 1.2424264440421982 | 0.0069043884840687608 | 0.0077093145302609594 | 0.061955260343277148 |
| ctx-rh-pericalcarine | GFAP | tau | 0.19946990249143939 | -0.50691300059785172 | 1.6606556016489129 | 3.1093586434976963 | 3.037437882813673 | 0.97686958343180375 | 0.0019676238267063305 | 0.050505903455223079 | 0.040326324342162614 |
| ctx-rh-pericalcarine | NFL | amyloid | 1.3112920305159057 | 0.9612973846056222 | 2.0275068735847883 | 0.9317326467799224 | 1.1072710435935884 | 1.1883999636809213 | 0.011296220054057442 | -0.0010881337958958835 | 0.062040822920275532 |
| ctx-rh-pericalcarine | NFL | tau | 1.0785522467651489 | 0.77571391308485882 | 1.3990536543403571 | 1.0366163537499449 | 0.95505249771660239 | 0.92131722045645292 | 0.0032192151095446191 | 0.01009509410096115 | 0.027762858122112623 |
| ctx-rh-postcentral | GFAP | amyloid | 14.571716964814666 | 12.753020849848481 | 15.282363810297737 | 2.7092687255786023 | 3.0470143582647653 | 1.1246630241944835 | 0.0052872015905219292 | 0.0053187710320889538 | 0.050193024373456706 |
| ctx-rh-postcentral | GFAP | tau | 0.63731180709484114 | -0.1689246258691256 | 1.6825123645071951 | 3.01678811336454 | 2.6516304820925796 | 0.8789581443740474 | 0.0028915222291141496 | 0.050896794821254712 | 0.028845817958061806 |
| ctx-rh-postcentral | NFL | amyloid | 1.4245555966337615 | 1.1072958314417922 | 2.1493155716542258 | 0.92287170100552185 | 1.0899685999021684 | 1.1810618948599083 | 0.0088094373872062114 | 0.00037565159823448524 | 0.062781029610166045 |
| ctx-rh-postcentral | NFL | tau | 1.3391169592275023 | 1.0931253426436889 | 1.6390771390008194 | 1.0276235618374796 | 0.88545900681876799 | 0.86165697216546 | 0.004817800795936876 | 0.010915519822730022 | 0.025983511199949499 |
| ctx-rh-posteriorcingulate | GFAP | amyloid | 13.51218537354063 | 11.899857082390293 | 14.336977738959847 | 2.7038406293033153 | 3.064529860069849 | 1.1333988500866157 | 0.0060781976087143736 | 0.0043539516932159777 | 0.044497611530460314 |
| ctx-rh-posteriorcingulate | GFAP | tau | 4.2091433018829321 | 2.9721534115366617 | 4.9203292239915282 | 2.9297919159205845 | 2.7930377691334103 | 0.95332291483089715 | -0.0029425537575653222 | 0.042437624067439526 | 0.034138888407437049 |
| ctx-rh-posteriorcingulate | NFL | amyloid | 1.1573390939628838 | 0.83136996126199958 | 1.8590968551287912 | 0.9313948515441588 | 1.0836661802249281 | 1.1634874064724738 | 0.010292006650374084 | -0.00078425589634310345 | 0.060788504196408841 |
| ctx-rh-posteriorcingulate | NFL | tau | 1.6151867847409225 | 1.3525205828764659 | 1.8949069721090075 | 1.0092285310792313 | 0.87006917551634688 | 0.86211313763189734 | -0.004982526859364551 | 0.0075403203618591508 | 0.024230258252356009 |
| ctx-rh-precentral | GFAP | amyloid | 13.724774530305568 | 12.080669223485184 | 14.449864430174486 | 2.7623385286668634 | 3.0386078258429277 | 1.1000128312692343 | 0.00622941285938855 | 0.0063403314056345991 | 0.045374604948391496 |
| ctx-rh-precentral | GFAP | tau | 2.0363872961915401 | 1.0856213494000353 | 2.7844797338656839 | 3.0647486732465072 | 2.5383886554692903 | 0.82825344786930255 | 0.0019244429670140244 | 0.048480242682139026 | 0.026239577875628736 |
| ctx-rh-precentral | NFL | amyloid | 1.3772851847311576 | 1.0562210672677459 | 2.1402267802754089 | 0.9384492530498284 | 1.1246120452377184 | 1.1983727852975397 | 0.0099757990924380542 | 0.00011483198366665301 | 0.066088443831819652 |
| ctx-rh-precentral | NFL | tau | 1.2195584681098881 | 0.96459509709483959 | 1.5185098316102257 | 1.0411870497935247 | 0.92909890484642921 | 0.89234581339700347 | 0.0030818083240143073 | 0.0084173253596966334 | 0.025896124304304002 |
| ctx-rh-precuneus | GFAP | amyloid | 13.279666031566109 | 11.629856076357784 | 14.17673372328097 | 2.6584954189730725 | 3.0950494587564279 | 1.1642109430273113 | 0.007649524247986113 | 0.0094757112781079858 | 0.045532043870277143 |
| ctx-rh-precuneus | GFAP | tau | 5.0424834704334751 | 4.1441621231509655 | 6.1474644761312387 | 2.765506996210318 | 2.7005971140672167 | 0.9765287586572553 | -0.00167011320486703 | 0.02880015903977615 | 0.030495660102196766 |
| ctx-rh-precuneus | NFL | amyloid | 1.2257070878765739 | 0.89914448665542024 | 1.8546440215652329 | 0.91844974366945364 | 1.0169553083765448 | 1.1072519921596744 | 0.011802503986077737 | 7.9883358915437959e-05 | 0.054480530958845835 |
| ctx-rh-precuneus | NFL | tau | 1.564631071172373 | 1.2982056552241876 | 1.9684950917434088 | 0.95541981139339116 | 0.82212907116068512 | 0.86048987194611981 | -0.0025768292404372496 | 0.004091253555133385 | 0.034983994574527909 |
| ctx-rh-rostralanteriorcingulate | GFAP | amyloid | 15.390826369708224 | 14.076128796327952 | 15.959774893222589 | 2.672937080548444 | 2.6336549632228725 | 0.98530376281153931 | 0.0052386709336141755 | 0.0022651623793615685 | 0.036283492773407776 |
| ctx-rh-rostralanteriorcingulate | GFAP | tau | -1.7081177084131074 | -2.437656688193675 | -0.97808935942295816 | 3.0034050858718055 | 2.4893775908749123 | 0.82885175981924353 | -0.0012014950711657414 | 0.046255929961681784 | 0.020147582882398256 |
| ctx-rh-rostralanteriorcingulate | NFL | amyloid | 1.8258911912614333 | 1.5561677027647378 | 2.5538026349648471 | 0.91478202360408345 | 1.0791104351607477 | 1.1796366864635561 | 0.0090114571306722253 | -0.0020560088847064307 | 0.063054019918018206 |
| ctx-rh-rostralanteriorcingulate | NFL | tau | 0.59465675543633856 | 0.35178792058379971 | 0.93722813230046065 | 1.0278809038007253 | 0.91811608210698803 | 0.89321251004093238 | -0.0020667878291517447 | 0.0082139768820186955 | 0.029674629526685065 |
| ctx-rh-rostralmiddlefrontal | GFAP | amyloid | 14.454160104815143 | 13.171498030062068 | 15.181996456159499 | 2.6182995189971283 | 2.7670143635436064 | 1.0567982553055808 | 0.0084588748178672409 | 0.0047483873161890703 | 0.035399365650586809 |
| ctx-rh-rostralmiddlefrontal | GFAP | tau | 4.915920665668958 | 4.124267185366346 | 5.8649407030441187 | 2.8935280531063756 | 2.6854619258412051 | 0.92809258336313727 | -0.0033266867462394601 | 0.044256926906047718 | 0.02619139364453742 |
| ctx-rh-rostralmiddlefrontal | NFL | amyloid | 1.3669674163766876 | 1.0633669776988393 | 2.1102094733364778 | 0.92049047735795397 | 1.1033810555451515 | 1.1986881805797067 | 0.012646486527924239 | -0.00026688569565530812 | 0.064382006724634275 |
| ctx-rh-rostralmiddlefrontal | NFL | tau | 1.2214212914069282 | 0.86363392657365468 | 1.5469275894308483 | 1.0172499362764615 | 0.95120247920198397 | 0.93507253751596442 | -0.0049735810051329708 | 0.0056972951608708442 | 0.030992687123908551 |
| ctx-rh-superiorfrontal | GFAP | amyloid | 14.729919867765036 | 13.206037858421032 | 15.524480275763642 | 2.6439907212263178 | 2.8131128448579283 | 1.0639647190415136 | 0.0072084526979363942 | 0.0038844084273285981 | 0.042056639483555439 |
| ctx-rh-superiorfrontal | GFAP | tau | 3.4696064144190188 | 2.8141600169973362 | 4.1403299669122848 | 2.954727063564075 | 2.2923282792908872 | 0.77581726838952636 | -0.0026923478309878145 | 0.047004948158563424 | 0.018510867946057011 |
| ctx-rh-superiorfrontal | NFL | amyloid | 1.4152359321478289 | 1.1161661732352799 | 2.1446679208556501 | 0.92014563987459042 | 1.0939433311864826 | 1.1888806334349198 | 0.011238374040855058 | -0.00046884864818698695 | 0.063185734394859444 |
| ctx-rh-superiorfrontal | NFL | tau | 1.4000080330589155 | 1.1296243692134649 | 1.7201667148089472 | 1.028286220042758 | 0.93084315573100795 | 0.90523741112887979 | -0.0041975182803637321 | 0.0077984533344116289 | 0.027733170113778603 |
| ctx-rh-superiorparietal | GFAP | amyloid | 13.004769512771521 | 11.623054798772836 | 13.838902109341715 | 2.7471586557476662 | 2.9693161782435018 | 1.0808681078652056 | 0.0062350160897944196 | 0.0098039522850696548 | 0.038133055734926452 |
| ctx-rh-superiorparietal | GFAP | tau | 5.2095666919560637 | 4.2310433479220695 | 5.9866817728916031 | 2.872218998057555 | 2.4722855150318814 | 0.86075801208189784 | -0.0041942457297188826 | 0.031774553395925359 | 0.02700563642981545 |
| ctx-rh-superiorparietal | NFL | amyloid | 1.0438551789824355 | 0.66610529106518013 | 1.5935850024972509 | 0.95017624077149165 | 0.99965372829135579 | 1.0520719056074177 | 0.011109746543523764 | 0.00041243669327656655 | 0.047619357466174204 |
| ctx-rh-superiorparietal | NFL | tau | 1.5267582173476399 | 1.0424632909740832 | 1.8161571234615164 | 0.99343161143491843 | 0.94326475038781621 | 0.94950144482050358 | -0.0074734381318918679 | 0.0040767622913292249 | 0.041951177162967576 |
| ctx-rh-superiortemporal | GFAP | amyloid | 14.249112590637203 | 12.531857345045829 | 14.890079580101997 | 2.8342063728496338 | 3.1343644716356769 | 1.1059055196761312 | 0.0080190389223998588 | 0.0021525948859477005 | 0.047393423061783388 |
| ctx-rh-superiortemporal | GFAP | tau | 0.67954354122233251 | -0.098722587227618994 | 1.4920541845939628 | 3.0592851467610696 | 2.6872375666591375 | 0.87838741331587644 | 0.0005537049076549419 | 0.040902592105003591 | 0.022423958676132925 |
| ctx-rh-superiortemporal | NFL | amyloid | 1.2159085608012234 | 0.87953236253902434 | 1.8525076288834224 | 0.96918452205279937 | 1.100768392769498 | 1.1357676146519498 | 0.011831815064280429 | -0.00046248282633078874 | 0.055144249573031608 |
| ctx-rh-superiortemporal | NFL | tau | 0.85406142485004866 | 0.51238832921661404 | 1.3783547267252056 | 1.0461524048461242 | 1.0867912809423808 | 1.0388460380227622 | 0.00081697247400255412 | 0.003542228766948062 | 0.045415964517779212 |
| ctx-rh-supramarginal | GFAP | amyloid | 12.599628426520979 | 11.205952903704471 | 13.287967204928565 | 2.7938415350989878 | 3.0516143296859535 | 1.0922646439851975 | 0.0068263208595521598 | 0.0047526713697686298 | 0.038463154404835602 |
| ctx-rh-supramarginal | GFAP | tau | 5.2505760116423135 | 4.4338630633942344 | 6.1723786589548659 | 2.9941299920273372 | 2.7477701916446811 | 0.91771906996735142 | -0.00073249160126365371 | 0.040114288456538187 | 0.025440238401199928 |
| ctx-rh-supramarginal | NFL | amyloid | 1.1735726258026655 | 0.82444297456554949 | 1.7603646061904796 | 0.96434065588761442 | 1.0511214755195335 | 1.0899897967612315 | 0.010820552359560474 | -0.00080649343285842286 | 0.050829800162040036 |
| ctx-rh-supramarginal | NFL | tau | 1.2858411922129682 | 0.956379879072496 | 1.6973568372818946 | 1.0334735324285738 | 0.92903654359756038 | 0.89894565699656048 | -0.0011610886577828356 | 0.0054509949731370395 | 0.035646802787901416 |
| ctx-rh-temporalpole | GFAP | amyloid | 14.662256501170194 | 13.255772927878803 | 15.42287121180804 | 2.8752340311182047 | 2.996626128092398 | 1.0422199012881685 | 0.0091225181348199135 | -0.0039931255721225092 | 0.038816635552330218 |
| ctx-rh-temporalpole | GFAP | tau | 1.1658478603292188 | 0.57524454863041063 | 2.077875657595444 | 3.1808744828520061 | 2.8321300368776692 | 0.89036208506358638 | -0.0066760525867309963 | 0.053407261230887917 | 0.025170468601514999 |
| ctx-rh-temporalpole | NFL | amyloid | 0.93647197282875161 | 0.60179136515171705 | 1.615287306649789 | 0.99333021345828276 | 1.1313910688438911 | 1.138987874842696 | 0.013655744277361256 | -0.0013479892231038698 | 0.058801157681548255 |
| ctx-rh-temporalpole | NFL | tau | 1.1582720611742527 | 0.8633485708036519 | 1.5287842038473232 | 1.0989222772264446 | 1.0212246597506689 | 0.9292965307138229 | -0.0099935637900946533 | 0.0068739461261785161 | 0.032094948123242178 |
| ctx-rh-transversetemporal | GFAP | amyloid | 13.736613065088823 | 12.213930238566819 | 14.460429245641224 | 2.7287761233399972 | 2.8833440924821394 | 1.0566436974510582 | 0.0042391925001283018 | 0.0019240481595476715 | 0.042023544008111514 |
| ctx-rh-transversetemporal | GFAP | tau | -0.97512619252648836 | -1.6441487822291978 | 0.22510080496996041 | 3.0255724243827191 | 2.8134600723016541 | 0.92989348052894805 | 0.0041751280216477341 | 0.046683005722886542 | 0.033124292971913077 |
| ctx-rh-transversetemporal | NFL | amyloid | 1.2269771856581011 | 0.87134850180903678 | 1.9562201691798431 | 0.92090960606530081 | 1.113497474047495 | 1.2091278739126736 | 0.0075319327205939333 | -0.0015749109254967794 | 0.06316936216047471 |
| ctx-rh-transversetemporal | NFL | tau | 0.88414507681058574 | 0.61883126961833523 | 1.3101393832991932 | 1.0210726653712974 | 1.0133477255935197 | 0.99243448577191262 | 0.0074181069526723133 | 0.0069638855843502925 | 0.036900990798599584 |

## T5 — All 136 model diagnostics

Source: tables/T5_all_model_diagnostics.csv

| region | outcome | n | df_resid | R2 | PET_correlation | VIF_amyloid | VIF_tau | max_leverage | leverage_flag_count | cooks_flag_count | max_abs_studentized_residual | residual_skewness |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ctx-lh-bankssts | GFAP | 165 | 160 | 0.24970631212241545 | 0.47161730375444783 | 1.3124125879330282 | 1.3565874586083031 | 0.19413068493579783 | 13 | 11 | 4.7171247776892642 | 0.46711717035445749 |
| ctx-lh-bankssts | NFL | 165 | 160 | 0.15209371045349285 | 0.47161730375444783 | 1.3124125879330282 | 1.3565874586083031 | 0.19413068493579783 | 13 | 7 | 5.0795799858166362 | 1.2626547206815986 |
| ctx-lh-caudalanteriorcingulate | GFAP | 165 | 160 | 0.27505423469312318 | 0.3794575028395476 | 1.1728734812453994 | 1.4203945815909365 | 0.093725492553407092 | 10 | 6 | 4.5717672584702749 | 0.38063432110712603 |
| ctx-lh-caudalanteriorcingulate | NFL | 165 | 160 | 0.15448272397431273 | 0.3794575028395476 | 1.1728734812453994 | 1.4203945815909365 | 0.093725492553407092 | 10 | 7 | 5.1432241191911325 | 1.2814984285974793 |
| ctx-lh-caudalmiddlefrontal | GFAP | 165 | 160 | 0.28562341600432439 | 0.42027936333081267 | 1.2266807539553468 | 1.3842783034604831 | 0.13355396518913099 | 8 | 10 | 4.6466836709468993 | 0.41693279636135228 |
| ctx-lh-caudalmiddlefrontal | NFL | 165 | 160 | 0.16728475472587601 | 0.42027936333081267 | 1.2266807539553468 | 1.3842783034604831 | 0.13355396518913099 | 8 | 6 | 5.1624742197348255 | 1.3297357457969863 |
| ctx-lh-cuneus | GFAP | 165 | 160 | 0.21797344011747211 | 0.41601450849422505 | 1.2203162965036252 | 1.3643418069315361 | 0.13931220072695724 | 8 | 9 | 4.7029425981069481 | 0.52282559566701614 |
| ctx-lh-cuneus | NFL | 165 | 160 | 0.16027759188318569 | 0.41601450849422505 | 1.2203162965036252 | 1.3643418069315361 | 0.13931220072695724 | 8 | 6 | 5.2244427047029802 | 1.2871773033429175 |
| ctx-lh-entorhinal | GFAP | 165 | 160 | 0.23026141310195258 | 0.52254774052043584 | 1.3773973707534919 | 1.6137806694152468 | 0.089316113020374871 | 9 | 8 | 4.7420804203198594 | 0.57068493265314979 |
| ctx-lh-entorhinal | NFL | 165 | 160 | 0.145020055375774 | 0.52254774052043584 | 1.3773973707534919 | 1.6137806694152468 | 0.089316113020374871 | 9 | 6 | 5.0836690334582739 | 1.2773430026575083 |
| ctx-lh-frontalpole | GFAP | 165 | 160 | 0.28796086927427067 | 0.36021333298361169 | 1.1582235424216019 | 1.3874570959015111 | 0.15837787831901609 | 10 | 6 | 4.5551582986730512 | 0.38138668387860236 |
| ctx-lh-frontalpole | NFL | 165 | 160 | 0.15463374169587041 | 0.36021333298361169 | 1.1582235424216019 | 1.3874570959015111 | 0.15837787831901609 | 10 | 6 | 4.993129752086169 | 1.2709713107030993 |
| ctx-lh-fusiform | GFAP | 165 | 160 | 0.25711789011334452 | 0.55202408381592161 | 1.4385253722297093 | 1.5912315289867898 | 0.16405362708974755 | 12 | 10 | 4.6428825698775222 | 0.44360808020561276 |
| ctx-lh-fusiform | NFL | 165 | 160 | 0.16276208499678735 | 0.55202408381592161 | 1.4385253722297093 | 1.5912315289867898 | 0.16405362708974755 | 12 | 6 | 5.2111849282289109 | 1.2615528150469764 |
| ctx-lh-inferiorparietal | GFAP | 165 | 160 | 0.26740837942623641 | 0.49801637120575687 | 1.3530527421342835 | 1.4261135128174325 | 0.17319919510744916 | 11 | 11 | 4.6023057761595716 | 0.38943438306208755 |
| ctx-lh-inferiorparietal | NFL | 165 | 160 | 0.15937083804928298 | 0.49801637120575687 | 1.3530527421342835 | 1.4261135128174325 | 0.17319919510744916 | 11 | 6 | 5.1087193527924004 | 1.2455313007390181 |
| ctx-lh-inferiortemporal | GFAP | 165 | 160 | 0.27132912546876953 | 0.60598028564523454 | 1.5859633247843323 | 1.7055396273449048 | 0.12539168277551513 | 12 | 10 | 4.5198025943475786 | 0.36775953109517268 |
| ctx-lh-inferiortemporal | NFL | 165 | 160 | 0.1640033836007011 | 0.60598028564523454 | 1.5859633247843323 | 1.7055396273449048 | 0.12539168277551513 | 12 | 5 | 5.1400281041072251 | 1.2584081317180231 |
| ctx-lh-insula | GFAP | 165 | 160 | 0.24922751487461692 | 0.44743668418587068 | 1.2515730091910289 | 1.5571351222014631 | 0.09020544922110213 | 13 | 9 | 4.7174748226572172 | 0.52252849234155907 |
| ctx-lh-insula | NFL | 165 | 160 | 0.15316154402045457 | 0.44743668418587068 | 1.2515730091910289 | 1.5571351222014631 | 0.09020544922110213 | 13 | 7 | 5.092857868049145 | 1.2747715244550708 |
| ctx-lh-isthmuscingulate | GFAP | 165 | 160 | 0.25349433918080377 | 0.44335004249778792 | 1.2599320925229234 | 1.383099892812127 | 0.20869351184402057 | 12 | 9 | 4.6583425134662022 | 0.43619559885717035 |
| ctx-lh-isthmuscingulate | NFL | 165 | 160 | 0.15966772066496482 | 0.44335004249778792 | 1.2599320925229234 | 1.383099892812127 | 0.20869351184402057 | 12 | 7 | 5.1277792847180352 | 1.2549800780442477 |
| ctx-lh-lateraloccipital | GFAP | 165 | 160 | 0.23088658803591044 | 0.4848868850701783 | 1.3179486193071435 | 1.482113075710797 | 0.12567907116840252 | 9 | 9 | 4.7037225144847756 | 0.52577532871743904 |
| ctx-lh-lateraloccipital | NFL | 165 | 160 | 0.1596299362659942 | 0.4848868850701783 | 1.3179486193071435 | 1.482113075710797 | 0.12567907116840252 | 9 | 4 | 5.227370324144708 | 1.2556759887868458 |
| ctx-lh-lateralorbitofrontal | GFAP | 165 | 160 | 0.27596540241729961 | 0.44916580228634018 | 1.2586278889528579 | 1.5504001365744129 | 0.089777394553514869 | 10 | 9 | 4.6570894099489308 | 0.45558529844124807 |
| ctx-lh-lateralorbitofrontal | NFL | 165 | 160 | 0.16037242154385578 | 0.44916580228634018 | 1.2586278889528579 | 1.5504001365744129 | 0.089777394553514869 | 10 | 6 | 5.1666441258405991 | 1.3204975042609091 |
| ctx-lh-lingual | GFAP | 165 | 160 | 0.21213782377912849 | 0.48129606776150713 | 1.3060952409527096 | 1.4999797799976875 | 0.12602632260106267 | 8 | 9 | 4.6917166706343512 | 0.52529971543148823 |
| ctx-lh-lingual | NFL | 165 | 160 | 0.15981170341580031 | 0.48129606776150713 | 1.3060952409527096 | 1.4999797799976875 | 0.12602632260106267 | 8 | 6 | 5.2851149005469482 | 1.2866804295172636 |
| ctx-lh-medialorbitofrontal | GFAP | 165 | 160 | 0.28483804998870621 | 0.39605659894878231 | 1.1906143151375053 | 1.445126284714862 | 0.097045343021598396 | 11 | 10 | 4.5501810341195128 | 0.37422261375048044 |
| ctx-lh-medialorbitofrontal | NFL | 165 | 160 | 0.15846922806386154 | 0.39605659894878231 | 1.1906143151375053 | 1.445126284714862 | 0.097045343021598396 | 11 | 5 | 5.1518206932290207 | 1.3279687961602127 |
| ctx-lh-middletemporal | GFAP | 165 | 160 | 0.26553384389434453 | 0.58838348049140288 | 1.5364961105387469 | 1.6945321528192043 | 0.13066405536140938 | 11 | 11 | 4.4783802035798832 | 0.35243246476131984 |
| ctx-lh-middletemporal | NFL | 165 | 160 | 0.15948217561531675 | 0.58838348049140288 | 1.5364961105387469 | 1.6945321528192043 | 0.13066405536140938 | 11 | 7 | 5.1105163593882956 | 1.2747210551428656 |
| ctx-lh-paracentral | GFAP | 165 | 160 | 0.26692541877902409 | 0.36931729696661492 | 1.1658443895086998 | 1.3949220838425762 | 0.10196132114564405 | 9 | 6 | 4.5950501569400277 | 0.38872286811326195 |
| ctx-lh-paracentral | NFL | 165 | 160 | 0.16539772042261491 | 0.36931729696661492 | 1.1658443895086998 | 1.3949220838425762 | 0.10196132114564405 | 9 | 6 | 5.085543470830598 | 1.2576984840771259 |
| ctx-lh-parahippocampal | GFAP | 165 | 160 | 0.24295409468554008 | 0.5463253523953584 | 1.4267837176136267 | 1.6623473565340297 | 0.083639598581633959 | 13 | 10 | 4.7368693810166826 | 0.51334571098051318 |
| ctx-lh-parahippocampal | NFL | 165 | 160 | 0.15449859444047331 | 0.5463253523953584 | 1.4267837176136267 | 1.6623473565340297 | 0.083639598581633959 | 13 | 5 | 5.0856877205702062 | 1.2536324435334782 |
| ctx-lh-parsopercularis | GFAP | 165 | 160 | 0.27820935132472935 | 0.42486326697429372 | 1.2254311302199352 | 1.502622490804624 | 0.11690896282324881 | 11 | 10 | 4.5901845585088212 | 0.40725602011005607 |
| ctx-lh-parsopercularis | NFL | 165 | 160 | 0.16452342805346909 | 0.42486326697429372 | 1.2254311302199352 | 1.502622490804624 | 0.11690896282324881 | 11 | 6 | 5.0430261343285414 | 1.2605720809233631 |
| ctx-lh-parsorbitalis | GFAP | 165 | 160 | 0.26373343080796152 | 0.42652879685684697 | 1.22580742266107 | 1.5656600688647107 | 0.11797735449252314 | 10 | 9 | 4.6623617539420259 | 0.45643106132670413 |
| ctx-lh-parsorbitalis | NFL | 165 | 160 | 0.16228806854092848 | 0.42652879685684697 | 1.22580742266107 | 1.5656600688647107 | 0.11797735449252314 | 10 | 5 | 5.1466446636807595 | 1.3131475675734376 |
| ctx-lh-parstriangularis | GFAP | 165 | 160 | 0.27616880448574854 | 0.41492668283158407 | 1.210585963967705 | 1.5338513330159622 | 0.10740245247245644 | 13 | 8 | 4.6573621789446733 | 0.45227146300950921 |
| ctx-lh-parstriangularis | NFL | 165 | 160 | 0.16034447983492928 | 0.41492668283158407 | 1.210585963967705 | 1.5338513330159622 | 0.10740245247245644 | 13 | 6 | 5.1110949503492256 | 1.2873839138181888 |
| ctx-lh-pericalcarine | GFAP | 165 | 160 | 0.21684413965129945 | 0.43740525639870748 | 1.2436061632942772 | 1.4679237302355803 | 0.10169938486609731 | 8 | 7 | 4.6187377164145786 | 0.50059642688286377 |
| ctx-lh-pericalcarine | NFL | 165 | 160 | 0.15441656740539866 | 0.43740525639870748 | 1.2436061632942772 | 1.4679237302355803 | 0.10169938486609731 | 8 | 6 | 5.2119649968941868 | 1.2986062118296198 |
| ctx-lh-postcentral | GFAP | 165 | 160 | 0.24359173641106957 | 0.40554231576724875 | 1.2009041913529233 | 1.4757843707562968 | 0.089339968094505604 | 10 | 7 | 4.6247117267466082 | 0.47593351790713079 |
| ctx-lh-postcentral | NFL | 165 | 160 | 0.15914932363308087 | 0.40554231576724875 | 1.2009041913529233 | 1.4757843707562968 | 0.089339968094505604 | 10 | 7 | 5.103909928850288 | 1.2692716505205062 |
| ctx-lh-posteriorcingulate | GFAP | 165 | 160 | 0.29606346951388396 | 0.42044231673392329 | 1.2247088959129664 | 1.4025934997808887 | 0.1291819696983241 | 12 | 11 | 4.5944978024950744 | 0.35342890732606003 |
| ctx-lh-posteriorcingulate | NFL | 165 | 160 | 0.17432459558412594 | 0.42044231673392329 | 1.2247088959129664 | 1.4025934997808887 | 0.1291819696983241 | 12 | 6 | 5.0718409194433827 | 1.247268095469013 |
| ctx-lh-precentral | GFAP | 165 | 160 | 0.24500688800978776 | 0.42209534623104777 | 1.2212878690265041 | 1.4942778321872416 | 0.10507311228486914 | 10 | 6 | 4.6278620692539381 | 0.49021358591019032 |
| ctx-lh-precentral | NFL | 165 | 160 | 0.1551835140933997 | 0.42209534623104777 | 1.2212878690265041 | 1.4942778321872416 | 0.10507311228486914 | 10 | 5 | 5.1036625502176944 | 1.2719194863026957 |
| ctx-lh-precuneus | GFAP | 165 | 160 | 0.28046470593612993 | 0.3726101732597239 | 1.1867828315411275 | 1.243289725091367 | 0.23552312027795225 | 13 | 11 | 4.5745281074356257 | 0.32722756025998173 |
| ctx-lh-precuneus | NFL | 165 | 160 | 0.16421197559701795 | 0.3726101732597239 | 1.1867828315411275 | 1.243289725091367 | 0.23552312027795225 | 13 | 7 | 5.1377282606786538 | 1.2804780980125163 |
| ctx-lh-rostralanteriorcingulate | GFAP | 165 | 160 | 0.28840067973550532 | 0.3786351703159514 | 1.1706319996863819 | 1.4752658387296766 | 0.096736428107554215 | 10 | 10 | 4.5166240281303294 | 0.34504295355589876 |
| ctx-lh-rostralanteriorcingulate | NFL | 165 | 160 | 0.1595800131494457 | 0.3786351703159514 | 1.1706319996863819 | 1.4752658387296766 | 0.096736428107554215 | 10 | 5 | 5.1373425637629886 | 1.3268080312483241 |
| ctx-lh-rostralmiddlefrontal | GFAP | 165 | 160 | 0.29942442915974699 | 0.39537311357897797 | 1.1923918615158779 | 1.4463843945845978 | 0.16481505779206651 | 11 | 9 | 4.5815072392564247 | 0.41260090980594039 |
| ctx-lh-rostralmiddlefrontal | NFL | 165 | 160 | 0.16598700701297664 | 0.39537311357897797 | 1.1923918615158779 | 1.4463843945845978 | 0.16481505779206651 | 11 | 7 | 5.0794270619475537 | 1.2893410370832517 |
| ctx-lh-superiorfrontal | GFAP | 165 | 160 | 0.30104819048798503 | 0.41019484493289315 | 1.2070235216211476 | 1.4711927513004701 | 0.1173992854426177 | 11 | 9 | 4.5162190470267962 | 0.35477228527624094 |
| ctx-lh-superiorfrontal | NFL | 165 | 160 | 0.16856901782212819 | 0.41019484493289315 | 1.2070235216211476 | 1.4711927513004701 | 0.1173992854426177 | 11 | 5 | 5.1600581881260172 | 1.3306560682333399 |
| ctx-lh-superiorparietal | GFAP | 165 | 160 | 0.27930553478323228 | 0.44444247166617445 | 1.2685353818675094 | 1.3531773250845183 | 0.16606698959743138 | 12 | 8 | 4.6809849411072602 | 0.4327490838730112 |
| ctx-lh-superiorparietal | NFL | 165 | 160 | 0.16410233817022946 | 0.44444247166617445 | 1.2685353818675094 | 1.3531773250845183 | 0.16606698959743138 | 12 | 5 | 5.1664187152549905 | 1.2484268485255179 |
| ctx-lh-superiortemporal | GFAP | 165 | 160 | 0.25628470288040661 | 0.49603762430077514 | 1.3301718526401951 | 1.5366679486886174 | 0.13331039123180766 | 11 | 10 | 4.5185660866902841 | 0.38967978589326258 |
| ctx-lh-superiortemporal | NFL | 165 | 160 | 0.15248847423780409 | 0.49603762430077514 | 1.3301718526401951 | 1.5366679486886174 | 0.13331039123180766 | 11 | 8 | 5.0789482027276955 | 1.2722149435289656 |
| ctx-lh-supramarginal | GFAP | 165 | 160 | 0.27236805794593677 | 0.47653270252927582 | 1.3054257713687778 | 1.464984482935876 | 0.1588131411972471 | 12 | 12 | 4.6094829360563327 | 0.40902543581708745 |
| ctx-lh-supramarginal | NFL | 165 | 160 | 0.15787682768123779 | 0.47653270252927582 | 1.3054257713687778 | 1.464984482935876 | 0.1588131411972471 | 12 | 6 | 5.0606937401157825 | 1.2656906118063802 |
| ctx-lh-temporalpole | GFAP | 165 | 160 | 0.28263254583093667 | 0.53909532203663202 | 1.4160459290449121 | 1.6995765954917303 | 0.089726199667384141 | 9 | 9 | 4.4518523318885901 | 0.34667844656711516 |
| ctx-lh-temporalpole | NFL | 165 | 160 | 0.1507625295939472 | 0.53909532203663202 | 1.4160459290449121 | 1.6995765954917303 | 0.089726199667384141 | 9 | 6 | 5.05599451562939 | 1.2622977122488499 |
| ctx-lh-transversetemporal | GFAP | 165 | 160 | 0.23761518756980493 | 0.39206659799921273 | 1.1859254105261026 | 1.4034635473846289 | 0.15666321422607349 | 9 | 9 | 4.5377013531997719 | 0.39124854169193335 |
| ctx-lh-transversetemporal | NFL | 165 | 160 | 0.14686624931191439 | 0.39206659799921273 | 1.1859254105261026 | 1.4034635473846289 | 0.15666321422607349 | 9 | 7 | 5.0777166157965903 | 1.2796986780004096 |
| ctx-rh-bankssts | GFAP | 165 | 160 | 0.25136788544822819 | 0.49432659635767112 | 1.3494851292441201 | 1.4107681519057738 | 0.16583568002540838 | 14 | 8 | 4.6587447028936699 | 0.42080890698010553 |
| ctx-rh-bankssts | NFL | 165 | 160 | 0.14559068739040781 | 0.49432659635767112 | 1.3494851292441201 | 1.4107681519057738 | 0.16583568002540838 | 14 | 8 | 5.0678600649054308 | 1.2504590446700641 |
| ctx-rh-caudalanteriorcingulate | GFAP | 165 | 160 | 0.27162816512276655 | 0.41027561939774032 | 1.2036766189150112 | 1.4776476877380087 | 0.095345389237731254 | 10 | 7 | 4.7030551979946855 | 0.44354496423760464 |
| ctx-rh-caudalanteriorcingulate | NFL | 165 | 160 | 0.1497598713890278 | 0.41027561939774032 | 1.2036766189150112 | 1.4776476877380087 | 0.095345389237731254 | 10 | 7 | 5.0806557161571622 | 1.2772598187898325 |
| ctx-rh-caudalmiddlefrontal | GFAP | 165 | 160 | 0.31587692955349278 | 0.45601453888292071 | 1.2744550921401061 | 1.4328787698506775 | 0.13981067697794547 | 12 | 8 | 4.4910429143451438 | 0.32347998273983719 |
| ctx-rh-caudalmiddlefrontal | NFL | 165 | 160 | 0.15572284864717145 | 0.45601453888292071 | 1.2744550921401061 | 1.4328787698506775 | 0.13981067697794547 | 12 | 7 | 5.075808298092884 | 1.2715296121626438 |
| ctx-rh-cuneus | GFAP | 165 | 160 | 0.22292935669542491 | 0.44561389838388754 | 1.2546502462850895 | 1.4172647569911214 | 0.12069450947786117 | 14 | 9 | 4.6160954006688035 | 0.48531123625240885 |
| ctx-rh-cuneus | NFL | 165 | 160 | 0.15743535542304476 | 0.44561389838388754 | 1.2546502462850895 | 1.4172647569911214 | 0.12069450947786117 | 14 | 6 | 5.3152917601367093 | 1.3056959232991305 |
| ctx-rh-entorhinal | GFAP | 165 | 160 | 0.23528945606878948 | 0.51394547849051664 | 1.3597512264404796 | 1.6342279700689482 | 0.08225716679216788 | 11 | 7 | 4.6825594673518474 | 0.51056583407341138 |
| ctx-rh-entorhinal | NFL | 165 | 160 | 0.13823335115973612 | 0.51394547849051664 | 1.3597512264404796 | 1.6342279700689482 | 0.08225716679216788 | 11 | 6 | 5.0227907539095318 | 1.228536741175684 |
| ctx-rh-frontalpole | GFAP | 165 | 160 | 0.28603287597475169 | 0.3412038677634664 | 1.1350757139683298 | 1.4014839060411892 | 0.10675904738967025 | 12 | 9 | 4.4731259440287001 | 0.34913160188686881 |
| ctx-rh-frontalpole | NFL | 165 | 160 | 0.15435577880387186 | 0.3412038677634664 | 1.1350757139683298 | 1.4014839060411892 | 0.10675904738967025 | 12 | 5 | 5.074346399661672 | 1.279790238627694 |
| ctx-rh-fusiform | GFAP | 165 | 160 | 0.25985702202867444 | 0.55166319711490486 | 1.4384495093268395 | 1.6508511488815434 | 0.10534114288550153 | 13 | 8 | 4.5679428336078267 | 0.3870250006034015 |
| ctx-rh-fusiform | NFL | 165 | 160 | 0.15542168563872127 | 0.55166319711490486 | 1.4384495093268395 | 1.6508511488815434 | 0.10534114288550153 | 13 | 8 | 5.2300726079557212 | 1.2707651442509096 |
| ctx-rh-inferiorparietal | GFAP | 165 | 160 | 0.27430638471455682 | 0.51442710289499727 | 1.3718911407660004 | 1.4904047319808438 | 0.13141104446309687 | 13 | 9 | 4.5681693920080502 | 0.34080349108323449 |
| ctx-rh-inferiorparietal | NFL | 165 | 160 | 0.15527910890585384 | 0.51442710289499727 | 1.3718911407660004 | 1.4904047319808438 | 0.13141104446309687 | 13 | 7 | 5.1120605926909315 | 1.2530235390966784 |
| ctx-rh-inferiortemporal | GFAP | 165 | 160 | 0.26727056809487304 | 0.57647700588683748 | 1.5022748212000592 | 1.6708225369446323 | 0.10887391413017213 | 14 | 8 | 4.5182707225187286 | 0.36497504427382738 |
| ctx-rh-inferiortemporal | NFL | 165 | 160 | 0.15384639533066025 | 0.57647700588683748 | 1.5022748212000592 | 1.6708225369446323 | 0.10887391413017213 | 14 | 8 | 5.1965409813573817 | 1.3013186811228545 |
| ctx-rh-insula | GFAP | 165 | 160 | 0.27338379736664975 | 0.45052309334248292 | 1.2565563885181923 | 1.5695365926463083 | 0.10274059297369262 | 11 | 8 | 4.5845333872195955 | 0.42148148051039647 |
| ctx-rh-insula | NFL | 165 | 160 | 0.15255140544223955 | 0.45052309334248292 | 1.2565563885181923 | 1.5695365926463083 | 0.10274059297369262 | 11 | 6 | 5.1118025433325212 | 1.2787256243506138 |
| ctx-rh-isthmuscingulate | GFAP | 165 | 160 | 0.25566109638271184 | 0.44698944653627598 | 1.2610143595825731 | 1.4251825222549819 | 0.15928564212374804 | 11 | 8 | 4.5923698967442768 | 0.39689943937364464 |
| ctx-rh-isthmuscingulate | NFL | 165 | 160 | 0.16007245572437911 | 0.44698944653627598 | 1.2610143595825731 | 1.4251825222549819 | 0.15928564212374804 | 11 | 6 | 5.1543480882400337 | 1.262348812027478 |
| ctx-rh-lateraloccipital | GFAP | 165 | 160 | 0.2488302007551817 | 0.49085380512870735 | 1.3269769658408583 | 1.4843518712374268 | 0.11998898426148598 | 12 | 7 | 4.6162014474945989 | 0.44614378234025104 |
| ctx-rh-lateraloccipital | NFL | 165 | 160 | 0.1537823093912587 | 0.49085380512870735 | 1.3269769658408583 | 1.4843518712374268 | 0.11998898426148598 | 12 | 5 | 5.2410156972081205 | 1.2882412596099879 |
| ctx-rh-lateralorbitofrontal | GFAP | 165 | 160 | 0.27872410042625206 | 0.46442931508277668 | 1.2797766375387116 | 1.5801403103599934 | 0.086618877386390736 | 11 | 9 | 4.6336474239255141 | 0.43605329629339135 |
| ctx-rh-lateralorbitofrontal | NFL | 165 | 160 | 0.1511061549754491 | 0.46442931508277668 | 1.2797766375387116 | 1.5801403103599934 | 0.086618877386390736 | 11 | 6 | 5.104191489413215 | 1.298856099549242 |
| ctx-rh-lingual | GFAP | 165 | 160 | 0.22239457408951901 | 0.47811768368158097 | 1.2998215039611281 | 1.5149457685739611 | 0.10858596194518325 | 11 | 9 | 4.6580179331889315 | 0.4889066045843109 |
| ctx-rh-lingual | NFL | 165 | 160 | 0.15227462623703092 | 0.47811768368158097 | 1.2998215039611281 | 1.5149457685739611 | 0.10858596194518325 | 11 | 6 | 5.2214668840514067 | 1.2779231122766843 |
| ctx-rh-medialorbitofrontal | GFAP | 165 | 160 | 0.26961594221449281 | 0.38812330049108007 | 1.1799314675563244 | 1.4633058746767289 | 0.10863630407736639 | 11 | 10 | 4.6335100240767959 | 0.42642369423076271 |
| ctx-rh-medialorbitofrontal | NFL | 165 | 160 | 0.15152144668065681 | 0.38812330049108007 | 1.1799314675563244 | 1.4633058746767289 | 0.10863630407736639 | 11 | 6 | 5.0752455209069263 | 1.2786853640078708 |
| ctx-rh-middletemporal | GFAP | 165 | 160 | 0.27015987779743322 | 0.57611763603512878 | 1.5035314054530593 | 1.7079298583991274 | 0.11288715849502087 | 16 | 9 | 4.5684500037184641 | 0.39188269380941843 |
| ctx-rh-middletemporal | NFL | 165 | 160 | 0.15216187771540934 | 0.57611763603512878 | 1.5035314054530593 | 1.7079298583991274 | 0.11288715849502087 | 16 | 10 | 5.1231396582896185 | 1.2848695609989906 |
| ctx-rh-paracentral | GFAP | 165 | 160 | 0.25288255812322247 | 0.40240931263594015 | 1.19499533895376 | 1.4283367677419725 | 0.090402428454953956 | 13 | 4 | 4.5676581349106291 | 0.40134532667050576 |
| ctx-rh-paracentral | NFL | 165 | 160 | 0.16167260095359559 | 0.40240931263594015 | 1.19499533895376 | 1.4283367677419725 | 0.090402428454953956 | 13 | 6 | 5.0675822425798085 | 1.2493757116055055 |
| ctx-rh-parahippocampal | GFAP | 165 | 160 | 0.23576010991925278 | 0.54318331862666536 | 1.4225219336803085 | 1.7224679148505377 | 0.091573824812063609 | 12 | 9 | 4.716448904651708 | 0.5097143902220882 |
| ctx-rh-parahippocampal | NFL | 165 | 160 | 0.14679636434140242 | 0.54318331862666536 | 1.4225219336803085 | 1.7224679148505377 | 0.091573824812063609 | 12 | 6 | 5.1063820686216905 | 1.2409164134071231 |
| ctx-rh-parsopercularis | GFAP | 165 | 160 | 0.29774872018205767 | 0.44549502775066802 | 1.2563120223525812 | 1.4996444462716498 | 0.13565692301868318 | 11 | 9 | 4.516559426353191 | 0.35678517281763089 |
| ctx-rh-parsopercularis | NFL | 165 | 160 | 0.15656385206484114 | 0.44549502775066802 | 1.2563120223525812 | 1.4996444462716498 | 0.13565692301868318 | 11 | 9 | 4.9861951330335987 | 1.2406968889563921 |
| ctx-rh-parsorbitalis | GFAP | 165 | 160 | 0.27907616908507316 | 0.41464794539615296 | 1.2141938707934259 | 1.4922236717380508 | 0.12112577244956177 | 11 | 10 | 4.4780640796138158 | 0.38546112002053001 |
| ctx-rh-parsorbitalis | NFL | 165 | 160 | 0.15287815564935958 | 0.41464794539615296 | 1.2141938707934259 | 1.4922236717380508 | 0.12112577244956177 | 11 | 7 | 5.0981903591971385 | 1.2833751691400503 |
| ctx-rh-parstriangularis | GFAP | 165 | 160 | 0.29138226859655159 | 0.4216879579246316 | 1.2210513698183632 | 1.5100104873641855 | 0.1193433898826565 | 10 | 9 | 4.5441501064343335 | 0.40805719619533704 |
| ctx-rh-parstriangularis | NFL | 165 | 160 | 0.14985703464549271 | 0.4216879579246316 | 1.2210513698183632 | 1.5100104873641855 | 0.1193433898826565 | 10 | 7 | 5.0487523739869085 | 1.2976840764174091 |
| ctx-rh-pericalcarine | GFAP | 165 | 160 | 0.22583606703399062 | 0.43146010273249286 | 1.2295371328480671 | 1.5219316037500146 | 0.10729949726635041 | 11 | 8 | 4.5123886722247608 | 0.41716347959457417 |
| ctx-rh-pericalcarine | NFL | 165 | 160 | 0.15232490380655217 | 0.43146010273249286 | 1.2295371328480671 | 1.5219316037500146 | 0.10729949726635041 | 11 | 7 | 5.2410729560525624 | 1.2900465279358104 |
| ctx-rh-postcentral | GFAP | 165 | 160 | 0.26539847336577105 | 0.42024649420493077 | 1.2176957074776293 | 1.5098166973842633 | 0.094013492041170571 | 11 | 7 | 4.6309199071715019 | 0.43139510964542926 |
| ctx-rh-postcentral | NFL | 165 | 160 | 0.16028418919171361 | 0.42024649420493077 | 1.2176957074776293 | 1.5098166973842633 | 0.094013492041170571 | 11 | 6 | 5.1258479026246917 | 1.2794109157243654 |
| ctx-rh-posteriorcingulate | GFAP | 165 | 160 | 0.28352345536611678 | 0.43690332633098405 | 1.2435024237593337 | 1.4600173253807407 | 0.12767170276724024 | 11 | 7 | 4.6071235863981288 | 0.36032063467053754 |
| ctx-rh-posteriorcingulate | NFL | 165 | 160 | 0.16245244050545704 | 0.43690332633098405 | 1.2435024237593337 | 1.4600173253807407 | 0.12767170276724024 | 11 | 7 | 5.0961308099199805 | 1.255147429799448 |
| ctx-rh-precentral | GFAP | 165 | 160 | 0.25836669818726565 | 0.44643523445483035 | 1.2538656738092318 | 1.5434300186185876 | 0.094311507432906019 | 9 | 7 | 4.56479266890147 | 0.42550535648876869 |
| ctx-rh-precentral | NFL | 165 | 160 | 0.15674481461385958 | 0.44643523445483035 | 1.2538656738092318 | 1.5434300186185876 | 0.094311507432906019 | 9 | 6 | 5.0771049946090478 | 1.2609928543267777 |
| ctx-rh-precuneus | GFAP | 165 | 160 | 0.28873066861805607 | 0.40712451982414055 | 1.2109443454847235 | 1.3103939339749124 | 0.16839904320584914 | 11 | 9 | 4.5530959554623545 | 0.3069608695956314 |
| ctx-rh-precuneus | NFL | 165 | 160 | 0.16367503960849239 | 0.40712451982414055 | 1.2109443454847235 | 1.3103939339749124 | 0.16839904320584914 | 11 | 6 | 5.179698292564499 | 1.2754666415791036 |
| ctx-rh-rostralanteriorcingulate | GFAP | 165 | 160 | 0.2698684121377446 | 0.40125154189409867 | 1.1925120275050696 | 1.5056121820489317 | 0.1007461856118704 | 11 | 6 | 4.7481741072147221 | 0.4870292079735401 |
| ctx-rh-rostralanteriorcingulate | NFL | 165 | 160 | 0.15751743289452957 | 0.40125154189409867 | 1.1925120275050696 | 1.5056121820489317 | 0.1007461856118704 | 11 | 5 | 5.1652933959048548 | 1.3408670452927334 |
| ctx-rh-rostralmiddlefrontal | GFAP | 165 | 160 | 0.30727765020216669 | 0.40691849149476006 | 1.2060515918428694 | 1.4729317672194362 | 0.15006836327321593 | 14 | 6 | 4.4920184875658657 | 0.34690798665702699 |
| ctx-rh-rostralmiddlefrontal | NFL | 165 | 160 | 0.15654646747968781 | 0.40691849149476006 | 1.2060515918428694 | 1.4729317672194362 | 0.15006836327321593 | 14 | 8 | 5.0712425034213791 | 1.2736383109447615 |
| ctx-rh-superiorfrontal | GFAP | 165 | 160 | 0.29746495501870118 | 0.41679401764387075 | 1.2126578829801524 | 1.5144438676724128 | 0.10259269256893794 | 14 | 6 | 4.5671169427729721 | 0.38330087346330305 |
| ctx-rh-superiorfrontal | NFL | 165 | 160 | 0.16176980998506285 | 0.41679401764387075 | 1.2126578829801524 | 1.5144438676724128 | 0.10259269256893794 | 14 | 7 | 5.1160182311626743 | 1.2805826520536139 |
| ctx-rh-superiorparietal | GFAP | 165 | 160 | 0.28599631288648353 | 0.46449621282887088 | 1.2881115170592683 | 1.4080597385296061 | 0.11521601513012364 | 12 | 6 | 4.5817453390282088 | 0.35567436032673455 |
| ctx-rh-superiorparietal | NFL | 165 | 160 | 0.15852093118334665 | 0.46449621282887088 | 1.2881115170592683 | 1.4080597385296061 | 0.11521601513012364 | 12 | 5 | 5.18986969460998 | 1.2415981825526181 |
| ctx-rh-superiortemporal | GFAP | 165 | 160 | 0.2602218437977204 | 0.49174494755653569 | 1.3232681852542822 | 1.5417886594508654 | 0.14342403366143019 | 13 | 10 | 4.6137793572728558 | 0.4147798970140204 |
| ctx-rh-superiortemporal | NFL | 165 | 160 | 0.14777647931236126 | 0.49174494755653569 | 1.3232681852542822 | 1.5417886594508654 | 0.14342403366143019 | 13 | 9 | 5.0563723138365377 | 1.2639754969547881 |
| ctx-rh-supramarginal | GFAP | 165 | 160 | 0.28085083694948909 | 0.48844407549885538 | 1.3227293613875306 | 1.5191783338113862 | 0.13952095666404143 | 12 | 10 | 4.6545643294348267 | 0.40118848977400934 |
| ctx-rh-supramarginal | NFL | 165 | 160 | 0.15593011218161124 | 0.48844407549885538 | 1.3227293613875306 | 1.5191783338113862 | 0.13952095666404143 | 12 | 8 | 5.0704467339164117 | 1.263712797321213 |
| ctx-rh-temporalpole | GFAP | 165 | 160 | 0.27508270438929627 | 0.52662428826983476 | 1.3897746083823608 | 1.7009480002044852 | 0.099447908888236652 | 10 | 8 | 4.5469544541182927 | 0.4145316422993619 |
| ctx-rh-temporalpole | NFL | 165 | 160 | 0.14762370045281692 | 0.52662428826983476 | 1.3897746083823608 | 1.7009480002044852 | 0.099447908888236652 | 10 | 7 | 5.0680431426302688 | 1.2374168657885809 |
| ctx-rh-transversetemporal | GFAP | 165 | 160 | 0.23993662120603931 | 0.40285197681334028 | 1.1939123342988105 | 1.4677487958564723 | 0.11387075871417278 | 9 | 6 | 4.7276243657141004 | 0.47399979015707455 |
| ctx-rh-transversetemporal | NFL | 165 | 160 | 0.14719445588941726 | 0.40285197681334028 | 1.1939123342988105 | 1.4677487958564723 | 0.11387075871417278 | 9 | 8 | 5.0324310012941229 | 1.2579155221536444 |

## Complete CSV table inventory

Source: All numerical contents embedded above; no significant-only subset

| filename | rows | columns |
| --- | --- | --- |
| T10_predictor_descriptives_and_scaling.csv | 137 | field, mean, sd |
| T11_analysis_sample_sizes.csv | 8 | analysis, model_or_variable_count, records_per_analysis, residual_df, purpose |
| T12_available_demographic_descriptives.csv | 5 | variable, statistic, value, units |
| T13_final_figure_inventory.csv | 6 | filenames_in_figures_folder, variables, measurement_units, scientific_purpose |
| T1_sample_flow.csv | 5 | stage, n, excluded_since_previous |
| T2_results_summary.csv | 4 | outcome, predictor, tests, Holm_passes, standardized_beta_min, standardized_beta_max, Holm_p_min, Holm_p_max |
| T3_all_272_tests.csv | 272 | region, outcome, predictor, n, df_resid, beta, se_HC3, t_HC3, ci95_low, ci95_high, p_raw, standardized_beta, standardized_ci95_low, standardized_ci95_high, partial_R2, p_Holm_272, passes_Holm_0_05 |
| T4_all_sensitivities.csv | 272 | region, outcome, predictor, n, beta, se_HC3, ci95_low, ci95_high, p_raw, standardized_beta, standardized_ci95_low, standardized_ci95_high, partial_R2, p_Holm_272, passes_Holm_0_05, base_beta, leave_one_out_min, leave_one_out_max, conventional_se, HC3_se, quadratic_age_beta, quadratic_age_ci_low, quadratic_age_ci_high, numeric_sex_contrast_beta, numeric_sex_contrast_ci_low, numeric_sex_contrast_ci_high, quadratic_age_standardized_change, numeric_sex_contrast_standardized_change, leave_one_out_max_standardized_change, HC3_to_conventional_SE_ratio |
| T5_all_model_diagnostics.csv | 136 | region, outcome, n, df_resid, R2, PET_correlation, VIF_amyloid, VIF_tau, max_leverage, leverage_flag_count, cooks_flag_count, max_abs_studentized_residual, residual_skewness |
| T6_hypothesis_assessment.csv | 4 | hypothesis, association, original_status, regional_evidence |
| T7_sensitivity_summary.csv | 5 | scope, outcome, predictor, n_tests, quadratic_age_sign_reversals, quadratic_age_median_abs_standardized_change, quadratic_age_max_abs_standardized_change, quadratic_age_median_abs_percent_change, quadratic_age_max_abs_percent_change, numeric_sex_contrast_sign_reversals, numeric_sex_contrast_median_abs_standardized_change, numeric_sex_contrast_max_abs_standardized_change, numeric_sex_contrast_median_abs_percent_change, numeric_sex_contrast_max_abs_percent_change, loo_ranges_crossing_zero, loo_max_abs_standardized_change, SE_ratio_min, SE_ratio_max |
| T8_prior_distribution_audit.csv | 6 | population, field, n, mean, sd, minimum, q1, median, q3, maximum, skewness, excess_kurtosis, nonpositive, missing |
| T9_prior_availability_audit.csv | 8 | biomarkers, imaging_amyloid, imaging_tau, n |

## Final figures

**F1_sample_flow.** Sequential one-to-one intersections: 644 → 618 → 270 → 165; no additional finite-value exclusions. These are overlapping stages, not independent groups. Source: T1.

**F2_lh_regional_effects.** Left hemisphere, all 34 regions in alphabetical order, identical axes across all eight hemisphere panels. Filled teal points: Holm p < .05 in the full 272-test family; hollow gray points: threshold not met. Bars are marginal 95% intervals, not simultaneous intervals. Models mutually adjust same-region PET fields, age and readable sex. Source: T3. Standardized slopes are unitless; clinical PET normalization remains unverified.

**F3_rh_regional_effects.** Right hemisphere, all 34 regions in alphabetical order, identical axes across all eight hemisphere panels. Filled teal points: Holm p < .05 in the full 272-test family; hollow gray points: threshold not met. Bars are marginal 95% intervals, not simultaneous intervals. Models mutually adjust same-region PET fields, age and readable sex. Source: T3. Standardized slopes are unitless; clinical PET normalization remains unverified.

**F4_age_sex_sensitivity.** Each point is one regional slope. Alternative estimates use the original sample and scaling. Identical axes and identity lines prevent visual exaggeration. These are descriptive comparisons, not alternative corrected significance tests. Source: T4.

**F5_single_record_influence.** Each point shows the largest absolute slope change across single-record deletions for one regional association. Original scaling is held fixed. These maxima are not confidence limits. All 22,440 case-deletion fits were previously checked independently. Source: T4.

