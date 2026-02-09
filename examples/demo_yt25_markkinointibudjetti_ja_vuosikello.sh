#!/bin/bash

# Shell script to demonstrate usage of the marketing budget and annual calendar tool
# This script shows how to run the YT25_Markkinointibudjetti_ja_vuosikello implementation

echo "==============================================="
echo "Marketing Budget and Annual Calendar Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Marketing Budget and Annual Calendar Tool..."
echo "--------------------------------------------------"
python yt25_markkinointibudjetti_ja_vuosikello.py
echo "✓ Completed Marketing Budget and Annual Calendar Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_marketing_budget_annual_calendar.json'"
echo "for detailed marketing budget and calendar results."
echo "==============================================="