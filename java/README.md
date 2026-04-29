# Competitive Programming (Java)

This module contains Java implementations of common competitive-programming algorithms, with JUnit 5 tests for selected classes.

## Overview

- **Language:** Java
- **Build/Dependency tool:** Maven (`pom.xml`)
- **Primary package:** `org.alexander`
- **Implemented algorithm classes:**
  - `org.alexander.algorithms.SinglePassAlgorithm`
  - `org.alexander.algorithms.KadaneAlgorithm`
  - `org.alexander.algorithms.BackTracking`

## Requirements

- JDK compatible with the version configured in `pom.xml`:
  - `maven.compiler.source = 25`
  - `maven.compiler.target = 25`
- Apache Maven 3.8+

> TODO: Confirm the exact JDK distribution/version officially intended for contributors.

## Setup

From this directory (`java/`):

```bash
mvn clean compile
```

This resolves dependencies and compiles sources under `src/main/java`.

## Run

### Main class

There is a `Main` class at `src/main/java/org/alexander/Main.java`.

```bash
mvn exec:java -Dexec.mainClass="org.alexander.Main"
```

> TODO: `Main` currently defines `static void main()` (without `String[] args`) and may not be directly runnable with standard Java/Maven entrypoint conventions. Confirm intended executable entry point.

### Direct Java run (after compile)

```bash
java -cp target/classes org.alexander.Main
```

> TODO: Verify runtime behavior after aligning `Main` method signature with `public static void main(String[] args)` if intended.

## Scripts / Commands

This repository uses Maven lifecycle/goals as its script equivalents:

- `mvn clean` — remove previous build artifacts.
- `mvn compile` — compile main source code.
- `mvn test` — run unit tests under `src/test/java`.
- `mvn package` — build project artifact.

## Environment Variables

No project-specific environment variables were found in the current codebase.

- `JAVA_HOME` (recommended) — points to the installed JDK.
- `MAVEN_OPTS` (optional) — JVM options for Maven.

> TODO: Add required application-specific env vars here if introduced later.

## Tests

JUnit 5 tests are located in:

- `src/test/java/tests/TestKadaneAlgorithm.java`
- `src/test/java/tests/TestSinglePass.java`

Run all tests:

```bash
mvn test
```

## Project Structure

```text
java/
├── pom.xml
├── README.md
├── src/
│   ├── main/java/org/amowe/
│   │   ├── Main.java
│   │   └── algorithms/
│   │       ├── BackTracking.java
│   │       ├── KadaneAlgorithm.java
│   │       └── SinglePassAlgorithm.java
│   └── test/java/algorithms/
│       ├── TestKadaneAlgorithm.java
│       └── TestSinglePass.java

```

## License

No root `LICENSE` file was detected in this module.

> TODO: Add a `LICENSE` file (for example, MIT/Apache-2.0) and update this section accordingly.