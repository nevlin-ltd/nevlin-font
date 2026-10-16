# Core Latin validation — 16 October 2026

| Checker (full Google Fonts profile, network enabled) | Pass | Fail | Error | Warn |
|---|---:|---:|---:|---:|
| FontBakery 1.1.0 | 613 | 0 | 0 | 12 |
| Fontspector 1.9.0 | 417 | 0 | 0 | 8 |

The checker suites and reporting units differ; their totals are not directly interchangeable. No checks were disabled, no warning severity was overridden, and no external approval is claimed.

## Repairs in this update

- Repaired acute contour joins with a small flat, trimming at most 24/2048 em on either adjacent segment after overlap removal. The reproducible `repair_joins.py` helper logs every changed glyph. All outline checks pass; before/after visual review, coverage and all advance-width comparisons pass. Regular and Medium outlines are unchanged.


- Added 50 auxiliary Latin characters already present in the source inventory. Language-shaping warnings are resolved.
- Added U+2028/U+2029 separators and U+20B9 rupee. The distributed repertoire now has 374 codepoints; all previous 321 remain.
- Normalized tiny axis slopes and redundant straight-line points in final contours, with at most one design-unit endpoint movement during axis normalization. Near-axis and redundant-point warnings are resolved.
- Corrected misleading inherited T-cedilla/T-comma glyph names without changing Unicode or drawing. Contour-count warning resolved.
- Added WWS-conformant metadata and STAT weight/italic axes, including italic linked value 1.
- Existing dot-removal, numeral alignment and coverage checks pass in all weights. Advance widths of all previous characters remain unchanged.
- Preserved the full beta separately; the NevlinUIPlus files are untouched.

## Remaining 12 FontBakery warning results

| Group | Results | What remains |
|---|---:|---|
| Designer catalog | 4 | Nevlin needs an accepted Google designer profile. Credit now uses Nevlin and Inter designer Rasmus Andersson; all upstream copyright notices remain. |
| Vendor ID | 4 | Microsoft registration is optional. NONE remains until a real vendor ID is confirmed; no borrowed registration is used. |
| Serving subsets | 4 | Google serving subsets omit required Latin Core marks. Preserve required coverage and request catalog review; do not add unrelated script claims. |

The current Fontspector report retains vendor and serving-subset warnings. The older FontBakery also reports unavailable designer profiles for both Nevlin and the correctly credited Inter designer; this is not evidence of incorrect attribution. See complete reports for details.

## Submission status

These are improved development fonts, not a warning-free or Google-approved release. The family remains substantially Inter-derived; originality/admission is a separate Google decision. External catalog acceptance and copyright-holder CLA requirements cannot be manufactured by changing local checker configuration.

See ONBOARDING-NOTES.md for the pending vendor request and designer-profile/subsetting notes. The Microsoft vendor registration request was sent on 16 October 2026 with user authorization. No Google onboarding issue, PR or agreement has been submitted. A review request is prepared in GOOGLE-FONTS-REVIEW-DRAFT.md.

Current Google QA guidance: https://googlefonts.github.io/gf-guide/qa.html

Warnings require human review and are not equivalent to FAIL. Remaining registry/catalog warnings cannot honestly be cleared by changing local font values alone. The package can be proposed for an initial eligibility review with these items disclosed; acceptance and production readiness are not claimed.
