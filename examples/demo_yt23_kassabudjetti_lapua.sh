#!/bin/bash

# Shell script to demonstrate usage of the cash budget tool
# This script shows how to run the YT23_Kassabudjetti_Lapua implementation

echo "==============================================="
echo "Cash Budget Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Cash Budget Tool..."
echo "---------------------------"
python yt23_kassabudjetti_lapua.py
echo "✓ Completed Cash Budget Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_cash_budget.json'"
echo "for detailed cash budget results."
echo "==============================================="