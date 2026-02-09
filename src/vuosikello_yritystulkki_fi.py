"""
Python implementation of Vuosikello - yritystulkki.fi annual calendar for business interpreter services.

This module provides programmatic access to the annual calendar functionality
originally implemented in the Vuosikello - yritystulkki.fi.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import json


class BusinessInterpreterCalendar:
    """
    A class representing an annual calendar for business interpreter services based on the 
    Vuosikello - yritystulkki.fi template.
    This tool helps interpreter service providers plan their activities throughout the year, 
    coordinate with client schedules, and manage seasonal demands specific to the business 
    interpretation sector.
    """
    
    def __init__(self, company_name: str = "Business Interpreter Services", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.monthly_activities = {}  # Planned activities by month
        self.client_calendar = {}  # Client schedules and needs
        self.events_schedule = {}  # Events requiring interpretation
        self.language_services = {}  # Language services offered
        self.substitutions = {}  # Substitution arrangements
        self.training_schedule = {}  # Professional development calendar
        self.leave_planning = {}  # Vacation and leave planning
        self.efficiency_metrics = {}  # Performance metrics
        self.pricing_levels = {}  # Service pricing
        self.projects = {}  # Interpretation projects
        self.competitor_monitoring = {}  # Competitor tracking
        self.market_research = {}  # Market research data
        self.expansion_plans = {}  # Growth plans
        self.financial_budget = {}  # Financial planning
        self.profitability_analysis = {}  # Profitability tracking
        self.risk_management = {}  # Risk management
        self.quality_assurance = {}  # Quality assurance measures
        self.customer_satisfaction = {}  # Customer satisfaction tracking
        self.reporting_framework = {}  # Reporting structure
        self.future_planning = {}  # Long-term planning
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the business interpreter calendar with default values."""
        # Define months in Finnish
        self.months = ["Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu", 
                      "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu"]
        
        # Initialize monthly activities with seasonal distribution
        self.monthly_activities = {month: {
            "scheduled_interpretations": 0,
            "revenue_expected": 0,
            "interpreter_hours": 0,
            "client_meetings": 0,
            "training_hours": 0,
            "admin_tasks": 0,
            "seasonal_factor": 1.0  # Adjusts based on season
        } for month in self.months}
        
        # Set seasonal factors based on the spreadsheet data
        # From the extracted data, it appears winter, spring, summer, and autumn each have 0.25 allocation
        self.seasonal_distribution = {
            "talvi": 0.25,  # Winter (Dec, Jan, Feb)
            "kevät": 0.25,  # Spring (Mar, Apr, May)
            "kesä": 0.25,   # Summer (Jun, Jul, Aug)
            "syksy": 0.25   # Autumn (Sep, Oct, Nov)
        }
        
        # Apply seasonal factors to months
        for month in self.months:
            if month in ["Tammikuu", "Helmikuu", "Joulukuu"]:  # Winter months
                self.monthly_activities[month]["seasonal_factor"] = self.seasonal_distribution["talvi"]
            elif month in ["Maaliskuu", "Huhtikuu", "Toukokuu"]:  # Spring months
                self.monthly_activities[month]["seasonal_factor"] = self.seasonal_distribution["kevät"]
            elif month in ["Kesäkuu", "Heinäkuu", "Elokuu"]:  # Summer months
                self.monthly_activities[month]["seasonal_factor"] = self.seasonal_distribution["kesä"]
            else:  # Autumn months
                self.monthly_activities[month]["seasonal_factor"] = self.seasonal_distribution["syksy"]
        
        # Define language services
        self.language_services = {
            "fi_en": {"name": "Finnish-English", "rate_per_hour": 0, "demand_factor": 1.0},
            "fi_sv": {"name": "Finnish-Swedish", "rate_per_hour": 0, "demand_factor": 1.0},
            "fi_ru": {"name": "Finnish-Russian", "rate_per_hour": 0, "demand_factor": 1.0},
            "fi_de": {"name": "Finnish-German", "rate_per_hour": 0, "demand_factor": 1.0},
            "fi_fr": {"name": "Finnish-French", "rate_per_hour": 0, "demand_factor": 1.0},
            "fi_es": {"name": "Finnish-Spanish", "rate_per_hour": 0, "demand_factor": 1.0}
        }
        
        # Define client types
        self.client_types = {
            "corporate": {"name": "Corporate clients", "priority": 1, "seasonal_demand": {"talvi": 0.25, "kevät": 0.25, "kesä": 0.20, "syksy": 0.30}},
            "government": {"name": "Government institutions", "priority": 2, "seasonal_demand": {"talvi": 0.30, "kevät": 0.25, "kesä": 0.15, "syksy": 0.30}},
            "legal": {"name": "Legal proceedings", "priority": 3, "seasonal_demand": {"talvi": 0.25, "kevät": 0.25, "kesä": 0.25, "syksy": 0.25}},
            "medical": {"name": "Medical appointments", "priority": 4, "seasonal_demand": {"talvi": 0.30, "kevät": 0.25, "kesä": 0.20, "syksy": 0.25}}
        }
        
        # Initialize interpreter staff
        self.interpreter_staff = {
            "interpreter_1": {"name": "Interpreeteri: Iina Interpreeteri", "specialties": ["fi_en", "fi_sv"], "availability_hours": 160},
            "interpreter_2": {"name": "Interpreter 2", "specialties": ["fi_ru", "fi_en"], "availability_hours": 160},
            "interpreter_3": {"name": "Interpreter 3", "specialties": ["fi_de", "fi_fr"], "availability_hours": 160},
            "interpreter_4": {"name": "Interpreter 4", "specialties": ["fi_es", "fi_en"], "availability_hours": 120}  # Part-time
        }
        
        # Initialize efficiency metrics
        self.efficiency_metrics = {
            "utilization_rate_target": 0.80,  # 80% target
            "billable_hours_per_day": 6,
            "client_satisfaction_target": 0.95,  # 95% target
            "on_time_completion_rate": 0.98,  # 98% target
            "repeat_client_rate": 0.70  # 70% target
        }
        
        # Initialize pricing levels
        self.pricing_levels = {
            "consecutive_interpretation": {"rate_per_hour": 80, "rate_per_day": 600},
            "simultaneous_interpretation": {"rate_per_hour": 120, "rate_per_day": 900},
            "whispered_interpretation": {"rate_per_hour": 90, "rate_per_day": 700},
            "escort_services": {"rate_per_hour": 70, "rate_per_day": 500},
            "document_translation": {"rate_per_page": 35, "rush_rate_multiplier": 1.5}
        }
    
    def set_monthly_activity(self, month: str, scheduled_interpretations: int, revenue_expected: float, 
                           interpreter_hours: float, client_meetings: int, training_hours: float, admin_tasks: int):
        """Set planned activities for a specific month."""
        if month in self.monthly_activities:
            self.monthly_activities[month]["scheduled_interpretations"] = scheduled_interpretations
            self.monthly_activities[month]["revenue_expected"] = revenue_expected
            self.monthly_activities[month]["interpreter_hours"] = interpreter_hours
            self.monthly_activities[month]["client_meetings"] = client_meetings
            self.monthly_activities[month]["training_hours"] = training_hours
            self.monthly_activities[month]["admin_tasks"] = admin_tasks
        else:
            raise ValueError(f"Unknown month: {month}")
    
    def set_language_service_rate(self, language_pair: str, rate_per_hour: float):
        """Set the hourly rate for a specific language pair."""
        if language_pair in self.language_services:
            self.language_services[language_pair]["rate_per_hour"] = rate_per_hour
        else:
            raise ValueError(f"Unknown language pair: {language_pair}")
    
    def assign_interpreter_to_month(self, interpreter_id: str, month: str, assigned_hours: float):
        """Assign an interpreter to work a certain number of hours in a specific month."""
        if interpreter_id in self.interpreter_staff and month in self.monthly_activities:
            # Track interpreter assignment
            if "assigned_interpreters" not in self.monthly_activities[month]:
                self.monthly_activities[month]["assigned_interpreters"] = {}
            self.monthly_activities[month]["assigned_interpreters"][interpreter_id] = assigned_hours
        else:
            raise ValueError(f"Unknown interpreter ID: {interpreter_id} or month: {month}")
    
    def set_client_requirement(self, client_type: str, month: str, required_hours: float, priority: int = 1):
        """Set client requirements for a specific month."""
        if client_type in self.client_types and month in self.months:
            if "client_requirements" not in self.monthly_activities[month]:
                self.monthly_activities[month]["client_requirements"] = {}
            self.monthly_activities[month]["client_requirements"][client_type] = {
                "required_hours": required_hours,
                "priority": priority
            }
        else:
            raise ValueError(f"Unknown client type: {client_type} or month: {month}")
    
    def calculate_monthly_revenue(self, month: str) -> float:
        """Calculate expected revenue for a specific month."""
        return self.monthly_activities[month]["revenue_expected"]
    
    def calculate_annual_revenue(self) -> float:
        """Calculate total expected annual revenue."""
        return sum(self.monthly_activities[month]["revenue_expected"] for month in self.months)
    
    def calculate_utilization_rate(self) -> float:
        """Calculate the overall utilization rate of interpreter staff."""
        total_contracted_hours = sum(interp["availability_hours"] * 12 for interp in self.interpreter_staff.values())  # Annual contracted hours
        total_assigned_hours = 0
        
        for month in self.months:
            if "assigned_interpreters" in self.monthly_activities[month]:
                for hours in self.monthly_activities[month]["assigned_interpreters"].values():
                    total_assigned_hours += hours
        
        if total_contracted_hours == 0:
            return 0.0
        return total_assigned_hours / total_contracted_hours
    
    def calculate_seasonal_distribution(self) -> Dict[str, float]:
        """Calculate the actual seasonal distribution of activities."""
        seasonal_totals = {"talvi": 0, "kevät": 0, "kesä": 0, "syksy": 0}
        
        # Map months to seasons
        month_to_season = {
            "Tammikuu": "talvi", "Helmikuu": "talvi", "Joulukuu": "talvi",
            "Maaliskuu": "kevät", "Huhtikuu": "kevät", "Toukokuu": "kevät",
            "Kesäkuu": "kesä", "Heinäkuu": "kesä", "Elokuu": "kesä",
            "Syyskuu": "syksy", "Lokakuu": "syksy", "Marraskuu": "syksy"
        }
        
        for month, data in self.monthly_activities.items():
            season = month_to_season.get(month, "unknown")
            if season != "unknown":
                seasonal_totals[season] += data["revenue_expected"]
        
        # Calculate percentages
        total_revenue = self.calculate_annual_revenue()
        if total_revenue == 0:
            return {season: 0.0 for season in seasonal_totals}
        
        return {season: (total / total_revenue) for season, total in seasonal_totals.items()}
    
    def generate_calendar_report(self) -> Dict:
        """Generate a comprehensive business interpreter calendar report."""
        seasonal_distribution = self.calculate_seasonal_distribution()
        utilization_rate = self.calculate_utilization_rate()
        
        # Calculate monthly details
        monthly_details = {}
        for month in self.months:
            monthly_details[month] = {
                "scheduled_interpretations": self.monthly_activities[month]["scheduled_interpretations"],
                "revenue_expected": self.monthly_activities[month]["revenue_expected"],
                "interpreter_hours": self.monthly_activities[month]["interpreter_hours"],
                "client_meetings": self.monthly_activities[month]["client_meetings"],
                "training_hours": self.monthly_activities[month]["training_hours"],
                "admin_tasks": self.monthly_activities[month]["admin_tasks"],
                "seasonal_factor": self.monthly_activities[month]["seasonal_factor"],
                "utilization_rate": self._calculate_monthly_utilization(month)
            }
        
        self.calendar_report = {
            "company_name": self.company_name,
            "year": self.year,
            "monthly_activities": monthly_details,
            "seasonal_distribution": seasonal_distribution,
            "total_annual_revenue": self.calculate_annual_revenue(),
            "utilization_rate": utilization_rate,
            "efficiency_metrics": self.efficiency_metrics,
            "language_services": self.language_services,
            "pricing_levels": self.pricing_levels,
            "interpreter_staff": self.interpreter_staff,
            "client_types": self.client_types
        }
        
        return self.calendar_report
    
    def _calculate_monthly_utilization(self, month: str) -> float:
        """Calculate utilization rate for a specific month."""
        if "assigned_interpreters" not in self.monthly_activities[month]:
            return 0.0
        
        total_monthly_capacity = sum(interp["availability_hours"] for interp in self.interpreter_staff.values())
        total_assigned_hours = sum(self.monthly_activities[month]["assigned_interpreters"].values())
        
        if total_monthly_capacity == 0:
            return 0.0
        return total_assigned_hours / total_monthly_capacity
    
    def generate_interpretation_schedule(self) -> Dict:
        """Generate a detailed interpretation schedule."""
        schedule = {
            "company_name": self.company_name,
            "year": self.year,
            "schedule": {}
        }
        
        for month in self.months:
            schedule["schedule"][month] = {
                "interpretation_assignments": self.monthly_activities[month]["scheduled_interpretations"],
                "expected_revenue": self.monthly_activities[month]["revenue_expected"],
                "required_interpreters": self.monthly_activities[month].get("assigned_interpreters", {}),
                "client_requirements": self.monthly_activities[month].get("client_requirements", {}),
                "seasonal_adjustment": self.monthly_activities[month]["seasonal_factor"]
            }
        
        return schedule
    
    def save_to_json(self, filepath: str):
        """Save the business interpreter calendar to a JSON file."""
        report = self.generate_calendar_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a business interpreter calendar from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.year = data.get("year", self.year)
        self.monthly_activities = data.get("monthly_activities", self.monthly_activities)
        self.language_services = data.get("language_services", self.language_services)
        self.interpreter_staff = data.get("interpreter_staff", self.interpreter_staff)
        self.efficiency_metrics = data.get("efficiency_metrics", self.efficiency_metrics)


