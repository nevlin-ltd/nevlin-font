# Nevlin Sprout 1.001 RC2 — quality report

## Results

Fontspector 1.9.0, all four fonts:

| Profile | PASS | WARN | FAIL / ERROR / FATAL | SKIP | INFO |
|---|---:|---:|---:|---:|---:|
| Universal (network enabled) | 299 | 0 | 0 | 158 | 4 |
| Google Fonts (network enabled) | 411 | 8 | 0 | 248 | 22 |

The original prototype had 16 `alt_caron` warnings. All are resolved with
proper base-plus-side-accent components, rather than hiding or downgrading
checks. The first broader Google baseline had 21 failures and 52 warnings;
the remaining results are recorded above. Both baselines and current reports
are included so the improvement is auditable.

Network checks were enabled for the final Google run. SKIP results are retained
in the unfiltered report; a zero failure count does not mean every possible
check ran or that all onboarding requirements have been met.

## Eight remaining Google warnings

- **Vendor ID, four weights:** `NONE` remains honest until Nevlin's requested
  vendor registration is confirmed or the reviewer accepts a disposition.
  No unconfirmed registration has been represented as approved.
- **Serving subsets, four weights:** several accents, auxiliary Latin letters,
  arrows and math symbols are not covered by the standard Latin/Latin-ext
  serving ranges used by the checker. The glyphs remain in the fonts. Removing
  required accents or declaring unrelated writing systems would be incorrect.
  The exact points and proposed review request are in SERVING-SUBSETS.md.

Neither category is waived. Google decides acceptable warning dispositions.

## Structural and shaping checks

All four weights pass `check.py`:

- All 324 named requirements in the pinned official Latin Core list are present, including unencoded forms. See `qa/latin-core-coverage.json`.
- Catalan l·l/L·L and Turkish/Azeri dotted-i substitutions pass; English text does not receive Catalan substitutions.
- All four side-caron glyphs have two components with `caroncomb.alt` as the accent.
- No missing glyphs in NFD shaping of every encoded character.
- Contextual dot removal works for i, j and į with above marks, including an
  intervening below mark; unaccented į retains its dot.
- All digits have a 640-unit tabular advance; optional slashed zero works with it.
- TTF and WOFF2 maps match, and all outlines fit the declared vertical bounds.

The built-in Google language-shaping check also passes in all four weights.
Coverage and shaping are not a certification of native-language typography.

## Visual evidence

The 0.100 browser specimen was inspected at 12–24px in the previous iteration.
For RC1, the changed side accents, joined AE/OE forms, comma-below letters and
European extensions are rendered in `qa/accents.png` and `qa/accents.svg`.
The final candidate browser specimen and small-size rows are inspected again
and saved as `preview.png` and `readability-preview.png`.

Side carons are visibly separate from the stems. The flattened-letter warnings
are resolved structurally as well as visually. This review is not a native
Czech/Slovak proofread or an independent type designer's approval.

No live Figma, Safari, Windows, Android or iOS test of RC1 is claimed.
No manual TrueType hinting is claimed; `gasp` defines unhinted rendering behavior.
An independent clean-environment build and GitHub CI run remain outstanding.

## Integrity

No prior font is read by the build. Generated drawings remain available as UFO,
Python geometry and individual SVGs. Quantization adjustments are logged in
`qa/alignment-*.json`; each is limited to three font units on an on-curve point.
`reproducibility.json` records the repeated-build result and final file hashes.

## 1.001 correction

The earlier coverage assertion was incomplete: it tested codepoints only.
The official list also requires unencoded glyphs. The corrected validator maps
encoded names through Glyphs glyph data and explicitly checks unencoded names.
`qa/latin-core-localization.png` was rendered from HarfBuzz-shaped final binaries
and visually inspected. Older browser screenshots and baseline reports are
historical evidence, not new cross-platform validation.
