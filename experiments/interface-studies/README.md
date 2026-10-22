# Interface design studies — experimental

Local design revisions following the Google Fonts design-quality rejection of Nevlin Font (#11141) and Nevlin Sprout (#11142) on 22 October 2026. These fixes do not establish that the reviewer’s overall design concerns have been resolved. Neither submission is reopened by this commit.

## Review

Open `B-reworked.html` for the current B2 comparison, text tester, complete character sheet and before/after proofs. `index.html` retains the A/B directions. B2 is the current working direction; A and B are comparisons.

Each study contains one Regular style: 101 encoded characters and 112 glyphs including tabular alternates. Sources are editable UFOs and Python drawings. TTF, WOFF2 and per-glyph SVG exports are included.

Changes include wider B2 proportions, a two-storey a, revised e/o/n/h/m/r/l/t/M/1, continuous G construction, the repaired lower-left B join and taller SVG export frames. Some earlier Sprout drawings remain. These are revisions of that project, not wholly independent completed families or modifications of Inter outlines.

## Build and checks

Use a Python environment with fonttools[woff], skia-pathops, ufoLib2 and Pillow. From this directory run:

    python sources/build.py
    python sources/audit.py

`qa/audit.json` records glyph bounds, closed/tiny contour checks, G/B contour topology, character-map agreement and equal tabular advances. Proof images were visually inspected. These checks do not certify design quality, full Latin Core coverage, complete kerning, hinting, language support or cross-platform rendering.

## Before further submission

Obtain a detailed independent type-design critique; refine outlines, optical alignment and spacing; select and clear a public family name; confirm ownership, licensing/CLA and maintenance commitments; expand language coverage and run current full validation. Do not claim Google approval or submission readiness.

The earlier release candidates remain unchanged. Working labels A, B and B2 are not proposed final names.
