"""
Python implementation of L3_Tilaus order form template.

This module provides programmatic access to the order form functionality
originally implemented in the L3_Tilaus.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class OrderForm:
    """
    A class representing an order form based on the L3_Tilaus template.
    This tool helps businesses create standardized order forms for customers to place 
    orders for products or services, capturing all necessary details for processing 
    the order accurately and efficiently.
    """
    
    def __init__(self, company_name: str = "Order Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.order_date = datetime.now().strftime('%d.%m.%Y')
        self.order_number = ""
        self.customer_info = {}  # Customer information
        self.contact_person = ""
        self.contact_info = ""
        self.delivery_info = {}  # Delivery information
        self.payment_terms = {}  # Payment terms and conditions
        self.order_items = []  # List of ordered items
        self.total_amount = 0.0
        self.vat_amount = 0.0
        self.total_including_vat = 0.0
        self.order_reference = ""  # Customer's reference for the order
        self.delivery_address = ""
        self.delivery_date = ""
        self.terms_conditions = {}  # General terms and conditions
        self.inventory_availability = {}  # Inventory tracking
        self.pricing_info = {}  # Pricing information and discounts
        self.shipping_info = {}  # Shipping and logistics
        self.invoice_info = {}  # Invoicing information
        self.quality_assurance = {}  # Quality assurance information
        self.return_policy = {}  # Return policy information
        self.handling_fees = {}  # Handling fees
        self.status_tracking = {}  # Order status tracking
        self.customer_history = {}  # Customer order history
        self.special_notes = ""
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the order form with default values."""
        # Default customer information
        self.customer_info = {
            "name": "",
            "address": "",
            "city": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "business_id": ""
        }
        
        # Default delivery information
        self.delivery_info = {
            "delivery_date": "",
            "delivery_method": "Standard delivery",
            "delivery_address_same_as_billing": True
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Invoice",
            "payment_period": "30 days",
            "late_fee": "8% per annum"
        }
        
        # Default terms and conditions
        self.terms_conditions = {
            "validity_period": "30 days",
            "cancellation_policy": "Orders can be cancelled within 14 days of placement",
            "dispute_resolution": "Handled according to Finnish law"
        }
        
        # Default shipping information
        self.shipping_info = {
            "shipping_method": "Standard shipping",
            "shipping_cost": 0.0,
            "estimated_delivery_time": "5-7 business days",
            "tracking_available": True
        }
        
        # Default quality assurance
        self.quality_assurance = {
            "inspection_required": True,
            "quality_standards": "ISO 9001",
            "warranty_period": "12 months"
        }
        
        # Default return policy
        self.return_policy = {
            "return_period": "30 days",
            "condition_requirement": "Item must be in original condition",
            "refund_method": "Original payment method"
        }
        
        # Default order items list
        self.order_items = []
        
        # Default inventory availability
        self.inventory_availability = {}
        
        # Default pricing info
        self.pricing_info = {
            "discounts_applicable": False,
            "discount_percentage": 0.0,
            "special_pricing": False
        }
    
    def add_order_item(self, product_id: str, product_name: str, quantity: int, 
                      unit_price_excl_vat: float, vat_percentage: float = 24.0):
        """Add an item to the order."""
        item = {
            "product_id": product_id,
            "product_name": product_name,
            "quantity": quantity,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_percentage": vat_percentage,
            "total_excl_vat": quantity * unit_price_excl_vat,
            "total_vat": quantity * unit_price_excl_vat * (vat_percentage / 100),
            "total_incl_vat": quantity * unit_price_excl_vat * (1 + vat_percentage / 100)
        }
        
        self.order_items.append(item)
        return item
    
    def set_customer_info(self, name: str, address: str, city: str, contact_person: str = "", 
                         phone: str = "", email: str = "", business_id: str = ""):
        """Set customer information."""
        self.customer_info = {
            "name": name,
            "address": address,
            "city": city,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "business_id": business_id
        }
    
    def set_order_number(self, number: str):
        """Set the order number."""
        self.order_number = number
    
    def set_order_reference(self, reference: str):
        """Set the customer's reference for the order."""
        self.order_reference = reference
    
    def set_delivery_info(self, delivery_date: str, delivery_address: str, 
                         delivery_method: str = "Standard delivery"):
        """Set delivery information."""
        self.delivery_info = {
            "delivery_date": delivery_date,
            "delivery_address": delivery_address,
            "delivery_method": delivery_method
        }
    
    def set_payment_terms(self, method: str, period: str, late_fee: str = "8% per annum"):
        """Set payment terms."""
        self.payment_terms = {
            "payment_method": method,
            "payment_period": period,
            "late_fee": late_fee
        }
    
    def apply_discount(self, discount_percentage: float):
        """Apply a discount to the entire order."""
        self.pricing_info["discounts_applicable"] = True
        self.pricing_info["discount_percentage"] = discount_percentage
    
    def calculate_order_totals(self) -> Dict:
        """Calculate total amounts for the order."""
        total_excl_vat = sum(item["total_excl_vat"] for item in self.order_items)
        total_vat = sum(item["total_vat"] for item in self.order_items)
        total_incl_vat = sum(item["total_incl_vat"] for item in self.order_items)
        
        # Apply discounts if applicable
        discount_amount = 0
        if self.pricing_info["discounts_applicable"] and self.pricing_info["discount_percentage"] > 0:
            discount_amount = total_incl_vat * (self.pricing_info["discount_percentage"] / 100)
        
        # Add shipping costs
        shipping_cost = self.shipping_info["shipping_cost"]
        
        final_total = total_incl_vat - discount_amount + shipping_cost
        
        self.total_amount = total_excl_vat
        self.vat_amount = total_vat
        self.total_including_vat = final_total
        
        return {
            "total_excl_vat": total_excl_vat,
            "total_vat": total_vat,
            "total_incl_vat": total_incl_vat,
            "discount_amount": discount_amount,
            "shipping_cost": shipping_cost,
            "final_total": final_total
        }
    
    def check_inventory_availability(self) -> Dict[str, bool]:
        """Check if ordered items are available in inventory."""
        availability = {}
        for item in self.order_items:
            product_id = item["product_id"]
            quantity_needed = item["quantity"]
            
            # In a real implementation, this would check against actual inventory
            # For this example, we'll assume all items are available
            availability[product_id] = True  # Placeholder - assume available
            
        return availability
    
    def generate_order_confirmation(self) -> Dict:
        """Generate an order confirmation document."""
        totals = self.calculate_order_totals()
        inventory_check = self.check_inventory_availability()
        
        confirmation = {
            "company_name": self.company_name,
            "order_date": self.order_date,
            "order_number": self.order_number,
            "customer_info": self.customer_info,
            "contact_person": self.contact_person,
            "contact_info": self.contact_info,
            "order_reference": self.order_reference,
            "delivery_info": self.delivery_info,
            "payment_terms": self.payment_terms,
            "order_items": self.order_items,
            "inventory_availability": inventory_check,
            "totals": totals,
            "terms_conditions": self.terms_conditions,
            "shipping_info": self.shipping_info,
            "quality_assurance": self.quality_assurance,
            "return_policy": self.return_policy,
            "special_notes": self.special_notes,
            "status": "Confirmed",
            "estimated_delivery": self._calculate_estimated_delivery()
        }
        
        return confirmation
    
    def _calculate_estimated_delivery(self) -> str:
        """Calculate estimated delivery date based on order date and shipping time."""
        # This is a simplified implementation
        # In a real implementation, we would calculate based on shipping time and holidays
        from datetime import datetime, timedelta
        order_date_obj = datetime.strptime(self.order_date, '%d.%m.%Y')
        est_delivery = order_date_obj + timedelta(days=7)  # 7 days as example
        return est_delivery.strftime('%d.%m.%Y')
    
    def generate_order_report(self) -> Dict:
        """Generate a comprehensive order report."""
        confirmation = self.generate_order_confirmation()
        
        report = {
            "order_confirmation": confirmation,
            "analytics": {
                "total_items_ordered": len(self.order_items),
                "total_quantity_ordered": sum(item["quantity"] for item in self.order_items),
                "average_item_value": sum(item["total_incl_vat"] for item in self.order_items) / len(self.order_items) if self.order_items else 0,
                "vat_percentage_breakdown": self._calculate_vat_breakdown(),
                "discount_percentage_applied": self.pricing_info["discount_percentage"],
                "shipping_cost_percentage": (self.shipping_info["shipping_cost"] / confirmation["totals"]["total_incl_vat"]) * 100 if confirmation["totals"]["total_incl_vat"] != 0 else 0
            }
        }
        
        return report
    
    def _calculate_vat_breakdown(self) -> Dict:
        """Calculate VAT breakdown by percentage."""
        vat_breakdown = {}
        for item in self.order_items:
            vat_pct = item["vat_percentage"]
            if vat_pct not in vat_breakdown:
                vat_breakdown[vat_pct] = {"excl_vat": 0, "vat": 0, "incl_vat": 0}
            vat_breakdown[vat_pct]["excl_vat"] += item["total_excl_vat"]
            vat_breakdown[vat_pct]["vat"] += item["total_vat"]
            vat_breakdown[vat_pct]["incl_vat"] += item["total_incl_vat"]
        
        return vat_breakdown
    
    def save_to_json(self, filepath: str):
        """Save the order to a JSON file."""
        report = self.generate_order_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load an order from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        confirmation = data.get("order_confirmation", {})
        self.company_name = confirmation.get("company_name", self.company_name)
        self.order_date = confirmation.get("order_date", self.order_date)
        self.order_number = confirmation.get("order_number", self.order_number)
        self.customer_info = confirmation.get("customer_info", self.customer_info)
        self.order_items = confirmation.get("order_items", self.order_items)
        self.delivery_info = confirmation.get("delivery_info", self.delivery_info)
        self.payment_terms = confirmation.get("payment_terms", self.payment_terms)
        self.terms_conditions = confirmation.get("terms_conditions", self.terms_conditions)
        self.shipping_info = confirmation.get("shipping_info", self.shipping_info)


