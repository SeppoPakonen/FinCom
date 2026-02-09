#!/bin/bash

# Shell script to demonstrate usage of the invoice form tool
# This script shows how to run the L5_Laskulomake_1 implementation

echo "==============================================="
echo "Invoice Form Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Invoice Form Tool..."
echo "-----------------------------"
python l5_laskulomake_1.py
echo "✓ Completed Invoice Form Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_invoice_form.json'"
echo "for detailed invoice form results."
echo "==============================================="