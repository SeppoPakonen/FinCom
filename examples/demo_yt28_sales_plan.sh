#!/bin/bash

# Shell script to demonstrate usage of the YT28 Sales Plan tool
# This script shows how to run the sales plan tool

echo "==============================================="
echo "YT28 Sales Plan Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running YT28 Sales Plan Tool..."
echo "--------------------------------"
python yt28_myyntisuunnitelma.py
echo "✓ Completed YT28 Sales Plan Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_sales_plan.json'"
echo "for detailed sales plan results."
echo "==============================================="