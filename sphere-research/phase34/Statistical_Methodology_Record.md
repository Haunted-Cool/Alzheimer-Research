# Phases 3 and 4: statistical methodology and Python record
Prepared 2 November 2026. Research-methodology notes, not manuscript prose.

## Status and scope
The statistical design and Python implementation are prepared. The actual source-data audit and artificial-fixture numerical validation were executed. **H1–H4 have not been fitted to SPHERE.** Final scientific execution remains pending defensible PET definitions, sex encoding, and measurement/inference documentation. The user confirmed on 2 November that no newer definitions are available.

The finalized Research Questions & Hypotheses PDF takes precedence over the original proposal's discordant-group design. The Dataset Understanding PDF sometimes still describes the original group hypotheses; it is used for data facts and unresolved metadata, not to reinstate superseded hypotheses. The original proposal's expected significant findings are predictions, not results.

This record specifies decisions before association testing in this chat. Earlier dataset summaries and literature were already known. It is therefore a dated prospective analysis specification relative to H1–H4, **not an external preregistration or a claim of complete blinding**. Measurement-dependent choices remain open; version and hash any amendment before fitting. Do not overwrite version 1.0. A local hash establishes file identity, not an independently certified timestamp.

## 1. Questions, estimands and tests
Use two ordinary least-squares models on the same eligible common sample:

GFAP = intercept + beta_A × standardized amyloid + beta_T × standardized tau + beta_age × standardized age + beta_sex × documented sex contrast + error.

NFL uses the same predictors. Standardization subtracts the analysis-sample mean and divides by its sample SD (ddof=1). Outcomes remain in released numeric units. Centering/scaling continuous predictors changes coefficient units but not fitted values or their zero-coefficient tests. Persist the means/SDs when the final model is implemented.

| Hypothesis | Coefficient | Direction | Testing family |
|---|---|---|---|
| H1, primary | Amyloid in GFAP model, conditional on tau, age and sex | Positive expected; two-sided test | One primary test, alpha .05 |
| H2, secondary | Tau in GFAP model, conditional on amyloid, age and sex | Unspecified | Holm across H2–H4 |
| H3, secondary | Amyloid in NFL model, conditional on tau, age and sex | Unspecified | Same secondary family |
| H4, secondary | Tau in NFL model, conditional on amyloid, age and sex | Unspecified | Same secondary family |

All nulls are beta=0; alternatives beta≠0. Use OLS estimates with HC3 heteroskedasticity-robust covariance, two-sided Student-t reference with n−rank(X) degrees of freedom, and marginal 95% confidence intervals. This small-sample reference is an approximation, not exact robust finite-sample inference. HC3 is selected in advance rather than after a variance test.

These are adjusted conditional associations, not total causal effects. Mutual adjustment deliberately asks how one PET measure relates to the outcome at a fixed value of the other. If tau mediates an amyloid pathway, the adjusted amyloid association does not represent that entire pathway.

Regression is appropriate because outcomes and pathology predictors are continuous and covariate adjustment is required. Pearson/Spearman correlations alone do not answer the adjusted questions. A t test, Mann–Whitney test, ANOVA or Kruskal–Wallis test would instead compare groups. ANCOVA would be appropriate for a separately specified validated group contrast, but is not the finalized primary design. No median splits, positivity thresholds, automatic stepwise selection, or screening of 217 PET fields for favorable associations.

## 2. Assumptions and diagnostics
The conditional mean must be adequately represented, design columns must be full rank, and errors must have mean zero conditional on predictors for an unbiased associational model under its target population. Confounding, selection, measurement error and timing can defeat biological interpretations even when numerical assumptions look satisfactory.

Usual HC3 inference assumes independent observations with sufficient finite moments and tolerable leverage. A unique synthetic row ID does not establish independence of the synthesis process. Obtain release-specific guidance about inferential validity after merging and selecting rows. Do not claim source-cohort equivalence or that synthetic CIs cover real-patient effects.

Normality of the marginal biomarker distribution is **not** an OLS assumption. Exact classical t inference requires stronger residual assumptions; HC3 relaxes constant variance, not nonlinearity, dependence or omitted confounding. Avoid using Shapiro–Wilk as a switch between tests.

