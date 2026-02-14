#!/usr/bin/env bash
set -euo pipefail

mkdir -p artifacts/sim tables figures

python scripts/run_sims.py --validate
