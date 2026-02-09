#!/bin/bash

# Shell script to demonstrate usage of the payment reminder tool
# This script shows how to run the L8_Maksumuistutus implementation

echo "==============================================="
echo "Payment Reminder Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Payment Reminder Tool..."
echo "--------------------------------"
python l8_maksumuistutus.py
echo "✓ Completed Payment Reminder Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_payment_reminder.json'"
echo "for detailed payment reminder results."
echo "==============================================="