After measurement resolution, examine:
- Histograms and Q-Q plots for outcomes; residual Q-Q and residual-versus-fitted plots for each model; partial-residual relationships for PET and age.
- PET correlation and VIF. VIF above 5 flags unstable separation of effects; above 10 indicates serious concern. These are review flags, not automatic predictor deletion rules. Preserve the mutually adjusted question or report that it is poorly identified.
- Leverage above 2p/n, Cook's distance above 4/n, and large studentized residuals. These flag investigation, not automatic exclusions.
- Rank, conditioning, residual spread and uncertainty. If diagnostics reveal material misspecification, report it and use an explicitly labeled amendment/sensitivity analysis.

The engine computes rank, VIF, condition number, leverage, Cook's-distance counts and residual extremes. Model residual plots and any nonlinear model beyond the implemented quadratic-age sensitivity remain pending final SPHERE execution.

## 3. Data and eligibility
Read original source CSVs locally and preserve them. Use exact string adrc_id keys; reject missing, duplicate, blank or padded keys and duplicate headers. Validate one-to-one joins. Prefix PET modality fields in any future preparation. Do not merge by row order or use demographic similarity.

Use all diagnoses in the finalized available-modality cohort. Restricting to AD diagnoses would change the question and might condition on downstream disease manifestations. Do not require CSF, WGS, cognition or plasma proteomics to enter the primary models.

The verified structural flow is 644 demographics → 618 with blood → 270 also with amyloid imaging → 165 also with tau imaging. Counts are synthetic release records, not newly recruited patients. The 165 is an upper bound on final eligible model n; approved summary availability and covariate coding still need verification. Future common-case selection requires both outcomes and all model predictors, and a separately logged exclusion count for every rule.

Current local biomarkers, demographics, tau, WGS and CSF files are checked against the prior attachment hash manifest. Numbered duplicates are not independent cohorts. Amyloid comes from the local project source folder previously reconciled to those same exports. This run did not freshly download the library-only CSV links. The three named Drive PDF texts were freshly retrieved. The proposal was reviewed via the existing extracted attachment text. Provenance limitations are retained rather than presented as a fresh attachment-byte verification.

## 4. Covariates and confounders
Age and documented sex representation are core adjustment variables. Readable sex labels and synthesized numeric orthogonal contrasts are not interchangeable. Do not round numeric contrasts, interpret them as probabilities, or include all redundant contrasts plus an intercept. The implemented engine accepts one numeric sex contrast; a validated multicategory encoding would require an explicit extension and new tests.

Renal function, vascular injury, neurological comorbidity, assay batch, tracer/processing differences, and blood–PET timing are potentially relevant. Their absence cannot be repaired by statistical significance screening. Record whether each is measured, usable and temporally relevant before adding it. No renal-function or timing adjustment has been claimed here.

APOE may be a scientifically motivated sensitivity covariate only with validated coding. WGS continuous synthesized values must not be rounded to genotype calls; the prior audit lacks a complete usable APOE definition. Diagnosis and cognition may be downstream of pathology; automatic adjustment can change the estimand or induce bias. Race/ethnicity are not substitutes for genetic ancestry. Describe clinical composition without implying source-person identities.

## 5. Missing data and selection
There are zero parsed missing cells and zero numeric infinities in the six tables reread by this audit. This does not establish absence of semantic missingness or original missing codes. Modality absence dominates: the common subset excludes 479 of 644 roster records.

Describe inclusion versus exclusion using age summaries and categorical proportions, not significance tests that purport to establish missing completely at random. Included mean age is 71.95 versus 73.33 outside the subset; age standardized mean difference is −0.157, using sqrt((variance_in+variance_out)/2). This descriptive imbalance does not identify the missingness mechanism. Included readable labels are 90 male/75 female; labels are descriptive pending regression coding.

