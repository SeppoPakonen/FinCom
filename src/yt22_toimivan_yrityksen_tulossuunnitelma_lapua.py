"""
Python implementation of YT22_Toimivan_yrityksen_tulossuunnitelma_Lapua operating business profit planning template.

This module provides programmatic access to the operating business profit planning functionality
originally implemented in the YT22_Toimivan_yrityksen_tulossuunnitelma_Lapua.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class OperatingBusinessProfitPlan:
    """
    A class representing an operating business profit plan based on the 
    YT22_Toimivan_yrityksen_tulossuunnitelma_Lapua template.
    This template is specifically designed for operating businesses in Lapua, 
    helping established entrepreneurs forecast revenues, expenses, and profitability 
    for ongoing business operations.
    """
    
    def __init__(self, company_name: str = "Operating Business", start_year: int = 2027):
        self.company_name = company_name
        self.start_year = start_year
        self.investment_plan = {}  # Investment plan
        self.revenue_projections = {}  # Revenue projections based on historical trends
        self.expense_projections = {}  # Expense projections for ongoing operations
        self.performance_metrics = {}  # Performance metrics and KPIs
        self.historical_data = {}  # Historical performance data
        self.seasonal_factors = {}  # Seasonal adjustment factors
        self.benchmarking_data = {}  # Benchmarking against industry standards
        self.profit_loss_statement = {}
        self.cash_flow = {}
        self.balance_sheet = {}
        self.financial_ratios = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the operating business profit plan with default values."""
        # Investment plan
        self.investment_plan = {
            "land_areas_water_areas_connections": 0,
            "new_constructions_buildings_with_vat": 0,
            "machines_equipment": 0,
            "intangible_investments": 0,
            "working_capital": 0,
            "development_investments": 0,
            "premises_acquisition": 0,
            "other_investments": 0
        }
        
        # Revenue projections by year for 4 years
        self.revenue_projections = {
            f"{self.start_year}": 0,
            f"{self.start_year + 1}": 0,
            f"{self.start_year + 2}": 0,
            f"{self.start_year + 3}": 0
        }
        
        # Expense projections by year for 4 years
        self.expense_projections = {
            f"{self.start_year}": {
                "fixed_costs": 0,
                "variable_costs": 0,
                "personnel_costs": 0,
                "marketing_costs": 0,
                "operational_costs": 0,
                "administrative_costs": 0,
                "financial_costs": 0
            },
            f"{self.start_year + 1}": {
                "fixed_costs": 0,
                "variable_costs": 0,
                "personnel_costs": 0,
                "marketing_costs": 0,
                "operational_costs": 0,
                "administrative_costs": 0,
                "financial_costs": 0
            },
            f"{self.start_year + 2}": {
                "fixed_costs": 0,
                "variable_costs": 0,
                "personnel_costs": 0,
                "marketing_costs": 0,
                "operational_costs": 0,
                "administrative_costs": 0,
                "financial_costs": 0
            },
            f"{self.start_year + 3}": {
                "fixed_costs": 0,
                "variable_costs": 0,
                "personnel_costs": 0,
                "marketing_costs": 0,
                "operational_costs": 0,
                "administrative_costs": 0,
                "financial_costs": 0
            }
        }
        
        # Historical data (previous 3 years)
        self.historical_data = {
            f"{self.start_year - 3}": {
                "revenue": 0,
                "expenses": 0,
                "net_profit": 0,
                "assets": 0,
                "liabilities": 0
            },
            f"{self.start_year - 2}": {
                "revenue": 0,
                "expenses": 0,
                "net_profit": 0,
                "assets": 0,
                "liabilities": 0
            },
            f"{self.start_year - 1}": {
                "revenue": 0,
                "expenses": 0,
                "net_profit": 0,
                "assets": 0,
                "liabilities": 0
            }
        }
        
        # Seasonal factors (monthly)
        self.seasonal_factors = {
            "Jan": 1.0, "Feb": 1.0, "Mar": 1.0, "Apr": 1.0, "May": 1.0, "Jun": 1.0,
            "Jul": 1.0, "Aug": 1.0, "Sep": 1.0, "Oct": 1.0, "Nov": 1.0, "Dec": 1.0
        }
        
        # Performance metrics
        self.performance_metrics = {
            "revenue_growth_rate": 0.0,
            "profit_margin": 0.0,
            "return_on_assets": 0.0,
            "return_on_equity": 0.0,
            "debt_to_equity_ratio": 0.0,
            "current_ratio": 0.0
        }
        
        # Benchmarking data
        self.benchmarking_data = {
            "industry_avg_revenue_growth": 0.05,  # 5% average
            "industry_avg_profit_margin": 0.10,  # 10% average
            "industry_avg_return_on_assets": 0.08,  # 8% average
            "benchmark_company_revenue": 0,
            "benchmark_company_profit": 0
        }
    
    def set_investment_item(self, category: str, amount: float):
        """Set the amount for a specific investment category."""
        if category in self.investment_plan:
            self.investment_plan[category] = amount
        else:
            raise ValueError(f"Unknown investment category: {category}")
    
    def set_revenue_projection(self, year: str, amount: float):
        """Set revenue projection for a specific year."""
        if year in self.revenue_projections:
            self.revenue_projections[year] = amount
        else:
            raise ValueError(f"Invalid year for revenue projection: {year}")
    
    def set_expense_projection(self, year: str, category: str, amount: float):
        """Set expense projection for a specific year and category."""
        if year in self.expense_projections:
            if category in self.expense_projections[year]:
                self.expense_projections[year][category] = amount
            else:
                raise ValueError(f"Unknown expense category: {category}")
        else:
            raise ValueError(f"Invalid year for expense projection: {year}")
    
    def set_historical_data(self, year: str, metric: str, value: float):
        """Set historical data for a specific year and metric."""
        if year in self.historical_data:
            if metric in self.historical_data[year]:
                self.historical_data[year][metric] = value
            else:
                raise ValueError(f"Unknown historical metric: {metric}")
        else:
            raise ValueError(f"Invalid year for historical data: {year}")
    
    def calculate_total_investment_need(self) -> float:
        """Calculate the total investment need."""
        return sum(self.investment_plan.values())
    
    def calculate_annual_net_income(self, year: str) -> float:
        """Calculate net income for a specific year."""
        revenue = self.revenue_projections.get(year, 0)
        expenses = sum(self.expense_projections.get(year, {}).values())
        return revenue - expenses
    
    def calculate_cumulative_net_income(self) -> Dict[str, float]:
        """Calculate cumulative net income over projected years."""
        cumulative = {}
        running_total = 0
        for year in sorted(self.revenue_projections.keys()):
            annual_net = self.calculate_annual_net_income(year)
            running_total += annual_net
            cumulative[year] = running_total
        return cumulative
    
    def calculate_performance_metrics(self) -> Dict:
        """Calculate key performance metrics based on projections and historical data."""
        # Calculate revenue growth rate based on historical data
        hist_revenues = [self.historical_data[year]["revenue"] for year in sorted(self.historical_data.keys())]
        if len(hist_revenues) >= 2 and hist_revenues[-2] != 0:
            revenue_growth = (hist_revenues[-1] - hist_revenues[-2]) / hist_revenues[-2]
        else:
            revenue_growth = 0.0
        
        # Calculate average profit margin
        projected_years = list(self.revenue_projections.keys())
        total_revenue = sum([self.revenue_projections[y] for y in projected_years])
        total_expenses = sum([sum(self.expense_projections[y].values()) for y in projected_years])
        avg_profit_margin = (total_revenue - total_expenses) / total_revenue if total_revenue != 0 else 0.0
        
        # Calculate ROA and ROE based on projections
        total_assets_est = sum([self.historical_data[y]["assets"] for y in self.historical_data.keys()]) / len(self.historical_data)
        avg_net_income = sum([self.calculate_annual_net_income(y) for y in projected_years]) / len(projected_years)
        roa = avg_net_income / total_assets_est if total_assets_est != 0 else 0.0
        
        # Estimate equity based on assets and liabilities
        avg_liabilities = sum([self.historical_data[y]["liabilities"] for y in self.historical_data.keys()]) / len(self.historical_data)
        avg_equity = total_assets_est - avg_liabilities
        roe = avg_net_income / avg_equity if avg_equity != 0 else 0.0
        
        # Calculate debt-to-equity ratio
        debt_to_equity = avg_liabilities / avg_equity if avg_equity != 0 else 0.0
        
        # Calculate current ratio (simplified)
        current_ratio = 1.5  # Placeholder value; would need more detailed data
        
        self.performance_metrics = {
            "revenue_growth_rate": revenue_growth,
            "profit_margin": avg_profit_margin,
            "return_on_assets": roa,
            "return_on_equity": roe,
            "debt_to_equity_ratio": debt_to_equity,
            "current_ratio": current_ratio
        }
        
        return self.performance_metrics
    
    def calculate_benchmarking_comparison(self) -> Dict:
        """Calculate benchmarking comparison against industry standards."""
        perf_metrics = self.calculate_performance_metrics()
        
        # Compare our metrics to industry averages
        revenue_growth_diff = perf_metrics["revenue_growth_rate"] - self.benchmarking_data["industry_avg_revenue_growth"]
        profit_margin_diff = perf_metrics["profit_margin"] - self.benchmarking_data["industry_avg_profit_margin"]
        roa_diff = perf_metrics["return_on_assets"] - self.benchmarking_data["industry_avg_return_on_assets"]
        
        self.benchmarking_data.update({
            "revenue_growth_vs_industry": revenue_growth_diff,
            "profit_margin_vs_industry": profit_margin_diff,
            "roa_vs_industry": roa_diff,
            "performance_rating": self._calculate_performance_rating(
                revenue_growth_diff, profit_margin_diff, roa_diff
            )
        })
        
        return self.benchmarking_data
    
    def _calculate_performance_rating(self, revenue_growth_diff, profit_margin_diff, roa_diff) -> str:
        """Calculate a simple performance rating based on differences from industry."""
        score = 0
        if revenue_growth_diff > 0: score += 1
        if profit_margin_diff > 0: score += 1
        if roa_diff > 0: score += 1
        
        if score >= 3:
            return "Excellent"
        elif score >= 2:
            return "Good"
        elif score >= 1:
            return "Average"
        else:
            return "Below Average"
    
    def calculate_seasonal_adjusted_revenue(self) -> Dict[str, Dict[str, float]]:
        """Calculate seasonal-adjusted monthly revenue projections."""
        result = {}
        for year, revenue in self.revenue_projections.items():
            result[year] = {}
            monthly_base = revenue / 12
            for month, factor in self.seasonal_factors.items():
                result[year][month] = monthly_base * factor
        return result
    
    def generate_operating_business_report(self) -> Dict:
        """Generate a comprehensive operating business financial report."""
        return {
            "company_name": self.company_name,
            "investment_plan": self.investment_plan,
            "total_investment_need": self.calculate_total_investment_need(),
            "revenue_projections": self.revenue_projections,
            "expense_projections": self.expense_projections,
            "historical_data": self.historical_data,
            "annual_net_income": {year: self.calculate_annual_net_income(year) 
                                  for year in self.revenue_projections.keys()},
            "cumulative_net_income": self.calculate_cumulative_net_income(),
            "seasonal_revenue_projections": self.calculate_seasonal_adjusted_revenue(),
            "performance_metrics": self.calculate_performance_metrics(),
            "benchmarking_comparison": self.calculate_benchmarking_comparison()
        }
    
    def save_to_json(self, filepath: str):
        """Save the operating business profit plan to a JSON file."""
        report = self.generate_operating_business_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
    
    def load_from_json(self, filepath: str):
        """Load an operating business profit plan from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.investment_plan = data.get("investment_plan", self.investment_plan)
        self.revenue_projections = data.get("revenue_projections", self.revenue_projections)
        self.expense_projections = data.get("expense_projections", self.expense_projections)


def create_sample_plan() -> OperatingBusinessProfitPlan:
    """Create a sample operating business profit plan with example data."""
    plan = OperatingBusinessProfitPlan(company_name="Sample Operating Business Oy", start_year=2027)
    
    # Set some example investment plan items
    plan.set_investment_item("land_areas_water_areas_connections", 50000)
    plan.set_investment_item("machines_equipment", 100000)
    plan.set_investment_item("working_capital", 30000)
    plan.set_investment_item("development_investments", 25000)
    
    # Set some example historical data
    plan.set_historical_data("2024", "revenue", 500000)
    plan.set_historical_data("2024", "expenses", 400000)
    plan.set_historical_data("2024", "net_profit", 100000)
    plan.set_historical_data("2024", "assets", 750000)
    plan.set_historical_data("2024", "liabilities", 300000)
    
    plan.set_historical_data("2025", "revenue", 550000)
    plan.set_historical_data("2025", "expenses", 430000)
    plan.set_historical_data("2025", "net_profit", 120000)
    plan.set_historical_data("2025", "assets", 780000)
    plan.set_historical_data("2025", "liabilities", 280000)
    
    plan.set_historical_data("2026", "revenue", 600000)
    plan.set_historical_data("2026", "expenses", 450000)
    plan.set_historical_data("2026", "net_profit", 150000)
    plan.set_historical_data("2026", "assets", 800000)
    plan.set_historical_data("2026", "liabilities", 250000)
    
    # Set revenue projections (growing based on historical trend)
    plan.set_revenue_projection("2027", 650000)
    plan.set_revenue_projection("2028", 700000)
    plan.set_revenue_projection("2029", 750000)
    plan.set_revenue_projection("2030", 800000)
    
    # Set expense projections (growing but at slower rate)
    for year in ["2027", "2028", "2029", "2030"]:
        plan.set_expense_projection(year, "fixed_costs", 200000)
        plan.set_expense_projection(year, "variable_costs", plan.revenue_projections[year] * 0.35)  # 35% of revenue
        plan.set_expense_projection(year, "personnel_costs", 180000)
        plan.set_expense_projection(year, "marketing_costs", 30000)
        plan.set_expense_projection(year, "operational_costs", 40000)
        plan.set_expense_projection(year, "administrative_costs", 25000)
        plan.set_expense_projection(year, "financial_costs", 10000)
    
    # Set seasonal factors (some months higher than others)
    plan.seasonal_factors = {
        "Jan": 0.8, "Feb": 0.85, "Mar": 0.95, "Apr": 1.0, "May": 1.1, "Jun": 1.2,
        "Jul": 1.25, "Aug": 1.2, "Sep": 1.0, "Oct": 0.95, "Nov": 0.9, "Dec": 1.1
    }
    
    return plan


if __name__ == "__main__":
    # Example usage
    print("YT22 Toimivan Yrityksen Tulossuunnitelma Lapua - Operating Business Profit Planning Tool")
    print("=" * 90)
    
    # Create a sample operating business profit plan
    sample_plan = create_sample_plan()
    
    # Generate and display the operating business report
    report = sample_plan.generate_operating_business_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Total Investment Need: €{report['total_investment_need']:,.2f}")
    
    print(f"\nRevenue Projections:")
    for year, revenue in report['revenue_projections'].items():
        print(f"  {year}: €{revenue:,.2f}")
    
    print(f"\nAnnual Net Income Projections:")
    for year, net_income in report['annual_net_income'].items():
        print(f"  {year}: €{net_income:,.2f}")
    
    print(f"\nPerformance Metrics:")
    perf_metrics = report['performance_metrics']
    print(f"  Revenue Growth Rate: {perf_metrics['revenue_growth_rate']:.2%}")
    print(f"  Profit Margin: {perf_metrics['profit_margin']:.2%}")
    print(f"  Return on Assets: {perf_metrics['return_on_assets']:.2%}")
    print(f"  Return on Equity: {perf_metrics['return_on_equity']:.2%}")
    print(f"  Debt-to-Equity Ratio: {perf_metrics['debt_to_equity_ratio']:.2f}")
    print(f"  Current Ratio: {perf_metrics['current_ratio']:.2f}")
    
    print(f"\nBenchmarking Comparison:")
    bench_data = report['benchmarking_comparison']
    print(f"  Revenue Growth vs Industry: {bench_data['revenue_growth_vs_industry']:.2%}")
    print(f"  Profit Margin vs Industry: {bench_data['profit_margin_vs_industry']:.2%}")
    print(f"  ROA vs Industry: {bench_data['roa_vs_industry']:.2%}")
    print(f"  Performance Rating: {bench_data['performance_rating']}")
    
    # Save the report to a JSON file
    sample_plan.save_to_json("sample_operating_business_profit_plan.json")
    print("\nOperating business profit plan saved to 'sample_operating_business_profit_plan.json'")