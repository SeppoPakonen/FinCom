"""
Python implementation of YT6_Aloittavan_yrityksen_tulossuunnitelma_Lapua startup profit planning template.

This module provides programmatic access to the startup profit planning functionality
originally implemented in the YT6_Aloittavan_yrityksen_tulossuunnitelma_Lapua.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class StartupProfitPlan:
    """
    A class representing a startup profit plan based on the YT6_Aloittavan_yrityksen_tulossuunnitelma_Lapua template.
    This template is specifically designed for startups in Lapua, helping new entrepreneurs forecast 
    revenues, expenses, and profitability during the early stages of their business operations.
    """
    
    def __init__(self, company_name: str = "Startup Business", start_year: int = 2026):
        self.company_name = company_name
        self.start_year = start_year
        self.startup_costs = {}  # Initial startup costs
        self.revenue_projections = {}  # Monthly/quarterly revenue projections
        self.expense_projections = {}  # Monthly/quarterly expense projections
        self.break_even_analysis = {}  # Break-even analysis
        self.unit_economics = {}  # Unit economics for early-stage business
        self.funding_requirements = {}  # Funding requirements for startups
        self.profit_loss_statement = {}
        self.cash_flow = {}
        self.balance_sheet = {}
        self.financial_ratios = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the startup profit plan with default values."""
        # Startup costs
        self.startup_costs = {
            "initial_investment": 0,
            "legal_setup_costs": 0,
            "equipment_tools": 0,
            "initial_inventory": 0,
            "marketing_promotion": 0,
            "office_setup": 0,
            "licensing_permits": 0,
            "consulting_services": 0,
            "working_capital": 0
        }
        
        # Revenue projections by month for first 2 years
        months = [f"{self.start_year}-{'{:02d}'.format(i)}" for i in range(1, 13)] + \
                 [f"{self.start_year + 1}-{'{:02d}'.format(i)}" for i in range(1, 13)]
        self.revenue_projections = {month: 0 for month in months}
        
        # Expense projections by month for first 2 years
        self.expense_projections = {month: {
            "fixed_costs": 0,
            "variable_costs": 0,
            "personnel_costs": 0,
            "marketing_costs": 0,
            "operational_costs": 0
        } for month in months}
        
        # Break-even analysis
        self.break_even_analysis = {
            "break_even_month": None,
            "break_even_revenue": 0,
            "break_even_customers": 0
        }
        
        # Unit economics
        self.unit_economics = {
            "customer_acquisition_cost": 0,
            "average_revenue_per_user": 0,
            "lifetime_value": 0,
            "payback_period_months": 0
        }
        
        # Funding requirements
        self.funding_requirements = {
            "total_startup_funding_needed": 0,
            "funding_gap": 0,
            "funding_sources": {
                "own_investment": 0,
                "loans": 0,
                "grants": 0,
                "investors": 0
            }
        }
        
        # Financial ratios specific to startups
        self.financial_ratios = {
            "burn_rate_per_month": 0,
            "months_of_runway": 0,
            "revenue_growth_rate": 0,
            "customer_acquisition_efficiency": 0
        }
    
    def set_startup_cost(self, category: str, amount: float):
        """Set the amount for a specific startup cost category."""
        if category in self.startup_costs:
            self.startup_costs[category] = amount
        else:
            raise ValueError(f"Unknown startup cost category: {category}")
    
    def set_revenue_projection(self, month: str, amount: float):
        """Set revenue projection for a specific month."""
        if month in self.revenue_projections:
            self.revenue_projections[month] = amount
        else:
            raise ValueError(f"Invalid month for revenue projection: {month}")
    
    def set_expense_projection(self, month: str, category: str, amount: float):
        """Set expense projection for a specific month and category."""
        if month in self.expense_projections:
            if category in self.expense_projections[month]:
                self.expense_projections[month][category] = amount
            else:
                raise ValueError(f"Unknown expense category: {category}")
        else:
            raise ValueError(f"Invalid month for expense projection: {month}")
    
    def calculate_total_startup_costs(self) -> float:
        """Calculate the total startup costs."""
        return sum(self.startup_costs.values())
    
    def calculate_monthly_net_income(self, month: str) -> float:
        """Calculate net income for a specific month."""
        revenue = self.revenue_projections.get(month, 0)
        expenses = sum(self.expense_projections.get(month, {}).values())
        return revenue - expenses
    
    def calculate_cumulative_net_income(self) -> Dict[str, float]:
        """Calculate cumulative net income over time."""
        cumulative = {}
        running_total = 0
        for month in self.revenue_projections.keys():
            monthly_net = self.calculate_monthly_net_income(month)
            running_total += monthly_net
            cumulative[month] = running_total
        return cumulative
    
    def calculate_break_even_point(self) -> Dict:
        """Calculate the break-even point for the startup."""
        cumulative_income = self.calculate_cumulative_net_income()
        
        # Find the first month where cumulative income becomes positive
        break_even_month = None
        for month, income in cumulative_income.items():
            if income >= 0 and break_even_month is None:
                break_even_month = month
                break
        
        # Calculate break-even revenue based on fixed and variable costs
        total_fixed_costs = sum([sum(expenses.values()) for expenses in self.expense_projections.values()])
        avg_variable_cost_ratio = 0.3  # Default assumption, could be calculated from data
        
        if break_even_month:
            months_to_break_even = list(self.revenue_projections.keys()).index(break_even_month) + 1
            avg_monthly_revenue = sum(list(self.revenue_projections.values())[:months_to_break_even]) / months_to_break_even
            break_even_revenue = avg_monthly_revenue
            
            self.break_even_analysis = {
                "break_even_month": break_even_month,
                "break_even_revenue": break_even_revenue,
                "break_even_customers": break_even_revenue / 100  # Assumption: avg order value of 100
            }
        
        return self.break_even_analysis
    
    def calculate_unit_economics(self) -> Dict:
        """Calculate unit economics for the startup."""
        # Calculate customer acquisition cost (CAC)
        total_marketing_spend = sum([exp["marketing_costs"] for exp in self.expense_projections.values()])
        estimated_customers = sum(self.revenue_projections.values()) / 100  # Assumption: avg order value of 100
        cac = total_marketing_spend / estimated_customers if estimated_customers > 0 else 0
        
        # Calculate average revenue per user (ARPU)
        arpu = sum(self.revenue_projections.values()) / estimated_customers if estimated_customers > 0 else 0
        
        # Calculate lifetime value (LTV) - simplified as 3x ARPU
        ltv = 3 * arpu
        
        # Calculate payback period
        monthly_net_income = [self.calculate_monthly_net_income(m) for m in self.revenue_projections.keys()]
        cumulative_investment = self.calculate_total_startup_costs()
        payback_months = 0
        running_income = 0
        
        for month_idx, income in enumerate(monthly_net_income):
            running_income += income
            if running_income >= cumulative_investment:
                payback_months = month_idx + 1
                break
        
        self.unit_economics = {
            "customer_acquisition_cost": cac,
            "average_revenue_per_user": arpu,
            "lifetime_value": ltv,
            "payback_period_months": payback_months
        }
        
        return self.unit_economics
    
    def calculate_funding_requirements(self) -> Dict:
        """Calculate funding requirements for the startup."""
        total_startup_funding = self.calculate_total_startup_costs()
        
        # Calculate burn rate (negative cash flow in early months)
        monthly_net_incomes = [self.calculate_monthly_net_income(m) for m in self.revenue_projections.keys()]
        negative_months = [income for income in monthly_net_incomes if income < 0]
        avg_burn_rate = abs(sum(negative_months) / len(negative_months)) if negative_months else 0
        
        # Calculate runway based on current funding
        current_funding = self.funding_requirements["funding_sources"]["own_investment"]
        months_of_runway = current_funding / avg_burn_rate if avg_burn_rate > 0 else float('inf')
        
        # Calculate funding gap
        funding_gap = max(0, total_startup_funding - current_funding)
        
        self.funding_requirements = {
            "total_startup_funding_needed": total_startup_funding,
            "funding_gap": funding_gap,
            "funding_sources": self.funding_requirements["funding_sources"],
            "avg_burn_rate_per_month": avg_burn_rate,
            "months_of_runway": months_of_runway
        }
        
        return self.funding_requirements
    
    def calculate_financial_ratios(self) -> Dict:
        """Calculate key financial ratios specific to startups."""
        # Calculate burn rate
        monthly_net_incomes = [self.calculate_monthly_net_income(m) for m in self.revenue_projections.keys()]
        negative_months = [income for income in monthly_net_incomes if income < 0]
        burn_rate = abs(sum(negative_months) / len(negative_months)) if negative_months else 0
        
        # Calculate months of runway with current funding
        current_funding = self.funding_requirements["funding_sources"]["own_investment"]
        months_of_runway = current_funding / burn_rate if burn_rate > 0 else float('inf')
        
        # Calculate revenue growth rate (simplified)
        first_half_revenue = sum(list(self.revenue_projections.values())[:6])
        second_half_revenue = sum(list(self.revenue_projections.values())[6:12])
        revenue_growth_rate = ((second_half_revenue - first_half_revenue) / first_half_revenue) if first_half_revenue != 0 else 0
        
        # Calculate customer acquisition efficiency
        cac = self.unit_economics.get("customer_acquisition_cost", 1)
        ltv = self.unit_economics.get("lifetime_value", 1)
        customer_acquisition_efficiency = ltv / cac if cac != 0 else 0
        
        self.financial_ratios = {
            "burn_rate_per_month": burn_rate,
            "months_of_runway": months_of_runway,
            "revenue_growth_rate": revenue_growth_rate,
            "customer_acquisition_efficiency": customer_acquisition_efficiency
        }
        
        return self.financial_ratios
    
    def generate_startup_report(self) -> Dict:
        """Generate a comprehensive startup financial report."""
        return {
            "company_name": self.company_name,
            "startup_costs": self.startup_costs,
            "total_startup_costs": self.calculate_total_startup_costs(),
            "revenue_projections": self.revenue_projections,
            "expense_projections": self.expense_projections,
            "monthly_net_income": {month: self.calculate_monthly_net_income(month) 
                                   for month in self.revenue_projections.keys()},
            "cumulative_net_income": self.calculate_cumulative_net_income(),
            "break_even_analysis": self.calculate_break_even_point(),
            "unit_economics": self.calculate_unit_economics(),
            "funding_requirements": self.calculate_funding_requirements(),
            "financial_ratios": self.calculate_financial_ratios()
        }
    
    def save_to_json(self, filepath: str):
        """Save the startup profit plan to a JSON file."""
        report = self.generate_startup_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    def load_from_json(self, filepath: str):
        """Load a startup profit plan from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.startup_costs = data.get("startup_costs", self.startup_costs)
        self.revenue_projections = data.get("revenue_projections", self.revenue_projections)


def create_sample_plan() -> StartupProfitPlan:
    """Create a sample startup profit plan with example data."""
    plan = StartupProfitPlan(company_name="Sample Startup Oy", start_year=2026)
    
    # Set some example startup costs
    plan.set_startup_cost("initial_investment", 10000)
    plan.set_startup_cost("legal_setup_costs", 2000)
    plan.set_startup_cost("equipment_tools", 15000)
    plan.set_startup_cost("initial_inventory", 8000)
    plan.set_startup_cost("marketing_promotion", 5000)
    plan.set_startup_cost("office_setup", 7000)
    plan.set_startup_cost("working_capital", 12000)
    
    # Set some example revenue projections (starting low and growing)
    months = list(plan.revenue_projections.keys())
    for i, month in enumerate(months):
        # Start with low revenue and gradually increase
        base_revenue = max(0, (i - 2) * 1000)  # Start generating revenue from month 3
        plan.set_revenue_projection(month, base_revenue)
    
    # Set some example expense projections
    for month in months:
        plan.set_expense_projection(month, "fixed_costs", 3000)  # Fixed costs remain constant
        plan.set_expense_projection(month, "variable_costs", plan.revenue_projections[month] * 0.3)  # 30% of revenue
        plan.set_expense_projection(month, "personnel_costs", 2000 if plan.revenue_projections[month] > 0 else 0)  # Personnel when revenue starts
        plan.set_expense_projection(month, "marketing_costs", 1000 if plan.revenue_projections[month] > 0 else 500)  # Higher marketing initially
        plan.set_expense_projection(month, "operational_costs", 1500)  # Operational costs
    
    # Set funding sources
    plan.funding_requirements["funding_sources"]["own_investment"] = 25000
    plan.funding_requirements["funding_sources"]["grants"] = 10000
    
    return plan


if __name__ == "__main__":
    # Example usage
    print("YT6 Aloittavan Yrityksen Tulossuunnitelma Lapua - Startup Profit Planning Tool")
    print("=" * 80)
    
    # Create a sample startup profit plan
    sample_plan = create_sample_plan()
    
    # Generate and display the startup report
    report = sample_plan.generate_startup_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Total Startup Costs: €{report['total_startup_costs']:,.2f}")
    print(f"Total Funding Available: €{report['funding_requirements']['funding_sources']['own_investment'] + report['funding_requirements']['funding_sources']['grants']:,.2f}")
    print(f"Funding Gap: €{report['funding_requirements']['funding_gap']:,.2f}")
    
    print(f"\nBreak-even Analysis:")
    be_analysis = report['break_even_analysis']
    print(f"  Break-even Month: {be_analysis['break_even_month']}")
    print(f"  Break-even Revenue: €{be_analysis['break_even_revenue']:,.2f}")
    print(f"  Break-even Customers: {int(be_analysis['break_even_customers'])}")
    
    print(f"\nUnit Economics:")
    unit_econ = report['unit_economics']
    print(f"  Customer Acquisition Cost: €{unit_econ['customer_acquisition_cost']:,.2f}")
    print(f"  Average Revenue Per User: €{unit_econ['average_revenue_per_user']:,.2f}")
    print(f"  Lifetime Value: €{unit_econ['lifetime_value']:,.2f}")
    print(f"  Payback Period (months): {unit_econ['payback_period_months']}")
    
    print(f"\nFinancial Ratios:")
    ratios = report['financial_ratios']
    print(f"  Burn Rate per Month: €{ratios['burn_rate_per_month']:,.2f}")
    print(f"  Months of Runway: {ratios['months_of_runway']:.1f}")
    print(f"  Revenue Growth Rate: {ratios['revenue_growth_rate']:.2%}")
    print(f"  Customer Acquisition Efficiency (LTV/CAC): {ratios['customer_acquisition_efficiency']:.2f}")
    
    # Save the report to a JSON file
    sample_plan.save_to_json("sample_startup_profit_plan.json")
    print("\nStartup profit plan saved to 'sample_startup_profit_plan.json'")