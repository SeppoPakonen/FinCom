"""
Python implementation of YT28_Myyntisuunnitelma sales plan template.

This module provides programmatic access to the sales plan functionality
originally implemented in the YT28_Myyntisuunnitelma.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class SalesPlan:
    """
    A class representing a sales plan based on the YT28_Myyntisuunnitelma template.
    This tool helps businesses plan and organize their sales activities, set targets, 
    track performance, and coordinate sales efforts across different channels and regions.
    """
    
    def __init__(self, company_name: str = "Sales Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.sales_targets = {}  # Sales targets by product/region
        self.customer_segments = {}  # Customer segments and their characteristics
        self.sales_channels = {}  # Sales channels and their strategies
        self.geographic_territories = {}  # Geographic territories and their plans
        self.sales_team = {}  # Sales team assignments and responsibilities
        self.performance_metrics = {}  # KPIs and performance metrics
        self.competitor_analysis = {}  # Competitor monitoring
        self.risk_management = {}  # Sales risk management
        self.forecasts = {}  # Sales forecasts
        self.sales_calendar = {}  # Calendar of sales activities
        self.roi_calculations = {}  # ROI calculations for sales activities
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the sales plan with default values."""
        # Define sales targets by product
        self.product_targets = {
            "product_1": {"name": "Tuote 1: Esimerkki-ikkuna", "target_amount": 0, "target_units": 0},
            "product_2": {"name": "Tuote 2", "target_amount": 0, "target_units": 0},
            "product_3": {"name": "Tuote 3", "target_amount": 0, "target_units": 0},
            "product_4": {"name": "Tuote 4", "target_amount": 0, "target_units": 0},
            "product_5": {"name": "Tuote 5", "target_amount": 0, "target_units": 0}
        }
        
        # Define customer segments
        self.customer_segments = {
            "segment_1": {"name": "Asiakassegmentti 1", "characteristics": "", "target_customers": 0},
            "segment_2": {"name": "Asiakassegmentti 2", "characteristics": "", "target_customers": 0},
            "segment_3": {"name": "Asiakassegmentti 3", "characteristics": "", "target_customers": 0}
        }
        
        # Define sales channels
        self.sales_channels = {
            "direct_sales": {"name": "Direct Sales", "target_revenue": 0, "conversion_rate": 0.0},
            "inside_sales": {"name": "Inside Sales", "target_revenue": 0, "conversion_rate": 0.0},
            "field_sales": {"name": "Field Sales", "target_revenue": 0, "conversion_rate": 0.0},
            "e_commerce": {"name": "E-commerce", "target_revenue": 0, "conversion_rate": 0.0},
            "retail": {"name": "Retail", "target_revenue": 0, "conversion_rate": 0.0},
            "partners": {"name": "Partners", "target_revenue": 0, "conversion_rate": 0.0}
        }
        
        # Define geographic territories
        self.geographic_territories = {
            "territory_1": {"name": "Alue 1", "target_revenue": 0, "sales_rep": ""},
            "territory_2": {"name": "Alue 2", "target_revenue": 0, "sales_rep": ""},
            "territory_3": {"name": "Alue 3", "target_revenue": 0, "sales_rep": ""}
        }
        
        # Define sales team members
        self.sales_team = {
            "member_1": {"name": "Myyjä: Mikko Myyjä", "territory": "", "targets": {}, "activities": []},
            "member_2": {"name": "Sales Rep 2", "territory": "", "targets": {}, "activities": []},
            "member_3": {"name": "Sales Rep 3", "territory": "", "targets": {}, "activities": []}
        }
        
        # Define performance metrics
        self.performance_metrics = {
            "revenue_target": 0,
            "revenue_actual": 0,
            "sales_cycle_length": 0,  # in days
            "win_rate": 0.0,  # percentage
            "average_deal_size": 0,
            "pipeline_value": 0,
            "conversion_rate": 0.0,
            "customer_acquisition_cost": 0,
            "customer_lifetime_value": 0,
            "marketing_cost": 0,
            "customers_acquired": 0,
            "active_opportunities": 0
        }
        
        # Define competitor analysis
        self.competitor_analysis = {
            "competitor_1": {"name": "Kilpailija 1", "strengths": "", "weaknesses": "", "market_share": 0.0},
            "competitor_2": {"name": "Kilpailija 2", "strengths": "", "weaknesses": "", "market_share": 0.0},
            "competitor_3": {"name": "Kilpailija 3", "strengths": "", "weaknesses": "", "market_share": 0.0}
        }
        
        # Define risk management
        self.risk_management = {
            "risk_1": {"description": "Risk 1", "probability": 0.0, "impact": 0, "mitigation_strategy": ""},
            "risk_2": {"description": "Risk 2", "probability": 0.0, "impact": 0, "mitigation_strategy": ""},
            "risk_3": {"description": "Risk 3", "probability": 0.0, "impact": 0, "mitigation_strategy": ""}
        }
    
    def set_product_target(self, product_id: str, amount: float, units: int):
        """Set the sales target for a specific product."""
        if product_id in self.product_targets:
            self.product_targets[product_id]["target_amount"] = amount
            self.product_targets[product_id]["target_units"] = units
        else:
            raise ValueError(f"Unknown product ID: {product_id}")
    
    def set_customer_segment_characteristics(self, segment_id: str, characteristics: str, target_customers: int):
        """Set characteristics and target for a customer segment."""
        if segment_id in self.customer_segments:
            self.customer_segments[segment_id]["characteristics"] = characteristics
            self.customer_segments[segment_id]["target_customers"] = target_customers
        else:
            raise ValueError(f"Unknown customer segment ID: {segment_id}")
    
    def set_sales_channel_target(self, channel_id: str, target_revenue: float, conversion_rate: float):
        """Set the target for a specific sales channel."""
        if channel_id in self.sales_channels:
            self.sales_channels[channel_id]["target_revenue"] = target_revenue
            self.sales_channels[channel_id]["conversion_rate"] = conversion_rate
        else:
            raise ValueError(f"Unknown sales channel ID: {channel_id}")
    
    def assign_sales_rep_to_territory(self, rep_id: str, territory_id: str):
        """Assign a sales rep to a territory."""
        if rep_id in self.sales_team and territory_id in self.geographic_territories:
            self.sales_team[rep_id]["territory"] = territory_id
            self.geographic_territories[territory_id]["sales_rep"] = self.sales_team[rep_id]["name"]
        else:
            raise ValueError(f"Unknown rep ID: {rep_id} or territory ID: {territory_id}")
    
    def set_performance_metric(self, metric: str, value: float):
        """Set a performance metric value."""
        if metric in self.performance_metrics:
            self.performance_metrics[metric] = value
        else:
            raise ValueError(f"Unknown performance metric: {metric}")
    
    def add_sales_activity(self, rep_id: str, activity: Dict):
        """Add a sales activity for a specific rep."""
        if rep_id in self.sales_team:
            self.sales_team[rep_id]["activities"].append(activity)
        else:
            raise ValueError(f"Unknown sales rep ID: {rep_id}")
    
    def calculate_total_revenue_target(self) -> float:
        """Calculate the total revenue target across all products and channels."""
        total = 0
        for product in self.product_targets.values():
            total += product["target_amount"]
        return total
    
    def calculate_pipeline_coverage_ratio(self) -> float:
        """Calculate the pipeline coverage ratio (pipeline value / target revenue)."""
        target = self.performance_metrics["revenue_target"]
        if target == 0:
            return 0
        return self.performance_metrics["pipeline_value"] / target
    
    def calculate_sales_efficiency(self) -> float:
        """Calculate sales efficiency (revenue generated per salesperson)."""
        num_salespeople = len([rep for rep in self.sales_team.values() if rep["territory"]])
        if num_salespeople == 0:
            return 0
        return self.performance_metrics["revenue_actual"] / num_salespeople
    
    def calculate_customer_acquisition_cost(self) -> float:
        """Calculate the cost per customer acquired."""
        total_sales_cost = sum([
            self.performance_metrics["marketing_cost"],
            sum(rep.get("travel_expenses", 0) for rep in self.sales_team.values()),
            sum(rep.get("training_cost", 0) for rep in self.sales_team.values())
        ])
        customers_acquired = self.performance_metrics["customers_acquired"]
        if customers_acquired == 0:
            return float('inf')
        return total_sales_cost / customers_acquired
    
    def generate_sales_report(self) -> Dict:
        """Generate a comprehensive sales report."""
        # Calculate derived metrics
        pipeline_coverage = self.calculate_pipeline_coverage_ratio()
        sales_efficiency = self.calculate_sales_efficiency()
        customer_acquisition_cost = self.calculate_customer_acquisition_cost()
        
        # Calculate achievement percentages
        revenue_achievement = 0
        if self.performance_metrics["revenue_target"] != 0:
            revenue_achievement = (self.performance_metrics["revenue_actual"] / 
                                   self.performance_metrics["revenue_target"]) * 100
        
        report = {
            "company_name": self.company_name,
            "year": self.year,
            "sales_targets": self.product_targets,
            "customer_segments": self.customer_segments,
            "sales_channels": self.sales_channels,
            "geographic_territories": self.geographic_territories,
            "sales_team": self.sales_team,
            "performance_metrics": {
                **self.performance_metrics,
                "pipeline_coverage_ratio": pipeline_coverage,
                "sales_efficiency": sales_efficiency,
                "customer_acquisition_cost": customer_acquisition_cost,
                "revenue_achievement_percentage": revenue_achievement
            },
            "competitor_analysis": self.competitor_analysis,
            "risk_management": self.risk_management,
            "total_revenue_target": self.calculate_total_revenue_target()
        }
        
        return report
    
    def generate_sales_dashboard(self) -> Dict:
        """Generate a sales dashboard with key metrics."""
        report = self.generate_sales_report()
        
        dashboard = {
            "company_name": self.company_name,
            "year": self.year,
            "key_metrics": {
                "total_revenue_target": report["total_revenue_target"],
                "revenue_actual": report["performance_metrics"]["revenue_actual"],
                "revenue_achievement_percentage": report["performance_metrics"]["revenue_achievement_percentage"],
                "pipeline_value": report["performance_metrics"]["pipeline_value"],
                "pipeline_coverage_ratio": report["performance_metrics"]["pipeline_coverage_ratio"],
                "active_opportunities": report["performance_metrics"].get("active_opportunities", 0),
                "win_rate": report["performance_metrics"]["win_rate"],
                "sales_cycle_length": report["performance_metrics"]["sales_cycle_length"],
                "average_deal_size": report["performance_metrics"]["average_deal_size"],
                "sales_efficiency": report["performance_metrics"]["sales_efficiency"]
            },
            "top_products": sorted(
                [(pid, prod["name"], prod["target_amount"]) 
                 for pid, prod in report["sales_targets"].items()],
                key=lambda x: x[2], reverse=True
            )[:3],  # Top 3 products by target amount
            "top_territories": sorted(
                [(tid, terr["name"], terr["target_revenue"]) 
                 for tid, terr in report["geographic_territories"].items()],
                key=lambda x: x[2], reverse=True
            )[:3],  # Top 3 territories by target revenue
            "team_performance": {
                rep_id: {
                    "name": rep["name"],
                    "territory": rep["territory"],
                    "activities_completed": len(rep["activities"])
                }
                for rep_id, rep in report["sales_team"].items()
            }
        }
        
        return dashboard
    
    def save_to_json(self, filepath: str):
        """Save the sales plan to a JSON file."""
        report = self.generate_sales_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a sales plan from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.product_targets = data.get("sales_targets", self.product_targets)
        self.customer_segments = data.get("customer_segments", self.customer_segments)
        self.sales_channels = data.get("sales_channels", self.sales_channels)
        self.geographic_territories = data.get("geographic_territories", self.geographic_territories)
        self.sales_team = data.get("sales_team", self.sales_team)
        self.performance_metrics = data.get("performance_metrics", self.performance_metrics)
        self.competitor_analysis = data.get("competitor_analysis", self.competitor_analysis)
        self.risk_management = data.get("risk_management", self.risk_management)


