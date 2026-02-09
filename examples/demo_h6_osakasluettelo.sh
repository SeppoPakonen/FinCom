#!/bin/bash

# Shell script to demonstrate usage of the shareholder registry tool
# This script shows how to run the H6_Osakasluettelo implementation

echo "==============================================="
echo "Shareholder Registry Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Shareholder Registry Tool..."
echo "------------------------------------"
python h6_osakasluettelo.py
echo "✓ Completed Shareholder Registry Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_shareholder_registry.json'"
echo "for detailed shareholder registry results."
echo "==============================================="