"""
Python implementation of Myyntibudjetti kuukausittain monthly sales budget template.

This module provides programmatic access to the monthly sales budget functionality
originally implemented in the Myyntibudjetti kuukausittain.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class MonthlySalesBudget:
    """
    A class representing a monthly sales budget based on the 
    Myyntibudjetti kuukausittain template.
    This tool helps businesses plan and track their sales performance on a monthly basis,
    allowing for better forecasting, resource allocation, and performance monitoring throughout the year.
    """
    
    def __init__(self, company_name: str = "Monthly Sales Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.products_services = {}  # Products and services with monthly targets
        self.monthly_targets = {}  # Monthly sales targets
        self.monthly_actuals = {}  # Monthly actual sales
        self.vat_rates = {}  # VAT rates for different products/services
        self.customer_segments = {}  # Customer segments and their monthly contributions
        self.sales_channels = {}  # Sales channels and their monthly performance
        self.geographic_regions = {}  # Geographic regions and their monthly performance
        self.performance_metrics = {}  # KPIs and performance metrics
        self.seasonal_factors = {}  # Seasonal adjustment factors
        self.monthly_budget = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the monthly sales budget with default values."""
        # Define months in Finnish
        self.months = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", 
                      "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
        
        # Define products/services with monthly targets
        self.products_services = {
            "product_1": {
                "name": "Tuote/palvelu 1",
                "vat_rate": 0.255,
                "monthly_targets": {month: 0 for month in self.months},
                "monthly_actuals": {month: 0 for month in self.months},
                "unit_price_incl_vat": 0,
                "unit_price_excl_vat": 0,
                "quantity": 0
            },
            "product_2": {
                "name": "Tuote/palvelu 2",
                "vat_rate": 0.255,
                "monthly_targets": {month: 0 for month in self.months},
                "monthly_actuals": {month: 0 for month in self.months},
                "unit_price_incl_vat": 0,
                "unit_price_excl_vat": 0,
                "quantity": 0
            },
            "product_3": {
                "name": "Tuote/palvelu 3",
                "vat_rate": 0.255,
                "monthly_targets": {month: 0 for month in self.months},
                "monthly_actuals": {month: 0 for month in self.months},
                "unit_price_incl_vat": 0,
                "unit_price_excl_vat": 0,
                "quantity": 0
            },
            "product_4": {
                "name": "Tuote/palvelu 4",
                "vat_rate": 0.255,
                "monthly_targets": {month: 0 for month in self.months},
                "monthly_actuals": {month: 0 for month in self.months},
                "unit_price_incl_vat": 0,
                "unit_price_excl_vat": 0,
                "quantity": 0
            },
            "product_5": {
                "name": "Tuote/palvelu 5",
                "vat_rate": 0.255,
                "monthly_targets": {month: 0 for month in self.months},
                "monthly_actuals": {month: 0 for month in self.months},
                "unit_price_incl_vat": 0,
                "unit_price_excl_vat": 0,
                "quantity": 0
            }
        }
        
        # Initialize customer segments
        self.customer_segments = {
            "segment_1": {"name": "Asiakassegmentti 1", "monthly_contribution": {month: 0 for month in self.months}},
            "segment_2": {"name": "Asiakassegmentti 2", "monthly_contribution": {month: 0 for month in self.months}},
            "segment_3": {"name": "Asiakassegmentti 3", "monthly_contribution": {month: 0 for month in self.months}}
        }
        
        # Initialize sales channels
        self.sales_channels = {
            "channel_1": {"name": "Myyntikanava 1", "monthly_performance": {month: 0 for month in self.months}},
            "channel_2": {"name": "Myyntikanava 2", "monthly_performance": {month: 0 for month in self.months}},
            "channel_3": {"name": "Myyntikanava 3", "monthly_performance": {month: 0 for month in self.months}}
        }
        
        # Initialize geographic regions
        self.geographic_regions = {
            "region_1": {"name": "Maantieteellinen alue 1", "monthly_performance": {month: 0 for month in self.months}},
            "region_2": {"name": "Maantieteellinen alue 2", "monthly_performance": {month: 0 for month in self.months}},
            "region_3": {"name": "Maantieteellinen alue 3", "monthly_performance": {month: 0 for month in self.months}}
        }
        
        # Initialize seasonal factors (multipliers for each month)
        self.seasonal_factors = {
            "Tammikuu": 1.0,
            "Helmikuu": 1.0,
            "Maaliskuu": 1.0,
            "Huhtikuu": 1.0,
            "Toukokuu": 1.0,
            "Kesäkuu": 1.2,  # Summer peak
            "Heinäkuu": 1.25, # Summer peak
            "Elokuu": 1.15,   # Late summer
            "Syyskuu": 0.95,  # Early fall
            "Lokakuu": 0.9,   # Fall
            "Marraskuu": 0.85, # Late fall
            "Joulukuu": 1.3   # Holiday season
        }
        
        # Initialize performance metrics
        self.performance_metrics = {
            "total_target_excl_vat": 0,
            "total_actual_excl_vat": 0,
            "total_target_incl_vat": 0,
            "total_actual_incl_vat": 0,
            "overall_variance_pct": 0.0,
            "monthly_variances": {month: 0.0 for month in self.months},
            "best_performing_month": "",
            "worst_performing_month": ""
        }
    
    def set_product_monthly_target(self, product_id: str, month: str, target: float):
        """Set the monthly target for a specific product/service."""
        if product_id in self.products_services:
            if month in self.months:
                self.products_services[product_id]["monthly_targets"][month] = target
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def set_product_monthly_actual(self, product_id: str, month: str, actual: float):
        """Set the monthly actual sales for a specific product/service."""
        if product_id in self.products_services:
            if month in self.months:
                self.products_services[product_id]["monthly_actuals"][month] = actual
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def set_product_details(self, product_id: str, unit_price_incl_vat: float, unit_price_excl_vat: float, quantity: int):
        """Set product details like unit price and quantity."""
        if product_id in self.products_services:
            self.products_services[product_id]["unit_price_incl_vat"] = unit_price_incl_vat
            self.products_services[product_id]["unit_price_excl_vat"] = unit_price_excl_vat
            self.products_services[product_id]["quantity"] = quantity
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def set_customer_segment_monthly_contribution(self, segment_id: str, month: str, contribution: float):
        """Set the monthly contribution for a customer segment."""
        if segment_id in self.customer_segments:
            if month in self.months:
                self.customer_segments[segment_id]["monthly_contribution"][month] = contribution
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown customer segment ID: {segment_id}")
    
    def set_sales_channel_monthly_performance(self, channel_id: str, month: str, performance: float):
        """Set the monthly performance for a sales channel."""
        if channel_id in self.sales_channels:
            if month in self.months:
                self.sales_channels[channel_id]["monthly_performance"][month] = performance
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown sales channel ID: {channel_id}")
    
    def set_geographic_region_monthly_performance(self, region_id: str, month: str, performance: float):
        """Set the monthly performance for a geographic region."""
        if region_id in self.geographic_regions:
            if month in self.months:
                self.geographic_regions[region_id]["monthly_performance"][month] = performance
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown geographic region ID: {region_id}")
    
    def calculate_monthly_totals(self, month: str) -> Dict:
        """Calculate total targets and actuals for a specific month."""
        target_excl_vat = 0
        actual_excl_vat = 0
        target_incl_vat = 0
        actual_incl_vat = 0
        
        for product in self.products_services.values():
            target_excl_vat += product["monthly_targets"][month]
            actual_excl_vat += product["monthly_actuals"][month]
            
            # Calculate VAT inclusive amounts
            vat_multiplier = 1 + product["vat_rate"]
            target_incl_vat += product["monthly_targets"][month] * vat_multiplier
            actual_incl_vat += product["monthly_actuals"][month] * vat_multiplier
        
        return {
            "target_excl_vat": target_excl_vat,
            "actual_excl_vat": actual_excl_vat,
            "target_incl_vat": target_incl_vat,
            "actual_incl_vat": actual_incl_vat,
            "variance_excl_vat": actual_excl_vat - target_excl_vat,
            "variance_pct": (actual_excl_vat / target_excl_vat - 1) * 100 if target_excl_vat != 0 else 0
        }
    
    def calculate_yearly_totals(self) -> Dict:
        """Calculate total targets and actuals for the entire year."""
        yearly_target_excl_vat = 0
        yearly_actual_excl_vat = 0
        yearly_target_incl_vat = 0
        yearly_actual_incl_vat = 0
        
        for month in self.months:
            monthly_totals = self.calculate_monthly_totals(month)
            yearly_target_excl_vat += monthly_totals["target_excl_vat"]
            yearly_actual_excl_vat += monthly_totals["actual_excl_vat"]
            yearly_target_incl_vat += monthly_totals["target_incl_vat"]
            yearly_actual_incl_vat += monthly_totals["actual_incl_vat"]
        
        return {
            "total_target_excl_vat": yearly_target_excl_vat,
            "total_actual_excl_vat": yearly_actual_excl_vat,
            "total_target_incl_vat": yearly_target_incl_vat,
            "total_actual_incl_vat": yearly_actual_incl_vat,
            "overall_variance_excl_vat": yearly_actual_excl_vat - yearly_target_excl_vat,
            "overall_variance_pct": (yearly_actual_excl_vat / yearly_target_excl_vat - 1) * 100 if yearly_target_excl_vat != 0 else 0
        }
    
    def calculate_performance_metrics(self) -> Dict:
        """Calculate overall performance metrics."""
        yearly_totals = self.calculate_yearly_totals()
        
        # Calculate monthly variances
        monthly_variances = {}
        for month in self.months:
            monthly_totals = self.calculate_monthly_totals(month)
            monthly_variances[month] = monthly_totals["variance_pct"]
        
        # Find best and worst performing months
        best_month = max(monthly_variances, key=monthly_variances.get)
        worst_month = min(monthly_variances, key=monthly_variances.get)
        
        self.performance_metrics = {
            "total_target_excl_vat": yearly_totals["total_target_excl_vat"],
            "total_actual_excl_vat": yearly_totals["total_actual_excl_vat"],
            "total_target_incl_vat": yearly_totals["total_target_incl_vat"],
            "total_actual_incl_vat": yearly_totals["total_actual_incl_vat"],
            "overall_variance_pct": yearly_totals["overall_variance_pct"],
            "monthly_variances": monthly_variances,
            "best_performing_month": best_month,
            "worst_performing_month": worst_month
        }
        
        return self.performance_metrics
    
    def apply_seasonal_adjustment(self, month: str, value: float) -> float:
        """Apply seasonal adjustment factor to a value."""
        if month in self.seasonal_factors:
            return value * self.seasonal_factors[month]
        else:
            return value
    
    def generate_monthly_report(self, month: str) -> Dict:
        """Generate a detailed report for a specific month."""
        monthly_totals = self.calculate_monthly_totals(month)
        
        report = {
            "company_name": self.company_name,
            "year": self.year,
            "month": month,
            "monthly_targets": {prod_id: prod["monthly_targets"][month] 
                                for prod_id, prod in self.products_services.items()},
            "monthly_actuals": {prod_id: prod["monthly_actuals"][month] 
                                for prod_id, prod in self.products_services.items()},
            "monthly_totals": monthly_totals,
            "customer_segment_contributions": {seg_id: seg["monthly_contribution"][month] 
                                              for seg_id, seg in self.customer_segments.items()},
            "sales_channel_performance": {chan_id: chan["monthly_performance"][month] 
                                         for chan_id, chan in self.sales_channels.items()},
            "geographic_region_performance": {reg_id: reg["monthly_performance"][month] 
                                             for reg_id, reg in self.geographic_regions.items()},
            "seasonal_factor": self.seasonal_factors[month]
        }
        
        return report
    
    def generate_yearly_report(self) -> Dict:
        """Generate a comprehensive yearly report."""
        yearly_totals = self.calculate_yearly_totals()
        performance_metrics = self.calculate_performance_metrics()
        
        # Generate monthly reports for all months
        monthly_reports = {month: self.generate_monthly_report(month) for month in self.months}
        
        report = {
            "company_name": self.company_name,
            "year": self.year,
            "yearly_totals": yearly_totals,
            "performance_metrics": performance_metrics,
            "monthly_reports": monthly_reports,
            "products_services": self.products_services,
            "customer_segments": self.customer_segments,
            "sales_channels": self.sales_channels,
            "geographic_regions": self.geographic_regions,
            "seasonal_factors": self.seasonal_factors
        }
        
        return report
    
    def save_to_json(self, filepath: str):
        """Save the monthly sales budget to a JSON file."""
        report = self.generate_yearly_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a monthly sales budget from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.products_services = data.get("products_services", self.products_services)
        self.customer_segments = data.get("customer_segments", self.customer_segments)
        self.sales_channels = data.get("sales_channels", self.sales_channels)
        self.geographic_regions = data.get("geographic_regions", self.geographic_regions)
        self.seasonal_factors = data.get("seasonal_factors", self.seasonal_factors)