Primary estimand is explicitly the eligible complete-case release subset. Extending to the full roster requires assumptions about selection. Do not impute entire absent PET modalities or use mean imputation by default. If genuine item missingness emerges, specify the imputation model, auxiliary variables, transformations, missing-at-random assumption and pooling method before use. Multiple imputation would need compatible models and Rubin pooling, with missing-not-at-random sensitivity. It is not implemented or run here. Weighting for availability would additionally need credible selection models, overlap and stable weights; it is not a substitute for unknown measurement definitions.

## 6. Distributions and transformations
Executed descriptive checks use count, missingness, mean, SD, quartiles, range, skewness, excess kurtosis, histograms and normal Q-Q plots. These check released numbers, not physiological normal ranges.

| Core variable | n | Mean (SD) | Median | Nonpositive |
|---|---:|---:|---:|---:|
| GFAP | 165 | 74.252 (36.234) | 74.065 | 5 |
| NFL | 165 | 25.924 (11.544) | 25.254 | 0 |

Units are unresolved; do not label these pg/mL. Core GFAP ranges from −23.427 to 239.279, with skewness .362. NFL ranges from .779 to 78.297, with skewness .879. Both show tail departures in Q-Q plots; regression residuals remain unevaluated.

Retain released-scale values provisionally for linear models. A direct GFAP logarithm is undefined for five core records. Dropping them would change n to 160 and the estimand. No clipping, zero replacement, shifting, winsorization or outlier deletion is applied. NFL positivity within this subset alone does not establish that a log scale is the correct measurement model.

If Stanford validates a positive concentration scale and a log analysis, specify it prospectively as a sensitivity or amendment. A log-outcome coefficient corresponds to 100×(exp(beta)−1)% change per predictor unit, with interval endpoints exponentiated similarly. Log transforms, ranks and nonlinear summaries can alter SPHERE preservation properties; raw-scale fidelity cannot be assumed to carry over.

## 7. Effect sizes, uncertainty and multiplicity
Report the adjusted slope in released outcome units per one sample SD of PET, its HC3 SE, marginal 95% CI, and exact p-value. Also report the fully standardized slope and descriptive partial R²=(SSE_reduced−SSE_full)/SSE_reduced. Partial R² measures incremental fit in this sample; it is not causal variance explained and is not a robust-inference test statistic.

A p-value is the probability, under the null and model assumptions, of a test statistic at least as extreme as observed. It is not the probability the null is true. A 95% CI describes long-run procedure coverage under assumptions; it does not assign a 95% probability to this fixed parameter. A wide interval spanning zero may include important positive and negative effects. Nonsignificance is not equivalence; equivalence needs a justified margin and a dedicated test.

Holm sorts the three secondary p-values, compares them sequentially with .05/3, .05/2 and .05, and enforces monotonic adjusted p-values. It controls familywise error for that secondary family under valid p-values, without requiring independence. H1 is separate as selected in the finalized design; this is not a claim of .05 familywise control over all four tests together. H2–H4 marginal 95% intervals are not simultaneous Holm-adjusted intervals.

Never infer that two associations differ because one is significant and the other is not. The optional RQ5 coefficient comparison needs a direct contrast and justified comparability of PET measures; it is deferred. If future exploratory regional screening is authorized, identify the whole search family and use a prespecified FDR procedure, reporting every screened result.

## 8. Sensitivity and exploratory register
| Analysis | Purpose and decision | Execution |
|---|---|---|
| Quadratic age with both PET predictors retained | Evaluate age-shape sensitivity; retain primary model regardless of p-value | Implemented; tested on artificial data only |
| Leave each record out once, keeping original scaling constants | Quantify dependence on individual rows without deleting them from primary results | Implemented; tested on artificial data only |
| Conventional vs HC3 covariance | Assess variance-assumption effect; coefficients are identical, inference differs | Both available from engine; actual-data comparison pending |
| Alternate validated PET region/composite | Check measurement dependence; require an external anatomical rationale before fitting | Deferred; no arbitrary composite |
| Approved sex label vs source-compatible contrast | Assess encoding sensitivity; do not claim these are equivalent | Deferred pending definition |
| Diagnosis or renal adjustment | Different conditioning question; require usable coding and stated causal rationale | Deferred |
| Log scale, robust regression, rank analysis | Different scale/estimand; not selected by significance | Optional exploratory, not implemented |
| A×T interaction, subgroup analyses, RQ5 | Additional scientific questions and multiplicity | Optional exploratory, not implemented |
| Bootstrap | Would require defensible row resampling/exchangeability; does not recover source-cohort synthesis uncertainty | Not performed |
| Imputation/selection weighting | Requires missingness and selection assumptions beyond observed completeness | Not performed |

