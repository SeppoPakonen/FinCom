#!/bin/bash

# Shell script to demonstrate usage of the payment demand notice tool
# This script shows how to run the L9_Maksukehotus implementation

echo "==============================================="
echo "Payment Demand Notice Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Payment Demand Notice Tool..."
echo "-------------------------------------"
python l9_maksukehotus.py
echo "✓ Completed Payment Demand Notice Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_payment_demand_notice.json'"
echo "for detailed payment demand notice results."
echo "==============================================="