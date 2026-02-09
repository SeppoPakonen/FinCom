"""
Python implementation of L4_Tilausvahvistus order confirmation template.

This module provides programmatic access to the order confirmation functionality
originally implemented in the L4_Tilausvahvistus.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class OrderConfirmation:
    """
    A class representing an order confirmation based on the L4_Tilausvahvistus template.
    This tool helps businesses create standardized confirmations for customer orders,
    acknowledging receipt of orders and providing details about expected delivery,
    payment terms, and other important information related to the order fulfillment process.
    """
    
    def __init__(self, company_name: str = "Order Confirmation Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.confirmation_date = datetime.now().strftime('%d.%m.%Y')
        self.confirmation_number = ""
        self.supplier_info = {}  # Supplier information
        self.customer_info = {}  # Customer information
        self.order_details = {}  # Original order details
        self.confirmed_items = []  # Confirmed items with availability status
        self.delivery_info = {}  # Delivery information
        self.payment_terms = {}  # Payment terms
        self.terms_conditions = {}  # General terms and conditions
        self.tracking_info = {}  # Tracking information
        self.processing_times = {}  # Processing time information
        self.special_requests = []  # Special requests from customer
        self.quality_assurance = {}  # Quality assurance information
        self.return_policy = {}  # Return policy information
        self.invoice_info = {}  # Invoicing information
        self.status_updates = []  # Status updates during fulfillment
        self.customer_communication_log = []  # Communication log
        self.risk_management = {}  # Risk management for order fulfillment
        self.performance_metrics = {}  # KPIs for order fulfillment
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the order confirmation with default values."""
        # Default supplier information
        self.supplier_info = {
            "name": self.company_name,
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default customer information
        self.customer_info = {
            "name": "",
            "address": "",
            "city": "",
            "customer_id": "",
            "reference": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default order details
        self.order_details = {
            "original_order_number": "",
            "original_order_date": "",
            "order_total_excl_vat": 0.0,
            "order_total_incl_vat": 0.0,
            "vat_amount": 0.0
        }
        
        # Default delivery information
        self.delivery_info = {
            "expected_delivery_date": "",
            "delivery_method": "Standard delivery",
            "delivery_address": "",
            "shipping_cost": 0.0,
            "tracking_available": True
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Invoice",
            "payment_period": "30 days",
            "late_fee": "8% per annum",
            "partial_payments_allowed": False
        }
        
        # Default terms and conditions
        self.terms_conditions = {
            "validity_period": "The order confirmation is valid for 30 days",
            "cancellation_policy": "Orders can be cancelled within 14 days of confirmation",
            "force_majeure": "Standard force majeure clauses apply",
            "dispute_resolution": "Handled according to Finnish law"
        }
        
        # Default tracking information
        self.tracking_info = {
            "tracking_number": "",
            "tracking_url": "",
            "estimated_delivery": ""
        }
        
        # Default processing times
        self.processing_times = {
            "order_processing_time": "1-2 business days",
            "fulfillment_time": "3-5 business days",
            "total_delivery_time": "5-7 business days"
        }
        
        # Default quality assurance
        self.quality_assurance = {
            "inspection_process": "All items inspected before shipping",
            "quality_standards": "ISO 9001",
            "warranty_period": "12 months",
            "defect_rate_target": "Less than 1%"
        }
        
        # Default return policy
        self.return_policy = {
            "return_period": "30 days",
            "condition_requirement": "Item must be in original condition",
            "return_shipping_cost": "Customer responsibility unless item is defective",
            "refund_method": "Original payment method"
        }
        
        # Default invoice information
        self.invoice_info = {
            "invoice_separate_from_shipment": True,
            "billing_address_same_as_delivery": True,
            "invoice_date": "",
            "due_date": ""
        }
        
        # Default performance metrics
        self.performance_metrics = {
            "confirmation_accuracy": 0.0,
            "delivery_on_time_rate": 0.0,
            "customer_satisfaction": 0.0,
            "order_processing_efficiency": 0.0
        }
        
        # Default risk management
        self.risk_management = {
            "inventory_shortage_risk": "Low",
            "delivery_delay_risk": "Low",
            "payment_default_risk": "Low",
            "mitigation_strategies": []
        }
    
    def set_supplier_info(self, name: str, address: str, business_id: str = "", 
                         contact_person: str = "", phone: str = "", email: str = ""):
        """Set supplier information."""
        self.supplier_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_customer_info(self, name: str, address: str, city: str, customer_id: str = "", 
                         reference: str = "", contact_person: str = "", 
                         phone: str = "", email: str = ""):
        """Set customer information."""
        self.customer_info = {
            "name": name,
            "address": address,
            "city": city,
            "customer_id": customer_id,
            "reference": reference,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_order_details(self, order_number: str, order_date: str, total_excl_vat: float, 
                         total_incl_vat: float, vat_amount: float):
        """Set original order details."""
        self.order_details = {
            "original_order_number": order_number,
            "original_order_date": order_date,
            "order_total_excl_vat": total_excl_vat,
            "order_total_incl_vat": total_incl_vat,
            "vat_amount": vat_amount
        }
    
    def add_confirmed_item(self, product_id: str, product_name: str, ordered_qty: int, 
                          confirmed_qty: int, unit_price_excl_vat: float, 
                          vat_percentage: float = 24.0, availability_status: str = "Confirmed"):
        """Add a confirmed item to the order confirmation."""
        item = {
            "product_id": product_id,
            "product_name": product_name,
            "ordered_quantity": ordered_qty,
            "confirmed_quantity": confirmed_qty,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_percentage": vat_percentage,
            "total_excl_vat": confirmed_qty * unit_price_excl_vat,
            "total_vat": confirmed_qty * unit_price_excl_vat * (vat_percentage / 100),
            "total_incl_vat": confirmed_qty * unit_price_excl_vat * (1 + vat_percentage / 100),
            "availability_status": availability_status,
            "delivery_date": self._calculate_item_delivery_date()
        }
        
        self.confirmed_items.append(item)
        return item
    
    def _calculate_item_delivery_date(self) -> str:
        """Calculate expected delivery date for an item."""
        # Simple calculation: add 7 days to confirmation date
        confirmation_date = datetime.strptime(self.confirmation_date, '%d.%m.%Y')
        delivery_date = confirmation_date + timedelta(days=7)
        return delivery_date.strftime('%d.%m.%Y')
    
    def set_delivery_info(self, expected_delivery_date: str, delivery_method: str = "Standard delivery", 
                         delivery_address: str = "", shipping_cost: float = 0.0):
        """Set delivery information."""
        self.delivery_info = {
            "expected_delivery_date": expected_delivery_date,
            "delivery_method": delivery_method,
            "delivery_address": delivery_address,
            "shipping_cost": shipping_cost
        }
    
    def set_payment_terms(self, method: str, period: str, late_fee: str = "8% per annum", 
                         partial_payments_allowed: bool = False):
        """Set payment terms."""
        self.payment_terms = {
            "payment_method": method,
            "payment_period": period,
            "late_fee": late_fee,
            "partial_payments_allowed": partial_payments_allowed
        }
    
    def add_special_request(self, request: str):
        """Add a special request from the customer."""
        self.special_requests.append(request)
    
    def add_status_update(self, status: str, date: str = "", notes: str = ""):
        """Add a status update for the order."""
        update = {
            "date": date or datetime.now().strftime('%d.%m.%Y'),
            "status": status,
            "notes": notes
        }
        self.status_updates.append(update)
    
    def calculate_confirmation_totals(self) -> Dict:
        """Calculate totals for the confirmed order."""
        total_excl_vat = sum(item["total_excl_vat"] for item in self.confirmed_items)
        total_vat = sum(item["total_vat"] for item in self.confirmed_items)
        total_incl_vat = sum(item["total_incl_vat"] for item in self.confirmed_items)
        
        # Calculate shipping cost
        shipping_cost = self.delivery_info["shipping_cost"]
        
        # Calculate final total
        final_total = total_incl_vat + shipping_cost
        
        return {
            "subtotal_excl_vat": total_excl_vat,
            "total_vat": total_vat,
            "subtotal_incl_vat": total_incl_vat,
            "shipping_cost": shipping_cost,
            "final_total": final_total
        }
    
    def check_inventory_availability(self) -> Dict[str, str]:
        """Check inventory availability for all confirmed items."""
        availability = {}
        for item in self.confirmed_items:
            if item["ordered_quantity"] <= item["confirmed_quantity"]:
                availability[item["product_id"]] = "Fully available"
            elif item["confirmed_quantity"] > 0:
                availability[item["product_id"]] = f"Partial availability ({item['confirmed_quantity']}/{item['ordered_quantity']})"
            else:
                availability[item["product_id"]] = "Out of stock"
        return availability
    
    def generate_confirmation_document(self) -> Dict:
        """Generate a complete order confirmation document."""
        totals = self.calculate_confirmation_totals()
        inventory_status = self.check_inventory_availability()
        
        confirmation_doc = {
            "company_name": self.company_name,
            "confirmation_date": self.confirmation_date,
            "confirmation_number": self.confirmation_number,
            "supplier_info": self.supplier_info,
            "customer_info": self.customer_info,
            "original_order_details": self.order_details,
            "confirmed_items": self.confirmed_items,
            "inventory_availability": inventory_status,
            "delivery_info": self.delivery_info,
            "payment_terms": self.payment_terms,
            "terms_conditions": self.terms_conditions,
            "tracking_info": self.tracking_info,
            "processing_times": self.processing_times,
            "special_requests": self.special_requests,
            "quality_assurance": self.quality_assurance,
            "return_policy": self.return_policy,
            "invoice_info": self.invoice_info,
            "status_updates": self.status_updates,
            "customer_communication_log": self.customer_communication_log,
            "risk_management": self.risk_management,
            "totals": totals
        }
        
        return confirmation_doc
    
    def generate_confirmation_report(self) -> Dict:
        """Generate a comprehensive order confirmation report."""
        confirmation_doc = self.generate_confirmation_document()
        
        report = {
            "confirmation_document": confirmation_doc,
            "analytics": {
                "total_items_confirmed": len(self.confirmed_items),
                "total_quantity_confirmed": sum(item["confirmed_quantity"] for item in self.confirmed_items),
                "fill_rate": self._calculate_fill_rate(),
                "average_item_value": sum(item["total_incl_vat"] for item in self.confirmed_items) / len(self.confirmed_items) if self.confirmed_items else 0,
                "confirmed_value": sum(item["total_incl_vat"] for item in self.confirmed_items),
                "out_of_stock_items": self._count_out_of_stock_items(),
                "special_requests_count": len(self.special_requests)
            }
        }
        
        return report
    
    def _calculate_fill_rate(self) -> float:
        """Calculate the order fill rate (confirmed quantity / ordered quantity)."""
        total_ordered = sum(item["ordered_quantity"] for item in self.confirmed_items)
        total_confirmed = sum(item["confirmed_quantity"] for item in self.confirmed_items)
        if total_ordered == 0:
            return 0.0
        return total_confirmed / total_ordered
    
    def _count_out_of_stock_items(self) -> int:
        """Count the number of out-of-stock items."""
        count = 0
        for item in self.confirmed_items:
            if item["confirmed_quantity"] == 0:
                count += 1
        return count
    
    def save_to_json(self, filepath: str):
        """Save the order confirmation to a JSON file."""
        report = self.generate_confirmation_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load an order confirmation from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        confirmation_doc = data.get("confirmation_document", {})
        self.company_name = confirmation_doc.get("company_name", self.company_name)
        self.confirmation_date = confirmation_doc.get("confirmation_date", self.confirmation_date)
        self.confirmation_number = confirmation_doc.get("confirmation_number", self.confirmation_number)
        self.supplier_info = confirmation_doc.get("supplier_info", self.supplier_info)
        self.customer_info = confirmation_doc.get("customer_info", self.customer_info)
        self.confirmed_items = confirmation_doc.get("confirmed_items", self.confirmed_items)
        self.delivery_info = confirmation_doc.get("delivery_info", self.delivery_info)
        self.payment_terms = confirmation_doc.get("payment_terms", self.payment_terms)
        self.totals = confirmation_doc.get("totals", self.totals)


def create_sample_confirmation() -> OrderConfirmation:
    """Create a sample order confirmation with example data."""
    confirmation = OrderConfirmation(company_name="Sample Confirmation Oy", year=2026)
    
    # Set supplier information
    confirmation.set_supplier_info(
        name="Sample Confirmation Oy",
        address="Toimittajankatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Toimittaja: Tiina Toimittaja",
        phone="0500 123 456",
        email="tiina.toimittaja@sampleconfirmation.fi"
    )
    
    # Set customer information
    confirmation.set_customer_info(
        name="Asiakas Oy",
        address="Asiakaskatu 20",
        city="00100 Helsinki",
        customer_id="CUST-001",
        reference="Customer reference XX0125",
        contact_person="Asiakas: Aino Asiakas",
        phone="0400 987 654",
        email="aino.asiakas@asiakas.fi"
    )
    
    # Set original order details
    confirmation.set_order_details(
        order_number="ORD-2026-001",
        order_date="01.02.2026",
        total_excl_vat=1000.00,
        total_incl_vat=1255.00,
        vat_amount=255.00
    )
    
    # Add confirmed items
    confirmation.add_confirmed_item(
        product_id="prod_1",
        product_name="Tuote 1: Esimerkki-ikkuna",
        ordered_qty=10,
        confirmed_qty=10,  # Fully available
        unit_price_excl_vat=100.00,
        vat_percentage=25.5,
        availability_status="Confirmed"
    )
    
    confirmation.add_confirmed_item(
        product_id="prod_2",
        product_name="Tuote 2: Esimerkki-ovi",
        ordered_qty=5,
        confirmed_qty=3,  # Partial availability
        unit_price_excl_vat=200.00,
        vat_percentage=25.5,
        availability_status="Partial availability"
    )
    
    confirmation.add_confirmed_item(
        product_id="prod_3",
        product_name="Tuote 3: Esimerkki-valaistus",
        ordered_qty=2,
        confirmed_qty=0,  # Out of stock
        unit_price_excl_vat=150.00,
        vat_percentage=25.5,
        availability_status="Out of stock"
    )
    
    # Set delivery information
    confirmation.set_delivery_info(
        expected_delivery_date="10.02.2026",
        delivery_method="Express delivery",
        delivery_address="Asiakaskatu 20, 00100 Helsinki",
        shipping_cost=50.00
    )
    
    # Set payment terms
    confirmation.set_payment_terms(
        method="Bank transfer",
        period="14 days",
        late_fee="10% per annum"
    )
    
    # Add special requests
    confirmation.add_special_request("Handle with care - fragile items")
    confirmation.add_special_request("Delivery only during business hours")
    
    # Add status updates
    confirmation.add_status_update("Order confirmed", "03.02.2026", "Initial confirmation sent to customer")
    confirmation.add_status_update("Processing", "04.02.2026", "Items being prepared for shipment")
    
    # Set tracking information
    confirmation.tracking_info["tracking_number"] = "TK-2026-00123"
    confirmation.tracking_info["tracking_url"] = "https://tracking.samplecompany.fi/TK-2026-00123"
    
    # Set invoice information
    confirmation.invoice_info["billing_address_same_as_delivery"] = False
    confirmation.invoice_info["invoice_separate_from_shipment"] = True
    
    return confirmation


if __name__ == "__main__":
    # Example usage
    print("L4 Tilausvahvistus - Order Confirmation Tool")
    print("=" * 50)
    
    # Create a sample order confirmation
    sample_confirmation = create_sample_confirmation()
    
    # Generate and display the confirmation document
    confirmation_doc = sample_confirmation.generate_confirmation_document()
    
    print(f"\nCompany: {confirmation_doc['company_name']}")
    print(f"Confirmation Date: {confirmation_doc['confirmation_date']}")
    print(f"Confirmation Number: {confirmation_doc['confirmation_number']}")
    print(f"Supplier: {confirmation_doc['supplier_info']['name']}")
    print(f"Customer: {confirmation_doc['customer_info']['name']}")
    
    print(f"\nOriginal Order Details:")
    orig_order = confirmation_doc['original_order_details']
    print(f"  Order Number: {orig_order['original_order_number']}")
    print(f"  Order Date: {orig_order['original_order_date']}")
    print(f"  Total (excl. VAT): €{orig_order['order_total_excl_vat']:,.2f}")
    print(f"  Total (incl. VAT): €{orig_order['order_total_incl_vat']:,.2f}")
    
    print(f"\nConfirmed Items:")
    for item in confirmation_doc['confirmed_items']:
        status_icon = "✓" if item['availability_status'] == 'Confirmed' else \
                     "⚠" if item['availability_status'] == 'Partial availability' else \
                     "✗"
        print(f"  {status_icon} {item['product_name']}")
        print(f"     Ordered: {item['ordered_quantity']}, Confirmed: {item['confirmed_quantity']}")
        print(f"     Unit Price (excl. VAT): €{item['unit_price_excl_vat']:,.2f}")
        print(f"     Total (excl. VAT): €{item['total_excl_vat']:,.2f}")
        print(f"     Total (incl. VAT): €{item['total_incl_vat']:,.2f}")
        print(f"     Expected Delivery: {item['delivery_date']}")
    
    print(f"\nInventory Availability:")
    for item_id, status in confirmation_doc['inventory_availability'].items():
        print(f"  {item_id}: {status}")
    
    print(f"\nDelivery Information:")
    delivery = confirmation_doc['delivery_info']
    print(f"  Expected Delivery: {delivery['expected_delivery_date']}")
    print(f"  Method: {delivery['delivery_method']}")
    print(f"  Address: {delivery['delivery_address']}")
    print(f"  Shipping Cost: €{delivery['shipping_cost']:,.2f}")
    
    print(f"\nPayment Terms:")
    payment = confirmation_doc['payment_terms']
    print(f"  Method: {payment['payment_method']}")
    print(f"  Period: {payment['payment_period']}")
    print(f"  Late Fee: {payment['late_fee']}")
    
    print(f"\nFinancial Summary:")
    totals = confirmation_doc['totals']
    print(f"  Subtotal (excl. VAT): €{totals['subtotal_excl_vat']:,.2f}")
    print(f"  Total VAT: €{totals['total_vat']:,.2f}")
    print(f"  Subtotal (incl. VAT): €{totals['subtotal_incl_vat']:,.2f}")
    print(f"  Shipping Cost: €{totals['shipping_cost']:,.2f}")
    print(f"  Final Total: €{totals['final_total']:,.2f}")
    
    print(f"\nSpecial Requests:")
    for req in confirmation_doc['special_requests']:
        print(f"  - {req}")
    
    print(f"\nStatus Updates:")
    for update in confirmation_doc['status_updates']:
        print(f"  {update['date']}: {update['status']} - {update['notes']}")
    
    print(f"\nTracking Information:")
    tracking = confirmation_doc['tracking_info']
    print(f"  Tracking Number: {tracking['tracking_number']}")
    print(f"  Tracking URL: {tracking['tracking_url']}")
    
    print(f"\nTerms & Conditions:")
    tc = confirmation_doc['terms_conditions']
    print(f"  Validity: {tc['validity_period']}")
    print(f"  Cancellation Policy: {tc['cancellation_policy']}")
    
    print(f"\nQuality Assurance:")
    qa = confirmation_doc['quality_assurance']
    print(f"  Inspection Process: {qa['inspection_process']}")
    print(f"  Warranty Period: {qa['warranty_period']}")
    
    print(f"\nReturn Policy:")
    rp = confirmation_doc['return_policy']
    print(f"  Return Period: {rp['return_period']}")
    print(f"  Condition Requirement: {rp['condition_requirement']}")
    
    # Generate and display the confirmation report
    print(f"\nGenerating confirmation report...")
    report = sample_confirmation.generate_confirmation_report()
    
    analytics = report['analytics']
    print(f"\nConfirmation Analytics:")
    print(f"  Total Items Confirmed: {analytics['total_items_confirmed']}")
    print(f"  Total Quantity Confirmed: {analytics['total_quantity_confirmed']}")
    print(f"  Fill Rate: {analytics['fill_rate']:.1%}")
    print(f"  Average Item Value: €{analytics['average_item_value']:,.2f}")
    print(f"  Confirmed Value: €{analytics['confirmed_value']:,.2f}")
    print(f"  Out-of-Stock Items: {analytics['out_of_stock_items']}")
    print(f"  Special Requests Count: {analytics['special_requests_count']}")
    
    # Save the confirmation to a JSON file
    sample_confirmation.save_to_json("sample_order_confirmation.json")
    print(f"\nOrder confirmation saved to 'sample_order_confirmation.json'")