def create_sample_budget() -> MonthlySalesBudget:
    """Create a sample monthly sales budget with example data."""
    budget = MonthlySalesBudget(company_name="Sample Monthly Sales Co", year=2026)
    
    # Set example product monthly targets with some seasonal variation
    for product_id in ["product_1", "product_2", "product_3"]:
        for i, month in enumerate(budget.months):
            # Base target with some variation
            base_target = 10000 + (i * 500)
            # Apply seasonal factor
            seasonal_target = budget.apply_seasonal_adjustment(month, base_target)
            budget.set_product_monthly_target(product_id, month, seasonal_target)
    
    # Set example actual sales (slightly below targets to show variance)
    for product_id in ["product_1", "product_2", "product_3"]:
        for i, month in enumerate(budget.months):
            target = budget.products_services[product_id]["monthly_targets"][month]
            # Actual is 95% of target
            actual = target * 0.95
            budget.set_product_monthly_actual(product_id, month, actual)
    
    # Set product details
    budget.set_product_details("product_1", 120.0, 100.0, 100)
    budget.set_product_details("product_2", 240.0, 200.0, 50)
    budget.set_product_details("product_3", 60.0, 50.0, 200)
    
    # Set example customer segment contributions
    for seg_id in ["segment_1", "segment_2", "segment_3"]:
        for i, month in enumerate(budget.months):
            base_contribution = 5000 + (i * 300)
            seasonal_contribution = budget.apply_seasonal_adjustment(month, base_contribution)
            budget.set_customer_segment_monthly_contribution(seg_id, month, seasonal_contribution)
    
    # Set example sales channel performance
    for chan_id in ["channel_1", "channel_2", "channel_3"]:
        for i, month in enumerate(budget.months):
            base_performance = 7000 + (i * 400)
            seasonal_performance = budget.apply_seasonal_adjustment(month, base_performance)
            budget.set_sales_channel_monthly_performance(chan_id, month, seasonal_performance)
    
    # Set example geographic region performance
    for reg_id in ["region_1", "region_2", "region_3"]:
        for i, month in enumerate(budget.months):
            base_performance = 6000 + (i * 350)
            seasonal_performance = budget.apply_seasonal_adjustment(month, base_performance)
            budget.set_geographic_region_monthly_performance(reg_id, month, seasonal_performance)
    
    return budget


