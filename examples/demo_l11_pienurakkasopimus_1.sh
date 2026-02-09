#!/bin/bash

# Shell script to demonstrate usage of the small construction contract tool
# This script shows how to run the L11_Pienurakkasopimus_1 implementation

echo "==============================================="
echo "Small Construction Contract Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Small Construction Contract Tool..."
echo "------------------------------------------"
python l11_pienurakkasopimus_1.py
echo "✓ Completed Small Construction Contract Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_small_construction_contract.json'"
echo "for detailed contract results."
echo "==============================================="