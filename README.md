> **22 October 2026 development update:** Direction A is being revised after Google’s design-quality feedback. See [the preliminary review candidate](experiments/interface-a/production/README.md). Its name and governance confirmations are pending; no new Google submission is implied.

# Nevlin Font

An Inter-derived, SIL OFL-licensed font project by Nevlin. **Core Latin development candidate 1.001**, not a Google Fonts-approved release.

## New original family: Nevlin Sprout

[Nevlin Sprout](families/nevlin-sprout) is a separate original geometric family for financial-learning interfaces. Its 1.001 RC2 package includes four weights, editable UFOs, drawing sources, build instructions, specimens and full QA evidence. It is not derived from the Inter-based family below. [The initial Google review #11129](https://github.com/google/fonts/issues/11129) identified incomplete Latin Core validation. RC2 corrects the missing unencoded forms and tests all 324 official glyph requirements. Eight vendor/subset warnings remain disclosed. [Official-template resubmission #11130](https://github.com/google/fonts/issues/11130) includes the correction evidence.

## Current candidate

374 encoded characters across Regular 400, Medium 500, SemiBold 600 and Bold 700. The installed family name is **Nevlin Font**.

- Download [the complete editable source and font package](NevlinFont-core-latin-candidate.zip).
- Individual desktop files: [Regular](NevlinFont-Regular.ttf), [Medium](NevlinFont-Medium.ttf), [SemiBold](NevlinFont-SemiBold.ttf), [Bold](NevlinFont-Bold.ttf). Matching WOFF2 files are included for websites.
- View the [alphabet proof](core-character-proof.svg).
- Read [validation and remaining warnings](CORE-VALIDATION.md).

Latest candidate 1.001: **Fontspector 1.9.0 Google profile: 418 PASS, 0 FAIL/ERROR/FATAL, 8 WARN** (19 October 2026, network checks enabled). All 324 official Latin Core named entries and Catalan/Turkish/Azeri shaping checks pass in four weights. The earlier FontBakery 613-pass report applies to 1.000, not this rebuilt candidate. Vendor registration and serving-subset warnings remain unresolved; no checks are suppressed. See [current evidence](qa/latin-core-googlefonts.md) and [coverage report](qa/latin-core-coverage.json). Google admission, naming, ownership/CLA and maintainer commitments remain pending.

## Editable sources and build

The four `NevlinFont-*.glyphs` files are editable text sources. The source archive also includes UFO 3 files. The sources retain the full design inventory; `repertoire.json` selects the core distribution. The build compiles with Fontmake and adds the documented i/j/į accent rules, exposed in generated UFO features. The `repair_joins.py` source helper trims needle-like junctions after overlap removal and logs each repair. No binary font is a build input.

Use Python 3.12:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements-lock.txt
python build_core.py
python check_core.py
python check_latin_core.py
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

Google Fonts review is requested; no acceptance is claimed. This separate font project does not restore the canceled Nevlin website font page.

Current Google guidance uses Fontspector. Install the [official checker](https://github.com/fonttools/fontspector/blob/main/INSTALLATION.md) and run `fontspector -p googlefonts googlefonts/nevlinfont/*.ttf`. Both full reports are published in this repository.

The earlier Inter-derived family has its own [Google review request #11128](https://github.com/google/fonts/issues/11128). Remaining warnings need external review, not fabricated registry entries or reduced required coverage.
