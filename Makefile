PYTHON ?= python3
.PHONY: build qa proof qa-fontspector
build:
	$(PYTHON) build.py
	$(PYTHON) prepare_submission.py
qa:
	$(PYTHON) qa/check_latin_core.py
	$(PYTHON) qa/check_shaping.py
	$(PYTHON) -m fontbakery check-googlefonts googlefonts/studya/*.ttf --skip-network --json qa/fontbakery.json --ghmarkdown qa/fontbakery.md -n
proof:
	$(PYTHON) qa/render_review.py
	$(PYTHON) qa/render_shaped.py

FONTSPECTOR ?= fontspector
qa-fontspector:
	$(FONTSPECTOR) -p googlefonts --timeout 15 --json qa/fontspector-network.json --ghmarkdown qa/fontspector-network.md googlefonts/studya/*.ttf
