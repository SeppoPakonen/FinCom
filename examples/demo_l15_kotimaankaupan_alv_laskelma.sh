#!/bin/bash

# Shell script to demonstrate usage of the domestic trade VAT calculator tool
# This script shows how to run the L15_Kotimaankaupan_Alv-laskelma_kirjanpitoon_ implementation

echo "==============================================="
echo "Domestic Trade VAT Calculator Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Domestic Trade VAT Calculator Tool..."
echo "--------------------------------------------"
python l15_kotimaankaupan_alv_laskelma.py
echo "✓ Completed Domestic Trade VAT Calculator Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_domestic_trade_vat_calculation.json'"
echo "for detailed VAT calculation results."
echo "==============================================="