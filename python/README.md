# Competitive Programming (Python)

## Overview

This directory contains Python implementations of common competitive-programming algorithms and data structures, plus `pytest` test coverage for most modules.

Current covered areas include:
- Algorithms: binary search, sorting, sliding window, two pointers, Dutch national flag, bitwise operations, prefix/postfix sum, majority voting, backtracking variants.
- Data structures: stack, queue, linked list, vector, hash table, graph, suffix array.

## Stack & Tooling Detection

- Language: Python
- Test framework: `pytest`
- Observed package manager workflow: `pip` + virtual environment (`venv` directory exists)
- Project layout style: source-under-`src` (tests import modules from `src`)
- Packaging config files: **not found** (`pyproject.toml`, `setup.py`, `requirements.txt` are missing)
- Task runners/scripts config: **not found** (`Makefile`, `tox.ini`, `noxfile.py`) 

## Requirements

- Python `3.12+` recommended (repository currently includes a local `venv` using Python 3.12)
- `pip`
- `pytest`

## Setup

From repository root:

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

> TODO: Add a pinned dependency file (for example `requirements.txt`) and update this section to install exact versions.

## Run Commands / Entry Points

### Run a sample algorithm script

```bash
cd python
PYTHONPATH=src python src/algorithms/backtracker.py
```

### Run standalone exercise script

```bash
cd python
python woven-test.py
```

> Note: `woven-test.py` depends on `python-dateutil` (`from dateutil.parser import parse`).
>
> TODO: Add dependency installation instructions for `python-dateutil` once dependency management is standardized.

## Scripts

No centralized script runner is currently configured (no `Makefile`, `pyproject` scripts, or similar).

Useful direct commands:

```bash
# run all tests
cd python
PYTHONPATH=src pytest -q

# run one test file
PYTHONPATH=src pytest -q tests/test_stack.py
```

## Environment Variables

- `PYTHONPATH=src` (required for tests and direct module execution in current layout)

Example:

```bash
cd python
export PYTHONPATH=src
pytest -q
```

## Tests

Tests live under `python/tests/` and are executed with `pytest`.

Verified command:

```bash
cd python
PYTHONPATH=src pytest -q tests/test_stack.py
```

## Project Structure

```text
python/
├── src/
│   ├── algorithms/
│   └── datastructures/
├── tests/
├── woven-test.py
└── README.md
```

## License

No root `LICENSE` file is currently present in the repository.

> TODO: Add a `LICENSE` file at repository root and update this section with the chosen license.
