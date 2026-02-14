PYTHON ?= python

.PHONY: replicate validate

replicate:
	$(PYTHON) scripts/run_sims.py --validate

validate:
	$(PYTHON) scripts/validate_replication.py

