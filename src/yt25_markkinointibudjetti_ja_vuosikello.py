"""
Python implementation of YT25_Markkinointibudjetti_ja_vuosikello marketing budget and annual calendar template.

This module provides programmatic access to the marketing budget and annual calendar functionality
originally implemented in the YT25_Markkinointibudjetti_ja_vuosikello.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class MarketingBudgetCalendar:
    """
    A class representing a marketing budget and annual calendar based on the 
    YT25_Markkinointibudjetti_ja_vuosikello template.
    This tool helps businesses plan and allocate resources for marketing activities 
    throughout the year, coordinating campaigns with seasonal events and business cycles.
    """
    
    def __init__(self, company_name: str = "Marketing Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.marketing_channels = {}  # Different marketing channels and their budgets
        self.monthly_allocations = {}  # Monthly budget allocations
        self.campaigns = {}  # Marketing campaigns with timelines
        self.performance_metrics = {}  # KPIs and performance metrics
        self.events_calendar = {}  # Business events integrated with marketing
        self.roi_calculations = {}  # ROI calculations for marketing activities
        self.marketing_calendar = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the marketing budget with default values."""
        # Define marketing channels
        self.marketing_channels = {
            "social_media": {"name": "Some", "budget": 0},
            "search_ads": {"name": "Hakukonemainonta", "budget": 0},
            "display_ads": {"name": "Verkkomainonta", "budget": 0},
            "print_ads": {"name": "Lehti", "budget": 0},
            "trade_shows": {"name": "Messut, näyttelyt", "budget": 0},
            "brochures": {"name": "Esite", "budget": 0},
            "direct_mail": {"name": "Suoramainos", "budget": 0},
            "signage": {"name": "Liikelahja", "budget": 0},
            "radio": {"name": "Radiokanava", "budget": 0},
            "outdoor": {"name": "Ulkomainonta", "budget": 0},
            "sponsorship": {"name": "Sponsorointi/yhteistyö", "budget": 0},
            "influencer": {"name": "Vaikuttajamarkkinointi", "budget": 0},
            "tv": {"name": "TV", "budget": 0},
            "product_demo": {"name": "Tuote-esittelyt", "budget": 0},
            "sales_contest": {"name": "Myyntikilpailut", "budget": 0},
            "other_contest": {"name": "Muut kilpailut", "budget": 0},
            "website": {"name": "Kotisivut", "budget": 0},
            "content_creation": {"name": "Mainosten valmistukulut", "budget": 0}
        }
        
        # Initialize monthly allocations (Jan-Dec)
        months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
        self.monthly_allocations = {channel: {month: 0 for month in months} for channel in self.marketing_channels}
        
        # Initialize performance metrics
        self.performance_metrics = {
            "revenue_target": 0,
            "marketing_roi_target": 0.0,
            "lead_target": 0,
            "conversion_rate_target": 0.0,
            "cost_per_lead_target": 0,
            "customer_acquisition_cost_target": 0
        }
        
        # Initialize events calendar
        self.events_calendar = {
            "q1_events": [],
            "q2_events": [],
            "q3_events": [],
            "q4_events": []
        }
        
        # Initialize campaigns
        self.campaigns = {
            "campaign_name": "",
            "start_date": "",
            "end_date": "",
            "budget": 0,
            "target_audience": "",
            "channels_used": [],
            "expected_outcome": ""
        }
    
    def set_channel_budget(self, channel: str, budget: float):
        """Set the annual budget for a specific marketing channel."""
        if channel in self.marketing_channels:
            self.marketing_channels[channel]["budget"] = budget
        else:
            raise ValueError(f"Unknown marketing channel: {channel}")
    
    def set_monthly_allocation(self, channel: str, month: str, amount: float):
        """Set the monthly allocation for a specific marketing channel."""
        if channel in self.monthly_allocations:
            if month in self.monthly_allocations[channel]:
                self.monthly_allocations[channel][month] = amount
            else:
                raise ValueError(f"Unknown month: {month}")
        else:
            raise ValueError(f"Unknown marketing channel: {channel}")
    
    def set_performance_metric(self, metric: str, value: float):
        """Set a performance metric value."""
        if metric in self.performance_metrics:
            self.performance_metrics[metric] = value
        else:
            raise ValueError(f"Unknown performance metric: {metric}")
    
    def add_event(self, quarter: str, event: str):
        """Add an event to the quarterly calendar."""
        if quarter in self.events_calendar:
            self.events_calendar[quarter].append(event)
        else:
            raise ValueError(f"Unknown quarter: {quarter}")
    
    def calculate_total_marketing_spend(self) -> float:
        """Calculate the total marketing spend across all channels."""
        total = 0
        for channel in self.marketing_channels.values():
            total += channel["budget"]
        return total
    
    def calculate_monthly_spend(self, month: str) -> float:
        """Calculate the total marketing spend for a specific month."""
        total = 0
        for channel_allocations in self.monthly_allocations.values():
            total += channel_allocations[month]
        return total
    
    def calculate_channel_spend_percentage(self, channel: str) -> float:
        """Calculate what percentage of the total budget is allocated to a specific channel."""
        total_spend = self.calculate_total_marketing_spend()
        if total_spend == 0:
            return 0
        return (self.marketing_channels[channel]["budget"] / total_spend) * 100
    
    def calculate_marketing_roi(self, revenue_generated: float) -> float:
        """Calculate the ROI of marketing activities."""
        total_spend = self.calculate_total_marketing_spend()
        if total_spend == 0:
            return 0
        return (revenue_generated - total_spend) / total_spend
    
    def calculate_cost_per_lead(self, leads_generated: int) -> float:
        """Calculate the cost per lead."""
        total_spend = self.calculate_total_marketing_spend()
        if leads_generated == 0:
            return float('inf')
        return total_spend / leads_generated
    
    def calculate_customer_acquisition_cost(self, customers_acquired: int) -> float:
        """Calculate the customer acquisition cost."""
        total_spend = self.calculate_total_marketing_spend()
        if customers_acquired == 0:
            return float('inf')
        return total_spend / customers_acquired
    
    def plan_campaign(self, name: str, start_date: str, end_date: str, budget: float, 
                     target_audience: str, channels: List[str], expected_outcome: str):
        """Plan a new marketing campaign."""
        self.campaigns = {
            "campaign_name": name,
            "start_date": start_date,
            "end_date": end_date,
            "budget": budget,
            "target_audience": target_audience,
            "channels_used": channels,
            "expected_outcome": expected_outcome
        }
    
    def generate_marketing_calendar(self) -> Dict:
        """Generate a marketing calendar with all planned activities."""
        # Calculate monthly spends
        months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
        monthly_spends = {month: self.calculate_monthly_spend(month) for month in months}
        
        # Calculate channel percentages
        channel_percentages = {channel: self.calculate_channel_spend_percentage(channel) 
                              for channel in self.marketing_channels}
        
        self.marketing_calendar = {
            "company_name": self.company_name,
            "year": self.year,
            "marketing_channels": self.marketing_channels,
            "monthly_allocations": self.monthly_allocations,
            "monthly_spends": monthly_spends,
            "channel_percentages": channel_percentages,
            "total_marketing_spend": self.calculate_total_marketing_spend(),
            "performance_metrics": self.performance_metrics,
            "events_calendar": self.events_calendar,
            "planned_campaigns": [self.campaigns]  # Could be a list of multiple campaigns
        }
        
        return self.marketing_calendar
    
    def generate_marketing_report(self, revenue: float, leads: int, customers: int) -> Dict:
        """Generate a comprehensive marketing report with performance metrics."""
        calendar = self.generate_marketing_calendar()
        
        report = {
            "calendar": calendar,
            "performance_analysis": {
                "actual_revenue": revenue,
                "actual_leads": leads,
                "actual_customers": customers,
                "marketing_roi": self.calculate_marketing_roi(revenue),
                "cost_per_lead": self.calculate_cost_per_lead(leads),
                "customer_acquisition_cost": self.calculate_customer_acquisition_cost(customers),
                "revenue_per_customer": revenue / customers if customers > 0 else 0
            },
            "recommendations": self._generate_recommendations(revenue, leads, customers)
        }
        
        return report
    
    def _generate_recommendations(self, revenue: float, leads: int, customers: int) -> List[str]:
        """Generate recommendations based on performance."""
        recommendations = []
        roi = self.calculate_marketing_roi(revenue)
        cpl = self.calculate_cost_per_lead(leads)
        cac = self.calculate_customer_acquisition_cost(customers)
        
        if roi < self.performance_metrics["marketing_roi_target"]:
            recommendations.append("Marketing ROI is below target. Consider optimizing channel mix or improving campaign effectiveness.")
        
        if cpl > self.performance_metrics["cost_per_lead_target"]:
            recommendations.append("Cost per lead is above target. Review targeting and ad creative effectiveness.")
        
        if cac > self.performance_metrics["customer_acquisition_cost_target"]:
            recommendations.append("Customer acquisition cost is above target. Evaluate customer lifetime value and retention strategies.")
        
        if leads > 0 and customers > 0:
            conversion_rate = customers / leads
            if conversion_rate < self.performance_metrics["conversion_rate_target"]:
                recommendations.append("Conversion rate is below target. Optimize landing pages and sales funnel.")
        
        if not recommendations:
            recommendations.append("Marketing performance is meeting targets. Consider scaling successful campaigns.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the marketing budget and calendar to a JSON file."""
        calendar = self.generate_marketing_calendar()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(calendar, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a marketing budget and calendar from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.marketing_channels = data.get("marketing_channels", self.marketing_channels)
        self.monthly_allocations = data.get("monthly_allocations", self.monthly_allocations)
        self.events_calendar = data.get("events_calendar", self.events_calendar)


def create_sample_budget() -> MarketingBudgetCalendar:
    """Create a sample marketing budget with example data."""
    budget = MarketingBudgetCalendar(company_name="Sample Marketing Co", year=2026)
    
    # Set example channel budgets
    budget.set_channel_budget("social_media", 12000)
    budget.set_channel_budget("search_ads", 18000)
    budget.set_channel_budget("display_ads", 15000)
    budget.set_channel_budget("print_ads", 8000)
    budget.set_channel_budget("trade_shows", 25000)
    budget.set_channel_budget("website", 5000)
    budget.set_channel_budget("content_creation", 10000)
    
    # Set example monthly allocations for social media
    months = ["Tam", "Hel", "Maa", "Huh", "Tou", "Kesä", "Hei", "Elo", "Syys", "Loka", "Mar", "Jou"]
    for i, month in enumerate(months):
        budget.set_monthly_allocation("social_media", month, 1000 + i*100)  # Increasing trend
    
    # Set example monthly allocations for search ads
    for i, month in enumerate(months):
        budget.set_monthly_allocation("search_ads", month, 1500 + i*50)  # Steady increase
    
    # Set performance metrics
    budget.set_performance_metric("revenue_target", 500000)
    budget.set_performance_metric("marketing_roi_target", 0.3)  # 30% ROI target
    budget.set_performance_metric("lead_target", 2000)
    budget.set_performance_metric("conversion_rate_target", 0.05)  # 5% conversion
    budget.set_performance_metric("cost_per_lead_target", 25)
    budget.set_performance_metric("customer_acquisition_cost_target", 250)
    
    # Add example events
    budget.add_event("q1_events", "New Year Sale")
    budget.add_event("q2_events", "Spring Product Launch")
    budget.add_event("q3_events", "Summer Promotion")
    budget.add_event("q4_events", "Holiday Campaign")
    
    # Plan a sample campaign
    budget.plan_campaign(
        name="Summer Social Media Push",
        start_date="2026-06-01",
        end_date="2026-08-31",
        budget=15000,
        target_audience="Young professionals aged 25-40",
        channels=["social_media", "display_ads"],
        expected_outcome="Increase brand awareness and drive 500 new leads"
    )
    
    return budget


if __name__ == "__main__":
    # Example usage
    print("YT25 Markkinointibudjetti ja Vuoosikello - Marketing Budget & Annual Calendar Tool")
    print("=" * 85)
    
    # Create a sample marketing budget
    sample_budget = create_sample_budget()
    
    # Generate and display the marketing calendar
    calendar = sample_budget.generate_marketing_calendar()
    
    print(f"\nCompany: {calendar['company_name']}")
    print(f"Year: {calendar['year']}")
    print(f"Total Marketing Spend: €{calendar['total_marketing_spend']:,.2f}")
    
    print(f"\nChannel Budgets:")
    for channel, info in list(calendar['marketing_channels'].items())[:5]:  # Show first 5 channels
        print(f"  {info['name']}: €{info['budget']:,.2f} ({calendar['channel_percentages'][channel]:.1f}%)")
    
    print(f"\nMonthly Spends:")
    for month, spend in list(calendar['monthly_spends'].items())[:6]:  # Show first 6 months
        print(f"  {month}: €{spend:,.2f}")
    
    print(f"\nPlanned Campaigns:")
    for campaign in calendar['planned_campaigns']:
        print(f"  {campaign['campaign_name']} ({campaign['start_date']} to {campaign['end_date']})")
        print(f"    Budget: €{campaign['budget']:,.2f}")
        print(f"    Target: {campaign['target_audience']}")
        print(f"    Channels: {', '.join(campaign['channels_used'])}")
    
    # Generate a sample performance report
    print(f"\nGenerating sample performance report...")
    report = sample_budget.generate_marketing_report(
        revenue=180000,  # Actual revenue generated
        leads=750,       # Actual leads generated
        customers=45     # Actual customers acquired
    )
    
    perf = report['performance_analysis']
    print(f"\nPerformance Analysis:")
    print(f"  Actual Revenue: €{perf['actual_revenue']:,.2f}")
    print(f"  Actual Leads: {perf['actual_leads']:,}")
    print(f"  Actual Customers: {perf['actual_customers']:,}")
    print(f"  Marketing ROI: {perf['marketing_roi']:.2%}")
    print(f"  Cost Per Lead: €{perf['cost_per_lead']:,.2f}")
    print(f"  Customer Acquisition Cost: €{perf['customer_acquisition_cost']:,.2f}")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the calendar to a JSON file
    sample_budget.save_to_json("sample_marketing_budget.json")
    print("\nMarketing budget saved to 'sample_marketing_budget.json'")