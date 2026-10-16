# Core Latin validation — 16 October 2026

| Checker (full Google Fonts profile, network enabled) | Pass | Fail | Error | Warn |
|---|---:|---:|---:|---:|
| FontBakery 1.1.0 | 611 | 0 | 0 | 14 |
| Fontspector 1.9.0 | 415 | 0 | 0 | 10 |

The checker suites and reporting units differ; their totals are not directly interchangeable. No checks were disabled, no warning severity was overridden, and no external approval is claimed.

## Repairs in this update

- Added 50 auxiliary Latin characters already present in the source inventory. Language-shaping warnings are resolved.
- Added U+2028/U+2029 separators and U+20B9 rupee. The distributed repertoire now has 374 codepoints; all previous 321 remain.
- Normalized tiny axis slopes and redundant straight-line points in final contours, with at most one design-unit endpoint movement during axis normalization. Near-axis and redundant-point warnings are resolved.
- Corrected misleading inherited T-cedilla/T-comma glyph names without changing Unicode or drawing. Contour-count warning resolved.
- Added WWS-conformant metadata and STAT weight/italic axes, including italic linked value 1.
- Existing dot-removal, numeral alignment and coverage checks pass in all weights. Advance widths of all previous characters remain unchanged.
- Preserved the full beta separately; the NevlinUIPlus files are untouched.

## Remaining 14 FontBakery warning results

| Group | Results | What remains |
|---|---:|---|
| Designer catalog | 4 | Nevlin needs an accepted Google designer profile. Credit now uses Nevlin and Inter designer Rasmus Andersson; all upstream copyright notices remain. |
| Vendor ID | 4 | Microsoft registration is optional. NONE remains until a real vendor ID is confirmed; no borrowed registration is used. |
| Serving subsets | 4 | Google serving subsets omit required Latin Core marks. Preserve required coverage and request catalog review; do not add unrelated script claims. |
| Tight outline joins | 2 | SemiBold r and Bold M/g (including derivatives) trigger an acute-angle heuristic. Enlarged visual proof shows the flags at the intentional-looking stem/shoulder and bowl junctions. Kept for qualified type-design/Google review rather than reshaping approved letters solely for the checker. No waiver is approved. |

The current Fontspector report also retains vendor, serving-subset and tight-join warnings. See complete reports for details.

## Submission status

These are improved development fonts, not a warning-free or Google-approved release. The family remains substantially Inter-derived; originality/admission is a separate Google decision. External catalog acceptance, outline review and copyright-holder CLA requirements cannot be manufactured by changing local checker configuration.

See ONBOARDING-NOTES.md for the unsent vendor request and designer-profile/subsetting notes. No emails, PRs, onboarding issues or agreements have been submitted.

Current Google QA guidance: https://googlefonts.github.io/gf-guide/qa.html
