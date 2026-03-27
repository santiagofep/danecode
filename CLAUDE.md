# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DaneCode is a Python utility package (published to PyPI) for looking up Colombian DANE codes (geographic identifiers) by department and municipality names. It handles typos via Levenshtein distance fuzzy matching and normalizes Unicode/accents with unidecode.

## Commands

```bash
# Install in development mode
pip install -e .

# Run tests
python -m unittest tests

# Build distribution
python -m build

# Check and publish to PyPI
python3 -m twine check dist/*
python3 -m twine upload dist/*
```

## Architecture

There are two independent data lookup paths:

1. **`get_data(department, municipality)`** — Main public API. Uses the hardcoded dictionary in `danecode/country_data.py` (departments → municipalities → DANE codes). Fuzzy matches both department and municipality names using `get_less_distant_item()` in `__init__.py`.

2. **`coordinadora_center_of_population(location)`** — Parses Coordinadora location format `"CITY (DEPT_CODE)"`, maps the abbreviation to a department name via `services/__init__.py`, then loads the corresponding CSV from `danecode/files/centros_poblados/{dept_code}.csv` using pandas to find the closest center of population.

### Data sources

- `danecode/country_data.py` — Hardcoded Python dict with all departments and municipalities (used by `get_data`)
- `danecode/files/departamentos.csv` — Department code-to-name mapping (used by services)
- `danecode/files/centros_poblados/*.csv` — Per-department CSV files with detailed center-of-population records (used by `coordinadora_center_of_population`)

### Dependencies

- **jellyfish** — Levenshtein distance for fuzzy matching
- **pandas** — CSV file loading in services
- **unidecode** — Accent/unicode normalization

## Conventions

- Variable and data names use Spanish: `departamento`, `municipio`, `centro_poblado`
- CSV files in `centros_poblados/` are named by two-digit department DANE code (e.g., `05.csv` for Antioquia)
- Version is maintained in `pyproject.toml`
