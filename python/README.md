# Competitive Programming (Python)

## Overview

This repository contains Python implementations of common competitive programming algorithms and data structures. It is designed for study and practice, featuring `pytest` coverage for most modules.

### Covered Areas

- **Algorithms**:
  - Backtracking (Backtracker, Backtracking variants)
  - Binary Search
  - Bitwise Operations
  - Dutch National Flag
  - Majority Voting (Boyer-Moore)
  - Prefix & Postfix Sum
  - Reversal Algorithm
  - Sliding Window
  - Sorting Algorithms
  - Two Pointers
- **Data Structures**:
  - Graph
  - Hash Table
  - Linked List
  - Queues
  - Stack
  - Suffix Array
  - Vector (Dynamic Array)

## Stack & Tooling

- **Language**: Python 3.11+
- **Package Manager**: [uv](https://github.com/astral-sh/uv) (recommended) or `pip`
- **Test Framework**: `pytest`
- **Configuration**: `pyproject.toml`, `uv.lock`

## Requirements

- Python `3.11+`
- `uv` (optional but recommended for dependency management)

## Setup

### Using `uv` (Recommended)

```bash
# Install dependencies and create a virtual environment
uv sync
```

### Using `pip`

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pytest
# Note: woven-test.py requires python-dateutil
pip install python-dateutil
```

## Run Commands / Entry Points

### Run an Algorithm Script

Most scripts in `src/algorithms` can be run directly.

```bash
export PYTHONPATH=src
python src/algorithms/backtracker.py
```

### Run Standalone Exercise

`woven-test.py` is a standalone script that includes its own tests.

```bash
# Note: requires python-dateutil
python woven-test.py
```

## Scripts

### Running Tests

We use `pytest` for all module tests.

```bash
# Run all tests using uv
uv run pytest

# Run a specific test file using uv
uv run pytest tests/test_stack.py
```

If not using `uv`:
```bash
export PYTHONPATH=src
pytest
```

## Environment Variables

- `PYTHONPATH`: Should be set to `src` when running scripts or tests manually to ensure imports work correctly.

## Project Structure

```text
python/
├── src/
│   ├── algorithms/       # Algorithm implementations
│   └── datastructures/   # Data structure implementations
├── tests/                # Pytest suite
├── pyproject.toml        # Project metadata and dependencies
├── uv.lock               # Locked dependencies
├── woven-test.py         # Standalone exercise script
└── README.md             # This file
```

## License

> TODO: Add a `LICENSE` file at the repository root and update this section. Currently, no license is specified.
