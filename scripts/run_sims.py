#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Notebook-first replication runner for simulation Designs A/B/C1/C2/D."
    )
    parser.add_argument(
        "--notebook",
        default="all_simulations_unified.ipynb",
        help="Notebook to execute (path relative to repo root).",
    )
    parser.add_argument(
        "--output",
        default="artifacts/notebook_runs/all_simulations_unified.executed.ipynb",
        help="Executed notebook output path (relative to repo root).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=-1,
        help="Cell timeout in seconds for nbconvert (default: -1 for no timeout).",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run scripts/validate_replication.py after execution.",
    )
    parser.add_argument(
        "--skip-execution",
        action="store_true",
        help="Skip notebook execution and only run validation (if --validate is set).",
    )
    return parser.parse_args()


def run_notebook(notebook: Path, output: Path, timeout: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        sys.executable,
        "-m",
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        str(notebook),
        "--ExecutePreprocessor.timeout",
        str(timeout),
        "--output",
        output.name,
        "--output-dir",
        str(output.parent),
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)


def run_validation() -> None:
    cmd = [sys.executable, str(ROOT / "scripts" / "validate_replication.py")]
    subprocess.run(cmd, check=True, cwd=ROOT)


def main() -> None:
    args = parse_args()
    notebook = (ROOT / args.notebook).resolve()
    output = (ROOT / args.output).resolve()

    if not notebook.exists():
        raise FileNotFoundError(f"Notebook not found: {notebook}")

    if not args.skip_execution:
        run_notebook(notebook=notebook, output=output, timeout=args.timeout)

    if args.validate:
        run_validation()


if __name__ == "__main__":
    main()
