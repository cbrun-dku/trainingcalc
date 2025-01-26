# TrainingCalc

**TrainingCalc** is a simple project designed to help you learn how to write and run tests in Python. The project implements a command-line calculator (with bugs, and REST API, a web interface, and provides an opportunity to practice testing, code coverage analysis, formatting, and linting.

## Purpose

The goal of this project is to:
- Learn how to write tests in Python using `pytest`.
- Understand how to measure test coverage with `pytest-cov`.
- Practice using tools like `black` for code formatting and `flake8` for linting.

---

## Setup

Clone the repository:
```
git clone https://github.com/cbrun-dku/trainingcalc.git
cd trainingcalc
```

Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
python -m pip install pip -U
```

Install package in edit mode and dependencies:
```
pip install -e ".[dev]"
```

## Running the Calculator

To use the calculator interactively:
```
trainingcalc
```

## Format code

To format the code:
```
black .
```

## Lint code

To lint the code:
```
flake8
```

## Execute tests

To execute the test:
```
pytest
```

To execute the test with code coverage:
```
pytest --cov=trainingcalc --cov-report=html
open htmlcov/index.html
```

## Run server

To run the server:
```
uvicorn trainingcalc.api:app --reload
```

open a browser and navigate to http://127.0.0.1:8000