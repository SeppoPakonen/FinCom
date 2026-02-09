"""
Python implementation of L11_Pienurakkasopimus_1 small construction contract template.

This module provides programmatic access to the small construction contract functionality
originally implemented in the L11_Pienurakkasopimus_1.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class SmallConstructionContract:
    """
    A class representing a small construction contract based on the 
    L11_Pienurakkasopimus_1 template.
    This tool helps businesses in the construction industry create standardized 
    contracts for small-scale construction projects, outlining project specifications, 
    terms, pricing, and other important contractual elements.
    """
    
    def __init__(self, company_name: str = "Construction Contract Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.contract_date = datetime.now().strftime('%d.%m.%Y')
        self.contractor_info = {}  # Contractor information
        self.client_info = {}  # Client information
        self.project_description = {}  # Project description and scope
        self.work_schedule = {}  # Work schedule and timeline
        self.materials = []  # Materials and supplies
        self.labor = []  # Labor and personnel
        self.pricing = {}  # Pricing and cost calculations
        self.payment_terms = {}  # Payment terms and conditions
        self.delivery_terms = {}  # Delivery terms and conditions
        self.quality_guarantee = {}  # Quality guarantee information
        self.safety_requirements = {}  # Safety requirements
        self.environmental_requirements = {}  # Environmental requirements
        self.contract_terms = {}  # General contract terms
        self.penalty_clauses = {}  # Penalty clauses for breaches
        self.warranty_terms = {}  # Warranty terms
        self.liability_exemptions = {}  # Liability exemptions
        self.change_orders = {}  # Change order procedures
        self.cancellation_terms = {}  # Cancellation terms
        self.work_acceptance = {}  # Work acceptance procedures
        self.contract_termination = {}  # Contract termination procedures
        self.invoicing_procedures = {}  # Invoicing procedures
        self.accounting_entries = {}  # Accounting entries
        self.reporting_analytics = {}  # Reporting and analytics
        self.audit_info = {}  # Audit information
        self.risk_management = {}  # Risk management
        self.quality_criteria = {}  # Quality criteria
        self.total_contract_value = 0.0
        self.total_with_vat = 0.0
        self.contract_period = {}  # Contract period information
        self.permits_insurances = {}  # Permits and insurances
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the small construction contract with default values."""
        # Default contractor information
        self.contractor_info = {
            "name": self.company_name,
            "address": "",
            "business_id": "",
            "contact_person": "",
            "phone": "",
            "email": "",
            "vat_registration": ""
        }
        
        # Default client information
        self.client_info = {
            "name": "",
            "address": "",
            "business_id_or_personal_id": "",
            "contact_person": "",
            "phone": "",
            "email": ""
        }
        
        # Default project description
        self.project_description = {
            "project_name": "",
            "project_location": "",
            "project_scope": "",
            "work_description": "",
            "special_requirements": ""
        }
        
        # Default work schedule
        self.work_schedule = {
            "start_date": "",
            "end_date": "",
            "work_days": "Monday-Sunday",
            "work_hours": "08:00-16:00",
            "break_times": "1 hour for lunch",
            "estimated_duration_days": 0
        }
        
        # Default pricing structure
        self.pricing = {
            "pricing_method": "Fixed price",
            "vat_rate": 0.255,  # Standard Finnish construction VAT rate
            "currency": "EUR",
            "exchange_rate": 1.0
        }
        
        # Default payment terms
        self.payment_terms = {
            "payment_method": "Invoice",
            "payment_schedule": "Milestone-based",
            "payment_period": "30 days",
            "advance_payment_percentage": 0.0,
            "retention_percentage": 0.05  # 5% retention
        }
        
        # Default delivery terms
        self.delivery_terms = {
            "delivery_method": "On-site completion",
            "delivery_location": "",
            "delivery_deadline": ""
        }
        
        # Default quality guarantee
        self.quality_guarantee = {
            "guarantee_period": "12 months",
            "guarantee_scope": "Construction defects",
            "guarantee_exclusions": "Damage due to misuse or normal wear"
        }
        
        # Default safety requirements
        self.safety_requirements = {
            "safety_protocols_required": True,
            "safety_certifications_required": True,
            "accident_prevention_measures": True,
            "safety_training_required": True
        }
        
        # Default environmental requirements
        self.environmental_requirements = {
            "environmental_compliance_required": True,
            "waste_management_plan": True,
            "noise_control_measures": True,
            "dust_control_measures": True
        }
        
        # Default contract terms
        self.contract_terms = {
            "termination_clause": "With 14 days notice",
            "dispute_resolution": "According to Finnish law",
            "jurisdiction": "Finnish courts",
            "applicable_law": "Finnish law"
        }
        
        # Default materials list
        self.materials = []
        
        # Default labor list
        self.labor = []
    
    def set_contractor_info(self, name: str, address: str, business_id: str = "", 
                           contact_person: str = "", phone: str = "", email: str = "",
                           vat_registration: str = ""):
        """Set contractor information."""
        self.contractor_info = {
            "name": name,
            "address": address,
            "business_id": business_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email,
            "vat_registration": vat_registration
        }
    
    def set_client_info(self, name: str, address: str, business_id_or_personal_id: str = "", 
                        contact_person: str = "", phone: str = "", email: str = ""):
        """Set client information."""
        self.client_info = {
            "name": name,
            "address": address,
            "business_id_or_personal_id": business_id_or_personal_id,
            "contact_person": contact_person,
            "phone": phone,
            "email": email
        }
    
    def set_project_description(self, project_name: str, project_location: str, project_scope: str, 
                                work_description: str = "", special_requirements: str = ""):
        """Set project description details."""
        self.project_description = {
            "project_name": project_name,
            "project_location": project_location,
            "project_scope": project_scope,
            "work_description": work_description,
            "special_requirements": special_requirements
        }
    
    def set_work_schedule(self, start_date: str, end_date: str, work_days: str = "Monday-Sunday", 
                         work_hours: str = "08:00-16:00", estimated_duration_days: int = 0):
        """Set work schedule details."""
        self.work_schedule = {
            "start_date": start_date,
            "end_date": end_date,
            "work_days": work_days,
            "work_hours": work_hours,
            "estimated_duration_days": estimated_duration_days
        }
    
    def set_contract_period(self, type_period: str, start_date: str = "", end_date: str = "", 
                           duration_months: int = 0):
        """Set contract period details."""
        self.contract_period = {
            "type": type_period,  # "fixed_term", "ongoing_with_notice", etc.
            "start_date": start_date,
            "end_date": end_date,
            "duration_months": duration_months
        }
    
    def add_material(self, name: str, quantity: float, unit: str, unit_price_excl_vat: float, 
                    vat_rate: float = 0.255, description: str = ""):
        """Add a material to the contract."""
        material = {
            "name": name,
            "description": description,
            "quantity": quantity,
            "unit": unit,
            "unit_price_excl_vat": unit_price_excl_vat,
            "vat_rate": vat_rate,
            "total_excl_vat": quantity * unit_price_excl_vat,
            "total_vat": quantity * unit_price_excl_vat * vat_rate,
            "total_incl_vat": quantity * unit_price_excl_vat * (1 + vat_rate)
        }
        
        self.materials.append(material)
        return material
    
    def add_labor(self, role: str, hours: float, hourly_rate: float, 
                 vat_rate: float = 0.255, description: str = ""):
        """Add labor to the contract."""
        labor = {
            "role": role,
            "description": description,
            "hours": hours,
            "hourly_rate": hourly_rate,
            "vat_rate": vat_rate,
            "total_excl_vat": hours * hourly_rate,
            "total_vat": hours * hourly_rate * vat_rate,
            "total_incl_vat": hours * hourly_rate * (1 + vat_rate)
        }
        
        self.labor.append(labor)
        return labor
    
    def set_pricing_method(self, method: str, vat_rate: float = 0.255):
        """Set the pricing method for the contract."""
        self.pricing["pricing_method"] = method
        self.pricing["vat_rate"] = vat_rate
    
    def set_payment_terms(self, method: str, schedule: str, period: str, 
                         advance_payment: float = 0.0, retention: float = 0.05):
        """Set payment terms for the contract."""
        self.payment_terms = {
            "payment_method": method,
            "payment_schedule": schedule,
            "payment_period": period,
            "advance_payment_percentage": advance_payment,
            "retention_percentage": retention
        }
    
    def calculate_contract_totals(self) -> Dict:
        """Calculate total contract value with and without VAT."""
        materials_total_excl_vat = sum(mat["total_excl_vat"] for mat in self.materials)
        materials_total_vat = sum(mat["total_vat"] for mat in self.materials)
        materials_total_incl_vat = sum(mat["total_incl_vat"] for mat in self.materials)
        
        labor_total_excl_vat = sum(lab["total_excl_vat"] for lab in self.labor)
        labor_total_vat = sum(lab["total_vat"] for lab in self.labor)
        labor_total_incl_vat = sum(lab["total_incl_vat"] for lab in self.labor)
        
        total_excl_vat = materials_total_excl_vat + labor_total_excl_vat
        total_vat = materials_total_vat + labor_total_vat
        total_incl_vat = materials_total_incl_vat + labor_total_incl_vat
        
        # Apply advance payment if applicable
        advance_amount = total_incl_vat * self.payment_terms["advance_payment_percentage"]
        
        # Apply retention if applicable
        retention_amount = total_incl_vat * self.payment_terms["retention_percentage"]
        
        # Calculate net amount due
        net_amount = total_incl_vat - advance_amount - retention_amount
        
        self.total_contract_value = total_excl_vat
        self.total_with_vat = total_incl_vat
        
        return {
            "materials_total_excl_vat": materials_total_excl_vat,
            "materials_total_vat": materials_total_vat,
            "materials_total_incl_vat": materials_total_incl_vat,
            "labor_total_excl_vat": labor_total_excl_vat,
            "labor_total_vat": labor_total_vat,
            "labor_total_incl_vat": labor_total_incl_vat,
            "total_excl_vat": total_excl_vat,
            "total_vat": total_vat,
            "total_incl_vat": total_incl_vat,
            "advance_amount": advance_amount,
            "retention_amount": retention_amount,
            "net_amount_due": net_amount
        }
    
    def generate_contract_document(self) -> Dict:
        """Generate a complete small construction contract document."""
        totals = self.calculate_contract_totals()
        
        contract_doc = {
            "company_name": self.company_name,
            "contract_date": self.contract_date,
            "contractor_info": self.contractor_info,
            "client_info": self.client_info,
            "project_description": self.project_description,
            "work_schedule": self.work_schedule,
            "materials_list": self.materials,
            "labor_list": self.labor,
            "pricing_info": self.pricing,
            "payment_terms": self.payment_terms,
            "delivery_terms": self.delivery_terms,
            "quality_guarantee": self.quality_guarantee,
            "safety_requirements": self.safety_requirements,
            "environmental_requirements": self.environmental_requirements,
            "contract_terms": self.contract_terms,
            "penalty_clauses": self.penalty_clauses,
            "warranty_terms": self.warranty_terms,
            "liability_exemptions": self.liability_exemptions,
            "change_orders": self.change_orders,
            "cancellation_terms": self.cancellation_terms,
            "work_acceptance": self.work_acceptance,
            "contract_termination": self.contract_termination,
            "invoicing_procedures": self.invoicing_procedures,
            "contract_period": self.contract_period,
            "permits_insurances": self.permits_insurances,
            "totals": totals
        }
        
        return contract_doc
    
    def generate_contract_report(self) -> Dict:
        """Generate a comprehensive contract report with additional analytics."""
        contract_doc = self.generate_contract_document()
        
        # Calculate additional analytics
        analytics = {
            "total_items": len(self.materials) + len(self.labor),
            "materials_percentage_of_total": (sum(m["total_incl_vat"] for m in self.materials) / contract_doc["totals"]["total_incl_vat"]) * 100 if contract_doc["totals"]["total_incl_vat"] > 0 else 0,
            "labor_percentage_of_total": (sum(l["total_incl_vat"] for l in self.labor) / contract_doc["totals"]["total_incl_vat"]) * 100 if contract_doc["totals"]["total_incl_vat"] > 0 else 0,
            "average_material_cost": sum(m["total_incl_vat"] for m in self.materials) / len(self.materials) if self.materials else 0,
            "average_labor_cost": sum(l["total_incl_vat"] for l in self.labor) / len(self.labor) if self.labor else 0,
            "contract_duration_days": self._calculate_contract_duration(),
            "cost_per_day": contract_doc["totals"]["total_incl_vat"] / self._calculate_contract_duration() if self._calculate_contract_duration() > 0 else 0,
            "vat_impact_percentage": (contract_doc["totals"]["total_vat"] / contract_doc["totals"]["total_excl_vat"]) * 100 if contract_doc["totals"]["total_excl_vat"] > 0 else 0
        }
        
        report = {
            "contract_document": contract_doc,
            "analytics": analytics,
            "recommendations": self._generate_recommendations(contract_doc)
        }
        
        return report
    
    def _calculate_contract_duration(self) -> int:
        """Calculate the contract duration in days."""
        from datetime import datetime
        if self.work_schedule["start_date"] and self.work_schedule["end_date"]:
            start = datetime.strptime(self.work_schedule["start_date"], '%Y-%m-%d')
            end = datetime.strptime(self.work_schedule["end_date"], '%Y-%m-%d')
            return (end - start).days
        else:
            return self.work_schedule.get("estimated_duration_days", 0)
    
    def _generate_recommendations(self, contract_doc: Dict) -> List[str]:
        """Generate recommendations based on the contract."""
        recommendations = []
        
        # Check if contract value is significant enough for detailed terms
        if contract_doc["totals"]["total_incl_vat"] > 10000:
            recommendations.append("For contracts over €10,000, consider adding more detailed penalty clauses and milestone payments.")
        
        # Check if environmental requirements are specified
        if not self.environmental_requirements.get("waste_management_plan", False):
            recommendations.append("Consider adding a waste management plan for environmental compliance.")
        
        # Check if safety requirements are comprehensive
        if not self.safety_requirements.get("safety_training_required", False):
            recommendations.append("Ensure safety training requirements are specified for construction work.")
        
        # Check if warranty period is appropriate
        if self.quality_guarantee.get("guarantee_period", "0 months") == "0 months":
            recommendations.append("Specify a warranty period for the construction work (typically 12 months).")
        
        # If no recommendations, add a positive note
        if not recommendations:
            recommendations.append("Contract appears to be in good order. All required elements are present.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the contract to a JSON file."""
        report = self.generate_contract_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a contract from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        contract_doc = data.get("contract_document", {})
        self.company_name = contract_doc.get("company_name", self.company_name)
        self.contract_date = contract_doc.get("contract_date", self.contract_date)
        self.contractor_info = contract_doc.get("contractor_info", self.contractor_info)
        self.client_info = contract_doc.get("client_info", self.client_info)
        self.project_description = contract_doc.get("project_description", self.project_description)
        self.work_schedule = contract_doc.get("work_schedule", self.work_schedule)
        self.materials = contract_doc.get("materials_list", self.materials)
        self.labor = contract_doc.get("labor_list", self.labor)
        self.pricing = contract_doc.get("pricing_info", self.pricing)
        self.payment_terms = contract_doc.get("payment_terms", self.payment_terms)
        self.totals = contract_doc.get("totals", self.totals)


def create_sample_contract() -> SmallConstructionContract:
    """Create a sample small construction contract with example data."""
    contract = SmallConstructionContract(company_name="Sample Construction Contract Oy", year=2026)
    
    # Set contractor information
    contract.set_contractor_info(
        name="Sample Construction Oy",
        address="Rakennuskatu 15, 33100 Tampere",
        business_id="1234567-8",
        contact_person="Urakoitsija: Urpo Urakoitsija",
        phone="0500 123 456",
        email="urpo.urakoitsija@sampleconstruction.fi",
        vat_registration="FI12345678"
    )
    
    # Set client information
    contract.set_client_info(
        name="Tilaaja Oy",
        address="Tilaajankatu 20, 00100 Helsinki",
        business_id_or_personal_id="8765432-1",
        contact_person="Tilaaja: Tero Tilaaja",
        phone="0400 987 654",
        email="tero.tilaaja@tilaaja.fi"
    )
    
    # Set project description
    contract.set_project_description(
        project_name="Esimerkkirakennusprojekti",
        project_location="Rakennuskatu 123, 33200 Tampere",
        project_scope="Rakennustyö - pienurakka",
        work_description="Uuden rakennuksen peruskorjaus ja sisustustyöt",
        special_requirements="Ympäristöystävälliset materiaalit, meluntorjuntatoimenpiteet"
    )
    
    # Set work schedule
    contract.set_work_schedule(
        start_date="2026-03-01",
        end_date="2026-05-31",
        work_days="Monday-Friday",
        work_hours="07:00-15:00",
        estimated_duration_days=90
    )
    
    # Add example materials
    contract.add_material(
        name="Betoni",
        description="Perusbetonimäärä rakenteisiin",
        quantity=50.0,
        unit="m³",
        unit_price_excl_vat=120.00,
        vat_rate=0.255
    )
    
    contract.add_material(
        name="Tiili",
        description="Ulkoseinien tiilet",
        quantity=10000,
        unit="kpl",
        unit_price_excl_vat=0.85,
        vat_rate=0.255
    )
    
    contract.add_material(
        name="Kipsilevyt",
        description="Sisäseinien kipsilevyt",
        quantity=500,
        unit="m²",
        unit_price_excl_vat=12.50,
        vat_rate=0.255
    )
    
    # Add example labor
    contract.add_labor(
        role="Mestarimies",
        description="Rakennusmestarimies työn johdossa",
        hours=400,
        hourly_rate=65.00,
        vat_rate=0.255
    )
    
    contract.add_labor(
        role="Aputyöntekijä",
        description="Apurakentajat työmaalla",
        hours=800,
        hourly_rate=25.00,
        vat_rate=0.255
    )
    
    # Set pricing method
    contract.set_pricing_method("Fixed price", 0.255)
    
    # Set payment terms
    contract.set_payment_terms(
        method="Bank transfer",
        schedule="Milestone-based",
        period="30 days",
        advance_payment=0.15,  # 15% advance
        retention=0.05  # 5% retention
    )
    
    # Set contract period
    contract.set_contract_period(
        type_period="fixed_term",
        start_date="2026-03-01",
        end_date="2026-05-31",
        duration_months=3
    )
    
    # Set delivery terms
    contract.delivery_terms = {
        "delivery_method": "On-site completion",
        "delivery_location": "Rakennuskatu 123, 33200 Tampere",
        "delivery_deadline": "2026-05-31"
    }
    
    # Set quality guarantee
    contract.quality_guarantee = {
        "guarantee_period": "12 months",
        "guarantee_scope": "Construction defects and workmanship",
        "guarantee_exclusions": "Damage due to misuse, normal wear, or external factors"
    }
    
    # Set safety requirements
    contract.safety_requirements = {
        "safety_protocols_required": True,
        "safety_certifications_required": True,
        "accident_prevention_measures": True,
        "safety_training_required": True
    }
    
    # Set environmental requirements
    contract.environmental_requirements = {
        "environmental_compliance_required": True,
        "waste_management_plan": True,
        "noise_control_measures": True,
        "dust_control_measures": True
    }
    
    return contract


if __name__ == "__main__":
    # Example usage
    print("L11 Pienurakkasopimus 1 - Small Construction Contract Tool")
    print("=" * 60)
    
    # Create a sample construction contract
    sample_contract = create_sample_contract()
    
    # Generate and display the contract document
    contract_doc = sample_contract.generate_contract_document()
    
    print(f"\nCompany: {contract_doc['company_name']}")
    print(f"Contract Date: {contract_doc['contract_date']}")
    
    print(f"\nContractor: {contract_doc['contractor_info']['name']}")
    print(f"  Address: {contract_doc['contractor_info']['address']}")
    print(f"  Business ID: {contract_doc['contractor_info']['business_id']}")
    print(f"  Contact: {contract_doc['contractor_info']['contact_person']}")
    print(f"  Phone: {contract_doc['contractor_info']['phone']}")
    
    print(f"\nClient: {contract_doc['client_info']['name']}")
    print(f"  Address: {contract_doc['client_info']['address']}")
    print(f"  Business ID: {contract_doc['client_info']['business_id_or_personal_id']}")
    print(f"  Contact: {contract_doc['client_info']['contact_person']}")
    
    print(f"\nProject: {contract_doc['project_description']['project_name']}")
    print(f"  Location: {contract_doc['project_description']['project_location']}")
    print(f"  Scope: {contract_doc['project_description']['project_scope']}")
    print(f"  Work Description: {contract_doc['project_description']['work_description']}")
    
    print(f"\nWork Schedule:")
    schedule = contract_doc['work_schedule']
    print(f"  Start Date: {schedule['start_date']}")
    print(f"  End Date: {schedule['end_date']}")
    print(f"  Work Days: {schedule['work_days']}")
    print(f"  Work Hours: {schedule['work_hours']}")
    print(f"  Estimated Duration: {schedule['estimated_duration_days']} days")
    
    print(f"\nMaterials:")
    for i, material in enumerate(contract_doc['materials_list'], 1):
        print(f"  {i}. {material['name']}")
        print(f"     Description: {material['description']}")
        print(f"     Quantity: {material['quantity']} {material['unit']}")
        print(f"     Unit Price (excl. VAT): €{material['unit_price_excl_vat']:.2f}")
        print(f"     VAT Rate: {material['vat_rate']:.1%}")
        print(f"     Total (excl. VAT): €{material['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{material['total_incl_vat']:.2f}")
    
    print(f"\nLabor:")
    for i, labor in enumerate(contract_doc['labor_list'], 1):
        print(f"  {i}. {labor['role']}")
        print(f"     Description: {labor['description']}")
        print(f"     Hours: {labor['hours']}")
        print(f"     Hourly Rate: €{labor['hourly_rate']:.2f}")
        print(f"     VAT Rate: {labor['vat_rate']:.1%}")
        print(f"     Total (excl. VAT): €{labor['total_excl_vat']:.2f}")
        print(f"     Total (incl. VAT): €{labor['total_incl_vat']:.2f}")
    
    print(f"\nFinancial Summary:")
    totals = contract_doc['totals']
    print(f"  Materials Total (excl. VAT): €{totals['materials_total_excl_vat']:.2f}")
    print(f"  Materials Total (incl. VAT): €{totals['materials_total_incl_vat']:.2f}")
    print(f"  Labor Total (excl. VAT): €{totals['labor_total_excl_vat']:.2f}")
    print(f"  Labor Total (incl. VAT): €{totals['labor_total_incl_vat']:.2f}")
    print(f"  Total Contract Value (excl. VAT): €{totals['total_excl_vat']:.2f}")
    print(f"  Total VAT: €{totals['total_vat']:.2f}")
    print(f"  Total Contract Value (incl. VAT): €{totals['total_incl_vat']:.2f}")
    print(f"  Advance Payment: €{totals['advance_amount']:.2f}")
    print(f"  Retention Amount: €{totals['retention_amount']:.2f}")
    print(f"  Net Amount Due: €{totals['net_amount_due']:.2f}")
    
    print(f"\nPayment Terms:")
    payment = contract_doc['payment_terms']
    print(f"  Method: {payment['payment_method']}")
    print(f"  Schedule: {payment['payment_schedule']}")
    print(f"  Period: {payment['payment_period']}")
    print(f"  Advance Payment: {payment['advance_payment_percentage']:.1%}")
    print(f"  Retention: {payment['retention_percentage']:.1%}")
    
    print(f"\nDelivery Terms:")
    delivery = contract_doc['delivery_terms']
    print(f"  Method: {delivery['delivery_method']}")
    print(f"  Location: {delivery['delivery_location']}")
    print(f"  Deadline: {delivery['delivery_deadline']}")
    
    print(f"\nQuality Guarantee:")
    quality = contract_doc['quality_guarantee']
    print(f"  Period: {quality['guarantee_period']}")
    print(f"  Scope: {quality['guarantee_scope']}")
    print(f"  Exclusions: {quality['guarantee_exclusions']}")
    
    print(f"\nSafety Requirements:")
    safety = contract_doc['safety_requirements']
    print(f"  Safety Protocols Required: {safety['safety_protocols_required']}")
    print(f"  Safety Certifications Required: {safety['safety_certifications_required']}")
    print(f"  Accident Prevention Measures: {safety['accident_prevention_measures']}")
    print(f"  Safety Training Required: {safety['safety_training_required']}")
    
    print(f"\nEnvironmental Requirements:")
    env = contract_doc['environmental_requirements']
    print(f"  Environmental Compliance Required: {env['environmental_compliance_required']}")
    print(f"  Waste Management Plan: {env['waste_management_plan']}")
    print(f"  Noise Control Measures: {env['noise_control_measures']}")
    print(f"  Dust Control Measures: {env['dust_control_measures']}")
    
    # Generate and display the contract report
    print(f"\nGenerating contract report...")
    report = sample_contract.generate_contract_report()
    
    analytics = report['analytics']
    print(f"\nContract Analytics:")
    print(f"  Total Items (materials + labor): {analytics['total_items']}")
    print(f"  Materials % of Total: {analytics['materials_percentage_of_total']:.1f}%")
    print(f"  Labor % of Total: {analytics['labor_percentage_of_total']:.1f}%")
    print(f"  Average Material Cost: €{analytics['average_material_cost']:.2f}")
    print(f"  Average Labor Cost: €{analytics['average_labor_cost']:.2f}")
    print(f"  Contract Duration: {analytics['contract_duration_days']} days")
    print(f"  Cost per Day: €{analytics['cost_per_day']:.2f}")
    print(f"  VAT Impact: {analytics['vat_impact_percentage']:.1f}%")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the contract to a JSON file
    sample_contract.save_to_json("sample_small_construction_contract.json")
    print(f"\nSmall construction contract saved to 'sample_small_construction_contract.json'")