"""
Python implementation of L5_Laskulomake_2026 invoice form template.

This module provides programmatic access to the 2026 invoice form functionality
originally implemented in the L5_Laskulomake_2026.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class InvoiceForm2026:
    """
    A class representing an invoice form for 2026 based on the 
    L5_Laskulomake_2026 template.
    This tool helps businesses create standardized invoices for customers in 2026, 
    detailing products or services provided, pricing, taxes, and payment terms.
    This is an updated version of the invoice form template specifically designed 
    for 2026 with any regulatory updates or business requirement changes.
    """
    
    def __init__(self, company_name: str = "Invoice Company 2026", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.invoice_date = datetime.now().strftime('%Y-%m-%d')
        self.invoice_number = ""
        self.sender_info = {}  # Sender information
        self.receiver_info = {}  # Receiver information
        self.invoice_items = []  # List of invoice items
        self.payment_terms = {}  # Payment terms and conditions
        self.vat_calculations = {}  # VAT calculations
        self.total_amounts = {}  # Total amounts (excl. and incl. VAT)
        self.due_date = ""
        self.reference_number = ""
        self.bank_account_info = {}  # Bank account information
        self.currency = "EUR"  # Default currency
        self.discount_info = {}  # Discount information
        self.late_payment_interest = 0.095  # Updated 2026 late payment interest (9.5%)
        self.delivery_info = {}  # Delivery information
        self.invoice_period = ""  # Billing period
        self.verification_info = {}  # Verification information
        self.accounting_info = {}  # Accounting information
        self.customer_history = {}  # Customer order history
        self.special_notes = ""
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the 2026 invoice form with default values."""
        # Default sender information
        self.sender_info = {
            "name": self.company_name,
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "website": "",
            "vat_registration": ""
        }
        
        # Default receiver information
        self.receiver_info = {
            "name": "",
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Bank transfer",
            "payment_period_days": 14,
            "due_date": "",
            "early_payment_discount": 0.0,  # 0% default
            "early_payment_discount_days": 0  # Days within which to pay for discount
        }
        
        # Default bank account information
        self.bank_account_info = {
            "iban": "",
            "bic": "",
            "bank_name": ""
        }
        
        # Default VAT calculations
        self.vat_calculations = {
            "vat_0_percent": 0.0,
            "vat_10_percent": 0.0,
            "vat_14_percent": 0.0,
            "vat_24_percent": 0.0  # Standard Finnish VAT rate
        }
        
        # Default discount information
        self.discount_info = {
            "discount_percentage": 0.0,
            "discount_reason": ""
        }
        
        # Default delivery information
        self.delivery_info = {
            "delivery_date": "",
            "delivery_method": ""
        }
        
        # Default invoice items list
        self.invoice_items = []
        
        # Default total amounts
        self.total_amounts = {
            "subtotal_excl_vat": 0.0,
            "total_vat": 0.0,
            "total_incl_vat": 0.0
        }
    
    def set_sender_info(self, name: str, address: str, business_id: str = "", 
                       contact_person: str = "", phone: str = "", email: str = "",
                       website: str = "", vat_registration: str = ""):
        """Set sender information."""
        self.sender_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "website": website,
            "vat_registration": vat_registration
        }
    
    def set_receiver_info(self, name: str, address: str, business_id: str = "", 
                         contact_person: str = "", phone: str = "", email: str = ""):
        """Set receiver information."""
        self.receiver_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def add_invoice_item(self, description: str, quantity: float, unit: str, 
                        unit_price_excl_vat: float, vat_percentage: float = 24.0):
        """Add an item to the invoice."""
        item = {
            "description": description,
            "quantity": quantity,
            "unit": unit,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_percentage": vat_percentage,
            "total_excl_vat": quantity * unit_price_excl_vat,
            "total_vat": quantity * unit_price_excl_vat * (vat_percentage / 100),
            "total_incl_vat": quantity * unit_price_excl_vat * (1 + vat_percentage / 100)
        }
        
        self.invoice_items.append(item)
        return item
    
    def set_payment_terms(self, payment_method: str, payment_period_days: int, 
                         early_payment_discount: float = 0.0, early_payment_discount_days: int = 0):
        """Set payment terms."""
        self.payment_terms = {
            "payment_method": payment_method,
            "payment_period_days": payment_period_days,
            "early_payment_discount": early_payment_discount,
            "early_payment_discount_days": early_payment_discount_days
        }
        
        # Calculate due date
        from datetime import datetime, timedelta
        invoice_date_obj = datetime.strptime(self.invoice_date, '%Y-%m-%d')
        due_date_obj = invoice_date_obj + timedelta(days=payment_period_days)
        self.due_date = due_date_obj.strftime('%Y-%m-%d')
        self.payment_terms["due_date"] = self.due_date
    
    def set_bank_account_info(self, iban: str, bic: str = "", bank_name: str = ""):
        """Set bank account information."""
        self.bank_account_info = {
            "iban": iban,
            "bic": bic,
            "bank_name": bank_name
        }
    
    def set_invoice_period(self, period: str):
        """Set the invoice period."""
        self.invoice_period = period
    
    def set_delivery_info(self, delivery_date: str, delivery_method: str = ""):
        """Set delivery information."""
        self.delivery_info = {
            "delivery_date": delivery_date,
            "delivery_method": delivery_method
        }
    
    def calculate_totals(self) -> Dict:
        """Calculate subtotal, VAT, and total amounts."""
        subtotal_excl_vat = sum(item["total_excl_vat"] for item in self.invoice_items)
        
        # Calculate VAT by rate
        vat_by_rate = {}
        for item in self.invoice_items:
            rate = item["vat_percentage"]
            if rate not in vat_by_rate:
                vat_by_rate[rate] = {"amount": 0.0, "percentage_of_total": 0.0}
            vat_by_rate[rate]["amount"] += item["total_vat"]
        
        # Calculate total VAT
        total_vat = sum(item["amount"] for item in vat_by_rate.values())
        
        # Calculate total including VAT
        total_incl_vat = subtotal_excl_vat + total_vat
        
        # Apply discount if applicable
        discount_amount = 0
        if self.discount_info["discount_percentage"] > 0:
            discount_amount = total_incl_vat * (self.discount_info["discount_percentage"] / 100)
        
        # Add shipping costs
        shipping_cost = getattr(self, 'shipping_cost', 0.0)
        
        final_total = total_incl_vat - discount_amount + shipping_cost
        
        self.total_amounts = {
            "subtotal_excl_vat": subtotal_excl_vat,
            "total_vat": total_vat,
            "total_incl_vat": total_incl_vat,
            "discount_amount": discount_amount,
            "shipping_cost": shipping_cost,
            "final_total": final_total,
            "vat_breakdown": vat_by_rate
        }
        
        return self.total_amounts
    
    def generate_reference_number(self) -> str:
        """Generate a reference number for the 2026 invoice."""
        # In a real implementation, this would follow Finnish reference number standards
        # For this example, we'll create a simple reference number based on 2026
        import random
        self.reference_number = f"{20000 + len(self.invoice_items) + self.year - 2000}"
        return self.reference_number
    
    def generate_invoice_document(self) -> Dict:
        """Generate a complete 2026 invoice document."""
        totals = self.calculate_totals()
        ref_number = self.generate_reference_number()
        
        invoice_doc = {
            "company_name": self.company_name,
            "invoice_date": self.invoice_date,
            "invoice_number": self.invoice_number,
            "sender_info": self.sender_info,
            "receiver_info": self.receiver_info,
            "invoice_items": self.invoice_items,
            "payment_terms": self.payment_terms,
            "due_date": self.due_date,
            "reference_number": ref_number,
            "bank_account_info": self.bank_account_info,
            "currency": self.currency,
            "discount_info": self.discount_info,
            "late_payment_interest": self.late_payment_interest,
            "delivery_info": self.delivery_info,
            "invoice_period": self.invoice_period,
            "totals": totals,
            "verification_info": self.verification_info,
            "accounting_info": self.accounting_info
        }
        
        return invoice_doc
    
    def generate_invoice_report(self) -> Dict:
        """Generate a comprehensive 2026 invoice report with additional analytics."""
        invoice_doc = self.generate_invoice_document()
        
        # Calculate additional analytics
        totals = self.calculate_totals()
        analytics = {
            "total_items": len(self.invoice_items),
            "average_item_value": sum(item["total_incl_vat"] for item in self.invoice_items) / len(self.invoice_items) if self.invoice_items else 0,
            "vat_rate_distribution": self._calculate_vat_rate_distribution(),
            "payment_terms_summary": f"{self.payment_terms['payment_period_days']} days, {self.payment_terms['payment_method']}",
            "days_until_due": self._calculate_days_until_due(),
            "invoice_age": self._calculate_invoice_age()
        }
        
        report = {
            "invoice_document": invoice_doc,
            "analytics": analytics,
            "recommendations": self._generate_recommendations(invoice_doc)
        }
        
        return report
    
    def _calculate_vat_rate_distribution(self) -> Dict:
        """Calculate the distribution of VAT rates in the invoice."""
        vat_dist = {}
        for item in self.invoice_items:
            rate = item["vat_percentage"]
            if rate not in vat_dist:
                vat_dist[rate] = {"amount": 0, "percentage_of_total": 0}
            vat_dist[rate]["amount"] += item["total_vat"]
        
        total_vat = sum(item["total_vat"] for item in self.invoice_items)
        if total_vat > 0:
            for rate in vat_dist:
                vat_dist[rate]["percentage_of_total"] = (vat_dist[rate]["amount"] / total_vat) * 100
        
        return vat_dist
    
    def _calculate_days_until_due(self) -> int:
        """Calculate the number of days until the invoice is due."""
        from datetime import datetime
        due_date_obj = datetime.strptime(self.due_date, '%Y-%m-%d')
        today = datetime.now()
        delta = due_date_obj - today
        return delta.days

    def _calculate_invoice_age(self) -> int:
        """Calculate the age of the invoice in days."""
        from datetime import datetime
        invoice_date_obj = datetime.strptime(self.invoice_date, '%Y-%m-%d')
        today = datetime.now()
        delta = today - invoice_date_obj
        return delta.days
    
    def _generate_recommendations(self, invoice_doc: Dict) -> List[str]:
        """Generate recommendations based on the 2026 invoice."""
        recommendations = []
        
        # Check if payment terms are reasonable
        if self.payment_terms["payment_period_days"] > 60:
            recommendations.append("Payment period is quite long (over 60 days). Consider reducing to improve cash flow.")
        
        # Check for high discount rates
        if self.discount_info["discount_percentage"] > 5:
            recommendations.append("High discount rate applied. Verify this is intentional and profitable.")
        
        # Check for items with zero VAT (could be compliance issue)
        zero_vat_items = [item for item in self.invoice_items if item["vat_percentage"] == 0]
        if len(zero_vat_items) > 0:
            recommendations.append(f"Found {len(zero_vat_items)} items with 0% VAT. Verify these comply with VAT regulations.")
        
        # If no recommendations, add a positive note
        if not recommendations:
            recommendations.append("Invoice appears to be in good order. Payment terms and VAT rates look appropriate for 2026.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the 2026 invoice to a JSON file."""
        report = self.generate_invoice_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a 2026 invoice from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        invoice_doc = data.get("invoice_document", {})
        self.company_name = invoice_doc.get("company_name", self.company_name)
        self.invoice_date = invoice_doc.get("invoice_date", self.invoice_date)
        self.invoice_number = invoice_doc.get("invoice_number", self.invoice_number)
        self.sender_info = invoice_doc.get("sender_info", self.sender_info)
        self.receiver_info = invoice_doc.get("receiver_info", self.receiver_info)
        self.invoice_items = invoice_doc.get("invoice_items", self.invoice_items)
        self.payment_terms = invoice_doc.get("payment_terms", self.payment_terms)
        self.due_date = invoice_doc.get("due_date", self.due_date)
        self.reference_number = invoice_doc.get("reference_number", self.reference_number)
        self.bank_account_info = invoice_doc.get("bank_account_info", self.bank_account_info)
        self.totals = invoice_doc.get("totals", self.totals)


def create_sample_invoice() -> InvoiceForm2026:
    """Create a sample 2026 invoice with example data."""
    invoice = InvoiceForm2026(company_name="Sample Invoice 2026 Oy", year=2026)
    
    # Set sender information
    invoice.set_sender_info(
        name="Sample Invoice 2026 Oy",
        address="Laskutuskatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Laskuttaja: Liisa Laskuttaja",
        phone="0500 123 456",
        email="liisa.laskuttaja@sampleinvoice2026.fi",
        website="www.sampleinvoice2026.fi",
        vat_registration="FI12345678"
    )
    
    # Set receiver information
    invoice.set_receiver_info(
        name="Asiakas Oy",
        address="Asiakaskatu 20, 00100 Helsinki",
        business_id="8765432-1",
        contact_person="Asiakas: Aino Asiakas",
        phone="0400 987 654",
        email="aino.asiakas@asiakas.fi"
    )
    
    # Set invoice details
    invoice.invoice_number = "INV-2026-001"
    invoice.invoice_date = "2026-01-01"  # Updated for 2026
    invoice.set_invoice_period("January 2026")
    
    # Add invoice items based on the 2026 template
    invoice.add_invoice_item(
        description="Esimerkkituote - Sample product",
        quantity=1,
        unit="kpl",
        unit_price_excl_vat=125.50,
        vat_percentage=25.5  # Updated VAT rate from the spreadsheet
    )
    
    invoice.add_invoice_item(
        description="Tuote - Product",
        quantity=1,
        unit="kg",
        unit_price_excl_vat=113.50,
        vat_percentage=13.5  # Different VAT rate
    )
    
    invoice.add_invoice_item(
        description="Tuote - Product",
        quantity=1,
        unit="kpl",
        unit_price_excl_vat=110.00,
        vat_percentage=10.0  # Another VAT rate
    )
    
    # Set payment terms
    invoice.set_payment_terms(
        payment_method="Bank transfer",
        payment_period_days=14,  # Standard 14 days
        early_payment_discount=2.0,  # 2% discount if paid within 7 days
        early_payment_discount_days=7
    )
    
    # Set bank account information
    invoice.set_bank_account_info(
        iban="FI0000000012345678",
        bic="SBLOFIHH",
        bank_name="Sample Bank Oy"
    )
    
    # Set delivery information
    invoice.set_delivery_info(
        delivery_date="2025-12-20",  # Past delivery date
        delivery_method="Courier service"
    )
    
    # Set discount information
    invoice.discount_info = {
        "discount_percentage": 0.0,  # No discount in this example
        "discount_reason": ""
    }
    
    # Set shipping cost
    invoice.shipping_cost = 10.0  # Example shipping cost
    
    return invoice


if __name__ == "__main__":
    # Example usage
    print("L5 Laskulomake 2026 - Invoice Form Tool")
    print("=" * 45)
    
    # Create a sample 2026 invoice
    sample_invoice = create_sample_invoice()
    
    # Generate and display the invoice document
    invoice_doc = sample_invoice.generate_invoice_document()
    
    print(f"\nCompany: {invoice_doc['company_name']}")
    print(f"Invoice Date: {invoice_doc['invoice_date']}")
    print(f"Invoice Number: {invoice_doc['invoice_number']}")
    print(f"Invoice Period: {invoice_doc['invoice_period']}")
    print(f"Reference Number: {invoice_doc['reference_number']}")
    print(f"Due Date: {invoice_doc['due_date']}")
    print(f"Days Until Due: {sample_invoice._calculate_days_until_due()}")
    
    print(f"\nSender: {invoice_doc['sender_info']['name']}")
    print(f"  Address: {invoice_doc['sender_info']['address']}")
    print(f"  Business ID: {invoice_doc['sender_info']['business_id']}")
    print(f"  Contact: {invoice_doc['sender_info']['contact_person']}")
    
    print(f"\nReceiver: {invoice_doc['receiver_info']['name']}")
    print(f"  Address: {invoice_doc['receiver_info']['address']}")
    print(f"  Business ID: {invoice_doc['receiver_info']['business_id']}")
    print(f"  Contact: {invoice_doc['receiver_info']['contact_person']}")
    
    print(f"\nInvoice Items:")
    for i, item in enumerate(invoice_doc['invoice_items'], 1):
        print(f"  {i}. {item['description']}")
        print(f"     Quantity: {item['quantity']} {item['unit']}")
        print(f"     Unit Price (excl. VAT): €{item['unit_price_excl_vat']:.2f}")
        print(f"     VAT Rate: {item['vat_percentage']}%")
        print(f"     Total (excl. VAT): €{item['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{item['total_incl_vat']:.2f}")
    
    print(f"\nFinancial Summary:")
    totals = invoice_doc['totals']
    print(f"  Subtotal (excl. VAT): €{totals['subtotal_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total (incl. VAT): €{totals['total_incl_vat']:.2f}")
    print(f"  Discount Applied: €{totals['discount_amount']:.2f}")
    print(f"  Shipping Cost: €{totals['shipping_cost']:.2f}")
    print(f"  Final Total: €{totals['final_total']:.2f}")
    
    print(f"\nVAT Breakdown:")
    for rate, data in totals['vat_breakdown'].items():
        print(f"  {rate}% VAT: €{data['amount']:.2f} ({data['percentage_of_total']:.1f}% of total VAT)")
    
    print(f"\nPayment Terms:")
    payment = invoice_doc['payment_terms']
    print(f"  Method: {payment['payment_method']}")
    print(f"  Period: {payment['payment_period_days']} days")
    print(f"  Due Date: {payment['due_date']}")
    if payment['early_payment_discount'] > 0:
        print(f"  Early Payment Discount: {payment['early_payment_discount']}% if paid within {payment['early_payment_discount_days']} days")
    
    print(f"\nBank Account Information:")
    bank = invoice_doc['bank_account_info']
    print(f"  IBAN: {bank['iban']}")
    print(f"  BIC: {bank['bic']}")
    print(f"  Bank: {bank['bank_name']}")
    
    print(f"\nDelivery Information:")
    delivery = invoice_doc['delivery_info']
    print(f"  Date: {delivery['delivery_date']}")
    print(f"  Method: {delivery['delivery_method']}")
    
    print(f"\nLate Payment Interest: {invoice_doc['late_payment_interest']:.1%}")
    
    # Generate and display the invoice report
    print(f"\nGenerating invoice report...")
    report = sample_invoice.generate_invoice_report()
    
    analytics = report['analytics']
    print(f"\nInvoice Analytics:")
    print(f"  Total Items: {analytics['total_items']}")
    print(f"  Average Item Value: €{analytics['average_item_value']:.2f}")
    print(f"  Payment Terms Summary: {analytics['payment_terms_summary']}")
    print(f"  Days Until Due: {analytics['days_until_due']}")
    print(f"  Invoice Age: {analytics['invoice_age']} days")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the invoice to a JSON file
    sample_invoice.save_to_json("sample_invoice_form_2026.json")
    print(f"\n2026 Invoice form saved to 'sample_invoice_form_2026.json'")