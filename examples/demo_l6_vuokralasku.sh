#!/bin/bash

# Shell script to demonstrate usage of the rental invoice tool
# This script shows how to run the L6_Vuokralasku implementation

echo "==============================================="
echo "Rental Invoice Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Rental Invoice Tool..."
echo "-------------------------------"
python l6_vuokralasku.py
echo "✓ Completed Rental Invoice Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_rental_invoice.json'"
echo "for detailed rental invoice results."
echo "==============================================="