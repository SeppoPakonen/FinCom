#!/bin/bash

# Shell script to demonstrate usage of the business proposal tool
# This script shows how to run the L1_Tarjous implementation

echo "==============================================="
echo "Business Proposal Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Business Proposal Tool..."
echo "---------------------------------"
python l1_tarjous.py
echo "✓ Completed Business Proposal Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_business_proposal.json'"
echo "for detailed business proposal results."
echo "==============================================="