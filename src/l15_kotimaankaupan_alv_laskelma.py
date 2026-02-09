"""
Python implementation of L15_Kotimaankaupan_Alv-laskelma_kirjanpitoon_ domestic trade VAT calculation.

This module provides programmatic access to the VAT calculation functionality
originally implemented in the L15_Kotimaankaupan_Alv-laskelma_kirjanpitoon_.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class DomesticTradeVATCalculator:
    """
    A class representing a domestic trade VAT calculation tool for accounting purposes.
    This tool helps businesses calculate and report VAT obligations for domestic trade 
    transactions, ensuring compliance with Finnish tax regulations.
    """
    
    def __init__(self, company_name: str = "VAT Calculator Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.calculation_date = datetime.now().strftime('%d.%m.%Y')
        self.company_info = {}  # Company information
        self.sales_transactions = []  # Sales transactions (output VAT)
        self.purchase_transactions = []  # Purchase transactions (input VAT)
        self.vat_rates = {}  # VAT rates used in calculations
        self.vat_periods = {}  # VAT return periods
        self.vat_registers = {}  # VAT registers
        self.unallocated_vat = {}  # Unallocated VAT amounts
        self.vat_corrections = {}  # VAT corrections and adjustments
        self.vat_credits = {}  # VAT credits and refunds
        self.prepaid_vat = {}  # Prepaid VAT amounts
        self.bookkeeping_entries = {}  # Bookkeeping entries for VAT
        self.balance_sheet_impact = {}  # Balance sheet impact of VAT
        self.profit_loss_impact = {}  # Profit & loss impact of VAT
        self.cash_flow_impact = {}  # Cash flow impact of VAT payments
        self.reporting_analytics = {}  # VAT reporting and analytics
        self.audit_trail = {}  # Audit trail for VAT calculations
        self.risk_management = {}  # Risk management for VAT compliance
        self.quality_criteria = {}  # Quality criteria for VAT calculations
        self.total_output_vat = 0.0  # Total output VAT (sales)
        self.total_input_vat = 0.0  # Total input VAT (purchases)
        self.net_vat_payable = 0.0  # Net VAT payable (output - input)
        self.vat_return_submissions = []  # VAT return submissions
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the VAT calculator with default values."""
        # Default company information
        self.company_info = {
            "name": self.company_name,
            "business_id": "",
            "address": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "vat_registration": ""
        }
        
        # Default VAT rates
        self.vat_rates = {
            "vat_0_percent": 0.0,
            "vat_10_percent": 0.10,
            "vat_14_percent": 0.14,
            "vat_24_percent": 0.24,
            "vat_25_5_percent": 0.255  # From the spreadsheet
        }
        
        # Default VAT periods
        self.vat_periods = {
            "current_period": f"{self.year}-Q1",
            "previous_period": f"{self.year-1}-Q4",
            "period_start_date": f"{self.year}-01-01",
            "period_end_date": f"{self.year}-03-31",
            "submission_deadline": f"{self.year}-05-12"  # Standard Finnish VAT return deadline
        }
        
        # Default registers
        self.vat_registers = {
            "sales_register": [],
            "purchase_register": [],
            "correction_register": []
        }
        
        # Default reporting analytics
        self.reporting_analytics = {
            "total_taxable_sales": 0.0,
            "total_taxable_purchases": 0.0,
            "vat_efficiency_ratio": 0.0,
            "compliance_score": 100.0,
            "audit_risk_level": "Low"
        }
    
    def set_company_info(self, name: str, business_id: str = "", address: str = "", 
                        contact_person: str = "", phone: str = "", email: str = "",
                        vat_registration: str = ""):
        """Set company information."""
        self.company_info = {
            "name": name,
            "business_id": business_id,
            "address": address,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "vat_registration": vat_registration
        }
    
    def add_sales_transaction(self, date: str, description: str, taxable_amount: float, 
                            vat_rate: float, customer: str = "", document_number: str = ""):
        """Add a sales transaction (generates output VAT)."""
        output_vat = taxable_amount * vat_rate
        transaction = {
            "date": date,
            "description": description,
            "taxable_amount": taxable_amount,
            "vat_rate": vat_rate,
            "output_vat": output_vat,
            "customer": customer,
            "document_number": document_number
        }
        
        self.sales_transactions.append(transaction)
        return transaction
    
    def add_purchase_transaction(self, date: str, description: str, taxable_amount: float, 
                               vat_rate: float, supplier: str = "", document_number: str = ""):
        """Add a purchase transaction (generates input VAT)."""
        input_vat = taxable_amount * vat_rate
        transaction = {
            "date": date,
            "description": description,
            "taxable_amount": taxable_amount,
            "vat_rate": vat_rate,
            "input_vat": input_vat,
            "supplier": supplier,
            "document_number": document_number
        }
        
        self.purchase_transactions.append(transaction)
        return transaction
    
    def add_vat_correction(self, date: str, description: str, amount: float, 
                          correction_type: str = "adjustment"):
        """Add a VAT correction or adjustment."""
        correction = {
            "date": date,
            "description": description,
            "amount": amount,
            "type": correction_type
        }
        
        self.vat_corrections = self.vat_corrections or []
        if isinstance(self.vat_corrections, list):
            self.vat_corrections.append(correction)
        else:
            self.vat_corrections = [correction]
        
        return correction
    
    def calculate_vat_obligations(self) -> Dict:
        """Calculate total output VAT, input VAT, and net VAT payable."""
        total_output_vat = sum(tx["output_vat"] for tx in self.sales_transactions)
        total_input_vat = sum(tx["input_vat"] for tx in self.purchase_transactions)
        
        # Add any corrections to the calculation
        correction_amount = sum(corr.get("amount", 0) for corr in (self.vat_corrections or []))
        
        net_vat_payable = total_output_vat - total_input_vat + correction_amount
        
        self.total_output_vat = total_output_vat
        self.total_input_vat = total_input_vat
        self.net_vat_payable = net_vat_payable
        
        # Update reporting analytics
        self.reporting_analytics["total_taxable_sales"] = sum(tx["taxable_amount"] for tx in self.sales_transactions)
        self.reporting_analytics["total_taxable_purchases"] = sum(tx["taxable_amount"] for tx in self.purchase_transactions)
        self.reporting_analytics["vat_efficiency_ratio"] = (total_input_vat / total_output_vat * 100) if total_output_vat > 0 else 0
        
        return {
            "total_output_vat": total_output_vat,
            "total_input_vat": total_input_vat,
            "correction_amount": correction_amount,
            "net_vat_payable": net_vat_payable,
            "vat_recovery_rate": (total_input_vat / total_output_vat * 100) if total_output_vat > 0 else 0
        }
    
    def submit_vat_return(self, period: str, submission_date: str = None) -> Dict:
        """Submit a VAT return for the specified period."""
        if submission_date is None:
            submission_date = datetime.now().strftime('%Y-%m-%d')
        
        vat_calculation = self.calculate_vat_obligations()
        
        vat_return = {
            "period": period,
            "submission_date": submission_date,
            "company_info": self.company_info,
            "calculation": vat_calculation,
            "sales_transactions_count": len(self.sales_transactions),
            "purchase_transactions_count": len(self.purchase_transactions),
            "corrections_count": len(self.vat_corrections or [])
        }
        
        self.vat_return_submissions.append(vat_return)
        
        return vat_return
    
    def generate_vat_report(self) -> Dict:
        """Generate a comprehensive VAT report."""
        vat_calculation = self.calculate_vat_obligations()
        
        report = {
            "company_name": self.company_name,
            "calculation_date": self.calculation_date,
            "company_info": self.company_info,
            "vat_periods": self.vat_periods,
            "sales_transactions": self.sales_transactions,
            "purchase_transactions": self.purchase_transactions,
            "vat_corrections": self.vat_corrections,
            "calculation": vat_calculation,
            "reporting_analytics": self.reporting_analytics,
            "vat_return_submissions": self.vat_return_submissions,
            "recommendations": self._generate_recommendations(vat_calculation)
        }
        
        return report
    
    def _generate_recommendations(self, vat_calculation: Dict) -> List[str]:
        """Generate recommendations based on the VAT calculation."""
        recommendations = []
        
        # Check if VAT recovery rate is low
        if vat_calculation["vat_recovery_rate"] < 70:
            recommendations.append("VAT recovery rate is low (<70%). Review deductible expenses to optimize VAT recovery.")
        
        # Check if net VAT payable is significantly high
        if vat_calculation["net_vat_payable"] > 10000:
            recommendations.append("Net VAT payable is high. Consider cash flow planning for VAT payments.")
        
        # Check if there are many small transactions
        total_transactions = len(self.sales_transactions) + len(self.purchase_transactions)
        if total_transactions > 100:
            recommendations.append("High number of transactions detected. Consider automation tools for VAT processing.")
        
        # Check if there are unallocated amounts
        if self.unallocated_vat:
            recommendations.append("Unallocated VAT amounts detected. Investigate and allocate properly.")
        
        # If no recommendations, add a positive note
        if not recommendations:
            recommendations.append("VAT calculations appear to be in good order. All required elements are present.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the VAT calculation to a JSON file."""
        report = self.generate_vat_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a VAT calculation from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.calculation_date = data.get("calculation_date", self.calculation_date)
        self.company_info = data.get("company_info", self.company_info)
        self.vat_periods = data.get("vat_periods", self.vat_periods)
        self.sales_transactions = data.get("sales_transactions", self.sales_transactions)
        self.purchase_transactions = data.get("purchase_transactions", self.purchase_transactions)
        self.vat_corrections = data.get("vat_corrections", self.vat_corrections)
        self.vat_return_submissions = data.get("vat_return_submissions", self.vat_return_submissions)
        self.reporting_analytics = data.get("reporting_analytics", self.reporting_analytics)


def create_sample_vat_calculation() -> DomesticTradeVATCalculator:
    """Create a sample VAT calculation with example data."""
    vat_calc = DomesticTradeVATCalculator(company_name="Sample VAT Company Oy", year=2026)
    
    # Set company information
    vat_calc.set_company_info(
        name="Sample VAT Company Oy",
        business_id="1234567-8",
        address="VATkatu 15, 33100 Tampere",
        contact_person="VAT Manager: Veijo VAT",
        phone="0500 123 456",
        email="veijo.vat@samplevatcompany.fi",
        vat_registration="FI12345678"
    )
    
    # Add example sales transactions (output VAT)
    vat_calc.add_sales_transaction(
        date="2026-01-15",
        description="Sale of goods to Customer A",
        taxable_amount=10000.00,
        vat_rate=0.24,
        customer="Customer A Oy",
        document_number="SALE-001"
    )
    
    vat_calc.add_sales_transaction(
        date="2026-01-20",
        description="Service provision to Customer B",
        taxable_amount=5000.00,
        vat_rate=0.24,
        customer="Customer B Ltd",
        document_number="SALE-002"
    )
    
    vat_calc.add_sales_transaction(
        date="2026-02-05",
        description="Sale of reduced VAT goods",
        taxable_amount=2000.00,
        vat_rate=0.10,
        customer="Customer C Ab",
        document_number="SALE-003"
    )
    
    # Add example purchase transactions (input VAT)
    vat_calc.add_purchase_transaction(
        date="2026-01-10",
        description="Office supplies purchase",
        taxable_amount=1500.00,
        vat_rate=0.24,
        supplier="Supplier X Oy",
        document_number="PURCHASE-001"
    )
    
    vat_calc.add_purchase_transaction(
        date="2026-01-25",
        description="Business equipment",
        taxable_amount=8000.00,
        vat_rate=0.24,
        supplier="Supplier Y Ltd",
        document_number="PURCHASE-002"
    )
    
    vat_calc.add_purchase_transaction(
        date="2026-02-10",
        description="Professional services",
        taxable_amount=3000.00,
        vat_rate=0.24,
        supplier="Consultant Z Ab",
        document_number="PURCHASE-003"
    )
    
    # Add a VAT correction
    vat_calc.add_vat_correction(
        date="2026-02-15",
        description="Correction for previous period error",
        amount=-120.00,  # Negative correction
        correction_type="error_correction"
    )
    
    # Set VAT periods
    vat_calc.vat_periods = {
        "current_period": "2026-Q1",
        "previous_period": "2025-Q4",
        "period_start_date": "2026-01-01",
        "period_end_date": "2026-03-31",
        "submission_deadline": "2026-05-12"
    }
    
    return vat_calc


if __name__ == "__main__":
    # Example usage
    print("L15 Kotimaankaupan Alv-laskelma - Domestic Trade VAT Calculator")
    print("=" * 70)
    
    # Create a sample VAT calculation
    sample_vat_calc = create_sample_vat_calculation()
    
    # Generate and display the VAT report
    vat_report = sample_vat_calc.generate_vat_report()
    
    print(f"\nCompany: {vat_report['company_name']}")
    print(f"Calculation Date: {vat_report['calculation_date']}")
    
    print(f"\nCompany Info: {vat_report['company_info']['name']}")
    print(f"  Business ID: {vat_report['company_info']['business_id']}")
    print(f"  Address: {vat_report['company_info']['address']}")
    print(f"  Contact: {vat_report['company_info']['contact_person']}")
    
    print(f"\nVAT Period: {vat_report['vat_periods']['current_period']}")
    print(f"  Period Start: {vat_report['vat_periods']['period_start_date']}")
    print(f"  Period End: {vat_report['vat_periods']['period_end_date']}")
    print(f"  Submission Deadline: {vat_report['vat_periods']['submission_deadline']}")
    
    print(f"\nSales Transactions (Output VAT):")
    for i, sale in enumerate(vat_report['sales_transactions'], 1):
        print(f"  {i}. {sale['description']}")
        print(f"     Date: {sale['date']}")
        print(f"     Customer: {sale['customer']}")
        print(f"     Document: {sale['document_number']}")
        print(f"     Taxable Amount: €{sale['taxable_amount']:.2f}")
        print(f"     VAT Rate: {sale['vat_rate']:.1%}")
        print(f"     Output VAT: €{sale['output_vat']:.2f}")
    
    print(f"\nPurchase Transactions (Input VAT):")
    for i, purchase in enumerate(vat_report['purchase_transactions'], 1):
        print(f"  {i}. {purchase['description']}")
        print(f"     Date: {purchase['date']}")
        print(f"     Supplier: {purchase['supplier']}")
        print(f"     Document: {purchase['document_number']}")
        print(f"     Taxable Amount: €{purchase['taxable_amount']:.2f}")
        print(f"     VAT Rate: {purchase['vat_rate']:.1%}")
        print(f"     Input VAT: €{purchase['input_vat']:.2f}")
    
    print(f"\nVAT Corrections:")
    for i, correction in enumerate(vat_report['vat_corrections'] or [], 1):
        print(f"  {i}. {correction['description']}")
        print(f"     Date: {correction['date']}")
        print(f"     Type: {correction['type']}")
        print(f"     Amount: €{correction['amount']:.2f}")
    
    print(f"\nVAT Calculation Summary:")
    calc = vat_report['calculation']
    print(f"  Total Output VAT (Sales): €{calc['total_output_vat']:.2f}")
    print(f"  Total Input VAT (Purchases): €{calc['total_input_vat']:.2f}")
    print(f"  Correction Amount: €{calc['correction_amount']:.2f}")
    print(f"  Net VAT Payable: €{calc['net_vat_payable']:.2f}")
    print(f"  VAT Recovery Rate: {calc['vat_recovery_rate']:.1f}%")
    
    print(f"\nReporting Analytics:")
    analytics = vat_report['reporting_analytics']
    print(f"  Total Taxable Sales: €{analytics['total_taxable_sales']:.2f}")
    print(f"  Total Taxable Purchases: €{analytics['total_taxable_purchases']:.2f}")
    print(f"  VAT Efficiency Ratio: {analytics['vat_efficiency_ratio']:.1f}%")
    print(f"  Compliance Score: {analytics['compliance_score']}/100")
    print(f"  Audit Risk Level: {analytics['audit_risk_level']}")
    
    print(f"\nVAT Return Submissions: {len(vat_report['vat_return_submissions'])}")
    
    print(f"\nRecommendations:")
    for rec in vat_report['recommendations']:
        print(f"  - {rec}")
    
    # Submit a VAT return
    print(f"\nSubmitting VAT return for {vat_report['vat_periods']['current_period']}...")
    vat_return = sample_vat_calc.submit_vat_return(vat_report['vat_periods']['current_period'])
    print(f"VAT return submitted successfully for period {vat_return['period']}")
    
    # Save the VAT calculation to a JSON file
    sample_vat_calc.save_to_json("sample_domestic_trade_vat_calculation.json")
    print(f"\nVAT calculation saved to 'sample_domestic_trade_vat_calculation.json'")