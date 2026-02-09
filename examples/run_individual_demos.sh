#!/bin/bash

# Shell script to demonstrate usage of individual financial planning tools
# This script shows how to run specific tools with custom parameters

echo "==============================================="
echo "Individual Financial Tool Demonstrations"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "1. Running YT4 Financial Plan for Lapua..."
echo "------------------------------------------"
echo "This tool helps create comprehensive financial plans for businesses in Lapua."
echo "Running sample plan..."
python yt4_taloussuunnitelma_lapua.py
echo "✓ YT4 Financial Plan completed"
echo

echo "2. Running YT5 Financial Plan (Version 5)..."
echo "--------------------------------------------"
echo "This is an enhanced version of the financial planning tool."
echo "Running sample plan..."
python yt5_taloussuunnitelma_lapua.py
echo "✓ YT5 Financial Plan completed"
echo

echo "3. Running YT6 Startup Profit Plan..."
echo "-------------------------------------"
echo "This tool is specifically designed for startup businesses."
echo "Running sample plan..."
python yt6_aloittavan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ YT6 Startup Profit Plan completed"
echo

echo "4. Running YT22 Operating Business Profit Plan..."
echo "------------------------------------------------"
echo "This tool is designed for established operating businesses."
echo "Running sample plan..."
python yt22_toimivan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ YT22 Operating Business Profit Plan completed"
echo

echo "5. Running YT23 Cash Budget..."
echo "------------------------------"
echo "This tool helps manage cash flow and budgeting."
echo "Running sample budget..."
python yt23_kassabudjetti_lapua.py
echo "✓ YT23 Cash Budget completed"
echo

echo "6. Running YT24 Company Valuation Calculator..."
echo "-----------------------------------------------"
echo "This tool calculates company valuation using multiple methods."
echo "Running sample valuation..."
python yt24_yrityksen_arvonmaarityslaskuri.py
echo "✓ YT24 Company Valuation completed"
echo

echo "7. Running YT25 Marketing Budget & Calendar..."
echo "----------------------------------------------"
echo "This tool helps plan marketing budgets and annual calendars."
echo "Running sample marketing plan..."
python yt25_markkinointibudjetti_ja_vuosikello.py
echo "✓ YT25 Marketing Budget & Calendar completed"
echo

echo "==============================================="
echo "Individual tool demonstrations completed!"
echo "All tools ran successfully with sample data."
echo "==============================================="