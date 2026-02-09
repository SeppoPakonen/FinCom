#!/bin/bash

# Shell script to demonstrate usage of the business interpreter calendar tool
# This script shows how to run the business interpreter calendar tool

echo "==============================================="
echo "Business Interpreter Calendar Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Business Interpreter Calendar Tool..."
echo "---------------------------------------------"
python vuosikello_yritystulkki_fi.py
echo "✓ Completed Business Interpreter Calendar Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_business_interpreter_calendar.json'"
echo "for detailed business interpreter calendar results."
echo "==============================================="