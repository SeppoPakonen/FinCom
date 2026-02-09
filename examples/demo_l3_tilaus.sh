#!/bin/bash

# Shell script to demonstrate usage of the order form tool
# This script shows how to run the L3_Tilaus implementation

echo "==============================================="
echo "Order Form Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Order Form Tool..."
echo "--------------------------"
python l3_tilaus.py
echo "✓ Completed Order Form Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_order_form.json'"
echo "for detailed order form results."
echo "==============================================="