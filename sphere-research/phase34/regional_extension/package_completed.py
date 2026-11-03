"""Package existing evidence, check integrity, and verify an extracted copy.

No source records are packaged. No previously verified artifact is overwritten.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
import tempfile
import zipfile

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(data_dir):
    archive = HERE / 'SPHERE_Regional_Analysis_Verified_Package.zip'
    receipt = HERE / 'completion/package_verification.json'
    environment = HERE / 'completion/environment_versions.json'
    if any(p.exists() for p in (archive, receipt, environment)):
        raise ValueError('Package evidence exists; use a separate working copy to rebuild')
    baseline = json.loads((HERE / 'completion/completion_verification.json').read_text())
    for relative, expected in baseline['baseline_sha256'].items():
        assert sha(HERE / relative) == expected, relative
    environment.write_text(json.dumps({
        'python': sys.version,
        'platform': platform.platform(),
        'machine': platform.machine(),
        'packages': dict(sorted((d.metadata['Name'], d.version)
                                for d in importlib.metadata.distributions())),
        'note': 'Observed installed environment; not a tested clean-install lockfile'
    }, indent=2) + '\n')
    files = [BASE / n for n in ['analysis.py', 'requirements.txt', 'protocol.json']]
    files += sorted((BASE / 'results').glob('*'))
    files += [HERE / n for n in [
        'plan.json', 'run.py', 'verify_and_report.py', 'complete_verification.py',
        'package_completed.py', 'requirements-complete.txt', 'REPRODUCE.md',
        'verification.json', 'Exploratory_Regional_Results_and_Methods.md']]
    for folder in ['results', 'repeat', 'completion']:
        files += sorted((HERE / folder).glob('*'))
    files = sorted({p for p in files if p.is_file()})
    entries = {str(p.relative_to(BASE.parent)): p for p in files}
    manifest = {
        'scope': 'Completed exploratory regional analysis and verification; no source records',
        'date_local': '2026-11-02',
        'files': {name: {'sha256': sha(p), 'bytes': p.stat().st_size}
                  for name, p in entries.items()}
    }
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for name, p in entries.items():
            z.write(p, name)
        z.writestr('Package_Manifest.json', json.dumps(manifest, indent=2) + '\n')
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        for name, details in manifest['files'].items():
            assert hashlib.sha256(z.read(name)).hexdigest() == details['sha256'], name
        with tempfile.TemporaryDirectory(prefix='sphere_package_check_') as tmp:
            z.extractall(tmp)
            extracted = Path(tmp) / 'phase34/regional_extension'
            command = [sys.executable, str(extracted / 'complete_verification.py'),
                       '--data-dir', str(data_dir.resolve()),
                       '--output', str(extracted / 'completion_extracted_check')]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout + result.stderr)
            checked = json.loads((extracted / 'completion_extracted_check/completion_verification.json').read_text())
            assert checked['status'] == 'PASS'
            for name in ['independent_sensitivity_checks.csv', 'sensitivity_summary.csv',
                         'all_tests_with_sensitivity_changes.csv', 'main_results_summary.csv',
                         'diagnostic_page_index.csv']:
                assert (extracted / 'completion_extracted_check' / name).read_bytes() == (HERE / 'completion' / name).read_bytes(), name
    for relative, expected in baseline['baseline_sha256'].items():
        assert sha(HERE / relative) == expected, relative
    report = {
        'status': 'PASS',
        'archive': archive.name,
        'archive_sha256': sha(archive),
        'archive_bytes': archive.stat().st_size,
        'packaged_files_excluding_manifest': len(entries),
        'CRC_and_all_SHA256_checks': 'PASS',
        'extracted_package_verifier_exit_code': result.returncode,
        'extracted_sensitivity_verification': checked['status'],
        'five_reproduced_completion_CSVs_byte_identical': True,
        'earlier_artifacts_unchanged': True,
        'fresh_environment_installation_tested': False,
        'source_records_included': False
    }
    receipt.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=Path, required=True)
    main(parser.parse_args().data_dir)
