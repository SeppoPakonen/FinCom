#!/bin/bash

# Shell script to demonstrate usage of the financial plan for BusinessOulu tool
# This script shows how to run the YT4_Taloussuunnitelma_BusinessOulu implementation

echo "==============================================="
echo "Financial Plan for BusinessOulu Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Financial Plan for BusinessOulu Tool..."
echo "---------------------------------------------"
python yt4_taloussuunnitelma_businessoulu.py
echo "✓ Completed Financial Plan for BusinessOulu Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_financial_plan_businessoulu.json'"
echo "for detailed financial planning results."
echo "==============================================="