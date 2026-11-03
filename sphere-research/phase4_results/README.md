# SPHERE Results & Figures handoff

Start with `deliverables/Results_Report.md`. Open `deliverables/Results_Tables.html` to view all five figures and readable results tables. Exact CSVs are in `deliverables/tables/`; PNG and editable SVG files and the original diagnostic PDF are in `deliverables/figures/`. Keep `Figure_Captions.md` with shared figures. This is research documentation, not final manuscript prose.

The results describe the completed exploratory regional extension, not completion of original H1–H4. All findings and important limitations are covered in the report. No individual-record data are included.

The ZIP includes the earlier verified analysis package as `Original_Analysis_Package.zip`. Extract that nested archive into the same directory that contains `phase4_results/`, yielding a sibling `phase34/` directory. The original hypothesis reference is supplied under `phase34/sources/`. Install dependencies using Python 3.12 and `phase34/regional_extension/requirements-complete.txt`; see the original package's instructions.

From this shared project directory, reproduce the presentation in a new directory:

```sh
phase34/.venv/bin/python phase4_results/build_results.py --output phase4_results/new_build
```

The presentation builder requires only the saved aggregate outputs, not the original record-level data. It does not refit models. Reproducing the underlying original models requires the four authorized CSV inputs described in the earlier package. No fresh-environment installation or separate-investigator reproduction is claimed.

`Phase4_Manifest.json` fingerprints the delivered files. `package_receipt.json` outside the archive records the final ZIP integrity check and hash. Earlier verified analysis files remain unchanged.
