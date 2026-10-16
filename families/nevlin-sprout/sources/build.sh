#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHON_BIN="${PYTHON_BIN:-python3}"
"$PYTHON_BIN" build.py
"$PYTHON_BIN" check.py
"$PYTHON_BIN" qa/check_latin_core.py
"$PYTHON_BIN" prepare_submission.py
