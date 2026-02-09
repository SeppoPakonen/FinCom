"""
Python implementation of Markkinoinnin_vuosikello_kehittäminen_strategia marketing calendar development strategy.

This module provides programmatic access to the marketing calendar development strategy functionality
originally implemented in the Markkinoinnin_vuosikello_kehittäminen_strategia.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json
import csv


class MarketingCalendarStrategy:
    """
    A class representing a marketing annual calendar development strategy based on the 
    Markkinoinnin_vuosikello_kehittäminen_strategia template.
    This tool helps businesses develop and implement a marketing calendar strategy aligned 
    with business objectives, seasonal opportunities, and strategic initiatives.
    """
    
    def __init__(self, company_name: str = "Marketing Strategy Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.monthly_activities = {}  # Marketing activities by month
        self.marketing_channels = {}  # Different marketing channels and their strategies
        self.campaigns = {}  # Marketing campaigns with timelines
        self.content_calendar = {}  # Content planning calendar
        self.events_schedule = {}  # Events and promotional activities
        self.budget_allocation = {}  # Budget allocation by month and channel
        self.performance_metrics = {}  # KPIs and performance metrics
        self.roi_calculations = {}  # ROI calculations for marketing activities
        self.competitor_monitoring = {}  # Competitor monitoring data
        self.customer_satisfaction_tracking = {}  # Customer satisfaction metrics
        self.trend_analysis = {}  # Trend analysis and insights
        self.strategic_initiatives = {}  # Strategic initiatives and alignment
        self.quarterly_plans = {}  # Quarterly marketing plans
        self.weekly_plans = {}  # Weekly marketing plans
        self.risk_management = {}  # Risk management for marketing activities
        self.seasonal_opportunities = {}  # Seasonal opportunities identification
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the marketing calendar strategy with default values."""
        # Define months in Finnish
        self.months = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", 
                      "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
        
        # Initialize monthly activities
        self.monthly_activities = {month: {
            "planned_activities": [],
            "budget_allocated": 0,
            "expected_roi": 0.0,
            "performance_metrics": {
                "reach": 0,
                "engagement": 0,
                "conversion_rate": 0.0,
                "cost_per_acquisition": 0
            }
        } for month in self.months}
        
        # Define marketing channels
        self.marketing_channels = {
            "digital_ads": {
                "name": "Digital Ads",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            },
            "social_media": {
                "name": "Social Media",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            },
            "email_marketing": {
                "name": "Email Marketing",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            },
            "content_marketing": {
                "name": "Content Marketing",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            },
            "events": {
                "name": "Events",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            },
            "pr": {
                "name": "Public Relations",
                "budget_allocation": 0,
                "target_audience": "",
                "seasonal_effectiveness": {month: 1.0 for month in self.months}
            }
        }
        
        # Initialize campaigns
        self.campaigns = {
            "campaign_1": {
                "name": "Campaign 1",
                "start_date": f"{self.year}-01-01",
                "end_date": f"{self.year}-03-31",
                "budget": 0,
                "channels": ["digital_ads", "social_media"],
                "target_audience": "Primary segment",
                "expected_roi": 0.0
            },
            "campaign_2": {
                "name": "Campaign 2",
                "start_date": f"{self.year}-04-01",
                "end_date": f"{self.year}-06-30",
                "budget": 0,
                "channels": ["email_marketing", "content_marketing"],
                "target_audience": "Secondary segment",
                "expected_roi": 0.0
            },
            "campaign_3": {
                "name": "Campaign 3",
                "start_date": f"{self.year}-07-01",
                "end_date": f"{self.year}-09-30",
                "budget": 0,
                "channels": ["events", "pr"],
                "target_audience": "Tertiary segment",
                "expected_roi": 0.0
            }
        }
        
        # Initialize content calendar
        self.content_calendar = {
            "weekly_themes": {f"Week {i}": "" for i in range(1, 53)},
            "daily_posts": {f"{self.year}-01-{day:02d}": {"type": "", "topic": "", "channel": ""} 
                            for day in range(1, 32)}  # Just Jan for example
        }
        
        # Initialize events schedule
        self.events_schedule = {
            "event_1": {
                "name": "Event 1",
                "date": f"{self.year}-06-15",
                "location": "",
                "expected_attendees": 0,
                "budget": 0,
                "expected_roi": 0.0
            },
            "event_2": {
                "name": "Event 2",
                "date": f"{self.year}-10-20",
                "location": "",
                "expected_attendees": 0,
                "budget": 0,
                "expected_roi": 0.0
            }
        }
        
        # Initialize budget allocation
        self.budget_allocation = {
            "total_annual_budget": 0,
            "monthly_budgets": {month: 0 for month in self.months},
            "channel_budgets": {channel: 0 for channel in self.marketing_channels}
        }
        
        # Initialize performance metrics
        self.performance_metrics = {
            "reach": 0,
            "impressions": 0,
            "engagement_rate": 0.0,
            "conversion_rate": 0.0,
            "cost_per_click": 0,
            "cost_per_acquisition": 0,
            "return_on_ad_spend": 0.0,
            "brand_awareness": 0.0,
            "customer_satisfaction_score": 0.0
        }
        
        # Initialize seasonal opportunities
        self.seasonal_opportunities = {
            "spring_opportunities": [],
            "summer_opportunities": [],
            "autumn_opportunities": [],
            "winter_opportunities": []
        }
    
    def set_monthly_activity(self, month: str, activity: str, budget: float, expected_roi: float):
        """Set a planned marketing activity for a specific month."""
        if month in self.monthly_activities:
            self.monthly_activities[month]["planned_activities"].append(activity)
            self.monthly_activities[month]["budget_allocated"] += budget
            self.monthly_activities[month]["expected_roi"] = expected_roi
        else:
            raise ValueError(f"Unknown month: {month}")
    
    def set_channel_budget(self, channel: str, budget: float):
        """Set the annual budget for a specific marketing channel."""
        if channel in self.marketing_channels:
            self.marketing_channels[channel]["budget_allocation"] = budget
        else:
            raise ValueError(f"Unknown marketing channel: {channel}")
    
    def set_campaign_details(self, campaign_id: str, name: str, start_date: str, end_date: str, 
                            budget: float, channels: List[str], target_audience: str, expected_roi: float):
        """Set details for a specific marketing campaign."""
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id] = {
                "name": name,
                "start_date": start_date,
                "end_date": end_date,
                "budget": budget,
                "channels": channels,
                "target_audience": target_audience,
                "expected_roi": expected_roi
            }
        else:
            raise ValueError(f"Unknown campaign ID: {campaign_id}")
    
    def set_performance_metric(self, metric: str, value: float):
        """Set a performance metric value."""
        if metric in self.performance_metrics:
            self.performance_metrics[metric] = value
        else:
            raise ValueError(f"Unknown performance metric: {metric}")
    
    def calculate_total_annual_budget(self) -> float:
        """Calculate the total annual marketing budget."""
        return sum(self.budget_allocation["monthly_budgets"].values())
    
    def calculate_channel_spend_percentage(self, channel: str) -> float:
        """Calculate what percentage of the total budget is allocated to a specific channel."""
        total_budget = self.calculate_total_annual_budget()
        if total_budget == 0:
            return 0
        return (self.marketing_channels[channel]["budget_allocation"] / total_budget) * 100
    
    def calculate_expected_campaign_roi(self, campaign_id: str) -> float:
        """Calculate the expected ROI for a specific campaign."""
        if campaign_id in self.campaigns:
            campaign = self.campaigns[campaign_id]
            if campaign["budget"] == 0:
                return 0
            return campaign["expected_roi"]
        else:
            raise ValueError(f"Unknown campaign ID: {campaign_id}")
    
    def calculate_monthly_spend(self, month: str) -> float:
        """Calculate the total marketing spend for a specific month."""
        total = 0
        for activity in self.monthly_activities[month]["planned_activities"]:
            # This would need to be linked to actual budget data
            total += self.monthly_activities[month]["budget_allocated"]
        return total
    
    def add_seasonal_opportunity(self, season: str, opportunity: str):
        """Add a seasonal opportunity to the appropriate season."""
        if season in self.seasonal_opportunities:
            self.seasonal_opportunities[season].append(opportunity)
        else:
            raise ValueError(f"Unknown season: {season}")
    
    def generate_marketing_calendar(self) -> Dict:
        """Generate a marketing calendar with all planned activities."""
        # Calculate monthly spends
        monthly_spends = {month: self.calculate_monthly_spend(month) for month in self.months}
        
        # Calculate channel percentages
        channel_percentages = {channel: self.calculate_channel_spend_percentage(channel) 
                              for channel in self.marketing_channels}
        
        self.marketing_calendar = {
            "company_name": self.company_name,
            "year": self.year,
            "marketing_channels": self.marketing_channels,
            "monthly_activities": self.monthly_activities,
            "monthly_budgets": self.budget_allocation["monthly_budgets"],
            "monthly_spends": monthly_spends,
            "channel_percentages": channel_percentages,
            "total_annual_budget": self.calculate_total_annual_budget(),
            "campaigns": self.campaigns,
            "content_calendar": self.content_calendar,
            "events_schedule": self.events_schedule,
            "performance_metrics": self.performance_metrics,
            "seasonal_opportunities": self.seasonal_opportunities,
            "strategic_initiatives": self.strategic_initiatives
        }
        
        return self.marketing_calendar
    
    def generate_marketing_report(self, revenue: float, leads: int, customers: int) -> Dict:
        """Generate a comprehensive marketing report with performance metrics."""
        calendar = self.generate_marketing_calendar()
        
        # Calculate additional metrics based on actual performance
        actual_metrics = {
            "actual_revenue": revenue,
            "actual_leads": leads,
            "actual_customers": customers,
            "marketing_roi": (revenue - self.calculate_total_annual_budget()) / self.calculate_total_annual_budget() if self.calculate_total_annual_budget() != 0 else 0,
            "cost_per_lead": self.calculate_total_annual_budget() / leads if leads != 0 else float('inf'),
            "customer_acquisition_cost": self.calculate_total_annual_budget() / customers if customers != 0 else float('inf'),
            "revenue_per_customer": revenue / customers if customers != 0 else 0
        }
        
        report = {
            "calendar": calendar,
            "actual_performance": actual_metrics,
            "performance_analysis": {
                "revenue_target_vs_actual": 0,  # Would need target to calculate
                "lead_target_vs_actual": 0,     # Would need target to calculate
                "customer_target_vs_actual": 0, # Would need target to calculate
                "roi_target_vs_actual": 0       # Would need target to calculate
            },
            "recommendations": self._generate_recommendations(revenue, leads, customers)
        }
        
        return report
    
    def _generate_recommendations(self, revenue: float, leads: int, customers: int) -> List[str]:
        """Generate recommendations based on performance."""
        recommendations = []
        roi = (revenue - self.calculate_total_annual_budget()) / self.calculate_total_annual_budget() if self.calculate_total_annual_budget() != 0 else 0
        
        if roi < 0.1:  # If ROI is below 10%
            recommendations.append("Marketing ROI is below industry standard of 10%. Consider optimizing channel mix or improving campaign effectiveness.")
        
        if leads > 0 and customers > 0:
            conversion_rate = customers / leads
            if conversion_rate < 0.02:  # If conversion rate is below 2%
                recommendations.append("Lead-to-customer conversion rate is below the typical 2% benchmark. Review sales funnel optimization.")
        
        if not recommendations:
            recommendations.append("Marketing performance is meeting targets. Consider scaling successful campaigns.")
        
        return recommendations
    
    def save_to_json(self, filepath: str):
        """Save the marketing calendar to a JSON file."""
        calendar = self.generate_marketing_calendar()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(calendar, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a marketing calendar from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.marketing_channels = data.get("marketing_channels", self.marketing_channels)
        self.monthly_activities = data.get("monthly_activities", self.monthly_activities)
        self.budget_allocation["monthly_budgets"] = data.get("monthly_budgets", self.budget_allocation["monthly_budgets"])
        self.campaigns = data.get("campaigns", self.campaigns)
        self.content_calendar = data.get("content_calendar", self.content_calendar)
        self.events_schedule = data.get("events_schedule", self.events_schedule)
        self.performance_metrics = data.get("performance_metrics", self.performance_metrics)


def create_sample_calendar() -> MarketingCalendarStrategy:
    """Create a sample marketing calendar with example data."""
    calendar = MarketingCalendarStrategy(company_name="Sample Marketing Strategy Oy", year=2026)
    
    # Set example channel budgets
    calendar.set_channel_budget("digital_ads", 30000)
    calendar.set_channel_budget("social_media", 25000)
    calendar.set_channel_budget("email_marketing", 15000)
    calendar.set_channel_budget("content_marketing", 20000)
    calendar.set_channel_budget("events", 35000)
    calendar.set_channel_budget("pr", 10000)
    
    # Set example monthly activities
    months = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", 
              "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
    
    for i, month in enumerate(months):
        calendar.set_monthly_activity(
            month, 
            f"Activity for {month}", 
            5000 + i*500,  # Increasing budget each month
            0.15 + i*0.01  # Slightly increasing ROI expectation
        )
    
    # Set example campaign details
    calendar.set_campaign_details(
        "campaign_1",
        "Spring Product Launch",
        f"{calendar.year}-03-01",
        f"{calendar.year}-05-31",
        25000,
        ["digital_ads", "social_media", "pr"],
        "Early adopters and tech enthusiasts",
        0.25
    )
    
    calendar.set_campaign_details(
        "campaign_2", 
        "Summer Awareness",
        f"{calendar.year}-06-01",
        f"{calendar.year}-08-31",
        20000,
        ["social_media", "content_marketing", "email_marketing"],
        "General consumer market",
        0.18
    )
    
    # Set performance metrics
    calendar.set_performance_metric("reach", 100000)
    calendar.set_performance_metric("engagement_rate", 0.035)  # 3.5%
    calendar.set_performance_metric("conversion_rate", 0.02)  # 2%
    calendar.set_performance_metric("cost_per_acquisition", 50)
    calendar.set_performance_metric("return_on_ad_spend", 4.2)  # 4.2x
    
    # Add seasonal opportunities
    calendar.add_seasonal_opportunity("spring_opportunities", "Garden and home improvement season")
    calendar.add_seasonal_opportunity("summer_opportunities", "Vacation and outdoor activities")
    calendar.add_seasonal_opportunity("autumn_opportunities", "Back to school and new year resolutions")
    calendar.add_seasonal_opportunity("winter_opportunities", "Holiday shopping season")
    
    return calendar


if __name__ == "__main__":
    # Example usage
    print("Markkinoinnin vuosikello - kehittäminen strategia")
    print("=" * 55)
    
    # Create a sample marketing calendar
    sample_calendar = create_sample_calendar()
    
    # Generate and display the marketing calendar
    calendar = sample_calendar.generate_marketing_calendar()
    
    print(f"\nCompany: {calendar['company_name']}")
    print(f"Year: {calendar['year']}")
    print(f"Total Annual Budget: €{calendar['total_annual_budget']:,.2f}")
    
    print(f"\nMarketing Channels and Budget Allocations:")
    for channel_id, channel_info in calendar['marketing_channels'].items():
        if channel_info['budget_allocation'] > 0:  # Only show channels with budget
            print(f"  {channel_info['name']}: €{channel_info['budget_allocation']:,.2f} "
                  f"({calendar['channel_percentages'][channel_id]:.1f}%)")
    
    print(f"\nMonthly Budget Allocations:")
    for month, budget in list(calendar['monthly_budgets'].items())[:6]:  # Show first 6 months
        print(f"  {month}: €{budget:,.2f}")
    
    print(f"\nPlanned Campaigns:")
    for camp_id, campaign in calendar['campaigns'].items():
        if campaign['budget'] > 0:  # Only show campaigns with budget
            print(f"  {campaign['name']} ({campaign['start_date']} to {campaign['end_date']})")
            print(f"    Budget: €{campaign['budget']:,.2f}")
            print(f"    Target: {campaign['target_audience']}")
            print(f"    Channels: {', '.join(campaign['channels'])}")
    
    print(f"\nSeasonal Opportunities:")
    for season, opportunities in calendar['seasonal_opportunities'].items():
        if opportunities:
            season_name = season.replace("_opportunities", "").replace("_", " ").title()
            print(f"  {season_name}:")
            for opp in opportunities:
                print(f"    - {opp}")
    
    # Generate a sample performance report
    print(f"\nGenerating sample performance report...")
    report = sample_calendar.generate_marketing_report(
        revenue=180000,  # Actual revenue generated
        leads=750,       # Actual leads generated
        customers=45     # Actual customers acquired
    )
    
    actual_metrics = report['actual_performance']
    print(f"\nActual Performance Metrics:")
    print(f"  Actual Revenue: €{actual_metrics['actual_revenue']:,.2f}")
    print(f"  Actual Leads: {actual_metrics['actual_leads']:,}")
    print(f"  Actual Customers: {actual_metrics['actual_customers']:,}")
    print(f"  Marketing ROI: {actual_metrics['marketing_roi']:.2%}")
    print(f"  Cost Per Lead: €{actual_metrics['cost_per_lead']:,.2f}")
    print(f"  Customer Acquisition Cost: €{actual_metrics['customer_acquisition_cost']:,.2f}")
    
    print(f"\nRecommendations:")
    for rec in report['recommendations']:
        print(f"  - {rec}")
    
    # Save the calendar to a JSON file
    sample_calendar.save_to_json("sample_marketing_calendar_strategy.json")
    print(f"\nMarketing calendar strategy saved to 'sample_marketing_calendar_strategy.json'")