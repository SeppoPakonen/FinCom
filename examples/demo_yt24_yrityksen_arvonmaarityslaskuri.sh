#!/bin/bash

# Shell script to demonstrate usage of the company valuation calculator tool
# This script shows how to run the YT24_Yrityksen_arvonmaarityslaskuri implementation

echo "==============================================="
echo "Company Valuation Calculator Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Company Valuation Calculator Tool..."
echo "-------------------------------------------"
python yt24_yrityksen_arvonmaarityslaskuri.py
echo "✓ Completed Company Valuation Calculator Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_company_valuation.json'"
echo "for detailed valuation results."
echo "==============================================="