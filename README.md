# Martingale AIPW/DML Replication Package

Replication package for the manuscript:
`Fixed-Horizon Self-Normalized Wald Inference for Adaptive Experiments via Martingale AIPW/DML with Logged Propensities`.

This repository is prepared for research collaboration and reproducibility review.
The simulation pipeline is notebook-first, with one canonical implementation:

- `all_simulations_unified.ipynb`

## What Is Included

- Executable simulation workflow for Designs `A`, `B`, `C1`, `C2`, `D`
- Replication-level artifacts in `artifacts/sim/`
- Publication-ready aggregate tables in `tables/`
- Figures in `figures/`
- Manuscript PDF (`main.pdf`)

Note:
- The manuscript LaTeX source is intentionally not distributed in this shared package.

## Repository Structure

- `all_simulations_unified.ipynb`: canonical simulation and aggregation workflow
- `scripts/run_sims.py`: executes the notebook and optionally runs validation
- `scripts/validate_replication.py`: validates required outputs and replication counts
- `scripts/make_sim_artifacts.sh`: one-command simulation + validation runner
- `docs/REPLICATION.md`: detailed replication steps
- `docs/FILE_MAP.md`: design-to-output mapping
- `artifacts/sim/`: replication-level outputs by design and method
- `tables/`: aggregated CSVs used for manuscript reporting
- `figures/`: paper figures
- `main.pdf`: manuscript PDF

## Quick Start

1. Create a Python 3.11+ environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Run full replication and validation:
   - `python scripts/run_sims.py --validate`
   - or `make replicate`

Executed notebook output is saved to:

- `artifacts/notebook_runs/all_simulations_unified.executed.ipynb`

## Validation Checklist

Validation (`python scripts/validate_replication.py`) checks that:

- Each design config exists: `artifacts/sim/{A,B,C1,C2,D}/config.json`
- Each design uses `global.n_reps = 1000`
- Required table files exist and carry the expected replication counts
- Required figure exists: `figures/var_ratio_hist.pdf`

## Canonical Output Files

- `tables/sim_designA_main.csv`
- `tables/sim_designA_conditional.csv`
- `tables/sim_designB.csv`
- `tables/sim_designC1.csv`
- `tables/sim_designC2.csv`
- `tables/sim_designD.csv`
- `figures/var_ratio_hist.pdf`

## Reproducibility Notes

- Randomization and design settings are recorded in per-design `config.json` files.
- Replication artifacts are already included for direct inspection.
- Re-running the notebook regenerates tables and figures from source simulation code.

## License

This repository is released under the license in `LICENSE`.
