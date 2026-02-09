#!/bin/bash

# Shell script to demonstrate usage of the financial plan for Lapua (version 5) tool
# This script shows how to run the YT5_Taloussuunnitelma_Lapua implementation

echo "==============================================="
echo "Financial Plan for Lapua (Version 5) Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Financial Plan for Lapua (Version 5) Tool..."
echo "--------------------------------------------------"
python yt5_taloussuunnitelma_lapua.py
echo "✓ Completed Financial Plan for Lapua (Version 5) Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_financial_plan_lapua_v5.json'"
echo "for detailed financial planning results."
echo "==============================================="