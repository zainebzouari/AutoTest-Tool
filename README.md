# AutoTest Tool — Vehicle Electronics Testing & Validation

Automated testing platform for vehicle electronic and comfort features (ABS, TPMS, ADAS,
lighting, climate control, seat adjustment, parking assistance, energy consumption, emissions,
engine). Built during a summer internship at **Primatec Engineering**, replacing a manual,
paper/Excel-based validation process with automated, repeatable, database-driven tests.

## Overview

The system reads vehicle sensor data from a MySQL database, compares it against expected
values/tolerance ranges defined in a metadata file, and reports each feature as **Pass** or
**Fail** with detailed error messages. Tests are written with `pytest`, exposed through a
Flask + web UI, and can be run in a CI pipeline (Jenkins).

## Features

- Enter a vehicle ID and select one or more subsystems to test (or test all at once)
- Automated comparison of measured values vs. expected values/tolerances from `metadata.py`
- Pass/Fail results table with mismatch details for each failed check
- HTML test reports (pytest-html) and interactive reports (Allure)
- Simple login-gated access to the test interface
- Continuous integration ready (Jenkins pipeline)

## Tested subsystems

Vehicle emissions · TPMS (tire pressure) · Seat adjustment · Parking assistance · Lighting ·
Engine · Energy consumption · Climate control · ADAS · ABS system

## Tech stack

- **Backend:** Python, Flask
- **Testing:** pytest, pytest-html, Allure
- **Database:** MySQL
- **Frontend:** HTML, CSS, React 
- **CI/CD:** Jenkins

## Project structure

```
├── app.py                # Flask app: routes for login, test page, results
├── automative.py         # DB connection + vehicle data retrieval
├── metadata.py           # Expected values / tolerance ranges per subsystem
├── test_automative.py    # Pytest test logic: compares DB data to metadata
├── templates/            # index, login, test, results pages
├── static/                # CSS, images
├── assets/                # additional styles
├── requirements.txt
└── .env.example
```

## Setup

### 1. Clone and install dependencies

```bash
git clone <your-repo-url>
cd INTERNSHIP_TASK3
pip install -r requirements.txt
```

### 2. Configure the database

Create a MySQL database and the tables matching each subsystem (e.g. `vehicleemissions`,
`tpms`, `seatadjustment`, `parkingassistance`, `lighting`, `engine`, `energyconsumption`,
`climatecontrol`, `adas`, `abs_system`), each keyed by `Vehicle_ID`.

### 3. Set environment variables

Copy `.env.example` to `.env` and fill in your own values:

```bash
cp .env.example .env
```

```
DB_USER=root
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_NAME=myDB

APP_USERNAME=primatec
APP_PASSWORD=your_password_here
```

> Credentials are no longer hardcoded in the source — they're loaded from `.env`
> (via `python-dotenv`), which is git-ignored and should never be committed.

### 4. Run the app

```bash
python app.py
```

Visit `http://localhost:5000`.

## Running the tests

```bash
# Run all tests
pytest

# Generate an HTML report
pytest --html=Report.html

# Generate an Allure report
pytest --alluredir=allure-results
allure serve allure-results
```

Test expectations (thresholds, tolerance ranges, custom checks) are defined per subsystem in
`metadata.py` and can be updated without touching the test scripts.

## Continuous Integration

A Jenkins pipeline can be configured to: clone the repo → install dependencies → run pytest →
archive HTML/Allure reports on every commit. See the internship report for the pipeline script
used during development.

## Notes / known limitations

- Test expectations rely on a static metadata file rather than adapting to real-time
  requirement changes.
- The UI is functional but could be further refined.
- Possible future work: dynamic/learning-based test thresholds, anomaly prediction via ML,
  cloud-based storage for scalability, and stronger security hardening.

## Context

Developed as part of a second-year engineering internship (Electronics and Communication
Systems) at Primatec Engineering, Sfax, Tunisia.