def create_sample_calendar() -> BusinessInterpreterCalendar:
    """Create a sample business interpreter calendar with example data."""
    calendar = BusinessInterpreterCalendar(company_name="Sample Business Interpreter Oy", year=2026)
    
    # Set example monthly activities with realistic seasonal variation
    monthly_revenues = [8000, 8500, 9000, 10000, 11000, 12000, 11500, 11000, 10000, 9500, 9000, 8500]
    monthly_interpretations = [12, 13, 14, 16, 18, 20, 19, 18, 16, 15, 14, 13]
    
    for i, month in enumerate(calendar.months):
        calendar.set_monthly_activity(
            month,
            scheduled_interpretations=monthly_interpretations[i],
            revenue_expected=monthly_revenues[i],
            interpreter_hours=monthly_revenues[i] / 60,  # Assuming ~€60/hr average
            client_meetings=max(5, 10 - i//2),  # Fewer meetings later in year
            training_hours=8 + (i % 3) * 2,  # Varying training hours
            admin_tasks=15
        )
    
    # Set language service rates
    calendar.set_language_service_rate("fi_en", 85)
    calendar.set_language_service_rate("fi_sv", 80)
    calendar.set_language_service_rate("fi_ru", 95)
    calendar.set_language_service_rate("fi_de", 90)
    
    # Assign interpreters to months based on availability
    for month_idx, month in enumerate(calendar.months):
        # More intensive months get more interpreter hours
        base_hours = 120 if month in ["Toukokuu", "Kesäkuu", "Heinäkuu", "Elokuu", "Syyskuu"] else 100
        calendar.assign_interpreter_to_month("interpreter_1", month, base_hours)
        calendar.assign_interpreter_to_month("interpreter_2", month, base_hours * 0.8)
        calendar.assign_interpreter_to_month("interpreter_3", month, base_hours * 0.6)
        if month_idx % 2 == 0:  # Part-time interpreter on alternating months
            calendar.assign_interpreter_to_month("interpreter_4", month, base_hours * 0.4)
    
    # Set client requirements
    for month in calendar.months:
        calendar.set_client_requirement("corporate", month, 60, 1)
        calendar.set_client_requirement("government", month, 30, 2)
        calendar.set_client_requirement("legal", month, 20, 3)
        calendar.set_client_requirement("medical", month, 15, 4)
    
    return calendar


if __name__ == "__main__":
    # Example usage
    print("Vuosikello - yritystulkki.fi - Business Interpreter Annual Calendar Tool")
    print("=" * 75)
    
    # Create a sample business interpreter calendar
    sample_calendar = create_sample_calendar()
    
    # Generate and display the calendar report
    report = sample_calendar.generate_calendar_report()
    
    print(f"\nCompany: {report['company_name']}")
    print(f"Year: {report['year']}")
    print(f"Total Annual Revenue: €{report['total_annual_revenue']:,.2f}")
    print(f"Utilization Rate: {report['utilization_rate']:.2%}")
    
    print(f"\nSeasonal Distribution:")
    for season, percentage in report['seasonal_distribution'].items():
        print(f"  {season.title()}: {percentage:.1%}")
    
    print(f"\nLanguage Services and Rates:")
    for lang_pair, details in list(report['language_services'].items())[:4]:  # Show first 4
        if details['rate_per_hour'] > 0:  # Only show if rate is set
            print(f"  {details['name']}: €{details['rate_per_hour']}/hour")
    
    print(f"\nInterpreter Staff:")
    for interp_id, details in report['interpreter_staff'].items():
        print(f"  {details['name']}: {details['availability_hours']} hours/month, specialties: {', '.join(details['specialties'])}")
    
    print(f"\nMonthly Schedule (First 6 months):")
    for month, data in list(report['monthly_activities'].items())[:6]:
        print(f"  {month}: {data['scheduled_interpretations']} interpretations, €{data['revenue_expected']:,.2f}, {data['interpreter_hours']:.1f} hours")
    
    print(f"\nClient Types:")
    for client_type, details in report['client_types'].items():
        print(f"  {details['name']}: Priority {details['priority']}")
    
    # Generate and display the detailed schedule
    print(f"\nGenerating detailed interpretation schedule...")
    schedule = sample_calendar.generate_interpretation_schedule()
    
    print(f"\nDetailed Schedule for {schedule['year']}:")
    for month, data in list(schedule['schedule'].items())[:3]:  # Show first 3 months
        print(f"  {month}: {data['interpretation_assignments']} assignments, €{data['expected_revenue']:,.2f}")
        print(f"    Required Interpreters: {len(data['required_interpreters'])}")
        print(f"    Client Requirements: {len(data['client_requirements'])}")
    
    # Save the calendar to a JSON file
    sample_calendar.save_to_json("sample_business_interpreter_calendar.json")
    print(f"\nBusiness interpreter calendar saved to 'sample_business_interpreter_calendar.json'")