# Nevlin Font

An Inter-derived, SIL OFL-licensed font project by Nevlin. **Core Latin development candidate 1.000**, not a Google Fonts-approved release.

## Current candidate

321 encoded characters across Regular 400, Medium 500, SemiBold 600 and Bold 700. The installed family name is **Nevlin Font**.

- Download [the complete editable source and font package](NevlinFont-core-latin-candidate.zip).
- Individual desktop files: [Regular](NevlinFont-Regular.ttf), [Medium](NevlinFont-Medium.ttf), [SemiBold](NevlinFont-SemiBold.ttf), [Bold](NevlinFont-Bold.ttf). Matching WOFF2 files are included for websites.
- View the [alphabet proof](core-character-proof.svg).
- Read [validation and remaining warnings](CORE-VALIDATION.md).

Full Google Fonts profile: **595 PASS, 0 FAIL, 0 ERROR, 22 WARN**. Warnings have not been suppressed. Outline review, optional language coverage, catalog subsets and designer/vendor profiles remain under review. Google admission and originality review are separate from these checks.

## Editable sources and build

The four `NevlinFont-*.glyphs` files are editable text sources. The source archive also includes UFO 3 files. The sources retain the full design inventory; `repertoire.json` selects the core distribution. The build compiles with Fontmake and adds the documented i/j/į accent rules, exposed in generated UFO features. No binary font is a build input.

Use Python 3.12:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements-lock.txt
python build_core.py
python check_core.py
python prepare_core_submission.py
fontbakery check-googlefonts googlefonts/nevlinfont/*.ttf
```

Outputs: `fonts/ttf/`, `fonts/woff2/`, `build/ufos/`, and `googlefonts/nevlinfont/`. The ZIP has the same workflow with the original script names `build.py` and `prepare_submission.py`.

## Preserved full beta

The older `NevlinUIPlus-*.ttf` and `.woff2` files remain unchanged: v0.400, 2,852 encoded characters, broader Latin/Greek/Cyrillic coverage. Its original `build.py`, `redraw.py`, `InterVariable.ttf`, `requirements.txt`, `QA.json` and beta validation files remain historical materials. Use `build_core.py` for the current candidate; the old `build.py` rebuilds the full beta.

## Design and license

Most letterforms, spacing and layout functionality are inherited from Inter 4.001 by the Inter Project Authors. Nevlin modifications include a, e, g, r, t, 1, 4, 7, dots, Q tail and tenge bars. This is not an independently drawn full family and contains no Apple font software.

SIL Open Font License 1.1; preserve copyright notices and OFL.txt when redistributing. Inter-OFL.txt preserves the upstream license. Using the font in a design does not require an attribution link.

Project: https://github.com/nevlin-ltd/nevlin-font  
Website: https://nevlin.com  
Contact: zhanat.salimova@nevlin.com

No Google Fonts submission or acceptance is claimed. This separate font project does not restore the canceled Nevlin website font page.
