"""
Python implementation of L6_Vuokralasku rental invoice template.

This module provides programmatic access to the rental invoice functionality
originally implemented in the L6_Vuokralasku.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class RentalInvoice:
    """
    A class representing a rental invoice based on the L6_Vuokralasku template.
    This tool helps businesses that provide rental services create standardized 
    invoices for customers, detailing rental periods, rates, additional charges, 
    and other rental-specific billing components.
    """
    
    def __init__(self, company_name: str = "Rental Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.invoice_date = datetime.now().strftime('%Y-%m-%d')
        self.invoice_number = ""
        self.sender_info = {}  # Sender information
        self.receiver_info = {}  # Receiver information
        self.rental_property_info = {}  # Rental property details
        self.rental_period = {}  # Rental period details
        self.rental_charges = {}  # Rental charges by type
        self.utility_costs = {}  # Utility costs (water, electricity, etc.)
        self.additional_services = {}  # Additional services and their charges
        self.deposits_guarantees = {}  # Deposits and guarantees
        self.payment_terms = {}  # Payment terms and conditions
        self.vat_calculations = {}  # VAT calculations
        self.total_amounts = {}  # Total amounts (excl. and incl. VAT)
        self.due_date = ""
        self.reference_number = ""
        self.late_payment_interest = 0.095  # Default 9.5% late payment interest
        self.rental_agreement_info = {}  # Rental agreement details
        self.meter_readings = {}  # Meter readings for utilities
        self.property_condition = {}  # Property condition at start/end of rental
        self.cleaning_maintenance_costs = {}  # Cleaning and maintenance costs
        self.damage_extra_charges = {}  # Damage and extra charges
        self.discount_info = {}  # Discount information
        self.seasonal_adjustments = {}  # Seasonal rate adjustments
        self.performance_metrics = {}  # KPIs and performance metrics
        self.special_notes = ""
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the rental invoice with default values."""
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
        
        # Default rental property information
        self.rental_property_info = {
            "property_id": "",
            "property_address": "",
            "property_type": "",  # apartment, equipment, vehicle, etc.
            "size_area": 0.0,
            "features": []
        }
        
        # Default rental period
        self.rental_period = {
            "start_date": "",
            "end_date": "",
            "duration_days": 0,
            "duration_months": 0
        }
        
        # Default rental charges
        self.rental_charges = {
            "base_rent": 0.0,
            "rent_per_day": 0.0,
            "rent_per_month": 0.0,
            "pro_rated_rent": 0.0
        }
        
        # Default utility costs
        self.utility_costs = {
            "water": 0.0,
            "electricity": 0.0,
            "heating": 0.0,
            "internet": 0.0,
            "other_utilities": 0.0
        }
        
        # Default additional services
        self.additional_services = {
            "cleaning": 0.0,
            "maintenance": 0.0,
            "parking": 0.0,
            "storage": 0.0,
            "other_services": 0.0
        }
        
        # Default deposits and guarantees
        self.deposits_guarantees = {
            "security_deposit": 0.0,
            "deposit_return_status": "Pending",
            "deposit_return_date": ""
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Bank transfer",
            "payment_period_days": 14,
            "due_date": "",
            "late_fee_rate": 0.095  # 9.5% per annum
        }
        
        # Default VAT calculations
        self.vat_calculations = {
            "vat_0_percent": 0.0,
            "vat_10_percent": 0.0,
            "vat_14_percent": 0.0,
            "vat_24_percent": 0.0  # Standard Finnish VAT rate
        }
        
        # Default total amounts
        self.total_amounts = {
            "subtotal_excl_vat": 0.0,
            "total_vat": 0.0,
            "total_incl_vat": 0.0
        }
        
        # Default rental agreement information
        self.rental_agreement_info = {
            "agreement_number": "",
            "agreement_date": "",
            "rental_terms": "",
            "cancellation_policy": ""
        }
        
        # Default meter readings
        self.meter_readings = {
            "water_start": 0,
            "water_end": 0,
            "electricity_start": 0,
            "electricity_end": 0,
            "heating_start": 0,
            "heating_end": 0
        }
        
        # Default property condition
        self.property_condition = {
            "condition_at_start": "Good",
            "condition_at_end": "Unknown",
            "damage_notes": ""
        }
        
        # Default cleaning and maintenance costs
        self.cleaning_maintenance_costs = {
            "cleaning_cost": 0.0,
            "maintenance_cost": 0.0,
            "extra_cleaning_required": False
        }
        
        # Default damage and extra charges
        self.damage_extra_charges = {
            "damage_cost": 0.0,
            "extra_usage_charges": 0.0,
            "other_extra_charges": 0.0
        }
        
        # Default discount information
        self.discount_info = {
            "discount_percentage": 0.0,
            "discount_reason": ""
        }
        
        # Default seasonal adjustments
        self.seasonal_adjustments = {
            "seasonal_rate_multiplier": 1.0,
            "seasonal_period": ""
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
    
    def set_rental_property_info(self, property_id: str, property_address: str, 
                                property_type: str, size_area: float = 0.0, features: List[str] = None):
        """Set rental property information."""
        self.rental_property_info = {
            "property_id": property_id,
            "property_address": property_address,
            "property_type": property_type,
            "size_area": size_area,
            "features": features or []
        }
    
    def set_rental_period(self, start_date: str, end_date: str):
        """Set rental period and calculate duration."""
        from datetime import datetime
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')
        duration = (end_dt - start_dt).days
        
        self.rental_period = {
            "start_date": start_date,
            "end_date": end_date,
            "duration_days": duration,
            "duration_months": round(duration / 30.44, 2)  # Approximate months
        }
    
    def set_rental_charges(self, base_rent: float, rent_per_day: float = 0, 
                          rent_per_month: float = 0, pro_rated_rent: float = 0):
        """Set rental charges."""
        self.rental_charges = {
            "base_rent": base_rent,
            "rent_per_day": rent_per_day,
            "rent_per_month": rent_per_month,
            "pro_rated_rent": pro_rated_rent
        }
    
    def set_utility_costs(self, water: float = 0, electricity: float = 0, 
                         heating: float = 0, internet: float = 0, other_utilities: float = 0):
        """Set utility costs."""
        self.utility_costs = {
            "water": water,
            "electricity": electricity,
            "heating": heating,
            "internet": internet,
            "other_utilities": other_utilities
        }
    
    def set_additional_services(self, cleaning: float = 0, maintenance: float = 0, 
                               parking: float = 0, storage: float = 0, other_services: float = 0):
        """Set additional service charges."""
        self.additional_services = {
            "cleaning": cleaning,
            "maintenance": maintenance,
            "parking": parking,
            "storage": storage,
            "other_services": other_services
        }
    
    def set_deposits_guarantees(self, security_deposit: float, 
                               deposit_return_status: str = "Pending", deposit_return_date: str = ""):
        """Set deposit and guarantee information."""
        self.deposits_guarantees = {
            "security_deposit": security_deposit,
            "deposit_return_status": deposit_return_status,
            "deposit_return_date": deposit_return_date
        }
    
    def set_meter_readings(self, water_start: float, water_end: float, 
                          electricity_start: float, electricity_end: float,
                          heating_start: float, heating_end: float):
        """Set meter readings for utilities."""
        self.meter_readings = {
            "water_start": water_start,
            "water_end": water_end,
            "electricity_start": electricity_start,
            "electricity_end": electricity_end,
            "heating_start": heating_start,
            "heating_end": heating_end
        }
    
    def set_property_condition(self, condition_at_start: str, condition_at_end: str = "Unknown", 
                              damage_notes: str = ""):
        """Set property condition information."""
        self.property_condition = {
            "condition_at_start": condition_at_start,
            "condition_at_end": condition_at_end,
            "damage_notes": damage_notes
        }
    
    def set_cleaning_maintenance_costs(self, cleaning_cost: float, maintenance_cost: float, 
                                      extra_cleaning_required: bool = False):
        """Set cleaning and maintenance costs."""
        self.cleaning_maintenance_costs = {
            "cleaning_cost": cleaning_cost,
            "maintenance_cost": maintenance_cost,
            "extra_cleaning_required": extra_cleaning_required
        }
    
    def set_damage_extra_charges(self, damage_cost: float, extra_usage_charges: float = 0, 
                                other_extra_charges: float = 0):
        """Set damage and extra charges."""
        self.damage_extra_charges = {
            "damage_cost": damage_cost,
            "extra_usage_charges": extra_usage_charges,
            "other_extra_charges": other_extra_charges
        }
    
    def apply_discount(self, discount_percentage: float, reason: str = ""):
        """Apply a discount to the rental invoice."""
        self.discount_info = {
            "discount_percentage": discount_percentage,
            "discount_reason": reason
        }
    
    def apply_seasonal_adjustment(self, multiplier: float, period: str = ""):
        """Apply seasonal adjustment to rental charges."""
        self.seasonal_adjustments = {
            "seasonal_rate_multiplier": multiplier,
            "seasonal_period": period
        }
    
    def calculate_rental_totals(self) -> Dict:
        """Calculate total amounts for the rental invoice."""
        # Calculate base rental charges
        base_rent = self.rental_charges["base_rent"]
        if self.rental_charges["pro_rated_rent"] > 0:
            base_rent = self.rental_charges["pro_rated_rent"]
        
        # Apply seasonal adjustment if applicable
        if self.seasonal_adjustments["seasonal_rate_multiplier"] != 1.0:
            base_rent *= self.seasonal_adjustments["seasonal_rate_multiplier"]
        
        # Calculate subtotal
        subtotal_excl_vat = (
            base_rent +
            sum(self.utility_costs.values()) +
            sum(self.additional_services.values()) +
            self.cleaning_maintenance_costs["cleaning_cost"] +
            self.cleaning_maintenance_costs["maintenance_cost"] +
            self.damage_extra_charges["damage_cost"] +
            self.damage_extra_charges["extra_usage_charges"] +
            self.damage_extra_charges["other_extra_charges"]
        )
        
        # Apply discount if applicable
        discount_amount = 0
        if self.discount_info["discount_percentage"] > 0:
            discount_amount = subtotal_excl_vat * (self.discount_info["discount_percentage"] / 100)
        
        # Calculate total before VAT
        total_before_vat = subtotal_excl_vat - discount_amount
        
        # Calculate VAT (simplified - assuming all items are subject to same VAT rate)
        vat_amount = total_before_vat * 0.24  # Standard 24% VAT rate
        
        # Calculate final total
        final_total = total_before_vat + vat_amount
        
        self.total_amounts = {
            "subtotal_excl_vat": subtotal_excl_vat,
            "discount_amount": discount_amount,
            "total_after_discount_excl_vat": total_before_vat,
            "total_vat": vat_amount,
            "total_incl_vat": final_total
        }
        
        return self.total_amounts
    
    def generate_rental_invoice_document(self) -> Dict:
        """Generate a complete rental invoice document."""
        totals = self.calculate_rental_totals()
        
        invoice_doc = {
            "company_name": self.company_name,
            "invoice_date": self.invoice_date,
            "invoice_number": self.invoice_number,
            "sender_info": self.sender_info,
            "receiver_info": self.receiver_info,
            "rental_property_info": self.rental_property_info,
            "rental_period": self.rental_period,
            "rental_charges": self.rental_charges,
            "utility_costs": self.utility_costs,
            "additional_services": self.additional_services,
            "deposits_guarantees": self.deposits_guarantees,
            "payment_terms": self.payment_terms,
            "meter_readings": self.meter_readings,
            "property_condition": self.property_condition,
            "cleaning_maintenance_costs": self.cleaning_maintenance_costs,
            "damage_extra_charges": self.damage_extra_charges,
            "discount_info": self.discount_info,
            "seasonal_adjustments": self.seasonal_adjustments,
            "totals": totals,
            "late_payment_interest": self.late_payment_interest,
            "rental_agreement_info": self.rental_agreement_info,
            "special_notes": self.special_notes
        }
        
        return invoice_doc
    
    def generate_rental_report(self) -> Dict:
        """Generate a comprehensive rental report with additional analytics."""
        invoice_doc = self.generate_rental_invoice_document()
        
        # Calculate additional analytics
        analytics = {
            "total_rental_days": self.rental_period["duration_days"],
            "daily_rate": self.rental_charges["rent_per_day"],
            "monthly_rate": self.rental_charges["rent_per_month"],
            "cost_per_square_meter": self.rental_charges["base_rent"] / self.rental_property_info["size_area"] if self.rental_property_info["size_area"] > 0 else 0,
            "utility_cost_percentage": (sum(self.utility_costs.values()) / invoice_doc["totals"]["total_after_discount_excl_vat"]) * 100 if invoice_doc["totals"]["total_after_discount_excl_vat"] > 0 else 0,
            "additional_services_percentage": (sum(self.additional_services.values()) / invoice_doc["totals"]["total_after_discount_excl_vat"]) * 100 if invoice_doc["totals"]["total_after_discount_excl_vat"] > 0 else 0,
            "discount_percentage_applied": self.discount_info["discount_percentage"],
            "seasonal_multiplier_applied": self.seasonal_adjustments["seasonal_rate_multiplier"]
        }
        
        report = {
            "invoice_document": invoice_doc,
            "analytics": analytics,
            "recommendations": self._generate_recommendations(invoice_doc)
        }
        
        return report
    
    def _generate_recommendations(self, invoice_doc: Dict) -> List[str]:
        """Generate recommendations based on the rental invoice."""
        recommendations = []
        
        # Check if utility costs are unusually high
        if sum(self.utility_costs.values()) > self.rental_charges["base_rent"] * 0.3:  # If utilities > 30% of rent
            recommendations.append("Utility costs represent a high percentage of the total invoice. Consider reviewing utility usage or meter accuracy.")
        
        # Check if damage costs are significant
        total_damage_costs = self.damage_extra_charges["damage_cost"]
        if total_damage_costs > self.rental_charges["base_rent"] * 0.1:  # If damages > 10% of rent
            recommendations.append("Significant damage costs were charged. Review property condition process and consider adjusting security deposit requirements.")
        
        # Check if discount is unusually high
        if self.discount_info["discount_percentage"] > 15:  # If discount > 15%
            recommendations.append("High discount applied. Verify this is in line with company policy.")
        
        # If no recommendations, add a positive note
        if not recommendations:
            recommendations.append("Rental invoice appears to be in good order. Charges and terms look appropriate.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the rental invoice to a JSON file."""
        report = self.generate_rental_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a rental invoice from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        invoice_doc = data.get("invoice_document", {})
        self.company_name = invoice_doc.get("company_name", self.company_name)
        self.invoice_date = invoice_doc.get("invoice_date", self.invoice_date)
        self.invoice_number = invoice_doc.get("invoice_number", self.invoice_number)
        self.sender_info = invoice_doc.get("sender_info", self.sender_info)
        self.receiver_info = invoice_doc.get("receiver_info", self.receiver_info)
        self.rental_property_info = invoice_doc.get("rental_property_info", self.rental_property_info)
        self.rental_period = invoice_doc.get("rental_period", self.rental_period)
        self.rental_charges = invoice_doc.get("rental_charges", self.rental_charges)
        self.utility_costs = invoice_doc.get("utility_costs", self.utility_costs)
        self.additional_services = invoice_doc.get("additional_services", self.additional_services)
        self.deposits_guarantees = invoice_doc.get("deposits_guarantees", self.deposits_guarantees)
        self.payment_terms = invoice_doc.get("payment_terms", self.payment_terms)
        self.totals = invoice_doc.get("totals", self.totals)


def create_sample_rental_invoice() -> RentalInvoice:
    """Create a sample rental invoice with example data."""
    invoice = RentalInvoice(company_name="Sample Rental Co", year=2026)
    
    # Set sender information
    invoice.set_sender_info(
        name="Sample Rental Oy",
        address="Vuokrakatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Vuokraaja: Veera Vuokraaja",
        phone="0500 123 456",
        email="veera.vuokraaja@samplerental.fi",
        website="www.samplerental.fi",
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
    
    # Set rental property information
    invoice.set_rental_property_info(
        property_id="PROP-001",
        property_address="Esimerkkikatu 123, 33200 Tampere",
        property_type="Asuntovaunu",
        size_area=45.5,
        features=["Kitchen", "Balcony", "Parking space"]
    )
    
    # Set rental period
    invoice.set_rental_period("2026-01-01", "2026-01-31")  # One month rental
    
    # Set rental charges
    invoice.set_rental_charges(
        base_rent=650.00,  # Base monthly rent
        rent_per_day=21.67,  # 650/30
        rent_per_month=650.00,
        pro_rated_rent=650.00  # For full month
    )
    
    # Set utility costs
    invoice.set_utility_costs(
        water=25.00,
        electricity=45.00,
        heating=35.00,
        internet=20.00,
        other_utilities=10.00
    )
    
    # Set additional services
    invoice.set_additional_services(
        cleaning=30.00,
        parking=50.00,
        storage=25.00
    )
    
    # Set deposits and guarantees
    invoice.set_deposits_guarantees(
        security_deposit=1000.00,
        deposit_return_status="Pending",
        deposit_return_date="2026-02-15"
    )
    
    # Set meter readings
    invoice.set_meter_readings(
        water_start=12345.0,
        water_end=12365.0,
        electricity_start=54321.0,
        electricity_end=54421.0,
        heating_start=9876.0,
        heating_end=9926.0
    )
    
    # Set property condition
    invoice.set_property_condition(
        condition_at_start="Good",
        condition_at_end="Good",
        damage_notes="Minor wear and tear as expected"
    )
    
    # Set cleaning and maintenance costs
    invoice.set_cleaning_maintenance_costs(
        cleaning_cost=0.00,  # Already included in additional services
        maintenance_cost=15.00,
        extra_cleaning_required=False
    )
    
    # Set damage and extra charges
    invoice.set_damage_extra_charges(
        damage_cost=0.00,  # No damages
        extra_usage_charges=0.00
    )
    
    # Set invoice details
    invoice.invoice_number = "REN-2026-001"
    invoice.invoice_date = "2026-02-01"
    
    # Set payment terms
    invoice.payment_terms = {
        "payment_method": "Bank transfer",
        "payment_period_days": 14,
        "due_date": "2026-02-15",
        "late_fee_rate": 0.095
    }
    
    # Apply a small discount
    invoice.apply_discount(5.0, "Long-term customer loyalty discount")
    
    # Add special notes
    invoice.special_notes = "Thank you for your rental business. Please contact us if you have any questions about this invoice."
    
    return invoice


if __name__ == "__main__":
    # Example usage
    print("L6 Vuokralasku - Rental Invoice Tool")
    print("=" * 45)
    
    # Create a sample rental invoice
    sample_invoice = create_sample_rental_invoice()
    
    # Generate and display the rental invoice document
    invoice_doc = sample_invoice.generate_rental_invoice_document()
    
    print(f"\nCompany: {invoice_doc['company_name']}")
    print(f"Invoice Date: {invoice_doc['invoice_date']}")
    print(f"Invoice Number: {invoice_doc['invoice_number']}")
    
    print(f"\nSender: {invoice_doc['sender_info']['name']}")
    print(f"  Address: {invoice_doc['sender_info']['address']}")
    print(f"  Business ID: {invoice_doc['sender_info']['business_id']}")
    print(f"  Contact: {invoice_doc['sender_info']['contact_person']}")
    
    print(f"\nReceiver: {invoice_doc['receiver_info']['name']}")
    print(f"  Address: {invoice_doc['receiver_info']['address']}")
    print(f"  Business ID: {invoice_doc['receiver_info']['business_id']}")
    print(f"  Contact: {invoice_doc['receiver_info']['contact_person']}")
    
    print(f"\nRental Property: {invoice_doc['rental_property_info']['property_address']}")
    print(f"  Type: {invoice_doc['rental_property_info']['property_type']}")
    print(f"  Size: {invoice_doc['rental_property_info']['size_area']} m²")
    print(f"  Features: {', '.join(invoice_doc['rental_property_info']['features'])}")
    
    print(f"\nRental Period: {invoice_doc['rental_period']['start_date']} to {invoice_doc['rental_period']['end_date']}")
    print(f"  Duration: {invoice_doc['rental_period']['duration_days']} days ({invoice_doc['rental_period']['duration_months']} months)")
    
    print(f"\nCharges Breakdown:")
    charges = invoice_doc['rental_charges']
    print(f"  Base Rent: €{charges['base_rent']:.2f}")
    print(f"  Pro-rated Rent: €{charges['pro_rated_rent']:.2f}")
    
    print(f"\nUtility Costs:")
    utils = invoice_doc['utility_costs']
    for util, cost in utils.items():
        if cost > 0:
            print(f"  {util.title()}: €{cost:.2f}")
    
    print(f"\nAdditional Services:")
    services = invoice_doc['additional_services']
    for service, cost in services.items():
        if cost > 0:
            print(f"  {service.title()}: €{cost:.2f}")
    
    print(f"\nMeter Readings:")
    meters = invoice_doc['meter_readings']
    print(f"  Water: {meters['water_start']} → {meters['water_end']}")
    print(f"  Electricity: {meters['electricity_start']} → {meters['electricity_end']}")
    print(f"  Heating: {meters['heating_start']} → {meters['heating_end']}")
    
    print(f"\nProperty Condition:")
    cond = invoice_doc['property_condition']
    print(f"  At Start: {cond['condition_at_start']}")
    print(f"  At End: {cond['condition_at_end']}")
    print(f"  Damage Notes: {cond['damage_notes']}")
    
    print(f"\nFinancial Summary:")
    totals = invoice_doc['totals']
    print(f"  Subtotal (excl. VAT): €{totals['subtotal_excl_vat']:.2f}")
    print(f"  Discount Applied: €{totals['discount_amount']:.2f} ({invoice_doc['discount_info']['discount_percentage']:.1f}%)")
    print(f"  Total After Discount (excl. VAT): €{totals['total_after_discount_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total (incl. VAT): €{totals['total_incl_vat']:.2f}")
    
    print(f"\nPayment Terms:")
    payment = invoice_doc['payment_terms']
    print(f"  Method: {payment['payment_method']}")
    print(f"  Period: {payment['payment_period_days']} days")
    print(f"  Due Date: {payment['due_date']}")
    print(f"  Late Fee Rate: {payment['late_fee_rate']:.1%}")
    
    print(f"\nDeposits & Guarantees:")
    deposit = invoice_doc['deposits_guarantees']
    print(f"  Security Deposit: €{deposit['security_deposit']:.2f}")
    print(f"  Return Status: {deposit['deposit_return_status']}")
    print(f"  Return Date: {deposit['deposit_return_date']}")
    
    print(f"\nLate Payment Interest: {invoice_doc['late_payment_interest']:.1%}")
    
    # Generate and display the rental report
    print(f"\nGenerating rental report...")
    report = sample_invoice.generate_rental_report()
    
    analytics = report['analytics']
    print(f"\nRental Analytics:")
    print(f"  Total Rental Days: {analytics['total_rental_days']}")
    print(f"  Daily Rate: €{analytics['daily_rate']:.2f}")
    print(f"  Monthly Rate: €{analytics['monthly_rate']:.2f}")
    print(f"  Cost per Square Meter: €{analytics['cost_per_square_meter']:.2f}")
    print(f"  Utility Cost % of Total: {analytics['utility_cost_percentage']:.1f}%")
    print(f"  Additional Services % of Total: {analytics['additional_services_percentage']:.1f}%")
    print(f"  Discount Applied: {analytics['discount_percentage_applied']:.1f}%")
    print(f"  Seasonal Multiplier: {analytics['seasonal_multiplier_applied']:.2f}")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    print(f"\nSpecial Notes: {invoice_doc['special_notes']}")
    
    # Save the invoice to a JSON file
    sample_invoice.save_to_json("sample_rental_invoice.json")
    print(f"\nRental invoice saved to 'sample_rental_invoice.json'")