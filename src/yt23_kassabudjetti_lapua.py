"""
Python implementation of YT23_Kassabudjetti_Lapua cash budget template.

This module provides programmatic access to the cash budget functionality
originally implemented in the YT23_Kassabudjetti_Lapua.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class CashBudget:
    """
    A class representing a cash budget based on the YT23_Kassabudjetti_Lapua template.
    This template helps businesses in Lapua plan and manage their cash flow effectively,
    ensuring sufficient liquidity for operations.
    """
    
    def __init__(self, company_name: str = "Cash Budget Business", start_date: str = "2026-01-01"):
        self.company_name = company_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.cash_inflows = {}  # Monthly cash inflows
        self.cash_outflows = {}  # Monthly cash outflows
        self.initial_cash_balance = 0  # Starting cash balance
        self.financing_activities = {}  # Financing activities (loans, investments)
        self.cash_forecast = {}
        self.liquidity_metrics = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the cash budget with default values."""
        # Generate 12 months of data starting from the start date
        months = []
        current_date = self.start_date
        for i in range(12):
            month_key = current_date.strftime("%Y-%m")
            months.append(month_key)
            # Move to next month
            if current_date.month == 12:
                current_date = current_date.replace(year=current_date.year + 1, month=1)
            else:
                current_date = current_date.replace(month=current_date.month + 1)
        
        # Initialize cash inflows for each month
        self.cash_inflows = {month: {
            "available_cash_reserves": 0,
            "sales_receivables": 0,
            "sales_revenue": 0,
            "grants_other_income": 0
        } for month in months}
        
        # Initialize cash outflows for each month
        self.cash_outflows = {month: {
            "material_supply_costs": 0,
            "external_services": 0,
            "premises_costs": 0,
            "leasing_rent_costs": 0,
            "personnel_costs": 0,
            "marketing_advertising": 0,
            "insurance_costs": 0,
            "investment_vat_deductible": 0,
            "investment_non_vat_deductible": 0,
            "other_fixed_costs": 0,
            "interest_financing_costs": 0,
            "taxes": 0,
            "vat": 0,
            "net_wages": 0,
            "employer_contributions": 0,
            "mandatory_staff_benefits": 0,
            "voluntary_staff_benefits": 0,
            "due_supplier_payments_1": 0,
            "due_supplier_payments_2": 0
        } for month in months}
        
        # Initialize financing activities
        self.financing_activities = {month: {
            "loan_drawdowns": 0,
            "loan_repayments": 0,
            "installment_repayments": 0,
            "dividends_private_withdrawals": 0,
            "owner_additional_investments": 0,
            "investments_deposits": 0
        } for month in months}
        
        # Initialize liquidity metrics
        self.liquidity_metrics = {
            "minimum_cash_balance_required": 0,
            "cash_buffer_days": 30,
            "credit_facility_available": 0
        }
    
    def set_initial_cash_balance(self, amount: float):
        """Set the initial cash balance."""
        self.initial_cash_balance = amount
    
    def set_cash_inflow(self, month: str, category: str, amount: float):
        """Set cash inflow for a specific month and category."""
        if month in self.cash_inflows:
            if category in self.cash_inflows[month]:
                self.cash_inflows[month][category] = amount
            else:
                raise ValueError(f"Unknown cash inflow category: {category}")
        else:
            raise ValueError(f"Invalid month for cash inflow: {month}")
    
    def set_cash_outflow(self, month: str, category: str, amount: float):
        """Set cash outflow for a specific month and category."""
        if month in self.cash_outflows:
            if category in self.cash_outflows[month]:
                self.cash_outflows[month][category] = amount
            else:
                raise ValueError(f"Unknown cash outflow category: {category}")
        else:
            raise ValueError(f"Invalid month for cash outflow: {month}")
    
    def set_financing_activity(self, month: str, category: str, amount: float):
        """Set financing activity for a specific month and category."""
        if month in self.financing_activities:
            if category in self.financing_activities[month]:
                self.financing_activities[month][category] = amount
            else:
                raise ValueError(f"Unknown financing activity category: {category}")
        else:
            raise ValueError(f"Invalid month for financing activity: {month}")
    
    def calculate_monthly_cash_position(self, month: str) -> Dict:
        """Calculate cash position for a specific month."""
        inflows = sum(self.cash_inflows[month].values())
        outflows = sum(self.cash_outflows[month].values())
        financing = sum(self.financing_activities[month].values())
        
        # Calculate net cash flow
        net_cash_flow = inflows - outflows + financing
        
        return {
            "total_inflows": inflows,
            "total_outflows": outflows,
            "financing_activities": financing,
            "net_cash_flow": net_cash_flow
        }
    
    def calculate_cash_forecast(self) -> Dict:
        """Calculate the complete cash forecast for all months."""
        forecast = {}
        running_balance = self.initial_cash_balance
        
        for month in sorted(self.cash_inflows.keys()):
            monthly_position = self.calculate_monthly_cash_position(month)
            
            # Calculate ending cash balance
            ending_balance = running_balance + monthly_position["net_cash_flow"]
            
            # Calculate if cash is sufficient for expenses
            days_covered = 0
            if monthly_position["total_outflows"] > 0:
                daily_outflow = monthly_position["total_outflows"] / 30
                days_covered = ending_balance / daily_outflow if daily_outflow > 0 else float('inf')
            
            forecast[month] = {
                "beginning_balance": running_balance,
                "total_inflows": monthly_position["total_inflows"],
                "total_outflows": monthly_position["total_outflows"],
                "financing_activities": monthly_position["financing_activities"],
                "net_cash_flow": monthly_position["net_cash_flow"],
                "ending_balance": ending_balance,
                "days_cash_coverage": days_covered,
                "cash_surplus_deficit": ending_balance - self.liquidity_metrics["minimum_cash_balance_required"]
            }
            
            # Update running balance for next month
            running_balance = ending_balance
        
        self.cash_forecast = forecast
        return self.cash_forecast
    
    def identify_cash_shortfalls(self) -> List[Tuple[str, float]]:
        """Identify months with cash shortfalls."""
        shortfalls = []
        for month, data in self.cash_forecast.items():
            if data["ending_balance"] < self.liquidity_metrics["minimum_cash_balance_required"]:
                shortfall_amount = self.liquidity_metrics["minimum_cash_balance_required"] - data["ending_balance"]
                shortfalls.append((month, shortfall_amount))
        return shortfalls
    
    def suggest_financing_options(self) -> Dict:
        """Suggest financing options based on cash forecast."""
        shortfalls = self.identify_cash_shortfalls()
        suggestions = {}
        
        if shortfalls:
            total_shortfall = sum([s[1] for s in shortfalls])
            suggestions = {
                "months_with_shortfall": [s[0] for s in shortfalls],
                "total_financing_needed": total_shortfall,
                "recommended_actions": [
                    f"Secure credit facility of at least €{total_shortfall:,.2f}",
                    "Consider delaying non-critical expenditures",
                    "Accelerate receivables collection",
                    "Negotiate extended payment terms with suppliers"
                ]
            }
        else:
            suggestions = {
                "months_with_shortfall": [],
                "total_financing_needed": 0,
                "recommended_actions": [
                    "Cash position is healthy",
                    "Consider investing excess cash",
                    "Maintain current operational pace"
                ]
            }
        
        return suggestions
    
    def generate_cash_budget_report(self) -> Dict:
        """Generate a comprehensive cash budget report."""
        forecast = self.calculate_cash_forecast()
        
        return {
            "company_name": self.company_name,
            "initial_cash_balance": self.initial_cash_balance,
            "cash_inflows": self.cash_inflows,
            "cash_outflows": self.cash_outflows,
            "financing_activities": self.financing_activities,
            "cash_forecast": forecast,
            "cash_shortfalls": self.identify_cash_shortfalls(),
            "financing_suggestions": self.suggest_financing_options(),
            "liquidity_metrics": self.liquidity_metrics
        }
    
    def save_to_json(self, filepath: str):
        """Save the cash budget to a JSON file."""
        report = self.generate_cash_budget_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a cash budget from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.initial_cash_balance = data.get("initial_cash_balance", self.initial_cash_balance)
        self.cash_inflows = data.get("cash_inflows", self.cash_inflows)
        self.cash_outflows = data.get("cash_outflows", self.cash_outflows)
        self.financing_activities = data.get("financing_activities", self.financing_activities)


