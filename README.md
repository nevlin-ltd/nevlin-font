# Nevlin Font

A free, open-source font for exploring finance interfaces. Public beta v0.400.
Four weights: Regular 400, Medium 500, Semibold 600 and Bold 700.
2,852 encoded characters per weight. TTF and WOFF2 files are included; the build also generates individual SVG glyphs.

Project: https://github.com/nevlin-ltd/nevlin-font
Website: https://nevlin.com
Contact: zhanat.salimova@nevlin.com

## Install

Desktop: open the TTF files in this repository and install each weight. Restart your design app.
Web: copy the WOFF2 files and nevlin-ui-plus.css together to your website, then load the stylesheet.

```css
body { font-family: "Nevlin UI Plus", system-ui, sans-serif; }
.amount { font-variant-numeric: tabular-nums; }
```

Only upright styles are supplied. Avoid synthetic italics if you need a designed italic.

## Design and origin

Derived from Inter 4.001 by the Inter Project Authors. Nevlin customizations include
redrawn a, e, g, r, t, 1, 4 and 7; adjusted dots, Q tail and tenge bars. Most of the
family and its OpenType functionality are inherited from Inter. This is not an
independently drawn full family and contains no Apple font software.

The single-storey g, rising e crossbar, short-footed 1, open 4 and uncrossed 7
are part of this version. Four weights have slightly more ink than Nevlin UI v0.300.

## License

SIL Open Font License 1.1. Retain OFL.txt and its copyright notice when redistributing
the font. See the full license for its terms. Personal and commercial use is allowed.
A link to the project page is welcome but never required. Your designs are not
required to use the font's license. Upstream: https://github.com/rsms/inter

## Beta status

The design is frozen for review. Optical spacing, small-size readability, hinting,
mark placement and cross-platform QA are not production-certified. Outlines retain
prototype overlaps (including open 4). The inherited optical size is fixed at 28;
review body text at your intended sizes. Some alternate forms remain upstream.
Report the character, weight, size, application, operating system and a screenshot
of any issue to the release contact. Do not send confidential interface content.

## Rebuild

Python 3.9 or later:

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python build.py
```

The exact upstream input and its provenance are in InterVariable.ttf and upstream-provenance.json. Rebuilding
generates the four TTFs, four WOFF2s and SVG glyphs. No Apple fonts are needed.
See FONTLOG.txt and QA.json for the earlier beta checks. New validation reports are separate from those checks.

## Google Fonts preparation

This repository is a development baseline, not a Google Fonts-approved release.
Most outlines remain derived from Inter. Passing automated checks does not establish
originality. Editable UFO sources, a Fontmake build, complete FontBakery validation,
and typography review are still required. The Nevlin website font rollout was canceled;
this separate project does not restore it.
