# Source Code Directory

This directory contains all Python implementations of spreadsheets and business tools converted from the original `.xlsx` files.

## Purpose

The Python scripts in this directory provide programmatic access to the functionality originally implemented in Excel spreadsheets. They allow for automated processing, integration with other systems, and easier maintenance compared to static spreadsheets.

## Contents

- `yt4_taloussuunnitelma_lapua.py` - Financial planning tool based on the Lapua template
- `yt4_taloussuunnitelma_businessoulu.py` - Financial planning tool based on the BusinessOulu template

## Usage

Each Python file can be run independently to test its functionality:

```bash
python yt4_taloussuunnitelma_lapua.py
```

Or imported as a module in other Python code:

```python
from yt4_taloussuunnitelma_lapua import FinancialPlan
```

## Adding New Tools

When converting additional spreadsheets to Python:

1. Create the Python implementation in this directory
2. Use descriptive names that match the original spreadsheet purpose
3. Include comprehensive docstrings explaining the purpose and usage
4. Follow the same structure and patterns as existing implementations