#!/bin/bash

# Shell script to demonstrate a complete business planning workflow
# This script shows how to use multiple tools together for comprehensive business planning

echo "==============================================="
echo "Complete Business Planning Workflow Demo"
echo "==============================================="
echo
echo "This demo simulates a complete business planning process"
echo "using multiple financial tools together."
echo

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo "Step 1: Creating a startup financial plan..."
echo "-------------------------------------------"
echo "Using YT6 tool for startup profit planning..."
python yt6_aloittavan_yrityksen_tulossuunnitelma_lapua.py
echo "✓ Startup financial plan created"
echo

echo "Step 2: Developing a cash budget..."
echo "----------------------------------"
echo "Using YT23 tool for cash flow management..."
python yt23_kassabudjetti_lapua.py
echo "✓ Cash budget created"
echo

echo "Step 3: Creating a marketing budget and calendar..."
echo "------------------------------------------------"
echo "Using YT25 tool for marketing planning..."
python yt25_markkinointibudjetti_ja_vuosikello.py
echo "✓ Marketing budget and calendar created"
echo

echo "Step 4: Performing company valuation..."
echo "--------------------------------------"
echo "Using YT24 tool for company valuation..."
python yt24_yrityksen_arvonmaarityslaskuri.py
echo "✓ Company valuation completed"
echo

echo "Step 5: Creating comprehensive financial plans..."
echo "-----------------------------------------------"
echo "Using YT5 tool for detailed financial planning..."
python yt5_taloussuunnitelma_lapua.py
echo "✓ Comprehensive financial plan created"
echo

echo "==============================================="
echo "Complete business planning workflow completed!"
echo
echo "The workflow demonstrates how different tools can be used together:"
echo "- Startup planning (YT6)"
echo "- Cash flow management (YT23)"
echo "- Marketing planning (YT25)"
echo "- Company valuation (YT24)"
echo "- Comprehensive financial planning (YT5)"
echo
echo "All tools generated JSON output files with detailed results."
echo "==============================================="