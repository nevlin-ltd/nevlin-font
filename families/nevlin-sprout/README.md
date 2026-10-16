# Nevlin Sprout — 1.000 RC1 review candidate

Original geometric sans-serif family for Nevlin's financial-learning product.
Four static upright weights: Regular 400, Medium 500, SemiBold 600 and Bold 700.
389 encoded characters, 404 glyphs per weight; full GF Latin Core coverage.

**Public review candidate. Not approved for the Google Fonts catalog.**
The earlier 0.100 prototype is preserved locally; this directory contains 1.000 RC1.
The existing Inter-derived Nevlin Font and its Google issue are unchanged.

## What changed

- Dedicated side-caron components for Ľ, ľ, ď and ť, with corrected spacing.
- Added missing core Latin and auxiliary European letters and symbols.
- Drew shared-stem AE/OE forms instead of overlapping complete letters.
- Corrected detached cedilla placement and added comma-below positioning.
- Added dotted-circle anchors and contextual dot removal under above accents.
- Preserved the dot in į when it does not have an additional above accent.
- Corrected family metadata, STAT, `gasp` and Latin script tags.
- Removed redundant straight-segment points and aligned quadratic on-curves
  within 3/1000 em of intended lines. Adjustment logs are in `qa/alignment-*.json`.
- Fontmake now compiles the editable UFO sources. Overlap removal happens in
  the source generator using pathops, before Fontmake runs.

## Checks

Fontspector 1.9.0:

| Profile | PASS | WARN | FAIL / ERROR / FATAL |
|---|---:|---:|---:|
| Universal, offline | 291 | 0 | 0 |
| Google Fonts, network enabled | 407 | 8 | 0 |

The eight Google warnings are four vendor-ID warnings and four serving-subset
warnings. They are **not suppressed or waived**. See QA.md and ONBOARDING.md.
Full Google output: `qa/googlefonts.json`, `qa/googlefonts.md`.

## Sources and build

Run these commands from `families/nevlin-sprout`.

No Inter, SF Pro or other font outlines or binaries are used as inputs.
Original source drawings are in `sources/design.py` and `sources/extended.py`.
The development process uses AI-assisted code and needs independent design review.

Use Python 3.12:

```sh
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r environment-lock.txt
python build.py
python check.py
python prepare_submission.py
```

`environment-lock.txt` pins the full environment used. `requirements.txt` lists
major direct dependencies. Run Fontspector 1.9.0 separately:

```sh
fontspector --profile googlefonts --full-lists \
  --json qa/googlefonts.json --ghmarkdown qa/googlefonts.md \
  googlefonts/nevlinsprout/*.ttf
```

No check exclusions, check-severity overrides, invented vendor registration,
or unsupported language-subset declarations are used.

The generator is authoritative and overwrites generated UFOs. To work in a
font editor, copy a UFO before editing it. Compile a modified copy with
Fontmake, then apply equivalent metadata/QA steps; direct UFO edits do not
backport themselves into the geometric generator. The checked candidate
binaries include the documented final quadratic-alignment step.

`reproducibility.json` records a same-environment repeated build of all eight
TTF/WOFF2 outputs. This is not an independent clean-machine build claim.
The included GitHub workflow is a prepared standalone-root template, not a
claim that GitHub CI has already run. If uploaded inside the existing font
repository, give its jobs that subdirectory as their working directory and
adjust artifact paths; do not replace the existing family's root files.

## Files

- `fonts/`: installable TTF and web WOFF2 files.
- `sources/`: editable UFOs and original drawing modules.
- `glyphs/`: individual SVG glyph exports.
- `googlefonts/nevlinsprout/`: metadata, license, fonts and article/specimen.
- `qa/`: full reports, accent proof, alignment logs and before/after evidence.
- `check.py`: coverage, components, shaping and numeric-feature assertions.
- `SUBMISSION-DRAFT.md`: preparation draft; the final public review request will be linked here.
- `ONBOARDING.md`: remaining external and human-review steps.
- `index.html`: interactive review specimen.
- `OFL.txt`: SIL Open Font License 1.1, no Reserved Font Names.

Install the TTFs and select **Nevlin Sprout**. For web use declare each WOFF2
with its corresponding CSS weight. Use `font-variant-numeric: tabular-nums`
for aligned amounts and `font-feature-settings: 'zero' 1` for a slashed zero.

## Limits

The name is provisional; Google naming eligibility and uniqueness are not
confirmed. Technical passes do not establish editorial acceptance. Spacing,
optical consistency, accents, hinting needs and small-text behavior still need
independent type-design/native-language and cross-platform review.
