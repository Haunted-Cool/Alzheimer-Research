# Stanford SPHERE exploratory regional biomarker analysis

Reproducible research code and verified reference outputs for 165 synthetic SPHERE records, 136 main OLS models, and 272 focal tests. All 68 shared cortical regions are analyzed. The 50 Holm-threshold findings are positive GFAP–amyloid associations. Original biological H1–H4 remain unassessed because their measurement definitions remain unresolved. This repository does not establish causal or clinical effects.

## Quick start

Use Python 3.12 (the recorded execution used 3.12.14). From the repository root:

```sh
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python reproduce.py --check-only
```

Regenerate figures and the complete Chat 10 report from the checked-in, verified aggregate outputs, without individual-record data:

```sh
python reproduce.py --output runs/reference_rebuild
```

Re-run the actual regional models, their sensitivities and independent verification, then regenerate figures and the final report:

```sh
python reproduce.py \
  --data-dir '/path/to/authorized/ADRC_SPHERE_all_data' \
  --output runs/full_rebuild
```

Use a different output directory for each run. Do not use Python `-O`. The wrapper checks reference hashes, works in an isolated copy, and preserves checked-in results. With data supplied, it runs the main analysis twice, checks agreement with the reference CSVs, independently verifies sensitivities, and uses the regenerated results to build figures and reports. Both modes run the artificial software-validation fixture; fixture results are never biological findings.

The final report appears at `runs/<run-name>/workspace/chat10_final_results/deliverables/Chat10_Final_Results_Report.html`. Logs and validation receipts are in the selected run directory. `run_summary.json` identifies whether models were freshly fitted or only saved outputs were presented. A failed check stops the run rather than silently substituting results.

## Data needed for a full model rerun

Keep these four source files outside the repository:

- `demographics_diagnosis.csv`
- `biomarkers.csv`
- `imaging_amyloid.csv`
- `imaging_tau.csv`

They must match `phase34/regional_extension/results/input_manifest.csv`. Hash mismatches indicate different inputs; do not bypass checks to force agreement. The exact region definitions and data processing are in `phase34/regional_extension/plan.json` and `run.py`. Do not log, clip, recode, create composites or delete observations to obtain different significance. No original individual-record CSV or merged analysis matrix is distributed here.

The older broad audit additionally needs `wgs.csv` and `proteomics_csf.csv`. Its code is included for historical completeness, but it is not needed for the regional rerun above. The original hypothesis engine remains deliberately gated by the unresolved measurement contract.

## Code map

| Path | Purpose |
| --- | --- |
| `reproduce.py` | Safe end-to-end entry point; isolated runs and comparisons |
| `phase34/analysis.py` | Strict data reading, earlier audit and statistical helpers |
| `phase34/validate.py` | Artificial-fixture software checks, not SPHERE findings |
| `phase34/reproduce.py` | Historical six-file audit workflow; writes outputs in place, so use only in a disposable copy |
| `phase34/run_models.py` | Original H1–H4 engine; unavailable for actual inference until its contract is resolved |
| `phase34/regional_extension/run.py` | 136 main models; HC3 tests; Holm; age/sex sensitivities; 22,440 deletion checks; figures |
| `phase34/regional_extension/verify_and_report.py` | Compares two runs; writes regional verification/report |
| `phase34/regional_extension/complete_verification.py` | Independent QR sensitivity checks and summaries |
| `phase4_results/build_results.py` | Exact results tables and five figures; no model fitting |
| `chat10_final_results/build_final_report.py` | Standalone final report with all numerical appendices |

Packaging scripts are also included. Their archive-building functions are secondary to the root reproduction command; do not run historical packaging scripts in the evidence copy because they deliberately refuse existing outputs.

## Reference outputs

`phase34/regional_extension/results/`, `repeat/` and `completion/` preserve the main analysis and verification. `phase4_results/deliverables/` contains exact tables and five figures in PNG/SVG, plus the diagnostic PDF. Start reading with `chat10_final_results/deliverables/Chat10_Final_Results_Report.html` or its Markdown equivalent.

`REFERENCE_MANIFEST.json` fingerprints the included scientific source files and reference outputs. Build scripts intentionally expect this exact study layout. Editing a statistical specification requires a documented new analysis version; changing JSON alone does not reconfigure all hard-coded options. Earlier reports are historical snapshots and must be read with the final report, which distinguishes completed E1 from original unexecuted H1–H4.

## Interpretation and reproducibility limits

PET normalization, tau tracer/reference region, plasma measurement units, source-compatible sex coding and synthetic-data inferential calibration are unresolved. Marginal CIs are not simultaneous intervals. Stability of coefficient signs does not imply preserved corrected significance in sensitivity models. Model assumptions and biological validity are not established by passing code checks. The final report describes selection bias, residual tails, confounding and unperformed analyses.

The pinned versions reproduce the installed analysis environment. A new clean installation and GitHub-hosted execution have not been tested. `LOCAL_VERIFICATION.json` records the local repository test. Historical graphical-review notes refer to the reviewed reference figures; the reproduction command performs numerical checks, not an automatic new graphical review.

## Put this folder on GitHub

Create an empty GitHub repository, then run from this folder:

```sh
git init
git add .
git status
git commit -m 'Add verified SPHERE analysis and reproducibility workflow'
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Replace the example remote with your own. Source-data filenames, private-data directories, environments, caches and reruns are ignored. Inspect `git status` before committing. No repository has been published by this preparation step. No open-source license is asserted for Stanford data or third-party materials; add your chosen code license only if you have the rights to grant it.
