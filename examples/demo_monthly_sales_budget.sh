#!/bin/bash

# Shell script to demonstrate usage of the Monthly Sales Budget tool
# This script shows how to run the monthly sales budget tool

echo "==============================================="
echo "Monthly Sales Budget Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Monthly Sales Budget Tool..."
echo "------------------------------------"
python myyntibudjetti_kuukausittain.py
echo "✓ Completed Monthly Sales Budget Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_monthly_sales_budget.json'"
echo "for detailed monthly sales budget results."
echo "==============================================="