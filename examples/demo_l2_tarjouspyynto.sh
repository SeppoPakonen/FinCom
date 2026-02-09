#!/bin/bash

# Shell script to demonstrate usage of the request for proposal tool
# This script shows how to run the L2_Tarjouspyynto implementation

echo "==============================================="
echo "Request for Proposal Tool Demo"
echo "==============================================="

# Change to the src directory
cd /common/active/sblo/Dev/Manager/DummyMusicCompany/src

echo
echo "Running Request for Proposal Tool..."
echo "------------------------------------"
python l2_tarjouspyynto.py
echo "✓ Completed Request for Proposal Tool"
echo

echo "==============================================="
echo "Demo completed! Check the generated JSON file 'sample_request_for_proposal.json'"
echo "for detailed RFP results."
echo "==============================================="