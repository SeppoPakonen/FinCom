#!/bin/bash

# Shell script to demonstrate usage of the order confirmation tool
# This script shows how to run the L4_Tilausvahvistus implementation

echo "==============================================="
echo "Order Confirmation Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Order Confirmation Tool..."
echo "----------------------------------"
python l4_tilausvahvistus.py
echo "✓ Completed Order Confirmation Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_order_confirmation.json'"
echo "for detailed order confirmation results."
echo "==============================================="