if __name__ == "__main__":
    # Example usage
    print("Myyntibudjetti kuukausittain - Monthly Sales Budget Tool")
    print("=" * 60)
    
    # Create a sample monthly sales budget
    sample_budget = create_sample_budget()
    
    # Generate and display the yearly report
    report = sample_budget.generate_yearly_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Year: {report['year']}")
    
    yearly_totals = report['yearly_totals']
    print(f"Total Target (excl. VAT): €{yearly_totals['total_target_excl_vat']:,.2f}")
    print(f"Total Actual (excl. VAT): €{yearly_totals['total_actual_excl_vat']:,.2f}")
    print(f"Overall Variance: {yearly_totals['overall_variance_pct']:.2f}%")
    
    perf_metrics = report['performance_metrics']
    print(f"Best Performing Month: {perf_metrics['best_performing_month']}")
    print(f"Worst Performing Month: {perf_metrics['worst_performing_month']}")
    
    print(f"\nMonthly Performance Summary:")
    for month in sample_budget.months[:3]:  # Show first 3 months as example
        monthly_data = report['monthly_reports'][month]['monthly_totals']
        print(f"  {month}: Target €{monthly_data['target_excl_vat']:,.2f}, "
              f"Actual €{monthly_data['actual_excl_vat']:,.2f}, "
              f"Variance {monthly_data['variance_pct']:.2f}%")
    
    print(f"\nProduct Performance Summary:")
    for prod_id, prod_data in list(report['products_services'].items())[:3]:  # Show first 3 products
        yearly_target = sum(prod_data['monthly_targets'].values())
        yearly_actual = sum(prod_data['monthly_actuals'].values())
        variance_pct = (yearly_actual/yearly_target - 1)*100 if yearly_target != 0 else 0
        print(f"  {prod_data['name']}: Target €{yearly_target:,.2f}, "
              f"Actual €{yearly_actual:,.2f}, Variance {variance_pct:.2f}%")
    
    # Save the report to a JSON file
    sample_budget.save_to_json("sample_monthly_sales_budget.json")
    print("\nMonthly sales budget saved to 'sample_monthly_sales_budget.json'")