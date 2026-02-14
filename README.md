# martingale-dml

Replication repository for the paper:
`Self-Normalized Martingale AIPW/DML for Adaptive Experiments with Logged Propensities`.

This repository is organized for a notebook-first replication workflow.
The single source of truth for the simulation pipeline is:

- `all_simulations_unified.ipynb`

The notebook itself is treated as the canonical implementation and is not
rewired to external Python modules.

The paper file is:

- `main.tex`

## Quick start

1. Create and activate an environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run the simulation notebook and validate outputs:
   - `python scripts/run_sims.py --validate`
   - or `make replicate`

Executed notebook output is written to:

- `artifacts/notebook_runs/all_simulations_unified.executed.ipynb`

## Canonical replication outputs

- Raw replication-level outputs: `artifacts/sim/`
- Aggregated tables (CSV): `tables/`
- Figures used by the paper: `figures/`

For the current paper version, the key designs are:

- `A`, `B`, `C1`, `C2`, `D`

and the key table files are:

- `tables/sim_designA_main.csv`
- `tables/sim_designA_conditional.csv`
- `tables/sim_designB.csv`
- `tables/sim_designC1.csv`
- `tables/sim_designC2.csv`
- `tables/sim_designD.csv`

## Repository map

- `main.tex`: manuscript (simulation tables are typed directly in this file)
- `all_simulations_unified.ipynb`: simulation engine and result generation
- `scripts/run_sims.py`: execute notebook + optional validation
- `scripts/validate_replication.py`: consistency checks for paper designs
- `docs/REPLICATION.md`: step-by-step reproducibility guide
- `docs/FILE_MAP.md`: design-to-output mapping
- `archive/legacy/`: old drafts and legacy outputs kept for provenance
- `Makefile`: convenience commands (`make replicate`, `make validate`)
