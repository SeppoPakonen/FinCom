"""
Python implementation of H6_Osakasluettelo shareholder list template.

This module provides programmatic access to the shareholder list functionality
originally implemented in the H6_Osakasluettelo.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class ShareholderRegistry:
    """
    A class representing a shareholder registry based on the H6_Osakasluettelo template.
    This tool helps businesses maintain and manage records of their shareholders, 
    including ownership percentages, contact information, and other relevant details 
    for corporate governance and administrative purposes.
    """
    
    def __init__(self, company_name: str = "Shareholder Registry Company", registration_date: str = "10.2.2020"):
        self.company_name = company_name
        self.registration_date = registration_date
        self.company_info = {
            "name_address": "",
            "domicile": "",
            "business_id": "",
            "registration_date": registration_date,
            "business_history": [],
            "industry_code": "",
            "industry_description": ""
        }
        self.shareholders = {}  # Shareholder information
        self.share_classes = {}  # Different share classes
        self.voting_rights = {}  # Voting rights by shareholder/share class
        self.dividend_records = {}  # Dividend payment tracking
        self.meeting_attendance = {}  # Meeting attendance records
        self.share_transfers = {}  # Share transfer history
        self.compliance_records = {}  # Compliance and reporting records
        self.tax_info = {}  # Tax-related information
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the shareholder registry with default values."""
        # Company information
        self.company_info = {
            "name_address": "Malliyritys Oy, Pääkatu 1, 12345 Kotikunta",
            "domicile": "Kotikunta",
            "business_id": "1234567-8",
            "registration_date": self.registration_date,
            "business_history": [
                {"name": "Malliyritys Oy, Kotikunta, alkaen 1.1.2008", "period": "2008-01-01 to present"},
                {"name": "Malliyritys Ky, Kotikunta, alkaen 1.1.2001", "period": "2001-01-01 to 2007-12-31"},
                {"name": "T:mi Malliyritys Matti Meikäläinen, alkaen 1.1.1998", "period": "1998-01-01 to 2000-12-31"}
            ],
            "industry_code": "25990",
            "industry_description": "Muu metallituotteiden valmistus"
        }
        
        # Share classes
        self.share_classes = {
            "class_A": {
                "name": "Ordinary Shares (A)", 
                "voting_rights": 1,  # 1 vote per share
                "dividend_rights": 1,  # Equal dividend rights
                "liquidation_rights": 1  # Equal liquidation rights
            },
            "class_B": {
                "name": "Preference Shares (B)", 
                "voting_rights": 0.5,  # 0.5 votes per share
                "dividend_rights": 1.2,  # 20% higher dividend rights
                "liquidation_rights": 1.1  # 10% higher liquidation rights
            }
        }
        
        # Shareholders information
        self.shareholders = {
            "shareholder_1": {
                "name_birthdate_id": "Meikäläinen Matti (010660)",
                "address": "Kotikatu 12, 00010 Helsinki",
                "tax_municipality": "Helsinki",
                "share_count": 100,
                "share_class": "class_A",
                "transfer_date": "2008-01-01 00:00:00",
                "voting_rights": 100,  # Calculated based on share class
                "ownership_percentage": 0.294,  # Calculated based on total shares
                "contact_info": {
                    "phone": "",
                    "email": "",
                    "representative": ""
                }
            },
            "shareholder_2": {
                "name_birthdate_id": "Meikäläinen Mauno (201063)",
                "address": "Sivukatu 15, 00020 Tampere",
                "tax_municipality": "Tampere",
                "share_count": 100,
                "share_class": "class_A",
                "transfer_date": "2008-01-01 00:00:00",
                "voting_rights": 100,
                "ownership_percentage": 0.294,
                "contact_info": {
                    "phone": "",
                    "email": "",
                    "representative": ""
                }
            },
            "shareholder_3": {
                "name_birthdate_id": "Meikäläinen Timo (051270)",
                "address": "Pääkatu 1, 90100 Oulu",
                "tax_municipality": "Oulu",
                "share_count": 50,
                "share_class": "class_A",
                "transfer_date": "2011-01-01 00:00:00",
                "voting_rights": 50,
                "ownership_percentage": 0.147,
                "contact_info": {
                    "phone": "",
                    "email": "",
                    "representative": ""
                }
            },
            "shareholder_4": {
                "name_birthdate_id": "Meikäläinen Invest Oy (2345678-8)",
                "address": "Pääkatu 1, 90100 Oulu",
                "tax_municipality": "Oulu",
                "share_count": 100,
                "share_class": "class_B",
                "transfer_date": "2019-01-01 00:00:00",
                "voting_rights": 50,  # Class B has 0.5 votes per share
                "ownership_percentage": 0.294,
                "contact_info": {
                    "phone": "",
                    "email": "",
                    "representative": ""
                }
            }
        }
        
        # Initialize total shares
        self.total_shares = sum(sh["share_count"] for sh in self.shareholders.values())
        
        # Calculate ownership percentages
        self._calculate_ownership_percentages()
        
        # Initialize dividend records
        self.dividend_records = {
            "dividend_year_1": {
                "year": 2026,
                "amount_per_share": 0.0,
                "total_dividend": 0.0,
                "payment_date": "",
                "shareholders_paid": []
            }
        }
        
        # Initialize meeting attendance
        self.meeting_attendance = {
            "meeting_1": {
                "date": "2026-06-15",
                "type": "Annual General Meeting",
                "attendees": [],
                "voting_results": {}
            }
        }
        
        # Initialize share transfers
        self.share_transfers = {
            "transfer_1": {
                "date": "2025-03-10",
                "from_shareholder": "",
                "to_shareholder": "",
                "share_count": 0,
                "share_class": "",
                "consideration": 0.0
            }
        }
        
        # Initialize compliance records
        self.compliance_records = {
            "last_registry_update": self.registration_date,
            "compliance_status": "Compliant",
            "next_reporting_date": "",
            "regulatory_submissions": []
        }
    
    def _calculate_ownership_percentages(self):
        """Recalculate ownership percentages based on share counts."""
        if self.total_shares == 0:
            return
        
        for sh_id, shareholder in self.shareholders.items():
            share_class = shareholder["share_class"]
            voting_multiplier = self.share_classes[share_class]["voting_rights"]
            
            shareholder["ownership_percentage"] = shareholder["share_count"] / self.total_shares
            shareholder["voting_rights"] = shareholder["share_count"] * voting_multiplier
    
    def add_shareholder(self, shareholder_id: str, name_birthdate_id: str, address: str, 
                       tax_municipality: str, share_count: int, share_class: str = "class_A", 
                       transfer_date: str = ""):
        """Add a new shareholder to the registry."""
        if share_class not in self.share_classes:
            raise ValueError(f"Unknown share class: {share_class}")
        
        self.shareholders[shareholder_id] = {
            "name_birthdate_id": name_birthdate_id,
            "address": address,
            "tax_municipality": tax_municipality,
            "share_count": share_count,
            "share_class": share_class,
            "transfer_date": transfer_date or str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            "voting_rights": share_count * self.share_classes[share_class]["voting_rights"],
            "ownership_percentage": share_count / self.total_shares if self.total_shares > 0 else 0,
            "contact_info": {
                "phone": "",
                "email": "",
                "representative": ""
            }
        }
        
        # Update total shares and recalculate percentages
        self.total_shares = sum(sh["share_count"] for sh in self.shareholders.values())
        self._calculate_ownership_percentages()
    
    def update_shareholder_shares(self, shareholder_id: str, new_share_count: int):
        """Update the number of shares for a specific shareholder."""
        if shareholder_id not in self.shareholders:
            raise ValueError(f"Unknown shareholder ID: {shareholder_id}")
        
        self.shareholders[shareholder_id]["share_count"] = new_share_count
        
        # Update voting rights based on share class
        share_class = self.shareholders[shareholder_id]["share_class"]
        voting_multiplier = self.share_classes[share_class]["voting_rights"]
        self.shareholders[shareholder_id]["voting_rights"] = new_share_count * voting_multiplier
        
        # Update total shares and recalculate percentages
        self.total_shares = sum(sh["share_count"] for sh in self.shareholders.values())
        self._calculate_ownership_percentages()
    
    def record_share_transfer(self, transfer_id: str, from_shareholder: str, to_shareholder: str, 
                             share_count: int, share_class: str, consideration: float = 0.0, 
                             transfer_date: str = ""):
        """Record a share transfer between shareholders."""
        if from_shareholder not in self.shareholders or to_shareholder not in self.shareholders:
            raise ValueError("Unknown shareholder in transfer")
        
        if share_class not in self.share_classes:
            raise ValueError(f"Unknown share class: {share_class}")
        
        # Update share counts
        self.shareholders[from_shareholder]["share_count"] -= share_count
        self.shareholders[to_shareholder]["share_count"] += share_count
        
        # Record the transfer
        self.share_transfers[transfer_id] = {
            "date": transfer_date or str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            "from_shareholder": from_shareholder,
            "to_shareholder": to_shareholder,
            "share_count": share_count,
            "share_class": share_class,
            "consideration": consideration
        }
        
        # Update total shares and recalculate percentages
        self.total_shares = sum(sh["share_count"] for sh in self.shareholders.values())
        self._calculate_ownership_percentages()
        
        # Update compliance records
        self.compliance_records["last_registry_update"] = str(datetime.now().strftime('%Y-%m-%d'))
    
    def calculate_voting_power(self, shareholder_id: str) -> float:
        """Calculate the total voting power for a specific shareholder."""
        if shareholder_id not in self.shareholders:
            raise ValueError(f"Unknown shareholder ID: {shareholder_id}")
        
        shareholder = self.shareholders[shareholder_id]
        share_class = shareholder["share_class"]
        voting_multiplier = self.share_classes[share_class]["voting_rights"]
        
        return shareholder["share_count"] * voting_multiplier
    
    def get_majority_shareholders(self, threshold: float = 0.10) -> List[Dict]:
        """Get shareholders with ownership above a certain threshold."""
        majority_sh = []
        for sh_id, sh in self.shareholders.items():
            if sh["ownership_percentage"] >= threshold:
                majority_sh.append({
                    "id": sh_id,
                    "name": sh["name_birthdate_id"],
                    "ownership_percentage": sh["ownership_percentage"],
                    "share_count": sh["share_count"]
                })
        
        return sorted(majority_sh, key=lambda x: x["ownership_percentage"], reverse=True)
    
    def generate_shareholder_report(self) -> Dict:
        """Generate a comprehensive shareholder report."""
        # Calculate total voting rights
        total_voting_rights = sum(sh["voting_rights"] for sh in self.shareholders.values())
        
        report = {
            "company_info": self.company_info,
            "total_shares": self.total_shares,
            "total_voting_rights": total_voting_rights,
            "shareholders": self.shareholders,
            "share_classes": self.share_classes,
            "dividend_records": self.dividend_records,
            "meeting_attendance": self.meeting_attendance,
            "share_transfers": self.share_transfers,
            "compliance_records": self.compliance_records,
            "majority_shareholders": self.get_majority_shareholders(0.05),  # Shareholders with >5% ownership
            "summary_stats": {
                "total_shareholders": len(self.shareholders),
                "individual_shareholders": len([sh for sh in self.shareholders.values() if "Oy" not in sh["name_birthdate_id"]]),
                "corporate_shareholders": len([sh for sh in self.shareholders.values() if "Oy" in sh["name_birthdate_id"]]),
                "largest_individual_holder": max(
                    [sh for sh in self.shareholders.values() if "Oy" not in sh["name_birthdate_id"]], 
                    key=lambda x: x["share_count"], 
                    default={"name_birthdate_id": "None", "share_count": 0}
                ),
                "largest_corporate_holder": max(
                    [sh for sh in self.shareholders.values() if "Oy" in sh["name_birthdate_id"]], 
                    key=lambda x: x["share_count"], 
                    default={"name_birthdate_id": "None", "share_count": 0}
                )
            }
        }
        
        return report
    
    def generate_compliance_report(self) -> Dict:
        """Generate a compliance report for regulatory purposes."""
        report = self.generate_shareholder_report()
        
        compliance_report = {
            "company_name": self.company_name,
            "business_id": report["company_info"]["business_id"],
            "reporting_date": str(datetime.now().strftime('%Y-%m-%d')),
            "compliance_status": self.compliance_records["compliance_status"],
            "last_registry_update": self.compliance_records["last_registry_update"],
            "next_reporting_date": self.compliance_records["next_reporting_date"],
            "total_shareholders": report["summary_stats"]["total_shareholders"],
            "total_shares": report["total_shares"],
            "major_shareholders": report["majority_shareholders"],
            "recent_transfers": list(self.share_transfers.values())[-5:],  # Last 5 transfers
            "regulatory_submissions": self.compliance_records["regulatory_submissions"]
        }
        
        return compliance_report
    
    def save_to_json(self, filepath: str):
        """Save the shareholder registry to a JSON file."""
        report = self.generate_shareholder_report()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load a shareholder registry from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.shareholders = data.get("shareholders", self.shareholders)
        self.share_classes = data.get("share_classes", self.share_classes)
        self.total_shares = data.get("total_shares", self.total_shares)
        self.dividend_records = data.get("dividend_records", self.dividend_records)
        self.meeting_attendance = data.get("meeting_attendance", self.meeting_attendance)
        self.share_transfers = data.get("share_transfers", self.share_transfers)
        self.compliance_records = data.get("compliance_records", self.compliance_records)