def create_sample_budget() -> CashBudget:
    """Create a sample cash budget with example data."""
    budget = CashBudget(company_name="Sample Cash Budget Oy", start_date="2026-01-01")
    
    # Set initial cash balance
    budget.set_initial_cash_balance(50000)
    
    # Set example cash inflows for first few months
    months = list(budget.cash_inflows.keys())
    for i, month in enumerate(months):
        # Gradually increasing sales revenue
        sales_revenue = 20000 + (i * 2000)
        budget.set_cash_inflow(month, "sales_revenue", sales_revenue)
        budget.set_cash_inflow(month, "sales_receivables", sales_revenue * 0.3)  # 30% from receivables
        budget.set_cash_inflow(month, "available_cash_reserves", 5000 if i == 0 else 0)  # Only in first month
        budget.set_cash_inflow(month, "grants_other_income", 2000 if i % 4 == 0 else 0)  # Quarterly grants
    
    # Set example cash outflows
    for month in months:
        budget.set_cash_outflow(month, "material_supply_costs", 8000)
        budget.set_cash_outflow(month, "external_services", 3000)
        budget.set_cash_outflow(month, "premises_costs", 2500)
        budget.set_cash_outflow(month, "leasing_rent_costs", 2000)
        budget.set_cash_outflow(month, "personnel_costs", 15000)
        budget.set_cash_outflow(month, "marketing_advertising", 1500)
        budget.set_cash_outflow(month, "insurance_costs", 800)
        budget.set_cash_outflow(month, "other_fixed_costs", 1200)
        budget.set_cash_outflow(month, "interest_financing_costs", 500)
        budget.set_cash_outflow(month, "taxes", 2000)
        budget.set_cash_outflow(month, "vat", 1000)
        budget.set_cash_outflow(month, "net_wages", 10000)
        budget.set_cash_outflow(month, "employer_contributions", 3000)
        budget.set_cash_outflow(month, "mandatory_staff_benefits", 1000)
        budget.set_cash_outflow(month, "due_supplier_payments_1", 5000)
        budget.set_cash_outflow(month, "due_supplier_payments_2", 3000)
    
    # Set example financing activities
    for i, month in enumerate(months):
        # Take a loan in the first month with shortfalls
        if i == 0:
            budget.set_financing_activity(month, "loan_drawdowns", 30000)
        elif i == 5:  # Repay loan in month 6
            budget.set_financing_activity(month, "loan_repayments", 5000)
        elif i == 11:  # Owner investment at year end
            budget.set_financing_activity(month, "owner_additional_investments", 10000)
    
    # Set liquidity metrics
    budget.liquidity_metrics["minimum_cash_balance_required"] = 10000
    budget.liquidity_metrics["cash_buffer_days"] = 45
    budget.liquidity_metrics["credit_facility_available"] = 50000
    
    return budget


