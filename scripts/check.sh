#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 tests/run.py
python3 benchmarks/run.py
