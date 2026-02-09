#!/bin/bash

# Shell script to demonstrate usage of the financial plan for Lapua tool
# This script shows how to run the YT4_Taloussuunnitelma_Lapua implementation

echo "==============================================="
echo "Financial Plan for Lapua Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Financial Plan for Lapua Tool..."
echo "--------------------------------------"
python yt4_taloussuunnitelma_lapua.py
echo "✓ Completed Financial Plan for Lapua Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_financial_plan_lapua.json'"
echo "for detailed financial planning results."
echo "==============================================="