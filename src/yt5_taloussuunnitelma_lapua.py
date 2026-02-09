"""
Python implementation of YT5_Taloussuunnitelma_Lapua financial planning template (Version 5).

This module provides programmatic access to the financial planning functionality
originally implemented in the YT5_Taloussuunnitelma_Lapua.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class FinancialPlanYT5:
    """
    A class representing a comprehensive financial plan based on the YT5_Taloussuunnitelma_Lapua template (Version 5).
    This version includes enhanced features compared to previous versions.
    """
    
    def __init__(self, company_name: str = "YT5 Business", start_year: int = 2026):
        self.company_name = company_name
        self.start_year = start_year
        self.investment_needs = {}  # Rahoitustarve
        self.funding_plan = {}      # Rahoitussuunnitelma
        self.operating_costs = {}   # Toimintakustannukset
        self.revenue_projections = {}
        self.balance_sheet = {}
        self.profit_loss_statement = {}
        self.cash_flow = {}
        self.financial_ratios = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the financial plan with default values."""
        # Investment needs (Rahoitustarve)
        self.investment_needs = {
            "premises_and_connection_fees": 0,  # Toimitilat ja liittymismaksut
            "land_premises_shares_franchise": 0,  # Tontit, toimitilaosakkeet, franchising
            "premises_vat_0": 0,  # Toimitilat alv 0 %
            "premises_with_vat": 0,  # Toimitilat sis. alv
            "machines_equipment": 0,  # Koneet ja kalusto
            "leasing_finance": 0,  # Leasingrahoitus
            "installment_purchase": 0,  # Osamaksu
            "business_grants": 0,  # Yritystuet
            "initial_stock_insurance_fees": 0,  # Alkuvarasto, vakuusmaksut
            "initial_stock_insurance_fees_vat": 0,  # Alkuvarasto, vakuusmaksut sis. alv
            "machines_goodwill_no_vat_deduct": 0,  # Koneet, liikearvo (ei alv-vähennystä)
            "intangible_investments": 0,  # Aineettomat investoinnit
            "vat_refund": 0,  # Arvonlisäveron palautus
            "own_funding": 0,  # Oma rahoitus
            "owner_capital_investments": 0,  # Omistajien pääomasijoitukset
            "intangible_development_investments_vat_0": 0,  # Aineettomat- ja kehittämisinvest. alv 0 %
            "development_investments_with_vat": 0,  # Kehittämisinvestoinnit sis. alv
            "working_capital": 0  # Käyttöpääoma
        }
        
        # Funding plan (Rahoitussuunnitelma)
        self.funding_plan = {
            "long_term_loans": {
                "amount": 0,
                "financier": "",
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "bank": {
                "amount": 0,
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "finnvera": {
                "amount": 0,
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "leasing_finance": {
                "amount": 0,
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "installment_purchase": {
                "amount": 0,
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "business_grants": 0,
            "support_for_machines_equipment": 0,
            "other_support": 0,
            "finnvera_entrepreneur_loan": {
                "amount": 0,
                "interest_rate": 0,
                "loan_period_years": 0,
                "capital": 0
            },
            "own_funding": 0,
            "owner_capital_investments": 0
        }
        
        # Operating costs (Toimintakustannukset)
        self.operating_costs = {
            "loan_repayments_interest": {
                "principal_repayment": 0,
                "interest_portion": 0,
                "total_principal_end_period": 0
            },
            "entrepreneur_compensation_yel": {
                "monthly_salary_total": 0,
                "benefits_total_monthly": 0,
                "salary_months_count": 12
            },
            "employee_salaries_tyel": {
                "monthly_salary_total": 0,
                "benefits_total_monthly": 0,
                "salary_months_count": 12
            },
            "employee_benefits": {
                "side_costs_percentage": 35,  # 35% of salary
                "side_costs_amount": 0
            },
            "entrepreneur_pension_insurance": {
                "annual_salary_base_for_pension_calc": 0,
                "pension_contribution_percentage_used_calc": 19.03,  # Default 19.03%
                "voluntary_pension_contributions_period": 0,
                "sickness_insurance_from_salary_accident_life_insurance_employees": 0,
                "sickness_insurance_percentage": 3  # 3% of salary
            },
            "other_personnel_costs": {
                "yel_employer_unemployment_fund_contributions": 0,
                "voluntary_life_sickness_travel_insurance_employees": 0
            },
            "other_personnel_expenses": {
                "yel_employer_unemployment_fund_contributions": 0,
                "voluntary_life_sickness_travel_insurance_employees": 0
            }
        }
        
        # Revenue projections
        self.revenue_projections = {
            f"{self.start_year}": 0,
            f"{self.start_year + 1}": 0,
            f"{self.start_year + 2}": 0,
            f"{self.start_year + 3}": 0
        }
        
        # Financial ratios
        self.financial_ratios = {
            "debt_to_equity_ratio": 0,
            "current_ratio": 0,
            "return_on_assets": 0,
            "return_on_equity": 0,
            "gross_profit_margin": 0,
            "net_profit_margin": 0,
            "operating_margin": 0
        }
    
    def set_investment_need(self, category: str, amount: float):
        """Set the amount for a specific investment need category."""
        if category in self.investment_needs:
            self.investment_needs[category] = amount
        else:
            raise ValueError(f"Unknown investment need category: {category}")
    
    def set_funding_source(self, source: str, amount: float, financier: str = "", interest_rate: float = 0, 
                          loan_period_years: int = 0, capital: float = 0):
        """Set funding details for a specific source."""
        if source in self.funding_plan:
            if isinstance(self.funding_plan[source], dict):
                self.funding_plan[source].update({
                    "amount": amount,
                    "financier": financier,
                    "interest_rate": interest_rate,
                    "loan_period_years": loan_period_years,
                    "capital": capital
                })
            else:
                self.funding_plan[source] = amount
        else:
            raise ValueError(f"Unknown funding source: {source}")
    
    def calculate_total_investment_need(self) -> float:
        """Calculate the total investment need."""
        return sum(self.investment_needs.values())
    
    def calculate_total_funding_available(self) -> float:
        """Calculate the total funding available."""
        total = 0
        for key, value in self.funding_plan.items():
            if isinstance(value, dict):
                total += value.get("amount", 0)
            else:
                total += value
        return total
    
    def calculate_funding_gap(self) -> float:
        """Calculate the difference between investment need and available funding."""
        total_need = self.calculate_total_investment_need()
        total_funding = self.calculate_total_funding_available()
        return total_need - total_funding
    
    def set_operating_cost(self, category: str, subcategory: str, value: float):
        """Set an operating cost value."""
        if category in self.operating_costs:
            if subcategory in self.operating_costs[category]:
                self.operating_costs[category][subcategory] = value
            else:
                raise ValueError(f"Unknown subcategory '{subcategory}' in category '{category}'")
        else:
            raise ValueError(f"Unknown operating cost category: {category}")
    
    def calculate_annual_revenue_projections(self) -> Dict[str, float]:
        """Calculate revenue projections for multiple years."""
        # This would typically involve more complex calculations based on business model
        return self.revenue_projections
    
    def calculate_balance_sheet(self) -> Dict:
        """Calculate the balance sheet based on current inputs."""
        # Simplified balance sheet calculation
        assets = {
            "fixed_assets": sum([
                self.investment_needs["premises_and_connection_fees"],
                self.investment_needs["land_premises_shares_franchise"],
                self.investment_needs["premises_vat_0"],
                self.investment_needs["premises_with_vat"],
                self.investment_needs["machines_equipment"],
                self.investment_needs["intangible_investments"],
                self.investment_needs["intangible_development_investments_vat_0"],
                self.investment_needs["development_investments_with_vat"]
            ]),
            "current_assets": self.investment_needs["working_capital"],
        }
        
        liabilities_and_equity = {
            "long_term_liabilities": (
                self.funding_plan["long_term_loans"]["amount"] +
                self.funding_plan["bank"]["amount"] +
                self.funding_plan["finnvera"]["amount"] +
                self.funding_plan["leasing_finance"]["amount"] +
                self.funding_plan["installment_purchase"]["amount"]
            ),
            "short_term_liabilities": 0,  # Would need more detailed input
            "equity": (
                self.funding_plan["own_funding"] +
                self.funding_plan["owner_capital_investments"]
            )
        }
        
        return {
            "assets": assets,
            "liabilities_and_equity": liabilities_and_equity
        }
    
    def calculate_profit_loss_statement(self) -> Dict:
        """Calculate the profit & loss statement based on current inputs."""
        # Simplified P&L calculation
        revenue = self.calculate_annual_revenue_projections()
        
        # Calculate total operating expenses
        total_operating_costs = 0
        
        # Loan repayments and interest
        loan_interest = (
            self.funding_plan["long_term_loans"]["amount"] * self.funding_plan["long_term_loans"]["interest_rate"] / 100 +
            self.funding_plan["bank"]["amount"] * self.funding_plan["bank"]["interest_rate"] / 100 +
            self.funding_plan["finnvera"]["amount"] * self.funding_plan["finnvera"]["interest_rate"] / 100 +
            self.funding_plan["leasing_finance"]["amount"] * self.funding_plan["leasing_finance"]["interest_rate"] / 100 +
            self.funding_plan["installment_purchase"]["amount"] * self.funding_plan["installment_purchase"]["interest_rate"] / 100
        )
        
        # Entrepreneur compensation
        entrepreneur_salary = (
            self.operating_costs["entrepreneur_compensation_yel"]["monthly_salary_total"] *
            self.operating_costs["entrepreneur_compensation_yel"]["salary_months_count"]
        )
        
        # Employee salaries
        employee_salary = (
            self.operating_costs["employee_salaries_tyel"]["monthly_salary_total"] *
            self.operating_costs["employee_salaries_tyel"]["salary_months_count"]
        )
        
        # Employee benefits
        employee_benefits = (
            self.operating_costs["employee_benefits"]["side_costs_amount"] *
            self.operating_costs["employee_salaries_tyel"]["salary_months_count"]
        )
        
        # Pension and insurance costs
        pension_costs = (
            self.operating_costs["entrepreneur_pension_insurance"]["annual_salary_base_for_pension_calc"] *
            self.operating_costs["entrepreneur_pension_insurance"]["pension_contribution_percentage_used_calc"] / 100
        )
        
        # Sum up all operating costs
        total_operating_costs = (
            loan_interest +
            entrepreneur_salary +
            employee_salary +
            employee_benefits +
            pension_costs +
            self.operating_costs["entrepreneur_pension_insurance"]["voluntary_pension_contributions_period"] +
            self.operating_costs["entrepreneur_pension_insurance"]["sickness_insurance_from_salary_accident_life_insurance_employees"] +
            self.operating_costs["other_personnel_costs"]["yel_employer_unemployment_fund_contributions"] +
            self.operating_costs["other_personnel_costs"]["voluntary_life_sickness_travel_insurance_employees"] +
            self.operating_costs["other_personnel_expenses"]["yel_employer_unemployment_fund_contributions"] +
            self.operating_costs["other_personnel_expenses"]["voluntary_life_sickness_travel_insurance_employees"]
        )
        
        # Calculate profit for each year
        profit_loss = {}
        for year, rev in revenue.items():
            profit_loss[year] = {
                "revenue": rev,
                "operating_costs": total_operating_costs,
                "net_profit": rev - total_operating_costs
            }
        
        return profit_loss
    
    def calculate_cash_flow(self) -> Dict:
        """Calculate the cash flow based on current inputs."""
        # Simplified cash flow calculation
        cash_flow = {}
        
        # Get profit/loss statement
        pl_statement = self.calculate_profit_loss_statement()
        
        # For simplicity, we'll use net profit as a proxy for operating cash flow
        # In reality, this would need adjustments for non-cash items and working capital changes
        for year, data in pl_statement.items():
            cash_flow[year] = {
                "operating_cash_flow": data["net_profit"],
                "investment_cash_flow": -self.calculate_total_investment_need() / 4,  # Spread over 4 years
                "financing_cash_flow": self.calculate_total_funding_available() / 4,  # Spread over 4 years
                "net_cash_flow": data["net_profit"] - self.calculate_total_investment_need()/4 + self.calculate_total_funding_available()/4
            }
        
        return cash_flow
    
    def calculate_financial_ratios(self) -> Dict:
        """Calculate key financial ratios based on the financial statements."""
        # Get financial statements
        balance_sheet = self.calculate_balance_sheet()
        pl_statement = self.calculate_profit_loss_statement()
        
        # Calculate ratios for the first year
        first_year = list(pl_statement.keys())[0]
        current_pl = pl_statement[first_year]
        
        # Calculate assets
        total_assets = sum(balance_sheet["assets"].values())
        total_liabilities = sum(balance_sheet["liabilities_and_equity"].values()) - balance_sheet["liabilities_and_equity"]["equity"]
        total_equity = balance_sheet["liabilities_and_equity"]["equity"]
        
        # Calculate ratios
        self.financial_ratios = {
            "debt_to_equity_ratio": total_liabilities / total_equity if total_equity != 0 else 0,
            "current_ratio": balance_sheet["assets"]["current_assets"] / 10000 if 10000 != 0 else 0,  # Assuming some current liabilities
            "return_on_assets": current_pl["net_profit"] / total_assets if total_assets != 0 else 0,
            "return_on_equity": current_pl["net_profit"] / total_equity if total_equity != 0 else 0,
            "gross_profit_margin": 0,  # Would need gross profit data
            "net_profit_margin": current_pl["net_profit"] / current_pl["revenue"] if current_pl["revenue"] != 0 else 0,
            "operating_margin": current_pl["net_profit"] / current_pl["revenue"] if current_pl["revenue"] != 0 else 0
        }
        
        return self.financial_ratios
    
    def generate_financial_report(self) -> Dict:
        """Generate a comprehensive financial report."""
        return {
            "company_name": self.company_name,
            "investment_needs": self.investment_needs,
            "funding_plan": self.funding_plan,
            "total_investment_need": self.calculate_total_investment_need(),
            "total_funding_available": self.calculate_total_funding_available(),
            "funding_gap": self.calculate_funding_gap(),
            "balance_sheet": self.calculate_balance_sheet(),
            "profit_loss_statement": self.calculate_profit_loss_statement(),
            "cash_flow": self.calculate_cash_flow(),
            "financial_ratios": self.calculate_financial_ratios()
        }
    
    def save_to_json(self, filepath: str):
        """Save the financial plan to a JSON file."""
        report = self.generate_financial_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    def load_from_json(self, filepath: str):
        """Load a financial plan from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.investment_needs = data.get("investment_needs", self.investment_needs)
        self.funding_plan = data.get("funding_plan", self.funding_plan)


def create_sample_plan() -> FinancialPlanYT5:
    """Create a sample financial plan with example data for YT5."""
    plan = FinancialPlanYT5(company_name="YT5 Sample Business", start_year=2026)
    
    # Set some example investment needs
    plan.set_investment_need("premises_and_connection_fees", 15000)
    plan.set_investment_need("machines_equipment", 20000)
    plan.set_investment_need("working_capital", 8000)
    
    # Set some example funding
    plan.set_funding_source("long_term_loans", 12000, "Local Bank", 3.0, 5, 7000)
    plan.set_funding_source("own_funding", 18000)
    plan.set_funding_source("business_grants", 8000)
    
    # Set revenue projections
    plan.revenue_projections = {
        "2026": 60000,
        "2027": 70000,
        "2028": 80000,
        "2029": 90000
    }
    
    # Set operating costs
    plan.set_operating_cost("entrepreneur_compensation_yel", "monthly_salary_total", 3500)
    plan.set_operating_cost("employee_salaries_tyel", "monthly_salary_total", 2500)
    
    return plan


if __name__ == "__main__":
    # Example usage
    print("YT5 Taloussuunnitelma Lapua - Financial Planning Tool (Version 5)")
    print("=" * 70)
    
    # Create a sample financial plan
    sample_plan = create_sample_plan()
    
    # Generate and display the financial report
    report = sample_plan.generate_financial_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Total Investment Need: €{report['total_investment_need']:,.2f}")
    print(f"Total Funding Available: €{report['total_funding_available']:,.2f}")
    print(f"Funding Gap: €{report['funding_gap']:,.2f}")
    
    print("\nRevenue Projections:")
    pl_statement = report['profit_loss_statement']
    for year, data in pl_statement.items():
        print(f"  {year}: Revenue €{data['revenue']:,.2f}, Net Profit €{data['net_profit']:,.2f}")
    
    print("\nFinancial Ratios:")
    ratios = report['financial_ratios']
    for ratio_name, value in ratios.items():
        print(f"  {ratio_name}: {value:.2f}")
    
    # Save the report to a JSON file
    sample_plan.save_to_json("sample_financial_plan_yt5.json")
    print("\nFinancial plan saved to 'sample_financial_plan_yt5.json'")