# Verified regional-analysis package

Start with `completion/Final_Verified_Results_Summary.md`. It distinguishes the completed exploratory regional analysis from the original unexecuted biological H1–H4 analysis. Earlier reports are preserved historical records.

The archive contains scripts, specifications, aggregate results, model diagnostic plots, both completed runs and independent verification records. It does not contain source CSVs or a merged record-level dataset. You need authorized access to the same four source CSVs to refit models. Source SHA-256 values are in `results/input_manifest.csv`.

From the extracted `phase34` directory, use Python 3.12:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r regional_extension/requirements-complete.txt
.venv/bin/python regional_extension/complete_verification.py \
  --data-dir '/path/to/ADRC_SPHERE_all_data' \
  --output regional_extension/completion_rerun
.venv/bin/python regional_extension/run.py \
  --data-dir '/path/to/ADRC_SPHERE_all_data' \
  --output regional_extension/new_run
```

Use new output directory names on each attempt and do not use Python `-O`. Do not rerun `verify_and_report.py` in the evidence copy: it writes its historical report and verification file. `complete_verification.py` provides a non-overwriting check of the archived pair and independent sensitivity verification. This latter script uses source hashes and fixed expected counts for this specific analyzed release; a different release requires a new protocol/version, not bypassing its checks.

`Package_Manifest.json` at the archive root records SHA-256 values for every packaged file except the manifest itself. The packaging script checks archive CRCs, checks every member against its SHA-256, and runs the extracted completion verifier in the existing environment. The external `completion/package_verification.json` receipt records the outcome and final ZIP hash. That receipt is not inside the archive because it is created after archive verification.

The extracted-package check confirms packaging and path handling in the installed environment. It is not a fresh dependency installation, another investigator's reproduction or validation of clinical interpretation. `completion/environment_versions.json` records the actual runtime and installed package versions; direct reproduction dependencies are in `requirements-complete.txt` and the preserved parent `requirements.txt`.
