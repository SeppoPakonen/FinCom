"""
Python implementation of T1_Matkalasku_2026 travel expense report template.

This module provides programmatic access to the travel expense report functionality
originally implemented in the T1_Matkalasku_2026.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class TravelExpenseReport:
    """
    A class representing a travel expense report based on the 
    T1_Matkalasku_2026 template.
    This tool helps employees document and submit their business-related 
    travel expenses for reimbursement, and assists employers in tracking 
    and managing travel-related costs.
    """
    
    def __init__(self, employee_name: str = "Travel Employee", year: int = 2026):
        self.employee_name = employee_name
        self.year = year
        self.payment_recipient = {}  # Payment recipient information
        self.iban_number = ""  # Bank account number
        self.personal_id = ""  # Personal identification number
        self.travel_info = []  # Travel details
        self.transportation_costs = []  # Transportation expenses
        self.daily_allowances = []  # Daily allowance information
        self.other_expenses = []  # Other expenses
        self.expense_summary = {}  # Summary of expenses
        self.approval_info = {}  # Approval information
        self.tax_information = {}  # Tax-related information
        self.accounting_entries = {}  # Accounting information
        self.audit_trail = {}  # Audit information
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the travel expense report with default values."""
        # Payment recipient information
        self.payment_recipient = {
            "name_address": "",
            "iban": "",
            "personal_id": ""
        }
        
        # Travel information structure
        self.travel_info = []
        
        # Transportation costs structure
        self.transportation_costs = []
        
        # Daily allowance structure
        self.daily_allowances = []
        
        # Other expenses structure
        self.other_expenses = []
        
        # Expense summary
        self.expense_summary = {
            "total_transportation": 0.0,
            "total_daily_allowances": 0.0,
            "total_other_expenses": 0.0,
            "grand_total": 0.0,
            "advance_payment": 0.0,
            "amount_due": 0.0
        }
        
        # Approval information
        self.approval_info = {
            "requester_name": self.employee_name,
            "requester_signature": "",
            "requester_date": "",
            "approver_name": "",
            "approver_signature": "",
            "approver_date": ""
        }
        
        # Default tax information
        self.tax_information = {
            "taxable_amount": 0.0,
            "non_taxable_amount": 0.0,
            "vat_amount": 0.0
        }
        
        # Daily allowance rates by location (in EUR/day)
        self.daily_allowance_rates = {
            "domestic": 24,  # Domestic travel within Finland
            "eu": 40,        # EU countries
            "outside_eu": 50 # Countries outside EU
        }
        
        # Transportation reimbursement rates (in EUR/km)
        self.transportation_rates = {
            "personal_vehicle": 0.55,  # Per km for personal vehicle
            "public_transport": 1.0,  # Per km for public transport
            "rental_car": 1.0         # Per km for rental car
        }
    
    def add_trip(self, departure_date: str, departure_time: str, arrival_date: str, arrival_time: str, 
                 route: str, purpose: str, transport_method: str, distance_km: float = 0):
        """Add a trip to the travel expense report."""
        trip = {
            "departure_date": departure_date,
            "departure_time": departure_time,
            "arrival_date": arrival_date,
            "arrival_time": arrival_time,
            "route": route,
            "purpose": purpose,
            "transport_method": transport_method,
            "distance_km": distance_km,
            "transport_cost": 0.0,
            "daily_allowance_days": 0,
            "daily_allowance_amount": 0.0
        }
        
        # Calculate transportation cost if using personal vehicle
        if transport_method.lower() == "personal_vehicle" and distance_km > 0:
            trip["transport_cost"] = distance_km * self.transportation_rates["personal_vehicle"]
        
        self.travel_info.append(trip)
    
    def add_daily_allowance(self, date: str, location_type: str, days: float, amount: float = 0):
        """Add daily allowance information."""
        if amount == 0:
            # Calculate based on location type and number of days
            rate = self.daily_allowance_rates[location_type]
            amount = days * rate
        
        allowance = {
            "date": date,
            "location_type": location_type,
            "days": days,
            "rate_per_day": self.daily_allowance_rates[location_type],
            "amount": amount
        }
        
        self.daily_allowances.append(allowance)
    
    def add_other_expense(self, date: str, description: str, amount: float, category: str = "other"):
        """Add an other expense to the report."""
        expense = {
            "date": date,
            "description": description,
            "amount": amount,
            "category": category
        }
        
        self.other_expenses.append(expense)
    
    def calculate_transportation_costs(self) -> float:
        """Calculate total transportation costs."""
        total = 0.0
        for trip in self.travel_info:
            total += trip["transport_cost"]
        return total
    
    def calculate_daily_allowances(self) -> float:
        """Calculate total daily allowance costs."""
        total = 0.0
        for allowance in self.daily_allowances:
            total += allowance["amount"]
        return total
    
    def calculate_other_expenses(self) -> float:
        """Calculate total other expenses."""
        total = 0.0
        for expense in self.other_expenses:
            total += expense["amount"]
        return total
    
    def calculate_expense_summary(self) -> Dict:
        """Calculate the expense summary."""
        transport_total = self.calculate_transportation_costs()
        allowance_total = self.calculate_daily_allowances()
        other_total = self.calculate_other_expenses()
        
        grand_total = transport_total + allowance_total + other_total
        
        # Calculate amount due after advance payment
        amount_due = grand_total - self.expense_summary.get("advance_payment", 0)
        
        self.expense_summary = {
            "total_transportation": transport_total,
            "total_daily_allowances": allowance_total,
            "total_other_expenses": other_total,
            "grand_total": grand_total,
            "advance_payment": self.expense_summary.get("advance_payment", 0),
            "amount_due": amount_due
        }
        
        return self.expense_summary
    
    def set_advance_payment(self, amount: float):
        """Set the advance payment amount."""
        self.expense_summary["advance_payment"] = amount
        # Recalculate amount due
        summary = self.calculate_expense_summary()
        self.expense_summary["amount_due"] = summary["grand_total"] - amount
    
    def calculate_tax_information(self) -> Dict:
        """Calculate tax-related information for the expenses."""
        # In Finland, daily allowances up to certain limits are tax-free
        # For simplicity, assuming daily allowances are tax-free up to a limit
        daily_allowances_total = self.calculate_daily_allowances()
        
        # Daily allowances up to 24€ per day are typically tax-free in Finland
        tax_free_daily_allowances = 0
        taxable_daily_allowances = 0
        
        for allowance in self.daily_allowances:
            if allowance["rate_per_day"] <= 24:  # Tax-free limit
                tax_free_daily_allowances += allowance["amount"]
            else:
                taxable_daily_allowances += allowance["amount"]
        
        # Transportation costs are typically fully deductible
        transport_total = self.calculate_transportation_costs()
        
        # Other expenses may or may not be taxable depending on category
        other_total = self.calculate_other_expenses()
        taxable_other = other_total  # For simplicity, assuming all other expenses are taxable
        
        self.tax_information = {
            "taxable_amount": taxable_daily_allowances + transport_total + taxable_other,
            "non_taxable_amount": tax_free_daily_allowances,
            "vat_amount": 0.0  # Would need more detailed info to calculate VAT
        }
        
        return self.tax_information
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive travel expense report."""
        summary = self.calculate_expense_summary()
        tax_info = self.calculate_tax_information()
        
        report = {
            "employee_name": self.employee_name,
            "year": self.year,
            "payment_recipient": self.payment_recipient,
            "travel_info": self.travel_info,
            "transportation_costs": self.transportation_costs,
            "daily_allowances": self.daily_allowances,
            "other_expenses": self.other_expenses,
            "expense_summary": summary,
            "tax_information": tax_info,
            "approval_info": self.approval_info,
            "accounting_entries": self.accounting_entries,
            "audit_trail": self.audit_trail
        }
        
        return report
    
    def generate_detailed_report(self) -> Dict:
        """Generate a detailed travel expense report with additional analytics."""
        basic_report = self.generate_report()
        
        # Calculate additional metrics
        total_distance = sum(trip["distance_km"] for trip in self.travel_info if "distance_km" in trip)
        total_days = sum(allowance["days"] for allowance in self.daily_allowances)
        
        # Calculate cost per km if using personal vehicle
        transport_cost = basic_report["expense_summary"]["total_transportation"]
        cost_per_km = transport_cost / total_distance if total_distance > 0 else 0
        
        # Calculate daily cost
        daily_cost = (basic_report["expense_summary"]["grand_total"] - transport_cost) / total_days if total_days > 0 else 0
        
        detailed_report = {
            **basic_report,
            "analytics": {
                "total_distance_km": total_distance,
                "total_travel_days": total_days,
                "cost_per_km": cost_per_km,
                "daily_cost": daily_cost,
                "transportation_percentage": (transport_cost / basic_report["expense_summary"]["grand_total"]) * 100 if basic_report["expense_summary"]["grand_total"] > 0 else 0,
                "daily_allowance_percentage": (basic_report["expense_summary"]["total_daily_allowances"] / basic_report["expense_summary"]["grand_total"]) * 100 if basic_report["expense_summary"]["grand_total"] > 0 else 0
            }
        }
        
        return detailed_report
    
    def save_to_json(self, filepath: str):
        """Save the travel expense report to a JSON file."""
        report = self.generate_detailed_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a travel expense report from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.employee_name = data.get("employee_name", self.employee_name)
        self.year = data.get("year", self.year)
        self.payment_recipient = data.get("payment_recipient", self.payment_recipient)
        self.travel_info = data.get("travel_info", self.travel_info)
        self.transportation_costs = data.get("transportation_costs", self.transportation_costs)
        self.daily_allowances = data.get("daily_allowances", self.daily_allowances)
        self.other_expenses = data.get("other_expenses", self.other_expenses)
        self.expense_summary = data.get("expense_summary", self.expense_summary)
        self.tax_information = data.get("tax_information", self.tax_information)
        self.approval_info = data.get("approval_info", self.approval_info)


def create_sample_report() -> TravelExpenseReport:
    """Create a sample travel expense report with example data."""
    report = TravelExpenseReport(employee_name="Matti Matkustaja", year=2026)
    
    # Set payment recipient information
    report.payment_recipient = {
        "name_address": "Matti Matkustaja, Matkatie 12, 00100 Helsinki",
        "iban": "FI4850001230000001",
        "personal_id": "010180-123X"
    }
    
    # Add example trips
    report.add_trip(
        departure_date="2026-09-22",
        departure_time="06:15",
        arrival_date="2026-09-22",
        arrival_time="14:30",
        route="Tampere - Lappeenranta - Tampere",
        purpose="Sales presentation at ABC Oy and XYZ Ky",
        transport_method="personal_vehicle",
        distance_km=798
    )
    
    report.add_trip(
        departure_date="2026-09-23",
        departure_time="09:00",
        arrival_date="2026-09-23",
        arrival_time="21:00",
        route="Lappeenranta area meetings",
        purpose="Meetings with clients in Lappeenranta area",
        transport_method="personal_vehicle",
        distance_km=150
    )
    
    # Add daily allowances
    report.add_daily_allowance(
        date="2026-09-22",
        location_type="domestic",
        days=1.0,
        amount=24.0  # Standard domestic rate
    )
    
    report.add_daily_allowance(
        date="2026-09-23",
        location_type="domestic",
        days=1.0,
        amount=24.0  # Standard domestic rate
    )
    
    # Add other expenses
    report.add_other_expense(
        date="2026-09-22",
        description="Parking fees at ABC Oy",
        amount=39.0,
        category="parking"
    )
    
    report.add_other_expense(
        date="2026-09-23",
        description="Hotel accommodation",
        amount=139.0,
        category="accommodation"
    )
    
    # Set advance payment
    report.set_advance_payment(100.0)
    
    # Set approval information
    report.approval_info = {
        "requester_name": "Matti Matkustaja",
        "requester_signature": "M. Matkustaja",
        "requester_date": "2026-09-24",
        "approver_name": "Manager Name",
        "approver_signature": "M. Manager",
        "approver_date": "2026-09-25"
    }
    
    return report


if __name__ == "__main__":
    # Example usage
    print("T1 Matkalasku 2026 - Travel Expense Report Tool")
    print("=" * 55)
    
    # Create a sample travel expense report
    sample_report = create_sample_report()
    
    # Generate and display the travel expense report
    report = sample_report.generate_detailed_report()
    
    print(f"\nEmployee: {report['employee_name']}")
    print(f"Year: {report['year']}")
    print(f"Payment Recipient: {report['payment_recipient']['name_address']}")
    print(f"IBAN: {report['payment_recipient']['iban']}")
    
    print(f"\nTravel Details:")
    for i, trip in enumerate(report['travel_info'], 1):
        print(f"  Trip {i}: {trip['route']}")
        print(f"    Date: {trip['departure_date']}")
        print(f"    Purpose: {trip['purpose']}")
        print(f"    Distance: {trip['distance_km']} km")
        print(f"    Transport Cost: €{trip['transport_cost']:.2f}")
    
    print(f"\nDaily Allowances:")
    for i, allowance in enumerate(report['daily_allowances'], 1):
        print(f"  Day {i}: {allowance['days']} days at {allowance['rate_per_day']:.2f}€/day = €{allowance['amount']:.2f}")
    
    print(f"\nOther Expenses:")
    for i, expense in enumerate(report['other_expenses'], 1):
        print(f"  {expense['description']}: €{expense['amount']:.2f}")
    
    print(f"\nExpense Summary:")
    summary = report['expense_summary']
    print(f"  Transportation: €{summary['total_transportation']:,.2f}")
    print(f"  Daily Allowances: €{summary['total_daily_allowances']:,.2f}")
    print(f"  Other Expenses: €{summary['total_other_expenses']:,.2f}")
    print(f"  Grand Total: €{summary['grand_total']:,.2f}")
    print(f"  Advance Payment: €{summary['advance_payment']:,.2f}")
    print(f"  Amount Due: €{summary['amount_due']:,.2f}")
    
    print(f"\nTax Information:")
    tax_info = report['tax_information']
    print(f"  Taxable Amount: €{tax_info['taxable_amount']:,.2f}")
    print(f"  Non-Taxable Amount: €{tax_info['non_taxable_amount']:,.2f}")
    
    print(f"\nAnalytics:")
    analytics = report['analytics']
    print(f"  Total Distance: {analytics['total_distance_km']} km")
    print(f"  Total Travel Days: {analytics['total_travel_days']}")
    print(f"  Cost per km: €{analytics['cost_per_km']:.2f}")
    print(f"  Daily Cost: €{analytics['daily_cost']:.2f}")
    print(f"  Transportation %: {analytics['transportation_percentage']:.1f}%")
    print(f"  Daily Allowance %: {analytics['daily_allowance_percentage']:.1f}%")
    
    print(f"\nApproval:")
    approval = report['approval_info']
    print(f"  Requester: {approval['requester_name']} on {approval['requester_date']}")
    print(f"  Approver: {approval['approver_name']} on {approval['approver_date']}")
    
    # Save the report to a JSON file
    sample_report.save_to_json("sample_travel_expense_report.json")
    print(f"\nTravel expense report saved to 'sample_travel_expense_report.json'")