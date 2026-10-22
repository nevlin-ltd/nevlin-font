PYTHON ?= python3
.PHONY: build qa proof
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
