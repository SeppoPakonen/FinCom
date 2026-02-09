#!/bin/bash

# Shell script to demonstrate usage of the YT25 Sales and Marketing Budget tool
# This script shows how to run the sales and marketing budget tool

echo "==============================================="
echo "YT25 Sales and Marketing Budget Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running YT25 Sales and Marketing Budget Tool..."
echo "------------------------------------------------"
python yt25_myynti_markkinointibudjetti.py
echo "✓ Completed YT25 Sales and Marketing Budget Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_sales_marketing_budget.json'"
echo "for detailed sales and marketing budget results."
echo "==============================================="