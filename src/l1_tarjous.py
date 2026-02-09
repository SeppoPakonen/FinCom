"""
Python implementation of L1_Tarjous business proposal/invoice template.

This module provides programmatic access to the business proposal functionality
originally implemented in the L1_Tarjous.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class BusinessProposal:
    """
    A class representing a business proposal based on the L1_Tarjous template.
    This tool helps businesses create professional proposals for potential clients, 
    outlining the scope of work, pricing, terms, and conditions.
    """
    
    def __init__(self, company_name: str = "Business Proposal Co", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.offer_date = datetime.now().strftime('%d.%m.%Y')
        self.offer_number = ""
        self.customer_info = {}  # Customer information
        self.contact_person = ""
        self.contact_info = ""
        self.validity_period = ""  # How long the offer is valid
        self.delivery_info = {}  # Delivery information
        self.payment_terms = {}  # Payment terms and conditions
        self.services_offered = []  # List of services/products offered
        self.total_amount = 0.0
        self.vat_amount = 0.0
        self.total_including_vat = 0.0
        self.offer_request_reference = ""  # Reference to the offer request
        self.delivery_address = ""
        self.delivery_timeframe = ""
        self.terms_conditions = {}  # General terms and conditions
        self.quality_guarantee = {}  # Quality guarantee information
        self.contract_terms = {}  # Contract terms
        self.references = []  # References/templates
        self.project_tracking = {}  # Project tracking information
        self.cost_tracking = {}  # Cost tracking
        self.profit_tracking = {}  # Profit tracking
        self.risk_management = {}  # Risk management
        self.quality_criteria = {}  # Quality criteria
        self.discounts = {}  # Discounts and special offers
        self.additional_parts = {}  # Additional components or services
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the business proposal with default values."""
        # Default customer information
        self.customer_info = {
            "name": "",
            "address": "",
            "city": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default delivery information
        self.delivery_info = {
            "delivery_time": "2 weeks from order",
            "delivery_method": "Standard delivery",
            "installation_included": True
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Bank transfer",
            "payment_period": "30 days",
            "late_fee": "8% per annum"
        }
        
        # Default terms and conditions
        self.terms_conditions = {
            "validity": "30 days from offer date",
            "acceptance_period": "Offer valid for acceptance within validity period",
            "cancellation_policy": "Cancellable with 14 days notice",
            "dispute_resolution": "Handled according to Finnish law"
        }
        
        # Default quality guarantee
        self.quality_guarantee = {
            "warranty_period": "12 months",
            "warranty_scope": "Defects in materials and workmanship",
            "warranty_exclusions": "Damage due to misuse or normal wear"
        }
        
        # Default services offered (empty list to be populated)
        self.services_offered = []
        
        # Default discounts
        self.discounts = {
            "early_payment_discount": 0.0,  # 0% default
            "volume_discount": 0.0,         # 0% default
            "loyalty_discount": 0.0         # 0% default
        }
    
    def add_service(self, name: str, description: str, quantity: float, unit: str, 
                   unit_price_excl_vat: float, vat_percentage: float = 24.0):
        """Add a service or product to the proposal."""
        service = {
            "name": name,
            "description": description,
            "quantity": quantity,
            "unit": unit,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_percentage": vat_percentage,
            "total_excl_vat": quantity * unit_price_excl_vat,
            "total_vat": quantity * unit_price_excl_vat * (vat_percentage / 100),
            "total_incl_vat": quantity * unit_price_excl_vat * (1 + vat_percentage / 100)
        }
        
        self.services_offered.append(service)
        return service
    
    def set_customer_info(self, name: str, address: str, city: str, contact_person: str = "", 
                         phone: str = "", email: str = ""):
        """Set customer information."""
        self.customer_info = {
            "name": name,
            "address": address,
            "city": city,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_offer_number(self, number: str):
        """Set the offer number."""
        self.offer_number = number
    
    def set_validity_period(self, period: str):
        """Set the validity period of the offer."""
        self.validity_period = period
    
    def set_delivery_info(self, timeframe: str, address: str, method: str = "Standard delivery"):
        """Set delivery information."""
        self.delivery_info = {
            "delivery_timeframe": timeframe,
            "delivery_address": address,
            "delivery_method": method
        }
    
    def set_payment_terms(self, method: str, period: str, late_fee: str = "8% per annum"):
        """Set payment terms."""
        self.payment_terms = {
            "payment_method": method,
            "payment_period": period,
            "late_fee": late_fee
        }
    
    def apply_discount(self, discount_type: str, percentage: float):
        """Apply a discount to the proposal."""
        if discount_type in self.discounts:
            self.discounts[discount_type] = percentage
        else:
            raise ValueError(f"Unknown discount type: {discount_type}")
    
    def calculate_totals(self) -> Dict:
        """Calculate total amounts for the proposal."""
        total_excl_vat = sum(service["total_excl_vat"] for service in self.services_offered)
        total_vat = sum(service["total_vat"] for service in self.services_offered)
        total_incl_vat = sum(service["total_incl_vat"] for service in self.services_offered)
        
        # Apply discounts
        discount_amount = 0
        for discount_type, percentage in self.discounts.items():
            if percentage > 0:
                discount_amount += total_incl_vat * (percentage / 100)
        
        final_total = total_incl_vat - discount_amount
        
        self.total_amount = total_excl_vat
        self.vat_amount = total_vat
        self.total_including_vat = final_total
        
        return {
            "total_excl_vat": total_excl_vat,
            "total_vat": total_vat,
            "total_incl_vat": total_incl_vat,
            "discounts_applied": discount_amount,
            "final_total": final_total
        }
    
    def generate_proposal_document(self) -> Dict:
        """Generate a complete proposal document."""
        totals = self.calculate_totals()
        
        proposal_doc = {
            "company_name": self.company_name,
            "offer_date": self.offer_date,
            "offer_number": self.offer_number,
            "customer_info": self.customer_info,
            "contact_person": self.contact_person,
            "contact_info": self.contact_info,
            "validity_period": self.validity_period,
            "offer_request_reference": self.offer_request_reference,
            "delivery_info": self.delivery_info,
            "delivery_address": self.delivery_address,
            "delivery_timeframe": self.delivery_timeframe,
            "payment_terms": self.payment_terms,
            "services_offered": self.services_offered,
            "totals": totals,
            "terms_conditions": self.terms_conditions,
            "quality_guarantee": self.quality_guarantee,
            "contract_terms": self.contract_terms,
            "references": self.references,
            "project_tracking": self.project_tracking,
            "cost_tracking": self.cost_tracking,
            "profit_tracking": self.profit_tracking,
            "risk_management": self.risk_management,
            "quality_criteria": self.quality_criteria,
            "discounts": self.discounts
        }
        
        return proposal_doc
    
    def generate_invoice_if_accepted(self) -> Dict:
        """Generate an invoice based on the accepted proposal."""
        proposal_doc = self.generate_proposal_document()
        
        # Create invoice from accepted proposal
        invoice = {
            "invoice_number": f"INV-{self.offer_number}",
            "invoice_date": datetime.now().strftime('%d.%m.%Y'),
            "customer_info": proposal_doc["customer_info"],
            "items": [
                {
                    "description": service["name"],
                    "quantity": service["quantity"],
                    "unit": service["unit"],
                    "unit_price": service["unit_price_excl_vat"],
                    "vat_percentage": service["vat_percentage"],
                    "total_excl_vat": service["total_excl_vat"],
                    "total_vat": service["total_vat"],
                    "total_incl_vat": service["total_incl_vat"]
                }
                for service in proposal_doc["services_offered"]
            ],
            "total_amount": proposal_doc["totals"]["final_total"],
            "payment_terms": proposal_doc["payment_terms"],
            "due_date": self._calculate_due_date()
        }
        
        return invoice
    
    def _calculate_due_date(self) -> str:
        """Calculate the due date based on payment terms."""
        # This is a simplified implementation
        # In a real implementation, we would calculate based on payment period
        from datetime import datetime, timedelta
        today = datetime.now()
        # Assuming payment period is in format like "30 days"
        days = int(self.payment_terms["payment_period"].split()[0])
        due_date = today + timedelta(days=days)
        return due_date.strftime('%d.%m.%Y')
    
    def save_to_json(self, filepath: str):
        """Save the proposal to a JSON file."""
        proposal_doc = self.generate_proposal_document()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(proposal_doc, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a proposal from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.offer_date = data.get("offer_date", self.offer_date)
        self.offer_number = data.get("offer_number", self.offer_number)
        self.customer_info = data.get("customer_info", self.customer_info)
        self.services_offered = data.get("services_offered", self.services_offered)
        self.total_amount = data.get("total_amount", self.total_amount)
        self.vat_amount = data.get("vat_amount", self.vat_amount)
        self.total_including_vat = data.get("total_including_vat", self.total_including_vat)
        self.delivery_info = data.get("delivery_info", self.delivery_info)
        self.payment_terms = data.get("payment_terms", self.payment_terms)
        self.terms_conditions = data.get("terms_conditions", self.terms_conditions)
        self.discounts = data.get("discounts", self.discounts)


def create_sample_proposal() -> BusinessProposal:
    """Create a sample business proposal with example data."""
    proposal = BusinessProposal(company_name="Sample Business Oy", year=2026)
    
    # Set customer information
    proposal.set_customer_info(
        name="Kauppatalo Oy",
        address="Kauppakatu 1",
        city="00001 HELSINKI",
        contact_person="Matti Meikäläinen",
        phone="0500 123 456"
    )
    
    # Set offer details
    proposal.set_offer_number("XX0125")
    proposal.set_validity_period("30 days from offer date")
    proposal.offer_request_reference = "Toukokuun kampanja"
    proposal.delivery_timeframe = "2 weeks from order"
    proposal.delivery_address = "Keskustakatu 10, Helsinki"
    
    # Add example services based on the spreadsheet content
    proposal.add_service(
        name="Design services",
        description="- Suunnittelu",
        quantity=10,
        unit="h",
        unit_price_excl_vat=62,
        vat_percentage=25.5
    )
    
    proposal.add_service(
        name="Layout work",
        description="- Lay out - työt",
        quantity=1,
        unit="kpl",
        unit_price_excl_vat=700,
        vat_percentage=25.5
    )
    
    proposal.add_service(
        name="Printing and mounting of signs",
        description="- ilmoitusten painatus ja pinnoitus",
        quantity=10,
        unit="kpl",
        unit_price_excl_vat=385,
        vat_percentage=25.5
    )
    
    proposal.add_service(
        name="Installation of signs to signboards",
        description="- ilmoitusten asennus mainostelineisiin",
        quantity=10,
        unit="kpl",
        unit_price_excl_vat=125,
        vat_percentage=25.5
    )
    
    # Add additional service
    proposal.add_service(
        name="Store lighting book",
        description="- Myymälän valaistus - kirja",
        quantity=1,
        unit="kpl",
        unit_price_excl_vat=30,
        vat_percentage=10
    )
    
    # Set payment terms
    proposal.set_payment_terms(
        method="Bank transfer",
        period="30 days",
        late_fee="8% per annum"
    )
    
    # Apply a small discount
    proposal.apply_discount("volume_discount", 5.0)  # 5% volume discount
    
    return proposal


if __name__ == "__main__":
    # Example usage
    print("L1 Tarjous - Business Proposal Tool")
    print("=" * 40)
    
    # Create a sample business proposal
    sample_proposal = create_sample_proposal()
    
    # Generate and display the proposal document
    proposal_doc = sample_proposal.generate_proposal_document()
    
    print(f"\nCompany: {proposal_doc['company_name']}")
    print(f"Offer Date: {proposal_doc['offer_date']}")
    print(f"Offer Number: {proposal_doc['offer_number']}")
    print(f"Validity Period: {proposal_doc['validity_period']}")
    
    print(f"\nCustomer: {proposal_doc['customer_info']['name']}")
    print(f"Address: {proposal_doc['customer_info']['address']}, {proposal_doc['customer_info']['city']}")
    print(f"Contact: {proposal_doc['customer_info']['contact_person']}")
    
    print(f"\nServices Offered:")
    for i, service in enumerate(proposal_doc['services_offered'], 1):
        print(f"  {i}. {service['name']}")
        print(f"     Description: {service['description']}")
        print(f"     Quantity: {service['quantity']} {service['unit']}")
        print(f"     Unit Price (excl. VAT): €{service['unit_price_excl_vat']:.2f}")
        print(f"     VAT: {service['vat_percentage']}%")
        print(f"     Total (excl. VAT): €{service['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{service['total_incl_vat']:.2f}")
    
    print(f"\nFinancial Summary:")
    totals = proposal_doc['totals']
    print(f"  Total (excl. VAT): €{totals['total_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total (incl. VAT): €{totals['total_incl_vat']:.2f}")
    print(f"  Discounts Applied: €{totals['discounts_applied']:.2f}")
    print(f"  Final Total: €{totals['final_total']:.2f}")
    
    print(f"\nDelivery Info:")
    print(f"  Timeframe: {proposal_doc['delivery_timeframe']}")
    print(f"  Address: {proposal_doc['delivery_address']}")
    
    print(f"\nPayment Terms:")
    print(f"  Method: {proposal_doc['payment_terms']['payment_method']}")
    print(f"  Period: {proposal_doc['payment_terms']['payment_period']}")
    print(f"  Late Fee: {proposal_doc['payment_terms']['late_fee']}")
    
    print(f"\nTerms & Conditions:")
    print(f"  Validity: {proposal_doc['terms_conditions']['validity']}")
    print(f"  Warranty: {proposal_doc['quality_guarantee']['warranty_period']} ({proposal_doc['quality_guarantee']['warranty_scope']})")
    
    # Generate an example invoice if the proposal is accepted
    print(f"\nGenerating example invoice if proposal is accepted...")
    invoice = sample_proposal.generate_invoice_if_accepted()
    print(f"Invoice Number: {invoice['invoice_number']}")
    print(f"Invoice Date: {invoice['invoice_date']}")
    print(f"Due Date: {invoice['due_date']}")
    print(f"Total Amount: €{invoice['total_amount']:.2f}")
    
    # Save the proposal to a JSON file
    sample_proposal.save_to_json("sample_business_proposal.json")
    print(f"\nBusiness proposal saved to 'sample_business_proposal.json'")