if __name__ == "__main__":
    # Example usage
    print("YT23 Kassabudjetti Lapua - Cash Budget Planning Tool")
    print("=" * 60)
    
    # Create a sample cash budget
    sample_budget = create_sample_budget()
    
    # Generate and display the cash budget report
    report = sample_budget.generate_cash_budget_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Initial Cash Balance: €{report['initial_cash_balance']:,.2f}")
    
    print(f"\nCash Forecast Summary:")
    for month, data in list(report['cash_forecast'].items())[:3]:  # Show first 3 months
        print(f"  {month}: Ending Balance €{data['ending_balance']:,.2f}, "
              f"Net Cash Flow €{data['net_cash_flow']:,.2f}")
    
    print(f"\nCash Shortfalls:")
    shortfalls = report['cash_shortfalls']
    if shortfalls:
        for month, amount in shortfalls[:3]:  # Show first 3 shortfalls
            print(f"  {month}: €{amount:,.2f}")
    else:
        print("  No cash shortfalls identified.")
    
    print(f"\nFinancing Suggestions:")
    suggestions = report['financing_suggestions']
    for action in suggestions['recommended_actions'][:3]:  # Show first 3 actions
        print(f"  - {action}")
    
    # Save the report to a JSON file
    sample_budget.save_to_json("sample_cash_budget.json")
    print("\nCash budget saved to 'sample_cash_budget.json'")