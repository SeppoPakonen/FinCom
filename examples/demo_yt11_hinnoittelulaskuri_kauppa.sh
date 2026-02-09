#!/bin/bash

# Shell script to demonstrate usage of the retail pricing calculator tool
# This script shows how to run the YT11_Hinnoittelulaskuri_kauppa implementation

echo "==============================================="
echo "Retail Pricing Calculator Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Retail Pricing Calculator Tool..."
echo "----------------------------------------"
python yt11_hinnoittelulaskuri_kauppa.py
echo "✓ Completed Retail Pricing Calculator Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_retail_pricing_calculation.json'"
echo "for detailed retail pricing calculation results."
echo "==============================================="