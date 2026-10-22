# Direction A — active design study

The latest four-weight, Latin Core candidate is in [production/](production/README.md). Open [production/index.html](production/index.html) for the current specimen. The original 101-character study below is retained as a baseline; its limited audit is not the current coverage report.

Selected by the user on 22 October 2026. First refinement revises D/P/R/U/S and 3/5/6/8/9 to reduce the contrast between boxier inherited forms and A's oval lowercase. This does not establish that Google's design-quality concerns are resolved.

Open index.html to compare the original and revised A, type sample text, inspect 12–20 px reading samples and toggle tabular numbers. Unsupported characters are identified rather than silently presented as our design. qa/proof.png is a Pillow rendering, not a cross-browser certification.

Editable UFO, TTF, WOFF2 and SVG exports are in A/. sources/build.py uses the shared interface-studies builder and earlier project drawings. Run it from a Python environment with fonttools[woff], skia-pathops, ufoLib2; sources/proof.py also requires Pillow and glyphsLib. The complete repository is required to resolve the shared sources and pinned Latin Core reference.

## Current results

112 glyphs; 101 encoded characters; no construction issues detected by the limited audit; TTF/WOFF2 cmap match; equal tabular advances. 223 requirements from the existing pinned Latin Core list are missing. See qa/report.json for the explicit list.

## Next design work

1. Refine lowercase optical alignment, joins, spacing and small-size text colour; review I/l/1, O/0 and rn/m.
2. Complete missing characters, accents and mark placement after settling the base glyphs. Review language samples.
3. Add weights, kerning and production build/QA, and check actual browsers/platforms.
4. Obtain independent design critique; resolve naming, ownership, CLA and maintenance commitments before submission.

Only the first capital/figure consistency pass is complete. No Google request was reopened and no approval is implied. The earlier A and B studies remain intact.
