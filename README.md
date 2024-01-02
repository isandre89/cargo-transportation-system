# Cargo Transportation System

This Python program is a simple Cargo Transportation System that allows users to manage and track packages. It provides a command-line interface for adding packages, generating reports based on specific dates, and other functionalities.

## Table of Contents

- [Cargo Transportation System](#cargo-transportation-system)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Demo Packages](#demo-packages)
    - [Normal Package](#normal-package)
    - [Options](#options)

## Prerequisites

- [`python`](https://www.python.org/) (`>= 3.8.10`)
- [`make`](https://www.gnu.org/software/make/) (`>= 4.2.1`)

## Usage

Run the program using the following command:

```bash
make run
```

Run tests using:

```bash
make tests
```

If make is not installed, you can run the program using:

```bash
python -B main.py
```

Tests can be run using:

```bash
python -B python tests.py
```

This ensures the functionality and correctness of the program.

### Demo Packages

To add demo packages, select option **Add package(s)** (1) and choose the **demo system** (0). Enter the number of demo packages you want to generate.

### Normal Package

To add a normal package, select option **Add package(s)** (1) and choose the **normal system** (1). You will be prompted to enter details such as client ID, origin, destination, date, and cost.

### Options

- Add package(s): Choose either the demo system (0) or normal system (1) to add packages.

- Generate report by date: Enter a specific date (DD/MM/YYYY) to generate a report. Press 'Enter' for today's date.

- Clear console: Clears the console screen.

- Exit: Exits the program.
