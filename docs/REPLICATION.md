# Replication Guide

This guide reproduces the simulation artifacts used in `main.tex` for Designs
`A`, `B`, `C1`, `C2`, and `D`.

## 1. Environment

1. Use Python 3.11+.
2. Install requirements:
   - `pip install -r requirements.txt`

## 2. Run the notebook

Execute the full simulation notebook and save an executed copy:

- `python scripts/run_sims.py`

Run notebook + validation in one command:

- `python scripts/run_sims.py --validate`

Output notebook:

- `artifacts/notebook_runs/all_simulations_unified.executed.ipynb`

## 3. Validate expected outputs

Validation checks:

- `artifacts/sim/{A,B,C1,C2,D}/config.json` exist and `global.n_reps=1000`
- required table CSV files exist and have `n_rep=1000`
- required paper figure exists (`figures/var_ratio_hist.pdf`)

Run validation directly:

- `python scripts/validate_replication.py`

## 4. Output files used in paper

- Design A main: `tables/sim_designA_main.csv`
- Design A conditional: `tables/sim_designA_conditional.csv`
- Design B: `tables/sim_designB.csv`
- Design C1: `tables/sim_designC1.csv`
- Design C2: `tables/sim_designC2.csv`
- Design D: `tables/sim_designD.csv`
- Figure (variance ratio): `figures/var_ratio_hist.pdf`

The current manuscript writes simulation tables directly in `main.tex` (no
`\input{...}` dependence).

