# Validation baseline — 2026-10-16

FontBakery 1.1.0 universal profile, four existing beta TTFs, with network checks disabled.

268 PASS · 23 FAIL · 20 WARN · 149 SKIP · 12 INFO. These are check results across fonts, not unique defects.

This is not a Google Fonts acceptance report. The full Google Fonts profile could not run because its optional dependency installation failed resolution. No font binaries were changed in this baseline.

## Failing check groups

- `opentype.family.underline_thickness`: 1 results
- `opentype.fsselection`: 1 results
- `opentype.mac_style`: 1 results
- `base_has_width`: 4 results
- `case_mapping`: 4 results
- `family.win_ascent_and_descent`: 4 results
- `no_mac_entries`: 4 results
- `smart_dropout`: 4 results

Full details: [FontBakery report](fontbakery-universal.md).

## Outstanding work

- Review and repair failures and warnings; rerun checks.
- Complete Google Fonts profile in a compatible, pinned environment.
- Prepare editable sources and a reproducible Fontmake build preserving shaping.
- Complete rendering, spacing, and design review. Most outlines remain inherited from Inter; passing checks cannot resolve originality or guarantee admission.
