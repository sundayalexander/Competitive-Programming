# Competitive Programming

Repository of competitive-programming algorithms and data structures implemented in multiple languages.

## Overview

This repo currently contains:

- `python/`: Python implementations (`src/algorithms`, `src/datastructures`) with `pytest` tests.
- `java/`: Java implementations under Maven project layout (`src/main`, `src/test`).
- `c/`: C implementations for selected data structures.

## Stack Detection

- Languages: `Python`, `Java`, `C`
- Frameworks/libraries:
  - Python tests: `pytest`
  - Java tests: `JUnit 5` (via Maven dependencies)
- Package/build tools:
  - Python: `pip` + virtual environment workflow (no lock/dependency file found)
  - Java: `Maven` (`java/pom.xml`)
  - C: no build system config detected at repo root

## Requirements

- Python `3.x` (project notes in `python/README.md` recommend `3.12+`)
- `pip`
- `pytest` (for Python tests)
- JDK matching Maven compiler target (`java/pom.xml` currently sets source/target to `25`)
- `mvn` (Maven CLI)
- C compiler for manual C builds (for example `gcc`)

## Setup & Run

### Python

```bash
cd python
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
```

Run an algorithm module:

```bash
cd python
PYTHONPATH=src python src/algorithms/backtracker.py
```

Run standalone script:

```bash
cd python
python woven-test.py
```

### Java

Compile package:

```bash
cd java
mvn compile
```

Run tests:

```bash
cd java
mvn test
```

> TODO: Confirm and document the canonical Java runtime entry point for this module. `src/main/java/org/alexander/Main.java` currently does not expose a standard `public static void main(String[] args)` method.

### C

No centralized build script/config is present.

> TODO: Add documented compile/run commands (or a `Makefile`) for `c/` sources.

## Scripts

No centralized script runner was found at repo root (`Makefile`, `justfile`, npm scripts, tox/nox configs not detected).

Current direct commands used in this repo:

- Python tests: `PYTHONPATH=src pytest -q` (from `python/`)
- Java tests: `mvn test` (from `java/`)

## Environment Variables

- `PYTHONPATH=src` (required for Python tests/module execution with current layout)

No other project-specific environment variables were identified from repository files.

## Tests

- Python test suite is in `python/tests/` and runs with `pytest`.
- Java test suite is in `java/src/test/java/` and runs with Maven + JUnit 5.

Examples:

```bash
# Python
cd python
PYTHONPATH=src pytest -q

# Java
cd java
mvn test
```

## Project Structure

```text
.
├── c/
│   └── datastructures/
├── java/
│   ├── pom.xml
│   ├── src/main/java/org/alexander/
│   └── src/test/java/tests/
├── python/
│   ├── src/algorithms/
│   ├── src/datastructures/
│   └── tests/
└── README.md
```

## License

No root `LICENSE` file is currently present.

> TODO: Add a `LICENSE` file at repository root and update this section with the selected license.