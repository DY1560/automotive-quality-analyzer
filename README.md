# Automotive Quality Data Analyzer

## Overview

A Python-based automotive quality analytics application
that analyzes synthetic supplier quality records.

## Business Problem

Automotive quality teams need to identify high-defect
components, problematic suppliers, and quality trends
efficiently.

## Features

- CSV data loading
- Data validation
- Supplier defect aggregation
- Component defect analysis
- High-defect identification
- Defect cost estimation
- Automated testing using pytest

## Technology Stack

- Python
- CSV
- pytest
- Git
- GitHub

## Project Structure

src/automotive_quality/
    main.py
    models.py
    validator.py
    analysis.py
    logger_config.py

tests/
    test_models.py
    test_validator.py
    test_analysis.py

## Installation

Create a virtual environment and install the package:

python -m pip install -e .

## Execution

python -m automotive_quality.main

## Testing

python -m pytest -v

## Data

This project uses synthetic automotive quality data.

No confidential employer data is used.

## Future Enhancements

- FastAPI integration
- Supplier risk scoring
- Predictive quality analytics
- AI-powered quality investigation
