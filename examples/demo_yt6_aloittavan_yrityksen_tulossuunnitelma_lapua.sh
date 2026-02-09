#!/bin/bash

# Shell script to demonstrate usage of the startup profit plan for Lapua tool
# This script shows how to run the YT6_Aloittavan_yrityksen_tulossuunnitelma_Lapua implementation

echo "==============================================="
echo "Startup Profit Plan for Lapua Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Startup Profit Plan for Lapua Tool..."
echo "--------------------------------------------"
python yt6_aloittavan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ Completed Startup Profit Plan for Lapua Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_startup_profit_plan_lapua.json'"
echo "for detailed profit planning results."
echo "==============================================="