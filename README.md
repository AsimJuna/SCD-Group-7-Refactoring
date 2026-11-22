# SCD Group 7 — Supermarket Receipt Refactoring

## Project Overview

This project focuses on refactoring a legacy Supermarket Receipt application as part of the Software Construction and Development (SCD) course at Khwaja Fareed University of Engineering and Information Technology (KFUEIT).

The application calculates shopping cart prices, generates customer receipts, and handles different types of special offers and discounts.

The primary objective of this assignment is to improve the internal software design by identifying code smells, eliminating duplicated pricing logic, and extracting pricing rules while preserving the application's existing external behavior.

## Refactoring Focus

**Duplicated Pricing Logic — Extract Pricing Rules**

The project focuses on:

- Identifying duplicated pricing calculations.
- Separating pricing rules from shopping cart responsibilities.
- Improving code readability and maintainability.
- Applying appropriate object-oriented design principles.
- Preserving existing behavior through characterization tests.
- Managing changes through Git branches, commits, and Pull Requests.

## Technologies Used

- Python
- Pytest
- Git
- GitHub
- Object-Oriented Programming
- UML Class Diagrams

## Project Structure

```text
SCD-Group-7-Refactoring/
│
├── python_pytest/
│   ├── src/
│   ├── tests/
│   ├── requirements.txt
│   ├── pytest.ini
│   └── README.md
│
├── docs/
│   ├── baseline-analysis.md
│   └── design-model.png
│
└── README.md
```

## Installation and Execution

### Requirements

- Python 3.x
- pip

### Setup

Navigate to the Python project directory:

```bash
cd python_pytest
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it using Git Bash:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

### Run Tests

Execute the test suite:

```bash
pytest -v
```

## Group Members

| No. | Name | Roll Number | Role |
|---|---|---|---|
| 1 | Asim Juna | SWEN241101098 | Group Leader |
| 2 | Tehreem Fatima | SWEN241101097 | Member |
| 3 | Amna Khalid | SWEN241101054 | Member |
| 4 | Mahnoor Hassan | SWEN241101073 | Member |
| 5 | Bisma | SWEN241101085 | Member |

## Repository Management

The project follows a Git-based collaborative development workflow.

- `main`: Stable release branch.
- `develop`: Integration and development branch.
- `feature/*` and `refactor/*`: Individual development branches.

Refactoring changes are developed separately and integrated into the `develop` branch through Pull Requests. The final verified version is merged into `main`.

## Changelog

### Unreleased

- Initial Python implementation added to the Group 7 repository.
- Baseline test execution verified.
- Refactoring activities are in progress.

## Academic Information

**Course:** Software Construction and Development (SCD)  
**Group:** 7  
**University:** Khwaja Fareed University of Engineering and Information Technology (KFUEIT)

**Repository:** https://github.com/AsimJuna/SCD-Group-7-Refactoring
