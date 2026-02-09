#!/bin/bash

# Shell script to demonstrate usage of the travel expense report tool
# This script shows how to run the T1_Matkalasku_2026 implementation

echo "==============================================="
echo "Travel Expense Report Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Travel Expense Report Tool..."
echo "------------------------------------"
python t1_matkalasku_2026.py
echo "✓ Completed Travel Expense Report Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_travel_expense_report.json'"
echo "for detailed travel expense report results."
echo "==============================================="