def create_sample_plan() -> SalesPlan:
    """Create a sample sales plan with example data."""
    plan = SalesPlan(company_name="Sample Sales Co", year=2026)
    
    # Set example product targets
    plan.set_product_target("product_1", 137900, 479)  # From the spreadsheet example
    plan.set_product_target("product_2", 90000, 900)
    plan.set_product_target("product_3", 21000, 210)
    
    # Set customer segment characteristics
    plan.set_customer_segment_characteristics(
        "segment_1", 
        "Asunto Oy, Hervanta - Residential property cooperative in Hervanta district", 
        50
    )
    plan.set_customer_segment_characteristics(
        "segment_2", 
        "Asunto Oy, Kaleva - Residential property cooperative in Kaleva district", 
        30
    )
    
    # Set sales channel targets
    plan.set_sales_channel_target("direct_sales", 100000, 0.15)
    plan.set_sales_channel_target("e_commerce", 50000, 0.08)
    plan.set_sales_channel_target("retail", 30000, 0.12)
    
    # Assign sales reps to territories
    plan.assign_sales_rep_to_territory("member_1", "territory_1")
    plan.assign_sales_rep_to_territory("member_2", "territory_2")
    
    # Set performance metrics
    plan.set_performance_metric("revenue_target", 200000)
    plan.set_performance_metric("revenue_actual", 180000)
    plan.set_performance_metric("sales_cycle_length", 45)
    plan.set_performance_metric("win_rate", 0.30)  # 30%
    plan.set_performance_metric("average_deal_size", 5000)
    plan.set_performance_metric("pipeline_value", 300000)
    plan.set_performance_metric("conversion_rate", 0.10)  # 10%
    plan.set_performance_metric("marketing_cost", 25000)
    plan.set_performance_metric("customers_acquired", 150)
    plan.set_performance_metric("active_opportunities", 45)
    
    # Add example sales activities
    plan.add_sales_activity("member_1", {
        "date": "2026-02-03",
        "activity_type": "phone_call",
        "description": "Soitto 3.2.20XX. Asiakaskäynti 7.2.20XX",
        "outcome": "Follow-up scheduled"
    })
    
    plan.add_sales_activity("member_1", {
        "date": "2026-01-08",
        "activity_type": "email",
        "description": "Sähköposti 3kpl",
        "outcome": "Response received"
    })
    
    # Set competitor analysis
    plan.competitor_analysis["competitor_1"]["strengths"] = "Strong brand recognition"
    plan.competitor_analysis["competitor_1"]["weaknesses"] = "Higher prices"
    plan.competitor_analysis["competitor_1"]["market_share"] = 0.25  # 25%
    
    plan.competitor_analysis["competitor_2"]["strengths"] = "Lower prices"
    plan.competitor_analysis["competitor_2"]["weaknesses"] = "Limited product range"
    plan.competitor_analysis["competitor_2"]["market_share"] = 0.18  # 18%
    
    # Set risk management
    plan.risk_management["risk_1"]["description"] = "Economic downturn affecting customer spending"
    plan.risk_management["risk_1"]["probability"] = 0.3  # 30%
    plan.risk_management["risk_1"]["impact"] = 25000  # €25k revenue impact
    plan.risk_management["risk_1"]["mitigation_strategy"] = "Diversify customer base and offer flexible payment options"
    
    return plan


