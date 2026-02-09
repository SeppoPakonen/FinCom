"""
Python implementation of YT24_Yrityksen_arvonmaarityslaskuri company valuation calculator.

This module provides programmatic access to the company valuation functionality
originally implemented in the YT24_Yrityksen_arvonmaarityslaskuri.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class CompanyValuationCalculator:
    """
    A class representing a company valuation calculator based on the 
    YT24_Yrityksen_arvonmaarityslaskuri template.
    This calculator helps entrepreneurs and business owners determine the value 
    of their company using various valuation methods and financial metrics.
    """
    
    def __init__(self, company_name: str = "Valuation Company"):
        self.company_name = company_name
        self.financial_data = {}  # Historical financial data
        self.adjustments = {}  # Adjustments to financial data
        self.valuation_methods = {}  # Different valuation methods
        self.market_multiples = {}  # Market multiples for comparison
        self.dcf_parameters = {}  # Parameters for discounted cash flow analysis
        self.asset_based_values = {}  # Values for asset-based valuation
        self.comparable_companies = []  # Comparable companies for analysis
        self.valuation_results = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the valuation calculator with default values."""
        # Historical financial data (last 3 fiscal years)
        self.financial_data = {
            "year_1": {  # Most recent year
                "revenue": 0,
                "adjusted_revenue": 0,
                "other_income": 0,
                "adjusted_other_income": 0,
                "total_income": 0,
                "adjusted_total_income": 0,
                "materials_costs": 0,
                "outsourced_services": 0,
                "personnel_costs": 0,
                "other_operating_expenses": 0,
                "operating_profit": 0,
                "adjusted_operating_profit": 0,
                "net_profit": 0,
                "adjusted_net_profit": 0,
                "total_assets": 0,
                "adjusted_total_assets": 0,
                "liabilities": 0,
                "adjusted_liabilities": 0,
                "net_assets": 0,
                "adjusted_net_assets": 0
            },
            "year_2": {  # Previous year
                "revenue": 0,
                "adjusted_revenue": 0,
                "other_income": 0,
                "adjusted_other_income": 0,
                "total_income": 0,
                "adjusted_total_income": 0,
                "materials_costs": 0,
                "outsourced_services": 0,
                "personnel_costs": 0,
                "other_operating_expenses": 0,
                "operating_profit": 0,
                "adjusted_operating_profit": 0,
                "net_profit": 0,
                "adjusted_net_profit": 0,
                "total_assets": 0,
                "adjusted_total_assets": 0,
                "liabilities": 0,
                "adjusted_liabilities": 0,
                "net_assets": 0,
                "adjusted_net_assets": 0
            },
            "year_3": {  # Two years ago
                "revenue": 0,
                "adjusted_revenue": 0,
                "other_income": 0,
                "adjusted_other_income": 0,
                "total_income": 0,
                "adjusted_total_income": 0,
                "materials_costs": 0,
                "outsourced_services": 0,
                "personnel_costs": 0,
                "other_operating_expenses": 0,
                "operating_profit": 0,
                "adjusted_operating_profit": 0,
                "net_profit": 0,
                "adjusted_net_profit": 0,
                "total_assets": 0,
                "adjusted_total_assets": 0,
                "liabilities": 0,
                "adjusted_liabilities": 0,
                "net_assets": 0,
                "adjusted_net_assets": 0
            }
        }
        
        # Adjustments to normalize financials
        self.adjustments = {
            "non_recurring_items": 0,
            "owner_compensation_adjustment": 0,
            "related_party_transactions": 0,
            "non_market_rent_adjustment": 0,
            "extraordinary_expenses": 0
        }
        
        # Valuation methods weights
        self.valuation_methods = {
            "asset_based": 0.25,
            "earnings_based": 0.35,
            "market_comparables": 0.25,
            "discounted_cash_flow": 0.15
        }
        
        # Market multiples
        self.market_multiples = {
            "price_to_earnings": 0,
            "ev_to_ebitda": 0,
            "price_to_sales": 0,
            "price_to_book": 0
        }
        
        # DCF parameters
        self.dcf_parameters = {
            "discount_rate": 0.10,  # 10%
            "projection_years": 5,
            "terminal_growth_rate": 0.02  # 2%
        }
        
        # Asset-based values
        self.asset_based_values = {
            "tangible_assets": 0,
            "intangible_assets": 0,
            "total_asset_value": 0,
            "liabilities_to_deduct": 0,
            "net_asset_value": 0
        }
    
    def set_financial_data(self, year_key: str, category: str, value: float):
        """Set financial data for a specific year and category."""
        if year_key in self.financial_data:
            if category in self.financial_data[year_key]:
                self.financial_data[year_key][category] = value
            else:
                raise ValueError(f"Unknown financial category: {category}")
        else:
            raise ValueError(f"Invalid year key: {year_key}")
    
    def set_adjustment(self, category: str, value: float):
        """Set an adjustment value."""
        if category in self.adjustments:
            self.adjustments[category] = value
        else:
            raise ValueError(f"Unknown adjustment category: {category}")
    
    def calculate_adjusted_financials(self):
        """Apply adjustments to financial data."""
        for year_key in self.financial_data:
            year_data = self.financial_data[year_key]
            
            # Apply adjustments to revenue
            year_data["adjusted_revenue"] = year_data["revenue"] + self.adjustments["non_recurring_items"]
            
            # Apply adjustments to other income
            year_data["adjusted_other_income"] = year_data["other_income"] + self.adjustments["extraordinary_expenses"]
            
            # Calculate adjusted total income
            year_data["adjusted_total_income"] = year_data["adjusted_revenue"] + year_data["adjusted_other_income"]
            
            # Apply adjustments to operating expenses
            adjusted_personnel_costs = year_data["personnel_costs"] + self.adjustments["owner_compensation_adjustment"]
            
            # Calculate adjusted operating profit
            total_adjusted_expenses = (
                year_data["materials_costs"] + 
                year_data["outsourced_services"] + 
                adjusted_personnel_costs + 
                year_data["other_operating_expenses"] + 
                self.adjustments["non_market_rent_adjustment"]
            )
            year_data["adjusted_operating_profit"] = year_data["adjusted_total_income"] - total_adjusted_expenses
            
            # Calculate adjusted net profit
            year_data["adjusted_net_profit"] = year_data["adjusted_operating_profit"]
            
            # Apply adjustments to assets and liabilities
            year_data["adjusted_total_assets"] = year_data["total_assets"]
            year_data["adjusted_liabilities"] = year_data["liabilities"] + self.adjustments["related_party_transactions"]
            year_data["adjusted_net_assets"] = year_data["adjusted_total_assets"] - year_data["adjusted_liabilities"]
    
    def calculate_asset_based_valuation(self) -> float:
        """Calculate valuation using asset-based approach."""
        # Calculate asset values based on the latest year's adjusted data
        latest_year = "year_1"
        total_assets = self.financial_data[latest_year]["adjusted_total_assets"]
        liabilities = self.financial_data[latest_year]["adjusted_liabilities"]
        
        # Calculate net asset value
        net_asset_value = total_assets - liabilities
        
        # Store for later use
        self.asset_based_values = {
            "tangible_assets": total_assets * 0.7,  # Assume 70% tangible
            "intangible_assets": total_assets * 0.3,  # Assume 30% intangible
            "total_asset_value": total_assets,
            "liabilities_to_deduct": liabilities,
            "net_asset_value": net_asset_value
        }
        
        return net_asset_value
    
    def calculate_earnings_based_valuation(self) -> float:
        """Calculate valuation using earnings-based approach."""
        # Use the latest year's adjusted net profit
        latest_year = "year_1"
        net_profit = self.financial_data[latest_year]["adjusted_net_profit"]
        
        # Apply a multiplier based on industry standards
        # For simplicity, using a fixed multiplier; in practice, this would vary by industry
        multiplier = 5.0  # Typical for many industries
        
        return net_profit * multiplier
    
    def calculate_market_comparables_valuation(self) -> float:
        """Calculate valuation using market comparables approach."""
        # Use the latest year's adjusted EBITDA
        latest_year = "year_1"
        ebitda = self.financial_data[latest_year]["adjusted_operating_profit"]
        
        # Apply market multiple
        ev_to_ebitda_multiple = self.market_multiples["ev_to_ebitda"]
        
        return ebitda * ev_to_ebitda_multiple if ev_to_ebitda_multiple > 0 else ebitda * 6.0  # Default multiple
    
    def calculate_discounted_cash_flow_valuation(self) -> float:
        """Calculate valuation using discounted cash flow approach."""
        # Get the latest year's adjusted free cash flow
        latest_year = "year_1"
        free_cash_flow = self.financial_data[latest_year]["adjusted_net_profit"]  # Simplified as proxy for FCF
        
        discount_rate = self.dcf_parameters["discount_rate"]
        projection_years = self.dcf_parameters["projection_years"]
        terminal_growth_rate = self.dcf_parameters["terminal_growth_rate"]
        
        # Project cash flows for the next few years (assuming steady growth)
        projected_flows = []
        growth_rate = 0.05  # 5% annual growth
        
        for year in range(1, projection_years + 1):
            projected_flow = free_cash_flow * (1 + growth_rate) ** year
            present_value = projected_flow / (1 + discount_rate) ** year
            projected_flows.append(present_value)
        
        # Calculate terminal value
        final_projected_flow = free_cash_flow * (1 + growth_rate) ** projection_years
        terminal_value = (final_projected_flow * (1 + terminal_growth_rate)) / (discount_rate - terminal_growth_rate)
        present_terminal_value = terminal_value / (1 + discount_rate) ** projection_years
        
        # Total DCF value
        dcf_value = sum(projected_flows) + present_terminal_value
        
        return dcf_value
    
    def calculate_weighted_valuation(self) -> Dict:
        """Calculate valuation using weighted average of all methods."""
        asset_based_value = self.calculate_asset_based_valuation()
        earnings_based_value = self.calculate_earnings_based_valuation()
        market_comparables_value = self.calculate_market_comparables_valuation()
        dcf_value = self.calculate_discounted_cash_flow_valuation()
        
        # Apply weights to each method
        weights = self.valuation_methods
        weighted_value = (
            asset_based_value * weights["asset_based"] +
            earnings_based_value * weights["earnings_based"] +
            market_comparables_value * weights["market_comparables"] +
            dcf_value * weights["discounted_cash_flow"]
        )
        
        self.valuation_results = {
            "asset_based": {
                "value": asset_based_value,
                "weight": weights["asset_based"],
                "weighted_value": asset_based_value * weights["asset_based"]
            },
            "earnings_based": {
                "value": earnings_based_value,
                "weight": weights["earnings_based"],
                "weighted_value": earnings_based_value * weights["earnings_based"]
            },
            "market_comparables": {
                "value": market_comparables_value,
                "weight": weights["market_comparables"],
                "weighted_value": market_comparables_value * weights["market_comparables"]
            },
            "discounted_cash_flow": {
                "value": dcf_value,
                "weight": weights["discounted_cash_flow"],
                "weighted_value": dcf_value * weights["discounted_cash_flow"]
            },
            "final_valuation": weighted_value,
            "valuation_range": {
                "low": min(asset_based_value, earnings_based_value, market_comparables_value, dcf_value),
                "high": max(asset_based_value, earnings_based_value, market_comparables_value, dcf_value)
            }
        }
        
        return self.valuation_results
    
    def generate_valuation_report(self) -> Dict:
        """Generate a comprehensive company valuation report."""
        # First calculate adjusted financials
        self.calculate_adjusted_financials()
        
        # Then calculate the weighted valuation
        valuation_results = self.calculate_weighted_valuation()
        
        return {
            "company_name": self.company_name,
            "financial_data": self.financial_data,
            "adjustments": self.adjustments,
            "valuation_methods": self.valuation_methods,
            "market_multiples": self.market_multiples,
            "dcf_parameters": self.dcf_parameters,
            "asset_based_values": self.asset_based_values,
            "valuation_results": valuation_results,
            "recommendations": self._generate_recommendations(valuation_results)
        }
    
    def _generate_recommendations(self, valuation_results: Dict) -> List[str]:
        """Generate recommendations based on the valuation."""
        recommendations = []
        final_valuation = valuation_results["final_valuation"]
        
        if final_valuation > 0:
            recommendations.append(f"The estimated value of the company is €{final_valuation:,.2f}")
            recommendations.append("Consider getting a professional appraisal for final valuation")
            recommendations.append("Prepare financial documentation for potential buyers/investors")
        else:
            recommendations.append("The valuation returned a negative value, indicating potential issues with the business model or financials")
            recommendations.append("Review and adjust financial projections and assumptions")
        
        # Add recommendation about valuation range
        valuation_range = valuation_results["valuation_range"]
        range_width = (valuation_range["high"] - valuation_range["low"]) / valuation_range["low"] if valuation_range["low"] != 0 else 0
        if range_width > 0.5:  # If range is more than 50% of low value
            recommendations.append("The valuation range is wide, suggesting high uncertainty. Consider additional analysis.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the valuation to a JSON file."""
        report = self.generate_valuation_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a valuation from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.financial_data = data.get("financial_data", self.financial_data)
        self.adjustments = data.get("adjustments", self.adjustments)
        self.valuation_results = data.get("valuation_results", self.valuation_results)


def create_sample_valuation() -> CompanyValuationCalculator:
    """Create a sample company valuation with example data."""
    valuation = CompanyValuationCalculator(company_name="Sample Valuation Oy")
    
    # Set example financial data for the last 3 years
    # Year 1 (most recent)
    valuation.set_financial_data("year_1", "revenue", 1000000)
    valuation.set_financial_data("year_1", "other_income", 50000)
    valuation.set_financial_data("year_1", "materials_costs", 300000)
    valuation.set_financial_data("year_1", "outsourced_services", 100000)
    valuation.set_financial_data("year_1", "personnel_costs", 400000)
    valuation.set_financial_data("year_1", "other_operating_expenses", 80000)
    valuation.set_financial_data("year_1", "total_assets", 750000)
    valuation.set_financial_data("year_1", "liabilities", 250000)
    
    # Year 2
    valuation.set_financial_data("year_2", "revenue", 900000)
    valuation.set_financial_data("year_2", "other_income", 40000)
    valuation.set_financial_data("year_2", "materials_costs", 270000)
    valuation.set_financial_data("year_2", "outsourced_services", 90000)
    valuation.set_financial_data("year_2", "personnel_costs", 360000)
    valuation.set_financial_data("year_2", "other_operating_expenses", 70000)
    valuation.set_financial_data("year_2", "total_assets", 700000)
    valuation.set_financial_data("year_2", "liabilities", 240000)
    
    # Year 3
    valuation.set_financial_data("year_3", "revenue", 800000)
    valuation.set_financial_data("year_3", "other_income", 30000)
    valuation.set_financial_data("year_3", "materials_costs", 240000)
    valuation.set_financial_data("year_3", "outsourced_services", 80000)
    valuation.set_financial_data("year_3", "personnel_costs", 320000)
    valuation.set_financial_data("year_3", "other_operating_expenses", 60000)
    valuation.set_financial_data("year_3", "total_assets", 650000)
    valuation.set_financial_data("year_3", "liabilities", 230000)
    
    # Set example adjustments
    valuation.set_adjustment("non_recurring_items", 10000)
    valuation.set_adjustment("owner_compensation_adjustment", -20000)
    valuation.set_adjustment("related_party_transactions", 5000)
    valuation.set_adjustment("non_market_rent_adjustment", -5000)
    valuation.set_adjustment("extraordinary_expenses", 3000)
    
    # Set market multiples
    valuation.market_multiples = {
        "price_to_earnings": 7.0,
        "ev_to_ebitda": 6.0,
        "price_to_sales": 2.0,
        "price_to_book": 1.5
    }
    
    # Set DCF parameters
    valuation.dcf_parameters = {
        "discount_rate": 0.08,  # 8%
        "projection_years": 5,
        "terminal_growth_rate": 0.02  # 2%
    }
    
    return valuation


if __name__ == "__main__":
    # Example usage
    print("YT24 Yrityksen Arvonmäärityslaskuri - Company Valuation Calculator")
    print("=" * 70)
    
    # Create a sample valuation
    sample_valuation = create_sample_valuation()
    
    # Generate and display the valuation report
    report = sample_valuation.generate_valuation_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Final Valuation: €{report['valuation_results']['final_valuation']:,.2f}")
    
    print(f"\nValuation Range: €{report['valuation_results']['valuation_range']['low']:,.2f} - €{report['valuation_results']['valuation_range']['high']:,.2f}")
    
    print(f"\nValuation Breakdown:")
    for method, data in report['valuation_results'].items():
        if method not in ['final_valuation', 'valuation_range']:
            print(f"  {method.replace('_', ' ').title()}: €{data['value']:,.2f} (Weight: {data['weight']})")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the report to a JSON file
    sample_valuation.save_to_json("sample_company_valuation.json")
    print("\nCompany valuation saved to 'sample_company_valuation.json'")