def create_sample_order() -> OrderForm:
    """Create a sample order with example data."""
    order = OrderForm(company_name="Sample Order Co", year=2026)
    
    # Set customer information
    order.set_customer_info(
        name="Kauppakeskus Oy",
        address="Kauppakatu 10",
        city="33100 TAMPERE",
        contact_person="Matti Meikäläinen",
        phone="0500 123 456",
        email="matti.meikalainen@kauppakeskus.fi",
        business_id="1234567-8"
    )
    
    # Set order details
    order.set_order_number("ORD-2026-001")
    order.set_order_reference("Customer reference XX0125")
    
    # Add example order items based on the spreadsheet structure
    order.add_order_item(
        product_id="prod_1",
        product_name="Esimerkki-ikkuna",
        quantity=100,
        unit_price_excl_vat=100.00,
        vat_percentage=25.5
    )
    
    order.add_order_item(
        product_id="prod_2",
        product_name="Additional service",
        quantity=5,
        unit_price_excl_vat=2000.00,
        vat_percentage=25.5
    )
    
    # Set delivery information
    order.set_delivery_info(
        delivery_date="2026-02-20",
        delivery_address="Toimitusosoite: Esimerkkikatu 15, 33200 Tampere",
        delivery_method="Express delivery"
    )
    
    # Set payment terms
    order.set_payment_terms(
        method="Bank transfer",
        period="14 days",
        late_fee="10% per annum"
    )
    
    # Apply a discount
    order.apply_discount(5.0)  # 5% discount
    
    # Set shipping information
    order.shipping_info["shipping_cost"] = 50.0
    order.shipping_info["shipping_method"] = "Express shipping"
    order.shipping_info["estimated_delivery_time"] = "2-3 business days"
    
    # Add special notes
    order.special_notes = "Handle with care - fragile items"
    
    return order


