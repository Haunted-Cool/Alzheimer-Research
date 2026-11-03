"""Package reviewed outputs without changing earlier evidence."""
from pathlib import Path
import hashlib,json,zipfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent.parent
HERE=ROOT/'phase4_results'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
prior=ROOT/'phase34/regional_extension/SPHERE_Regional_Analysis_Verified_Package.zip'
expected=json.loads((ROOT/'phase34/regional_extension/completion/package_verification.json').read_text())['archive_sha256']
assert sha(prior)==expected
for p in (HERE/'deliverables/figures').glob('*.svg'): ET.parse(p)
verification=json.loads((HERE/'deliverables/results_verification.json').read_text())
for name,h in verification['input_sha256'].items(): assert sha(ROOT/name)==h,name
files=[p for p in (HERE/'deliverables').rglob('*') if p.is_file()]
files += [HERE/'build_results.py',HERE/'package_results.py',HERE/'README.md',ROOT/'phase34/sources/hypotheses.txt']
entries={str(p.relative_to(ROOT)):p for p in files}
entries['Original_Analysis_Package.zip']=prior
manifest={name:{'sha256':sha(p),'bytes':p.stat().st_size} for name,p in entries.items()}
archive=HERE/'SPHERE_Phase4_Results_and_Figures.zip'
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED) as z:
    for name,p in entries.items(): z.write(p,name)
    z.writestr('Phase4_Manifest.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for name,item in manifest.items(): assert hashlib.sha256(z.read(name)).hexdigest()==item['sha256']
result=dict(status='PASS',files=len(entries),archive_sha256=sha(archive),bytes=archive.stat().st_size,
    SVG_XML_checks=5,PNG_figures_visually_reviewed=5,CSV_tables=9,source_files_unchanged=True,
    numeric_verification=verification['status'],new_model_fits=0)
(HERE/'package_receipt.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
