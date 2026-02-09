#!/bin/bash

# Shell script to demonstrate usage of the 2026 invoice form tool
# This script shows how to run the L5_Laskulomake_2026 implementation

echo "==============================================="
echo "2026 Invoice Form Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running 2026 Invoice Form Tool..."
echo "----------------------------------"
python l5_laskulomake_2026.py
echo "✓ Completed 2026 Invoice Form Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_invoice_form_2026.json'"
echo "for detailed 2026 invoice form results."
echo "==============================================="