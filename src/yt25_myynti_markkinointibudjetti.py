"""
Python implementation of YT25_Myynti_Markkinointibudjetti sales and marketing budget template.

This module provides programmatic access to the sales and marketing budget functionality
originally implemented in the YT25_Myynti_Markkinointibudjetti.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class SalesMarketingBudget:
    """
    A class representing a sales and marketing budget based on the 
    YT25_Myynti_Markkinointibudjetti template.
    This tool helps businesses plan and allocate resources for both sales and marketing activities,
    coordinating efforts to maximize revenue generation and market penetration.
    """
    
    def __init__(self, company_name: str = "Sales Marketing Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.sales_budget = {}  # Sales budget components
        self.marketing_budget = {}  # Marketing budget components
        self.monthly_allocations = {}  # Monthly budget allocations
        self.target_segments = {}  # Target segments and their allocations
        self.channels = {}  # Sales and marketing channels
        self.performance_metrics = {}  # KPIs and performance metrics
        self.roi_calculations = {}  # ROI calculations for sales and marketing activities
        self.sales_marketing_calendar = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the sales and marketing budget with default values."""
        # Define marketing channels
        self.marketing_channels = {
            "advertising_agency": {"name": "Mainos-/mediatoimisto", "budget": 0},
            "national_newspaper": {"name": "Sanomalehti", "budget": 0},
            "local_newspaper": {"name": "Paikallislehti", "budget": 0},
            "periodical": {"name": "Aikakausilehti", "budget": 0},
            "search_ads": {"name": "Hakukonemainonta/Google AD", "budget": 0},
            "online_ads_1": {"name": "Verkkomainonta 1", "budget": 0},
            "online_ads_2": {"name": "Verkkomainonta 2", "budget": 0},
            "online_ads_3": {"name": "Verkkomainonta 3", "budget": 0},
            "online_ads_4": {"name": "Verkkomainonta 4", "budget": 0},
            "online_ads_5": {"name": "Verkkomainonta 5", "budget": 0},
            "trade_shows_1": {"name": "Messut, näyttelyt 1", "budget": 0},
            "trade_shows_2": {"name": "Messut, näyttelyt 2", "budget": 0},
            "brochures_1": {"name": "Esite 1", "budget": 0},
            "brochures_2": {"name": "Esite 2", "budget": 0},
            "direct_mail_1": {"name": "Suoramainos 1", "budget": 0},
            "direct_mail_2": {"name": "Suoramainos 2", "budget": 0},
            "promotional_gifts_1": {"name": "Liikelahja 1", "budget": 0},
            "promotional_gifts_2": {"name": "Liikelahja 2", "budget": 0},
            "radio_1": {"name": "Radiokanava 1", "budget": 0},
            "radio_2": {"name": "Radiokanava 2", "budget": 0},
            "sponsorship_collaboration": {"name": "Sponsorointi/yhteistyö", "budget": 0},
            "influencer_marketing": {"name": "Vaikuttajamarkkinointi", "budget": 0},
            "outdoor_advertising": {"name": "Ulkomainonta", "budget": 0},
            "tv": {"name": "TV", "budget": 0},
            "product_demos": {"name": "Tuote-esittelyt", "budget": 0},
            "sales_contests": {"name": "Myyntikilpailut", "budget": 0},
            "other_contests": {"name": "Muut kilpailut", "budget": 0},
            "website": {"name": "Kotisivut", "budget": 0}
        }
        
        # Define sales channels
        self.sales_channels = {
            "direct_sales": {"name": "Direct Sales", "budget": 0},
            "inside_sales": {"name": "Inside Sales", "budget": 0},
            "field_sales": {"name": "Field Sales", "budget": 0},
            "telemarketing": {"name": "Telemarketing", "budget": 0},
            "retail_partners": {"name": "Retail Partners", "budget": 0},
            "distributors": {"name": "Distributors", "budget": 0},
            "e_commerce": {"name": "E-commerce", "budget": 0},
            "wholesale": {"name": "Wholesale", "budget": 0}
        }
        
        # Initialize monthly allocations (Jan-Dec)
        months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
        self.monthly_allocations = {
            "marketing": {channel: {month: 0 for month in months} for channel in self.marketing_channels},
            "sales": {channel: {month: 0 for month in months} for channel in self.sales_channels}
        }
        
        # Initialize target segments
        self.target_segments = {
            "segment_1": {"name": "Primary Segment", "allocation": 0, "description": ""},
            "segment_2": {"name": "Secondary Segment", "allocation": 0, "description": ""},
            "segment_3": {"name": "Tertiary Segment", "allocation": 0, "description": ""}
        }
        
        # Initialize performance metrics
        self.performance_metrics = {
            "revenue_target": 0,
            "marketing_roi_target": 0.0,
            "sales_roi_target": 0.0,
            "lead_target": 0,
            "conversion_rate_target": 0.0,
            "cost_per_lead_target": 0,
            "customer_acquisition_cost_target": 0,
            "sales_cycle_target": 0  # in days
        }
    
    def set_marketing_channel_budget(self, channel: str, budget: float):
        """Set the annual budget for a specific marketing channel."""
        if channel in self.marketing_channels:
            self.marketing_channels[channel]["budget"] = budget
        else:
            raise ValueError(f"Unknown marketing channel: {channel}")
    
    def set_sales_channel_budget(self, channel: str, budget: float):
        """Set the annual budget for a specific sales channel."""
        if channel in self.sales_channels:
            self.sales_channels[channel]["budget"] = budget
        else:
            raise ValueError(f"Unknown sales channel: {channel}")
    
    def set_monthly_allocation(self, category: str, channel: str, month: str, amount: float):
        """Set the monthly allocation for a specific channel and category."""
        if category in self.monthly_allocations:
            if channel in self.monthly_allocations[category]:
                if month in self.monthly_allocations[category][channel]:
                    self.monthly_allocations[category][channel][month] = amount
                else:
                    raise ValueError(f"Unknown month: {month}")
            else:
                raise ValueError(f"Unknown channel: {channel}")
        else:
            raise ValueError(f"Unknown category: {category}")
    
    def set_performance_metric(self, metric: str, value: float):
        """Set a performance metric value."""
        if metric in self.performance_metrics:
            self.performance_metrics[metric] = value
        else:
            raise ValueError(f"Unknown performance metric: {metric}")
    
    def set_target_segment_allocation(self, segment: str, allocation: float, description: str = ""):
        """Set the allocation for a target segment."""
        if segment in self.target_segments:
            self.target_segments[segment]["allocation"] = allocation
            if description:
                self.target_segments[segment]["description"] = description
        else:
            raise ValueError(f"Unknown target segment: {segment}")
    
    def calculate_total_marketing_spend(self) -> float:
        """Calculate the total marketing spend across all channels."""
        total = 0
        for channel in self.marketing_channels.values():
            total += channel["budget"]
        return total
    
    def calculate_total_sales_spend(self) -> float:
        """Calculate the total sales spend across all channels."""
        total = 0
        for channel in self.sales_channels.values():
            total += channel["budget"]
        return total
    
    def calculate_total_spend(self) -> float:
        """Calculate the total spend across both sales and marketing."""
        return self.calculate_total_marketing_spend() + self.calculate_total_sales_spend()
    
    def calculate_monthly_spend(self, category: str, month: str) -> float:
        """Calculate the total spend for a specific category and month."""
        total = 0
        for channel_allocations in self.monthly_allocations[category].values():
            total += channel_allocations[month]
        return total
    
    def calculate_channel_spend_percentage(self, category: str, channel: str) -> float:
        """Calculate what percentage of the total budget is allocated to a specific channel."""
        if category == "marketing":
            total_spend = self.calculate_total_marketing_spend()
            if total_spend == 0:
                return 0
            return (self.marketing_channels[channel]["budget"] / total_spend) * 100
        elif category == "sales":
            total_spend = self.calculate_total_sales_spend()
            if total_spend == 0:
                return 0
            return (self.sales_channels[channel]["budget"] / total_spend) * 100
        else:
            raise ValueError(f"Unknown category: {category}")
    
    def calculate_combined_roi(self, revenue_generated: float) -> float:
        """Calculate the combined ROI of sales and marketing activities."""
        total_spend = self.calculate_total_spend()
        if total_spend == 0:
            return 0
        return (revenue_generated - total_spend) / total_spend
    
    def calculate_cost_per_lead(self, leads_generated: int) -> float:
        """Calculate the cost per lead."""
        total_spend = self.calculate_total_spend()
        if leads_generated == 0:
            return float('inf')
        return total_spend / leads_generated
    
    def calculate_customer_acquisition_cost(self, customers_acquired: int) -> float:
        """Calculate the customer acquisition cost."""
        total_spend = self.calculate_total_spend()
        if customers_acquired == 0:
            return float('inf')
        return total_spend / customers_acquired
    
    def calculate_sales_marketing_alignment_score(self) -> float:
        """Calculate a score representing how well sales and marketing are aligned."""
        # This is a simplified calculation - in practice, this would be more complex
        # based on shared goals, coordinated activities, etc.
        marketing_budget = self.calculate_total_marketing_spend()
        sales_budget = self.calculate_total_sales_spend()
        
        if marketing_budget == 0 and sales_budget == 0:
            return 0.0
        
        # Calculate the ratio of marketing to sales budget
        ratio = marketing_budget / sales_budget if sales_budget != 0 else float('inf')
        
        # A ratio between 0.5 and 2.0 is considered well-aligned
        if 0.5 <= ratio <= 2.0:
            return 1.0  # Perfect alignment
        else:
            # Closer to 1.0 is better alignment
            return min(ratio, 2.0/ratio) if ratio < 2.0 else 2.0/ratio
    
    def generate_sales_marketing_calendar(self) -> Dict:
        """Generate a sales and marketing calendar with all planned activities."""
        # Calculate monthly spends
        months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
        monthly_marketing_spends = {month: self.calculate_monthly_spend("marketing", month) for month in months}
        monthly_sales_spends = {month: self.calculate_monthly_spend("sales", month) for month in months}
        
        # Calculate channel percentages
        marketing_channel_percentages = {channel: self.calculate_channel_spend_percentage("marketing", channel) 
                                        for channel in self.marketing_channels}
        sales_channel_percentages = {channel: self.calculate_channel_spend_percentage("sales", channel) 
                                    for channel in self.sales_channels}
        
        self.sales_marketing_calendar = {
            "company_name": self.company_name,
            "year": self.year,
            "marketing_channels": self.marketing_channels,
            "sales_channels": self.sales_channels,
            "monthly_marketing_allocations": self.monthly_allocations["marketing"],
            "monthly_sales_allocations": self.monthly_allocations["sales"],
            "monthly_marketing_spends": monthly_marketing_spends,
            "monthly_sales_spends": monthly_sales_spends,
            "marketing_channel_percentages": marketing_channel_percentages,
            "sales_channel_percentages": sales_channel_percentages,
            "total_marketing_spend": self.calculate_total_marketing_spend(),
            "total_sales_spend": self.calculate_total_sales_spend(),
            "total_combined_spend": self.calculate_total_spend(),
            "target_segments": self.target_segments,
            "performance_metrics": self.performance_metrics,
            "alignment_score": self.calculate_sales_marketing_alignment_score()
        }
        
        return self.sales_marketing_calendar
    
    def generate_sales_marketing_report(self, revenue: float, leads: int, customers: int) -> Dict:
        """Generate a comprehensive sales and marketing report with performance metrics."""
        calendar = self.generate_sales_marketing_calendar()
        
        report = {
            "calendar": calendar,
            "performance_analysis": {
                "actual_revenue": revenue,
                "actual_leads": leads,
                "actual_customers": customers,
                "combined_roi": self.calculate_combined_roi(revenue),
                "cost_per_lead": self.calculate_cost_per_lead(leads),
                "customer_acquisition_cost": self.calculate_customer_acquisition_cost(customers),
                "revenue_per_customer": revenue / customers if customers > 0 else 0,
                "sales_marketing_alignment_score": self.calculate_sales_marketing_alignment_score()
            },
            "recommendations": self._generate_recommendations(revenue, leads, customers)
        }
        
        return report
    
    def _generate_recommendations(self, revenue: float, leads: int, customers: int) -> List[str]:
        """Generate recommendations based on performance."""
        recommendations = []
        combined_roi = self.calculate_combined_roi(revenue)
        cpl = self.calculate_cost_per_lead(leads)
        cac = self.calculate_customer_acquisition_cost(customers)
        alignment_score = self.calculate_sales_marketing_alignment_score()
        
        if combined_roi < (self.performance_metrics["marketing_roi_target"] + self.performance_metrics["sales_roi_target"]) / 2:
            recommendations.append("Combined sales and marketing ROI is below target. Consider optimizing channel mix or improving campaign effectiveness.")
        
        if cpl > self.performance_metrics["cost_per_lead_target"]:
            recommendations.append("Cost per lead is above target. Review targeting and ad creative effectiveness.")
        
        if cac > self.performance_metrics["customer_acquisition_cost_target"]:
            recommendations.append("Customer acquisition cost is above target. Evaluate customer lifetime value and retention strategies.")
        
        if alignment_score < 0.7:  # Below 70% alignment
            recommendations.append("Sales and marketing alignment is suboptimal. Improve coordination between teams.")
        
        if not recommendations:
            recommendations.append("Sales and marketing performance is meeting targets. Consider scaling successful campaigns.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the sales and marketing budget to a JSON file."""
        calendar = self.generate_sales_marketing_calendar()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(calendar, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a sales and marketing budget from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.marketing_channels = data.get("marketing_channels", self.marketing_channels)
        self.sales_channels = data.get("sales_channels", self.sales_channels)
        self.monthly_allocations["marketing"] = data.get("monthly_marketing_allocations", self.monthly_allocations["marketing"])
        self.monthly_allocations["sales"] = data.get("monthly_sales_allocations", self.monthly_allocations["sales"])
        self.target_segments = data.get("target_segments", self.target_segments)


def create_sample_budget() -> SalesMarketingBudget:
    """Create a sample sales and marketing budget with example data."""
    budget = SalesMarketingBudget(company_name="Sample Sales Marketing Co", year=2026)
    
    # Set example marketing channel budgets
    budget.set_marketing_channel_budget("search_ads", 25000)
    budget.set_marketing_channel_budget("online_ads_1", 20000)
    budget.set_marketing_channel_budget("online_ads_2", 15000)
    budget.set_marketing_channel_budget("influencer_marketing", 18000)
    budget.set_marketing_channel_budget("trade_shows_1", 30000)
    budget.set_marketing_channel_budget("website", 10000)
    budget.set_marketing_channel_budget("product_demos", 12000)
    
    # Set example sales channel budgets
    budget.set_sales_channel_budget("direct_sales", 50000)
    budget.set_sales_channel_budget("inside_sales", 30000)
    budget.set_sales_channel_budget("e_commerce", 20000)
    
    # Set example monthly allocations for search ads
    months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
    for i, month in enumerate(months):
        budget.set_monthly_allocation("marketing", "search_ads", month, 2000 + i*100)  # Increasing trend
    
    # Set example monthly allocations for direct sales
    for i, month in enumerate(months):
        budget.set_monthly_allocation("sales", "direct_sales", month, 4000 + i*100)  # Increasing trend
    
    # Set performance metrics
    budget.set_performance_metric("revenue_target", 500000)
    budget.set_performance_metric("marketing_roi_target", 0.3)  # 30% ROI target
    budget.set_performance_metric("sales_roi_target", 0.2)  # 20% ROI target
    budget.set_performance_metric("lead_target", 2000)
    budget.set_performance_metric("conversion_rate_target", 0.05)  # 5% conversion
    budget.set_performance_metric("cost_per_lead_target", 25)
    budget.set_performance_metric("customer_acquisition_cost_target", 250)
    budget.set_performance_metric("sales_cycle_target", 45)  # 45 days
    
    # Set target segment allocations
    budget.set_target_segment_allocation("segment_1", 0.6, "Primary target: Young professionals aged 25-40")
    budget.set_target_segment_allocation("segment_2", 0.3, "Secondary target: Middle-aged professionals")
    budget.set_target_segment_allocation("segment_3", 0.1, "Tertiary target: Students and young adults")
    
    return budget


if __name__ == "__main__":
    # Example usage
    print("YT25 Myynti-Markkinointibudjetti - Sales and Marketing Budget Tool")
    print("=" * 70)
    
    # Create a sample sales and marketing budget
    sample_budget = create_sample_budget()
    
    # Generate and display the sales and marketing calendar
    calendar = sample_budget.generate_sales_marketing_calendar()
    
    print(f"\nCompany: {calendar['company_name']}")
    print(f"Year: {calendar['year']}")
    print(f"Total Marketing Spend: €{calendar['total_marketing_spend']:,.2f}")
    print(f"Total Sales Spend: €{calendar['total_sales_spend']:,.2f}")
    print(f"Total Combined Spend: €{calendar['total_combined_spend']:,.2f}")
    print(f"Sales-Marketing Alignment Score: {calendar['alignment_score']:.2f}")
    
    print(f"\nMarketing Channel Budgets:")
    for channel, info in list(calendar['marketing_channels'].items())[:5]:  # Show first 5 channels
        if info['budget'] > 0:  # Only show channels with budget
            print(f"  {info['name']}: €{info['budget']:,.2f} ({calendar['marketing_channel_percentages'][channel]:.1f}%)")
    
    print(f"\nSales Channel Budgets:")
    for channel, info in list(calendar['sales_channels'].items())[:5]:  # Show first 5 channels
        if info['budget'] > 0:  # Only show channels with budget
            print(f"  {info['name']}: €{info['budget']:,.2f} ({calendar['sales_channel_percentages'][channel]:.1f}%)")
    
    print(f"\nMonthly Marketing Spends:")
    for month, spend in list(calendar['monthly_marketing_spends'].items())[:6]:  # Show first 6 months
        print(f"  {month}: €{spend:,.2f}")
    
    print(f"\nMonthly Sales Spends:")
    for month, spend in list(calendar['monthly_sales_spends'].items())[:6]:  # Show first 6 months
        print(f"  {month}: €{spend:,.2f}")
    
    print(f"\nTarget Segments:")
    for seg_key, segment in calendar['target_segments'].items():
        if segment['allocation'] > 0:  # Only show segments with allocation
            print(f"  {segment['name']}: {segment['allocation']*100:.1f}% - {segment['description']}")
    
    # Generate a sample performance report
    print(f"\nGenerating sample performance report...")
    report = sample_budget.generate_sales_marketing_report(
        revenue=250000,  # Actual revenue generated
        leads=1200,      # Actual leads generated
        customers=85     # Actual customers acquired
    )
    
    perf = report['performance_analysis']
    print(f"\nPerformance Analysis:")
    print(f"  Actual Revenue: €{perf['actual_revenue']:,.2f}")
    print(f"  Actual Leads: {perf['actual_leads']:,}")
    print(f"  Actual Customers: {perf['actual_customers']:,}")
    print(f"  Combined ROI: {perf['combined_roi']:.2%}")
    print(f"  Cost Per Lead: €{perf['cost_per_lead']:,.2f}")
    print(f"  Customer Acquisition Cost: €{perf['customer_acquisition_cost']:,.2f}")
    print(f"  Sales-Marketing Alignment Score: {perf['sales_marketing_alignment_score']:.2f}")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the calendar to a JSON file
    sample_budget.save_to_json("sample_sales_marketing_budget.json")
    print("\nSales and marketing budget saved to 'sample_sales_marketing_budget.json'")