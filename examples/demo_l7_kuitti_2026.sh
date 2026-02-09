#!/bin/bash

# Shell script to demonstrate usage of the receipt tool
# This script shows how to run the L7_Kuitti_2026 implementation

echo "==============================================="
echo "Receipt Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Receipt Tool..."
echo "-----------------------"
python l7_kuitti_2026.py
echo "✓ Completed Receipt Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_receipt_2026.json'"
echo "for detailed receipt results."
echo "==============================================="