POETRY ?= poetry
PYTHON ?= python3
VENV_DIR ?= .venv
VENV_PYTHON := $(VENV_DIR)/bin/python
EX ?=
EXERCISM ?= exercism
.PHONY: help bootstrap test test-all shell

help:
	@printf "Targets:\n"
	@printf "  make bootstrap   Use Poetry when available, otherwise create .venv\n"
	@printf "  make test        Run tests from the repo root\n"
	@printf "  make test EX=... Run tests for a specific exercise folder\n"
	@printf "  make shell       Show the preferred activation command\n"

bootstrap:
	@if command -v $(POETRY) >/dev/null 2>&1; then \
		$(POETRY) install --no-root; \
	else \
		$(PYTHON) -m venv $(VENV_DIR); \
	fi

test:
	@if command -v $(POETRY) >/dev/null 2>&1; then \
		$(POETRY) run python runtests.py $(EX); \
	elif [ -x "$(VENV_PYTHON)" ]; then \
		$(VENV_PYTHON) runtests.py $(EX); \
	else \
		$(PYTHON) runtests.py $(EX); \
	fi

test-all:
	@if command -v $(POETRY) >/dev/null 2>&1; then \
		$(POETRY) run python runtests.py; \
	elif [ -x "$(VENV_PYTHON)" ]; then \
		$(VENV_PYTHON) runtests.py; \
	else \
		$(PYTHON) runtests.py; \
	fi

shell:
	@if command -v $(POETRY) >/dev/null 2>&1; then \
		printf '%s\n' 'eval $$(poetry env activate)'; \
	else \
		printf "source $(VENV_DIR)/bin/activate\n"; \
	fi

submit:
	@if command -v $(POETRY) >/dev/null 2>&1; then \
		$(POETRY) run python submit.py $(EX); \
	elif [ -x "$(VENV_PYTHON)" ]; then \
		$(VENV_PYTHON) submit.py $(EX); \
	else \
		$(PYTHON) submit.py $(EX); \
	fi
