# Completed diagnostic review

Date: 2 November 2026. Supplement to the preserved earlier verification record.

All 136 pages of `../results/all_model_diagnostics.pdf` were rendered and visually reviewed using 12 contact sheets, with 12 model pages per sheet except the final four-page sheet. The original first two pages had also been inspected separately earlier. This is an AI-assisted graphical review, not an independent statistical review by a second investigator. The exact page-to-model mapping is in `diagnostic_page_index.csv`.

The plots comprise residual versus fitted values, residual normal Q-Q, and residual versus leverage for each GFAP/NFL model. Across the reviewed pages, the Q-Q plots show conspicuous positive-tail departures: GFAP commonly has one especially large positive residual; NFL commonly has several upper-tail residuals. Normality is therefore not declared satisfied. The residual clouds do not establish a correctly specified linear conditional mean or constant variance; a contact-sheet review is particularly limited for subtle curvature. No formal normality or heteroskedasticity test was added after viewing results.

The numerical diagnostics provide the more precise influence evidence: maximum leverage 0.235523; maximum absolute internally studentized residual 5.315292; 4–12 observations per model exceed Cook's distance 4/165. The largest PET VIF is 1.722468. No observation was deleted or winsorized in response to these diagnostics. All 22,440 single-record deletions had already been evaluated and independently checked against direct least-squares fits. Their sensitivity summaries are retained separately.

HC3 inference accounts approximately for heteroskedasticity in standard errors. It does not fix misspecification, outliers in the fitted mean, dependent synthetic records, selection bias, uncertain measurements, or synthesis uncertainty. Single-deletion sign stability does not establish stability under simultaneous removal of several observations or guarantee corrected significance.

All rendered panels were present and readable at the review scale. Rendering and review did not modify the diagnostic PDF or earlier CSV/JSON/PNG outputs. The earlier `verification.json` correctly records its narrower review at that time; this addendum expands that review scope without rewriting history.