def create_sample_registry() -> ShareholderRegistry:
    """Create a sample shareholder registry with example data."""
    registry = ShareholderRegistry(company_name="Sample Shareholder Registry Oy", registration_date="15.3.2020")
    
    # Add some example shareholders
    registry.add_shareholder(
        "shareholder_5", 
        "Virtanen Anna (010170)", 
        "Sivukatu 20, 00100 Helsinki", 
        "Helsinki", 
        75, 
        "class_A", 
        "2022-05-20 00:00:00"
    )
    
    registry.add_shareholder(
        "shareholder_6", 
        "Korhonen Ky (1234567-1)", 
        "Pikkukatu 5, 00200 Helsinki", 
        "Helsinki", 
        25, 
        "class_A", 
        "2023-01-10 00:00:00"
    )
    
    # Record a share transfer
    registry.record_share_transfer(
        "transfer_1",
        "shareholder_1",  # From Matti Meikäläinen
        "shareholder_5",  # To Anna Virtanen
        10,  # Transfer 10 shares
        "class_A",
        1000.0,  # Consideration of €1000
        "2025-03-10 00:00:00"
    )
    
    # Update dividend records
    registry.dividend_records["dividend_year_1"] = {
        "year": 2026,
        "amount_per_share": 2.50,
        "total_dividend": registry.total_shares * 2.50,
        "payment_date": "2026-09-30",
        "shareholders_paid": list(registry.shareholders.keys())
    }
    
    # Update meeting attendance
    registry.meeting_attendance["meeting_1"] = {
        "date": "2026-06-15",
        "type": "Annual General Meeting",
        "attendees": ["shareholder_1", "shareholder_2", "shareholder_5"],
        "voting_results": {
            "resolution_1": {"passed": True, "votes_for": 250, "votes_against": 100},
            "resolution_2": {"passed": False, "votes_for": 150, "votes_against": 200}
        }
    }
    
    # Update compliance records
    registry.compliance_records["next_reporting_date"] = "2026-12-31"
    registry.compliance_records["regulatory_submissions"] = [
        {"date": "2025-01-15", "type": "Annual filing", "status": "Submitted"},
        {"date": "2025-06-20", "type": "Share transfer notification", "status": "Approved"}
    ]
    
    return registry


