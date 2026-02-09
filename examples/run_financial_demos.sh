#!/bin/bash

# Shell script to demonstrate usage of the financial planning Python tools
# This script shows how to run the different financial planning tools

echo "==============================================="
echo "Financial Planning Tools Demonstration"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "1. Running YT4 Financial Plan for Lapua..."
echo "------------------------------------------"
python yt4_taloussuunnitelma_lapua.py
echo "✓ Completed YT4 Financial Plan for Lapua"
echo

echo "2. Running YT4 Financial Plan for BusinessOulu..."
echo "------------------------------------------------"
python yt4_taloussuunnitelma_businessoulu.py
echo "✓ Completed YT4 Financial Plan for BusinessOulu"
echo

echo "3. Running YT5 Financial Plan (Version 5)..."
echo "--------------------------------------------"
python yt5_taloussuunnitelma_lapua.py
echo "✓ Completed YT5 Financial Plan (Version 5)"
echo

echo "4. Running YT6 Startup Profit Plan..."
echo "-------------------------------------"
python yt6_aloittavan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ Completed YT6 Startup Profit Plan"
echo

echo "5. Running YT22 Operating Business Profit Plan..."
echo "------------------------------------------------"
python yt22_toimivan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ Completed YT22 Operating Business Profit Plan"
echo

echo "6. Running YT23 Cash Budget..."
echo "------------------------------"
python yt23_kassabudjetti_lapua.py
echo "✓ Completed YT23 Cash Budget"
echo

echo "7. Running YT24 Company Valuation Calculator..."
echo "-----------------------------------------------"
python yt24_yrityksen_arvonmaarityslaskuri.py
echo "✓ Completed YT24 Company Valuation Calculator"
echo

echo "8. Running YT25 Marketing Budget & Calendar..."
echo "----------------------------------------------"
python yt25_markkinointibudjetti_ja_vuosikello.py
echo "✓ Completed YT25 Marketing Budget & Calendar"
echo

echo "==============================================="
echo "Demonstration completed!"
echo "Check the generated JSON files in the src directory for detailed results."
echo "==============================================="