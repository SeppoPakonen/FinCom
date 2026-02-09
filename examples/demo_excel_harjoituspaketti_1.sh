#!/bin/bash

# Shell script to demonstrate usage of the Excel exercise package tool
# This script shows how to run the Excel exercise package tool

echo "==============================================="
echo "Excel Exercise Package Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Excel Exercise Package Tool..."
echo "-------------------------------------"
python excel_harjoituspaketti_1.py
echo "✓ Completed Excel Exercise Package Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_excel_exercise_package.json'"
echo "for detailed exercise package results."
echo "==============================================="