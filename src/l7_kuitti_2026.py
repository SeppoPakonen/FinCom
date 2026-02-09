"""
Python implementation of L7_Kuitti_2026 receipt template.

This module provides programmatic access to the receipt functionality
originally implemented in the L7_Kuitti_2026.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class Receipt2026:
    """
    A class representing a receipt for 2026 based on the L7_Kuitti_2026 template.
    This tool helps businesses create standardized receipts for customers, 
    documenting transactions, payments, and other financial exchanges in a compliant format.
    """
    
    def __init__(self, company_name: str = "Receipt Company 2026", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.receipt_date = datetime.now().strftime('%d.%m.%Y')
        self.receipt_number = ""
        self.payee_info = {}  # Payee (business) information
        self.payer_info = {}  # Payer (customer) information
        self.transaction_details = {}  # Transaction details
        self.items = []  # List of items in the receipt
        self.payment_info = {}  # Payment information
        self.vat_calculations = {}  # VAT calculations
        self.total_amounts = {}  # Total amounts (excl. and incl. VAT)
        self.receipt_reference = ""  # Reference number
        self.cashier_info = {}  # Cashier/operator information
        self.store_location = {}  # Store/location information
        self.exchange_conditions = {}  # Exchange conditions
        self.return_policy = {}  # Return policy
        self.accounting_info = {}  # Accounting information
        self.revenue_tracking = {}  # Revenue tracking
        self.expense_tracking = {}  # Expense tracking
        self.vat_reporting = {}  # VAT reporting information
        self.cash_register_info = {}  # Cash register accounting
        self.card_payment_info = {}  # Card payment tracking
        self.cash_payment_info = {}  # Cash payment tracking
        self.invoice_correlation = {}  # Invoice-receipt correlation
        self.warranty_terms = {}  # Warranty terms
        self.credits_refunds = {}  # Credits and refunds
        self.correction_policy = {}  # Correction policies
        self.audit_trail = {}  # Audit trail for receipts
        self.reporting_analytics = {}  # Reporting and analytics
        self.late_payment_interest = {}  # Late payment interest tracking
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the receipt with default values."""
        # Default payee information
        self.payee_info = {
            "name": self.company_name,
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "website": "",
            "vat_registration": ""
        }
        
        # Default payer information
        self.payer_info = {
            "name": "",
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default transaction details
        self.transaction_details = {
            "transaction_date": self.receipt_date,
            "transaction_time": datetime.now().strftime('%H:%M:%S'),
            "transaction_id": "",
            "location": "",
            "cash_register_id": ""
        }
        
        # Default payment information
        self.payment_info = {
            "payment_method": "Cash",
            "payment_reference": "",
            "currency": "EUR",
            "exchange_rate": 1.0
        }
        
        # Default VAT calculations
        self.vat_calculations = {
            "vat_0_percent": 0.0,
            "vat_10_percent": 0.0,
            "vat_14_percent": 0.0,
            "vat_24_percent": 0.0  # Standard Finnish VAT rate
        }
        
        # Default cashier information
        self.cashier_info = {
            "name": "",
            "employee_id": ""
        }
        
        # Default store/location information
        self.store_location = {
            "name": "",
            "address": "",
            "location_id": ""
        }
        
        # Default exchange conditions
        self.exchange_conditions = {
            "time_limit": "14 days",
            "condition_requirement": "Item must be in original condition",
            "receipt_required": True
        }
        
        # Default return policy
        self.return_policy = {
            "return_period": "30 days",
            "condition_requirement": "Item must be unused and in original packaging",
            "refund_method": "Original payment method",
            "restocking_fee": 0.0
        }
        
        # Default warranty terms
        self.warranty_terms = {
            "warranty_period": "12 months",
            "warranty_scope": "Manufacturing defects",
            "warranty_exclusions": "Damage due to misuse or normal wear"
        }
        
        # Default items list
        self.items = []
        
        # Default total amounts
        self.total_amounts = {
            "subtotal_excl_vat": 0.0,
            "total_vat": 0.0,
            "total_incl_vat": 0.0
        }
    
    def add_item(self, product_name: str, quantity: float, unit: str, 
                unit_price_excl_vat: float, vat_percentage: float = 24.0):
        """Add an item to the receipt."""
        item = {
            "product_name": product_name,
            "quantity": quantity,
            "unit": unit,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_percentage": vat_percentage,
            "total_excl_vat": quantity * unit_price_excl_vat,
            "total_vat": quantity * unit_price_excl_vat * (vat_percentage / 100),
            "total_incl_vat": quantity * unit_price_excl_vat * (1 + vat_percentage / 100)
        }
        
        self.items.append(item)
        return item
    
    def set_payee_info(self, name: str, address: str, business_id: str = "", 
                      contact_person: str = "", phone: str = "", email: str = "",
                      website: str = "", vat_registration: str = ""):
        """Set payee (business) information."""
        self.payee_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "website": website,
            "vat_registration": vat_registration
        }
    
    def set_payer_info(self, name: str, address: str, business_id: str = "", 
                      contact_person: str = "", phone: str = "", email: str = ""):
        """Set payer (customer) information."""
        self.payer_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_transaction_details(self, transaction_date: str, location: str, 
                               cash_register_id: str = "", transaction_id: str = ""):
        """Set transaction details."""
        self.transaction_details = {
            "transaction_date": transaction_date,
            "transaction_time": datetime.now().strftime('%H:%M:%S'),
            "transaction_id": transaction_id,
            "location": location,
            "cash_register_id": cash_register_id
        }
    
    def set_payment_info(self, method: str, reference: str = "", currency: str = "EUR", exchange_rate: float = 1.0):
        """Set payment information."""
        self.payment_info = {
            "payment_method": method,
            "payment_reference": reference,
            "currency": currency,
            "exchange_rate": exchange_rate
        }
    
    def set_cashier_info(self, name: str, employee_id: str = ""):
        """Set cashier information."""
        self.cashier_info = {
            "name": name,
            "employee_id": employee_id
        }
    
    def set_store_location(self, name: str, address: str, location_id: str = ""):
        """Set store/location information."""
        self.store_location = {
            "name": name,
            "address": address,
            "location_id": location_id
        }
    
    def calculate_receipt_totals(self) -> Dict:
        """Calculate subtotal, VAT, and total amounts for the receipt."""
        subtotal_excl_vat = sum(item["total_excl_vat"] for item in self.items)
        
        # Calculate VAT by rate
        vat_by_rate = {}
        for item in self.items:
            rate = item["vat_percentage"]
            if rate not in vat_by_rate:
                vat_by_rate[rate] = 0.0
            vat_by_rate[rate] += item["total_vat"]
        
        # Calculate total VAT
        total_vat = sum(vat_by_rate.values())
        
        # Calculate total including VAT
        total_incl_vat = subtotal_excl_vat + total_vat
        
        # Update VAT calculations
        for rate, amount in vat_by_rate.items():
            rate_str = f"vat_{int(rate)}_percent"
            if rate_str in self.vat_calculations:
                self.vat_calculations[rate_str] = amount
        
        self.total_amounts = {
            "subtotal_excl_vat": subtotal_excl_vat,
            "total_vat": total_vat,
            "total_incl_vat": total_incl_vat,
            "vat_breakdown": vat_by_rate
        }
        
        return self.total_amounts
    
    def generate_receipt_document(self) -> Dict:
        """Generate a complete receipt document."""
        totals = self.calculate_receipt_totals()
        
        receipt_doc = {
            "company_name": self.company_name,
            "receipt_date": self.receipt_date,
            "receipt_number": self.receipt_number,
            "payee_info": self.payee_info,
            "payer_info": self.payer_info,
            "transaction_details": self.transaction_details,
            "items": self.items,
            "payment_info": self.payment_info,
            "cashier_info": self.cashier_info,
            "store_location": self.store_location,
            "exchange_conditions": self.exchange_conditions,
            "return_policy": self.return_policy,
            "warranty_terms": self.warranty_terms,
            "totals": totals,
            "receipt_reference": self.receipt_reference,
            "vat_calculations": self.vat_calculations
        }
        
        return receipt_doc
    
    def generate_receipt_report(self) -> Dict:
        """Generate a comprehensive receipt report with additional analytics."""
        receipt_doc = self.generate_receipt_document()
        
        # Calculate additional analytics
        analytics = {
            "total_items": len(self.items),
            "average_item_value": sum(item["total_incl_vat"] for item in self.items) / len(self.items) if self.items else 0,
            "vat_rate_distribution": self._calculate_vat_rate_distribution(),
            "payment_method_summary": f"{self.payment_info['payment_method']}",
            "transaction_value_category": self._categorize_transaction_value(),
            "most_expensive_item": max(self.items, key=lambda x: x["total_incl_vat"]) if self.items else None,
            "least_expensive_item": min(self.items, key=lambda x: x["total_incl_vat"]) if self.items else None
        }
        
        report = {
            "receipt_document": receipt_doc,
            "analytics": analytics,
            "compliance_check": self._check_compliance(),
            "recommendations": self._generate_recommendations(receipt_doc)
        }
        
        return report
    
    def _calculate_vat_rate_distribution(self) -> Dict:
        """Calculate the distribution of VAT rates in the receipt."""
        vat_dist = {}
        for item in self.items:
            rate = item["vat_percentage"]
            if rate not in vat_dist:
                vat_dist[rate] = {"amount": 0, "percentage_of_total": 0}
            vat_dist[rate]["amount"] += item["total_vat"]
        
        total_vat = sum(item["total_vat"] for item in self.items)
        if total_vat > 0:
            for rate in vat_dist:
                vat_dist[rate]["percentage_of_total"] = (vat_dist[rate]["amount"] / total_vat) * 100
        
        return vat_dist
    
    def _categorize_transaction_value(self) -> str:
        """Categorize the transaction value."""
        total = self.total_amounts["total_incl_vat"]
        if total < 50:
            return "Small"
        elif total < 200:
            return "Medium"
        elif total < 500:
            return "Large"
        else:
            return "Extra Large"
    
    def _check_compliance(self) -> Dict:
        """Check if the receipt meets compliance requirements."""
        compliance = {
            "has_receipt_number": bool(self.receipt_number),
            "has_transaction_date": bool(self.transaction_details["transaction_date"]),
            "has_payee_info": bool(self.payee_info["name"]),
            "has_items": len(self.items) > 0,
            "has_total_amount": self.total_amounts["total_incl_vat"] > 0,
            "has_vat_breakdown": len(self.total_amounts["vat_breakdown"]) > 0,
            "overall_compliant": False
        }
        
        # Check if all required elements are present
        compliance["overall_compliant"] = all([
            compliance["has_receipt_number"],
            compliance["has_transaction_date"],
            compliance["has_payee_info"],
            compliance["has_items"],
            compliance["has_total_amount"],
            compliance["has_vat_breakdown"]
        ])
        
        return compliance
    
    def _generate_recommendations(self, receipt_doc: Dict) -> List[str]:
        """Generate recommendations based on the receipt."""
        recommendations = []
        
        # Check if transaction value is high enough for special attention
        if self.total_amounts["total_incl_vat"] > 1000:
            recommendations.append("High-value transaction. Consider additional verification or special handling.")
        
        # Check VAT rate distribution
        vat_dist = self._calculate_vat_rate_distribution()
        if len(vat_dist) > 1:
            recommendations.append("Multiple VAT rates applied. Verify correct classification of items.")
        
        # Check if any items have zero VAT (could be compliance issue)
        zero_vat_items = [item for item in self.items if item["vat_percentage"] == 0]
        if len(zero_vat_items) > 0:
            recommendations.append(f"Found {len(zero_vat_items)} items with 0% VAT. Verify these comply with VAT regulations.")
        
        # If no recommendations, add a positive note
        if not recommendations:
            recommendations.append("Receipt appears to be in good order. All required elements are present.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the receipt to a JSON file."""
        report = self.generate_receipt_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a receipt from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        receipt_doc = data.get("receipt_document", {})
        self.company_name = receipt_doc.get("company_name", self.company_name)
        self.receipt_date = receipt_doc.get("receipt_date", self.receipt_date)
        self.receipt_number = receipt_doc.get("receipt_number", self.receipt_number)
        self.payee_info = receipt_doc.get("payee_info", self.payee_info)
        self.payer_info = receipt_doc.get("payer_info", self.payer_info)
        self.transaction_details = receipt_doc.get("transaction_details", self.transaction_details)
        self.items = receipt_doc.get("items", self.items)
        self.payment_info = receipt_doc.get("payment_info", self.payment_info)
        self.totals = receipt_doc.get("totals", self.totals)


def create_sample_receipt() -> Receipt2026:
    """Create a sample receipt with example data."""
    receipt = Receipt2026(company_name="Sample Receipt Co 2026", year=2026)
    
    # Set payee information
    receipt.set_payee_info(
        name="Sample Receipt Oy",
        address="Kassakatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Kassamies: Kaisa Kassamies",
        phone="0500 123 456",
        email="kaisa.kassamies@samplereceipt.fi",
        website="www.samplereceipt.fi",
        vat_registration="FI12345678"
    )
    
    # Set payer information
    receipt.set_payer_info(
        name="Asiakas Oy",
        address="Asiakaskatu 20, 00100 Helsinki",
        business_id="8765432-1",
        contact_person="Asiakas: Aino Asiakas",
        phone="0400 987 654",
        email="aino.asiakas@asiakas.fi"
    )
    
    # Set transaction details
    receipt.set_transaction_details(
        transaction_date="2026-02-01",
        location="Tampere Store",
        cash_register_id="CR-001",
        transaction_id="TX-2026-001"
    )
    
    # Set payment information
    receipt.set_payment_info(
        method="Card",
        reference="POS-123456789",
        currency="EUR",
        exchange_rate=1.0
    )
    
    # Set cashier information
    receipt.set_cashier_info(
        name="Kaisa Kassamies",
        employee_id="EMP-001"
    )
    
    # Set store location
    receipt.set_store_location(
        name="Tampere Store",
        address="Kauppakeskus, Kauppakatu 10, 33100 Tampere"
    )
    
    # Add example items based on the spreadsheet structure
    receipt.add_item(
        product_name="Tuote 1: Esimerkki-ikkuna",
        quantity=1,
        unit="kpl",
        unit_price_excl_vat=125.50,
        vat_percentage=25.5
    )
    
    receipt.add_item(
        product_name="Tuote 2",
        quantity=1,
        unit="kg",
        unit_price_excl_vat=113.50,
        vat_percentage=13.5
    )
    
    receipt.add_item(
        product_name="Tuote 3",
        quantity=1,
        unit="l",
        unit_price_excl_vat=110.00,
        vat_percentage=10.0
    )
    
    # Set receipt number
    receipt.receipt_number = "REC-2026-001"
    
    # Set receipt reference
    receipt.receipt_reference = "REF-2026-001"
    
    return receipt


if __name__ == "__main__":
    # Example usage
    print("L7 Kuitti 2026 - Receipt Tool")
    print("=" * 35)
    
    # Create a sample receipt
    sample_receipt = create_sample_receipt()
    
    # Generate and display the receipt document
    receipt_doc = sample_receipt.generate_receipt_document()
    
    print(f"\nCompany: {receipt_doc['company_name']}")
    print(f"Receipt Date: {receipt_doc['receipt_date']}")
    print(f"Receipt Number: {receipt_doc['receipt_number']}")
    print(f"Transaction ID: {receipt_doc['transaction_details']['transaction_id']}")
    print(f"Cash Register: {receipt_doc['transaction_details']['cash_register_id']}")
    print(f"Location: {receipt_doc['transaction_details']['location']}")
    
    print(f"\nPayee: {receipt_doc['payee_info']['name']}")
    print(f"  Address: {receipt_doc['payee_info']['address']}")
    print(f"  Business ID: {receipt_doc['payee_info']['business_id']}")
    print(f"  Contact: {receipt_doc['payee_info']['contact_person']}")
    
    print(f"\nPayer: {receipt_doc['payer_info']['name']}")
    print(f"  Address: {receipt_doc['payer_info']['address']}")
    print(f"  Business ID: {receipt_doc['payer_info']['business_id']}")
    print(f"  Contact: {receipt_doc['payer_info']['contact_person']}")
    
    print(f"\nCashier: {receipt_doc['cashier_info']['name']} (ID: {receipt_doc['cashier_info']['employee_id']})")
    
    print(f"\nItems Purchased:")
    for i, item in enumerate(receipt_doc['items'], 1):
        print(f"  {i}. {item['product_name']}")
        print(f"     Quantity: {item['quantity']} {item['unit']}")
        print(f"     Unit Price (excl. VAT): €{item['unit_price_excl_vat']:.2f}")
        print(f"     VAT Rate: {item['vat_percentage']}%")
        print(f"     Total (excl. VAT): €{item['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{item['total_incl_vat']:.2f}")
    
    print(f"\nFinancial Summary:")
    totals = receipt_doc['totals']
    print(f"  Subtotal (excl. VAT): €{totals['subtotal_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total (incl. VAT): €{totals['total_incl_vat']:.2f}")
    
    print(f"\nVAT Breakdown:")
    for rate, amount in totals['vat_breakdown'].items():
        print(f"  {rate}% VAT: €{amount:.2f}")
    
    print(f"\nPayment Information:")
    payment = receipt_doc['payment_info']
    print(f"  Method: {payment['payment_method']}")
    print(f"  Reference: {payment['payment_reference']}")
    print(f"  Currency: {payment['currency']}")
    
    print(f"\nExchange Conditions:")
    exchange = receipt_doc['exchange_conditions']
    print(f"  Time Limit: {exchange['time_limit']}")
    print(f"  Condition: {exchange['condition_requirement']}")
    print(f"  Receipt Required: {exchange['receipt_required']}")
    
    print(f"\nReturn Policy:")
    ret = receipt_doc['return_policy']
    print(f"  Return Period: {ret['return_period']}")
    print(f"  Condition: {ret['condition_requirement']}")
    print(f"  Refund Method: {ret['refund_method']}")
    print(f"  Restocking Fee: €{ret['restocking_fee']:.2f}")
    
    print(f"\nWarranty Terms:")
    warranty = receipt_doc['warranty_terms']
    print(f"  Period: {warranty['warranty_period']}")
    print(f"  Scope: {warranty['warranty_scope']}")
    print(f"  Exclusions: {warranty['warranty_exclusions']}")
    
    # Generate and display the receipt report
    print(f"\nGenerating receipt report...")
    report = sample_receipt.generate_receipt_report()
    
    analytics = report['analytics']
    print(f"\nReceipt Analytics:")
    print(f"  Total Items: {analytics['total_items']}")
    print(f"  Average Item Value: €{analytics['average_item_value']:.2f}")
    print(f"  Transaction Category: {analytics['transaction_value_category']}")
    
    if analytics['most_expensive_item']:
        print(f"  Most Expensive Item: {analytics['most_expensive_item']['product_name']} (€{analytics['most_expensive_item']['total_incl_vat']:.2f})")
    
    if analytics['least_expensive_item']:
        print(f"  Least Expensive Item: {analytics['least_expensive_item']['product_name']} (€{analytics['least_expensive_item']['total_incl_vat']:.2f})")
    
    print(f"\nCompliance Check:")
    compliance = report['compliance_check']
    for check, result in compliance.items():
        if check != 'overall_compliant':
            print(f"  {check.replace('_', ' ').title()}: {'✓' if result else '✗'}")
    print(f"  Overall Compliant: {'✓' if compliance['overall_compliant'] else '✗'}")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the receipt to a JSON file
    sample_receipt.save_to_json("sample_receipt_2026.json")
    print(f"\nReceipt saved to 'sample_receipt_2026.json'")