There is no observed-power calculation or significance-driven stopping. Precision will be assessed from CIs after fitting. The analysis uses the available eligible release sample, not a sample chosen to meet a p-value target.

## 9. Code, debugging and verification
- analysis.py: strict CSV/key checks; source-data audit; regression engine; sensitivity engine.
- protocol.json: machine-readable decisions and explicit unresolved measurement fields.
- validate.py: entirely artificial 240-row fixture, seed 20261102. It independently computes OLS by least squares and the HC3 sandwich covariance, then checks t-based p-values/CIs against statsmodels. It also checks a hand-calculated Holm example, row-order invariance, invalid-input rejection, and sensitivity execution.
- reproduce.py: runs two fresh-process audits, compares output bytes, validates numerics, records command outcomes, dependency versions and source/attachment hash reconciliation.
- results/: actual SPHERE aggregate outputs only.
- verification/artificial_fixture_*: software-test outputs only. They must never be cited as SPHERE findings.
- verification/numerical_validation.json and reproduction.json: machine-readable evidence of completed checks.

The independent HC3 calculation is (X'X)⁻¹ X' diag[e_i²/(1−h_i)²] X (X'X)⁻¹. Comparing it with library output catches mistakes in leverage correction, SEs and confidence-interval reference distributions. Tests also reject missing and infinite numbers, duplicate keys/headers, constant variables and rank deficiency. These are meaningful safeguards, not a proof of biological validity.

Debug from the first failed invariant. A duplicate key requires fixing provenance or the join design, never silently dropping rows. Nonfinite log values require revisiting the scale, never replacing them with zero. Rank deficiency requires examining redundant coding, not deleting the scientifically necessary predictor with the least favorable p-value. Preserve full errors in run logs.

## 10. What is needed to finish H1–H4
Supply the exact amyloid and tau summary definitions or justified source-column recipes, including tracer/scale/reference region, anatomical justification and source citation. Establish how released plasma units and negative values should be interpreted; no assay-specific clinical interpretation is currently supported. Confirm the sex representation and how subset regression uncertainty may be interpreted under this release.

Then append a dated protocol amendment, implement the explicit mapping (without outcome-based selection), verify every source-to-model field, log exclusions/scaling constants and the final n, run both models and all prespecified sensitivities once, produce residual/partial-residual diagnostics, and archive all estimates and deviations. If inferential fidelity remains unverified, label results as synthetic-release associations with model-based uncertainty rather than validated patient-cohort findings.

## Sources
Project sources: sources/hypotheses.txt, sources/dataset.txt and sources/literature.txt contain text retrieved from the three named Drive PDFs on 2 November 2026. The original proposal extraction remains in ../phase2/sources/project_plan_extracted.txt. Original Drive IDs are recorded in sources/README.md.

Public methods references checked 2 November 2026:
- [Stanford SPHERE portal](https://adrc-sphere.stanford.edu/): dataset context and attribution. The readable portal did not resolve this export's summary or sex coding.
- [statsmodels robust covariance API](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html): HC3 and explicit t-reference configuration.
- [statsmodels multiple-testing API](https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html): Holm implementation.
- [statsmodels HC3 covariance](https://www.statsmodels.org/stable/generated/statsmodels.stats.sandwich_covariance.cov_hc3.html): covariance cross-check reference.

Attribution carried from supplied materials: Stanford Alzheimer's Disease Research Center, NIH/NIA grant P30 AG066515; He Z et al., SPHERE methods preprint, DOI 10.64898/2026.09.01.748580. This package is a local research-methodology record, not a clinical validation or manuscript submission.

