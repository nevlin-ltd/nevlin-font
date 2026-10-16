# Core Latin validation — 16 October 2026

Full Google Fonts profile, with network checks enabled: **595 PASS, 0 FAIL, 0 ERROR, 22 WARN, 247 SKIP, 29 INFO**. No checks disabled or warnings suppressed.

All four weights contain the 321 requested codepoints. Coverage, tabular-digit alignment, specimen coverage and i/j/į dot removal pass the supplied check_core.py. The earlier broad candidate remains unchanged (all eight binary hashes verified against its manifest).

The editable Glyphs/UFO sources retain the full design inventory. repertoire.json controls the core distribution. build.py adds explicit dot-removal rules and a dotless-ogonek alternate, retaining its mark-positioning lookups; generated UFOs expose those rules for editing. The broad candidate has a separately verified reproducible build; this core candidate has not yet undergone a second independent clean-build comparison.

## Remaining warnings

| Check | Weight-level results | Disposition |
|---|---:|---|
| vendorspecific.googlefonts.metadata.designer_profiles | 4 | Needs Google designer catalog profiles; no profiles or photos submitted. |
| vendorspecific.googlefonts.metadata.unreachable_subsetting | 4 | 13 Latin accents/symbols fall outside the selected serving subsets. Preserve required Latin Core coverage; coordinate serving ranges with Google. Do not falsely claim other scripts. |
| vendorspecific.googlefonts.glyphsets.shape_languages | 4 | Missing optional auxiliary orthography characters. Mandatory language shaping passes; optional language expansion remains outside this core release. |
| outline_colinear_vectors | 1 | Review near-collinear K segments; no waiver has been approved. |
| outline_jaggy_segments | 2 | Review joins on inherited M and customized g; no waiver has been approved. |
| outline_semi_vertical | 3 | Review near-axis optical segments; no waiver has been approved. |
| vendorspecific.googlefonts.vendor_id | 4 | Vendor ID is unregistered. Registration is optional and has not been claimed. |

## Admission is separate from testing

This remains an Inter-derived development candidate. Zero automated failures do not establish originality, visual quality or Google Fonts acceptance. Human outline review, cross-platform rendering, design eligibility and the copyright-holder agreement process remain before submission. No Google onboarding issue, PR or CLA has been sent.

The full machine-readable and Markdown reports are in core-fontbakery.json and core-fontbakery.md (also in the source archive). The full beta is separately preserved as the unchanged NevlinUIPlus files in this repository.
