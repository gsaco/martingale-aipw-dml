#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

DESIGNS = ["A", "B", "C1", "C2", "D"]
REQUIRED_TABLES = [
    "sim_designA_main.csv",
    "sim_designA_conditional.csv",
    "sim_designB.csv",
    "sim_designC1.csv",
    "sim_designC2.csv",
    "sim_designD.csv",
]
REQUIRED_FIGURES = ["var_ratio_hist.pdf"]
EXPECTED_REPS = 1000


def fail(msg: str) -> None:
    print(f"[FAIL] {msg}")
    raise SystemExit(1)


def validate_configs() -> None:
    for design in DESIGNS:
        cfg_path = ROOT / "artifacts" / "sim" / design / "config.json"
        if not cfg_path.exists():
            fail(f"Missing config: {cfg_path}")
        with cfg_path.open("r", encoding="utf-8") as f:
            cfg = json.load(f)
        n_reps = cfg.get("global", {}).get("n_reps")
        if n_reps != EXPECTED_REPS:
            fail(f"{cfg_path}: expected global.n_reps={EXPECTED_REPS}, got {n_reps}")
        print(f"[OK] {cfg_path} (n_reps={n_reps})")


def validate_tables() -> None:
    for name in REQUIRED_TABLES:
        path = ROOT / "tables" / name
        if not path.exists():
            fail(f"Missing table CSV: {path}")
        df = pd.read_csv(path)
        if "n_rep" in df.columns:
            reps = sorted(df["n_rep"].dropna().unique().tolist())
            if reps != [EXPECTED_REPS]:
                fail(f"{path}: expected n_rep={[EXPECTED_REPS]}, got {reps}")
            print(f"[OK] {path} (rows={len(df)}, n_rep={reps[0]})")
            continue

        # Design A conditional table stores per-regime counts instead of n_rep.
        if name == "sim_designA_conditional.csv":
            required_cols = {"n", "method", "count"}
            if not required_cols.issubset(df.columns):
                fail(f"{path}: expected columns {sorted(required_cols)}")
            grouped = (
                df.groupby(["n", "method"], as_index=False)["count"].sum().rename(columns={"count": "count_sum"})
            )
            bad = grouped[grouped["count_sum"] != EXPECTED_REPS]
            if not bad.empty:
                fail(
                    f"{path}: expected regime counts to sum to {EXPECTED_REPS} per (n,method), "
                    f"found {bad.to_dict(orient='records')}"
                )
            print(f"[OK] {path} (rows={len(df)}, regime counts sum to {EXPECTED_REPS})")
            continue

        fail(f"{path}: missing 'n_rep' column")


def validate_figures() -> None:
    for name in REQUIRED_FIGURES:
        path = ROOT / "figures" / name
        if not path.exists():
            fail(f"Missing figure: {path}")
        print(f"[OK] {path}")


def main() -> None:
    print("Validating replication artifacts for Designs A, B, C1, C2, D")
    validate_configs()
    validate_tables()
    validate_figures()
    print("[SUCCESS] Replication artifacts are present and consistent (n_rep=1000).")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        fail(str(exc))