if __name__ == "__main__":
    # Example usage
    print("YT28 Myyntisuunnitelma - Sales Plan Tool")
    print("=" * 50)
    
    # Create a sample sales plan
    sample_plan = create_sample_plan()
    
    # Generate and display the sales report
    report = sample_plan.generate_sales_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Year: {report['year']}")
    print(f"Total Revenue Target: €{report['total_revenue_target']:,.2f}")
    print(f"Actual Revenue: €{report['performance_metrics']['revenue_actual']:,.2f}")
    print(f"Revenue Achievement: {report['performance_metrics']['revenue_achievement_percentage']:.1f}%")
    
    print(f"\nTop Products by Target Amount:")
    for pid, product in list(report['sales_targets'].items())[:3]:  # Show top 3
        if product['target_amount'] > 0:
            print(f"  {product['name']}: €{product['target_amount']:,.2f} ({product['target_units']} units)")
    
    print(f"\nSales Team:")
    for rep_id, rep in report['sales_team'].items():
        if rep['territory']:
            print(f"  {rep['name']} - Territory: {rep['territory']}, Activities: {len(rep['activities'])}")
    
    print(f"\nKey Performance Metrics:")
    pm = report['performance_metrics']
    print(f"  Pipeline Coverage Ratio: {pm['pipeline_coverage_ratio']:.2f}x")
    print(f"  Win Rate: {pm['win_rate']:.1%}")
    print(f"  Avg. Deal Size: €{pm['average_deal_size']:,.2f}")
    print(f"  Sales Cycle Length: {pm['sales_cycle_length']} days")
    print(f"  Sales Efficiency: €{pm['sales_efficiency']:,.2f}/rep")
    
    # Generate and display the sales dashboard
    print(f"\nGenerating sales dashboard...")
    dashboard = sample_plan.generate_sales_dashboard()
    
    print(f"\nSales Dashboard:")
    km = dashboard['key_metrics']
    print(f"  Total Revenue Target: €{km['total_revenue_target']:,.2f}")
    print(f"  Actual Revenue: €{km['revenue_actual']:,.2f}")
    print(f"  Pipeline Value: €{km['pipeline_value']:,.2f}")
    print(f"  Pipeline Coverage: {km['pipeline_coverage_ratio']:.2f}x")
    print(f"  Active Opportunities: {km['active_opportunities']}")
    print(f"  Win Rate: {km['win_rate']:.1%}")
    
    print(f"\nTop Territories:")
    for tid, name, target in dashboard['top_territories']:
        print(f"  {name}: €{target:,.2f}")
    
    # Save the report to a JSON file
    sample_plan.save_to_json("sample_sales_plan.json")
    print("\nSales plan saved to 'sample_sales_plan.json'")