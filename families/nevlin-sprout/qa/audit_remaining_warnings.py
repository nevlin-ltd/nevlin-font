"""Extract unresolved warnings without changing fonts or QA severity."""
from pathlib import Path
import hashlib
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
report_path = ROOT / 'qa/googlefonts.json'
report = json.loads(report_path.read_text())
warnings = []
for target, sections in report['results'].items():
    for checks in sections.values():
        for check in checks:
            if check['worst_status'] == 'WARN':
                for result in check['subresults']:
                    if result['severity'] == 'WARN':
                        warnings.append({'target': target, 'check_id': check['check_id'],
                                         'message': result})
counts = Counter(w['check_id'] for w in warnings)
assert len(warnings) == report['summary']['WARN'] == 8
assert counts == {'googlefonts/vendor_id': 4,
                  'googlefonts/metadata/unreachable_subsetting': 4}, counts
hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
          for p in sorted((ROOT / 'fonts').glob('*.ttf'))}
audit = {'status': 'unresolved; external disposition required',
         'source_report': 'qa/googlefonts.json',
         'source_report_sha256': hashlib.sha256(report_path.read_bytes()).hexdigest(),
         'font_sha256': hashes, 'counts': dict(counts), 'warnings': warnings,
         'resolution_requirements': {
             'googlefonts/vendor_id': 'Confirm Nevlin vendor registration, then update source vendor ID, rebuild and rerun QA. A registry-cache lag may require evidence for reviewers.',
             'googlefonts/metadata/unreachable_subsetting': 'Obtain Google guidance on serving the 18 retained codepoints. Do not claim unrelated scripts or delete required marks to clear the check.'},
         'registration_verification': {
             'public_registry': 'NVLN/Nevlin not found during this review',
             'mailbox': 'Current lookup unavailable: rate-limit/permission error. No conclusion about replies.'},
         'check_exclusions_added': False, 'severity_overrides_added': False}
(ROOT / 'qa/remaining-warning-audit.json').write_text(json.dumps(audit, indent=2, ensure_ascii=False)+'\n')
print(json.dumps({'warning_count': len(warnings), 'counts': dict(counts), 'font_binaries_changed': False}, indent=2))