if __name__ == "__main__":
    # Example usage
    print("H6 Osakasluettelo - Shareholder Registry Tool")
    print("=" * 50)
    
    # Create a sample shareholder registry
    sample_registry = create_sample_registry()
    
    # Generate and display the shareholder report
    report = sample_registry.generate_shareholder_report()
    
    print(f"\nCompany: {report['company_info']['name_address']}")
    print(f"Domicile: {report['company_info']['domicile']}")
    print(f"Business ID: {report['company_info']['business_id']}")
    print(f"Registration Date: {report['company_info']['registration_date']}")
    print(f"Industry: {report['company_info']['industry_description']} ({report['company_info']['industry_code']})")
    print(f"Total Shares: {report['total_shares']:,}")
    print(f"Total Shareholders: {report['summary_stats']['total_shareholders']}")
    
    print(f"\nShare Classes:")
    for class_id, details in report['share_classes'].items():
        print(f"  {details['name']}: {details['voting_rights']} votes/share, {details['dividend_rights']} dividend rights")
    
    print(f"\nShareholders:")
    for sh_id, sh in report['shareholders'].items():
        print(f"  {sh['name_birthdate_id']}")
        print(f"    Address: {sh['address']}")
        print(f"    Tax Municipality: {sh['tax_municipality']}")
        print(f"    Shares: {sh['share_count']:,} ({sh['ownership_percentage']:.2%})")
        print(f"    Voting Rights: {sh['voting_rights']:,}")
        print(f"    Share Class: {sh['share_class']}")
        print(f"    Transfer Date: {sh['transfer_date']}")
        print()
    
    print(f"Largest Individual Shareholder: {report['summary_stats']['largest_individual_holder']['name_birthdate_id']} with {report['summary_stats']['largest_individual_holder']['share_count']} shares")
    print(f"Largest Corporate Shareholder: {report['summary_stats']['largest_corporate_holder']['name_birthdate_id']} with {report['summary_stats']['largest_corporate_holder']['share_count']} shares")
    
    print(f"\nMajority Shareholders (>5% ownership):")
    for sh in report['majority_shareholders']:
        print(f"  {sh['name']}: {sh['ownership_percentage']:.2%} ({sh['share_count']} shares)")
    
    print(f"\nRecent Share Transfers:")
    for transfer_id, transfer in list(sample_registry.share_transfers.items())[-3:]:  # Show last 3 transfers
        print(f"  {transfer['date']}: {transfer['share_count']} shares of class {transfer['share_class']} transferred from {transfer['from_shareholder']} to {transfer['to_shareholder']} for €{transfer['consideration']}")
    
    print(f"\nDividend Information:")
    for div_id, div_info in report['dividend_records'].items():
        print(f"  Year {div_info['year']}: €{div_info['amount_per_share']}/share, Total: €{div_info['total_dividend']:,.2f}")
    
    # Generate and display compliance report
    print(f"\nGenerating compliance report...")
    compliance_report = sample_registry.generate_compliance_report()
    print(f"Compliance Status: {compliance_report['compliance_status']}")
    print(f"Last Registry Update: {compliance_report['last_registry_update']}")
    print(f"Next Reporting Date: {compliance_report['next_reporting_date']}")
    
    # Save the registry to a JSON file
    sample_registry.save_to_json("sample_shareholder_registry.json")
    print(f"\nShareholder registry saved to 'sample_shareholder_registry.json'")