if __name__ == "__main__":
    # Example usage
    print("L3 Tilaus - Order Form Tool")
    print("=" * 35)
    
    # Create a sample order
    sample_order = create_sample_order()
    
    # Generate and display the order confirmation
    confirmation = sample_order.generate_order_confirmation()
    
    print(f"\nCompany: {confirmation['company_name']}")
    print(f"Order Date: {confirmation['order_date']}")
    print(f"Order Number: {confirmation['order_number']}")
    print(f"Customer Reference: {confirmation['order_reference']}")
    
    print(f"\nCustomer: {confirmation['customer_info']['name']}")
    print(f"Address: {confirmation['customer_info']['address']}, {confirmation['customer_info']['city']}")
    print(f"Contact: {confirmation['customer_info']['contact_person']}")
    
    print(f"\nDelivery:")
    print(f"  Date: {confirmation['delivery_info']['delivery_date']}")
    print(f"  Address: {confirmation['delivery_info']['delivery_address']}")
    print(f"  Method: {confirmation['delivery_info']['delivery_method']}")
    
    print(f"\nPayment Terms:")
    print(f"  Method: {confirmation['payment_terms']['payment_method']}")
    print(f"  Period: {confirmation['payment_terms']['payment_period']}")
    print(f"  Late Fee: {confirmation['payment_terms']['late_fee']}")
    
    print(f"\nOrder Items:")
    for i, item in enumerate(confirmation['order_items'], 1):
        print(f"  {i}. {item['product_name']}")
        print(f"     Quantity: {item['quantity']}")
        print(f"     Unit Price (excl. VAT): €{item['unit_price_excl_vat']:.2f}")
        print(f"     VAT: {item['vat_percentage']}%")
        print(f"     Total (excl. VAT): €{item['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{item['total_incl_vat']:.2f}")
    
    print(f"\nFinancial Summary:")
    totals = confirmation['totals']
    print(f"  Total (excl. VAT): €{totals['total_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total (incl. VAT): €{totals['total_incl_vat']:.2f}")
    print(f"  Discount Applied: €{totals['discount_amount']:.2f}")
    print(f"  Shipping Cost: €{totals['shipping_cost']:.2f}")
    print(f"  Final Total: €{totals['final_total']:.2f}")
    
    print(f"\nInventory Availability:")
    for item_id, available in confirmation['inventory_availability'].items():
        status = "Available" if available else "Out of Stock"
        print(f"  {item_id}: {status}")
    
    print(f"\nTerms & Conditions:")
    print(f"  Validity: {confirmation['terms_conditions']['validity_period']}")
    print(f"  Cancellation Policy: {confirmation['terms_conditions']['cancellation_policy']}")
    
    print(f"\nQuality Assurance:")
    print(f"  Warranty Period: {confirmation['quality_assurance']['warranty_period']}")
    print(f"  Quality Standards: {confirmation['quality_assurance']['quality_standards']}")
    
    print(f"\nReturn Policy:")
    print(f"  Return Period: {confirmation['return_policy']['return_period']}")
    print(f"  Condition Requirement: {confirmation['return_policy']['condition_requirement']}")
    
    print(f"\nSpecial Notes: {confirmation['special_notes']}")
    print(f"Status: {confirmation['status']}")
    print(f"Estimated Delivery: {confirmation['estimated_delivery']}")
    
    # Generate and display the order report
    print(f"\nGenerating order report...")
    report = sample_order.generate_order_report()
    
    analytics = report['analytics']
    print(f"\nOrder Analytics:")
    print(f"  Total Items Ordered: {analytics['total_items_ordered']}")
    print(f"  Total Quantity Ordered: {analytics['total_quantity_ordered']}")
    print(f"  Average Item Value: €{analytics['average_item_value']:.2f}")
    print(f"  Discount Applied: {analytics['discount_percentage_applied']:.1f}%")
    print(f"  Shipping Cost % of Order: {analytics['shipping_cost_percentage']:.1f}%")
    
    print(f"\nVAT Breakdown:")
    for vat_rate, breakdown in analytics['vat_percentage_breakdown'].items():
        print(f"  {vat_rate}% VAT: €{breakdown['excl_vat']:.2f} excl. VAT, €{breakdown['vat']:.2f} VAT, €{breakdown['incl_vat']:.2f} incl. VAT")
    
    # Save the order to a JSON file
    sample_order.save_to_json("sample_order_form.json")
    print(f"\nOrder form saved to 'sample_order_form.json'")