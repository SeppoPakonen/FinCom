"""
Python implementation of L2_Tarjouspyynto request for proposal template.

This module provides programmatic access to the request for proposal functionality
originally implemented in the L2_Tarjouspyynto.xlsx spreadsheet.
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json


class RequestForProposal:
    """
    A class representing a request for proposal based on the L2_Tarjouspyynto template.
    This tool helps businesses create professional requests for proposals from potential 
    vendors or service providers, outlining project requirements, evaluation criteria, 
    and submission guidelines.
    """
    
    def __init__(self, company_name: str = "RFP Company", year: int = 2026):
        self.company_name = company_name
        self.year = year
        self.rfp_date = datetime.now().strftime('%d.%m.%Y')
        self.rfp_reference = ""
        self.contact_person = ""
        self.contact_info = ""
        self.project_description = {}
        self.content_requirements = {}
        self.evaluation_criteria = {}
        self.timeline = {}
        self.required_proposal_content = {}
        self.attachments = []
        self.terms_conditions = {}
        self.budget_expectations = {}
        self.quality_requirements = {}
        self.delivery_terms = {}
        self.payment_terms = {}
        self.vendor_qualifications = {}
        self.risk_management_requirements = {}
        self.warranty_terms = {}
        self.project_management_requirements = {}
        self.vendor_evaluation_matrix = {}
        self.submission_guidelines = {}
        self.qa_session_info = {}
        
        # Initialize with default values
        self._initialize_defaults()
    
    def _initialize_defaults(self):
        """Initialize the RFP with default values."""
        # Project description defaults
        self.project_description = {
            "title": "Project Title",
            "overview": "Brief project overview",
            "objectives": [],
            "scope": "",
            "deliverables": [],
            "timeline_high_level": "Project duration",
            "location": "Project location"
        }
        
        # Content requirements
        self.content_requirements = {
            "executive_summary": True,
            "technical_approach": True,
            "project_timeline": True,
            "team_qualifications": True,
            "pricing_structure": True,
            "references": True,
            "risk_management_plan": False,
            "sustainability_plan": False
        }
        
        # Evaluation criteria with weights (total should be 100%)
        self.evaluation_criteria = {
            "technical_competence": {"weight": 0.30, "description": "Technical competence and approach"},
            "cost_competitiveness": {"weight": 0.25, "description": "Cost competitiveness"},
            "past_experience": {"weight": 0.20, "description": "Past experience and references"},
            "project_timeline": {"weight": 0.15, "description": "Project timeline and feasibility"},
            "innovation": {"weight": 0.10, "description": "Innovation and added value"}
        }
        
        # Timeline for RFP process
        self.timeline = {
            "rfp_issue_date": self.rfp_date,
            "qa_session_date": "",
            "proposal_deadline": "",
            "evaluation_period": "",  # e.g., "2 weeks from proposal deadline"
            "award_notification": "",
            "project_start_date": ""
        }
        
        # Required proposal content
        self.required_proposal_content = {
            "company_profile": True,
            "understanding_of_requirements": True,
            "methodology": True,
            "project_schedule": True,
            "resource_allocation": True,
            "pricing_details": True,
            "team_bios": True,
            "case_studies": True,
            "references": True,
            "terms_and_conditions_response": True
        }
        
        # Budget expectations
        self.budget_expectations = {
            "estimated_budget_range_min": 0,
            "estimated_budget_range_max": 0,
            "budget_flexibility": "Medium",
            "payment_schedule_preference": "Milestone-based",
            "currency": "EUR"
        }
        
        # Vendor qualifications
        self.vendor_qualifications = {
            "minimum_experience_years": 3,
            "relevant_project_examples": 2,
            "certifications_required": [],
            "financial_stability_proof": True,
            "insurance_requirements": "Professional indemnity and general liability"
        }
        
        # Submission guidelines
        self.submission_guidelines = {
            "submission_format": "PDF document and electronic files",
            "number_of_copies": 3,
            "submission_method": "Electronic submission via email",
            "late_submission_policy": "Late submissions will not be accepted",
            "confidentiality_agreement": True
        }
    
    def set_project_details(self, title: str, overview: str, scope: str, location: str):
        """Set the main project details."""
        self.project_description["title"] = title
        self.project_description["overview"] = overview
        self.project_description["scope"] = scope
        self.project_description["location"] = location
    
    def add_project_objective(self, objective: str):
        """Add an objective for the project."""
        self.project_description["objectives"].append(objective)
    
    def add_deliverable(self, deliverable: str, description: str = ""):
        """Add a deliverable to the project."""
        self.project_description["deliverables"].append({
            "name": deliverable,
            "description": description
        })
    
    def set_evaluation_criterion(self, criterion: str, weight: float, description: str = ""):
        """Set the weight and description for an evaluation criterion."""
        if criterion in self.evaluation_criteria:
            self.evaluation_criteria[criterion]["weight"] = weight
            if description:
                self.evaluation_criteria[criterion]["description"] = description
        else:
            self.evaluation_criteria[criterion] = {
                "weight": weight,
                "description": description
            }
    
    def set_vendor_qualification(self, qualification: str, value):
        """Set a vendor qualification requirement."""
        if qualification in self.vendor_qualifications:
            self.vendor_qualifications[qualification] = value
        else:
            raise ValueError(f"Unknown vendor qualification: {qualification}")
    
    def set_timeline_milestone(self, milestone: str, date: str):
        """Set a date for a specific RFP process milestone."""
        if milestone in self.timeline:
            self.timeline[milestone] = date
        else:
            raise ValueError(f"Unknown timeline milestone: {milestone}")
    
    def set_budget_range(self, min_budget: float, max_budget: float):
        """Set the estimated budget range."""
        self.budget_expectations["estimated_budget_range_min"] = min_budget
        self.budget_expectations["estimated_budget_range_max"] = max_budget
    
    def calculate_total_evaluation_weight(self) -> float:
        """Calculate the total weight of all evaluation criteria."""
        return sum(item["weight"] for item in self.evaluation_criteria.values())
    
    def evaluate_proposal(self, vendor_name: str, scores: Dict[str, float]) -> Dict:
        """
        Evaluate a vendor's proposal based on the defined criteria.
        
        Args:
            vendor_name: Name of the vendor
            scores: Dictionary with criterion names as keys and scores (0-10) as values
        
        Returns:
            Dictionary with evaluation results
        """
        total_score = 0
        weighted_scores = {}
        
        for criterion, details in self.evaluation_criteria.items():
            if criterion in scores:
                score = scores[criterion]
                weight = details["weight"]
                weighted_score = score * weight
                weighted_scores[criterion] = {
                    "raw_score": score,
                    "weight": weight,
                    "weighted_score": weighted_score
                }
                total_score += weighted_score
            else:
                # If a criterion is not scored, we'll assign it a default low score
                weighted_scores[criterion] = {
                    "raw_score": 0,
                    "weight": details["weight"],
                    "weighted_score": 0
                }
        
        evaluation_result = {
            "vendor_name": vendor_name,
            "total_score": total_score,
            "weighted_scores": weighted_scores,
            "rank": 0  # Will be calculated later when comparing with other vendors
        }
        
        return evaluation_result
    
    def generate_rfp_document(self) -> Dict:
        """Generate a complete RFP document."""
        # Calculate total evaluation weight
        total_weight = self.calculate_total_evaluation_weight()
        
        rfp_doc = {
            "company_name": self.company_name,
            "rfp_date": self.rfp_date,
            "rfp_reference": self.rfp_reference,
            "contact_person": self.contact_person,
            "contact_info": self.contact_info,
            "project_description": self.project_description,
            "content_requirements": self.content_requirements,
            "evaluation_criteria": self.evaluation_criteria,
            "evaluation_criteria_total_weight": total_weight,
            "rfp_timeline": self.timeline,
            "required_proposal_content": self.required_proposal_content,
            "attachments": self.attachments,
            "terms_conditions": self.terms_conditions,
            "budget_expectations": self.budget_expectations,
            "quality_requirements": self.quality_requirements,
            "delivery_terms": self.delivery_terms,
            "payment_terms": self.payment_terms,
            "vendor_qualifications": self.vendor_qualifications,
            "risk_management_requirements": self.risk_management_requirements,
            "warranty_terms": self.warranty_terms,
            "project_management_requirements": self.project_management_requirements,
            "submission_guidelines": self.submission_guidelines,
            "qa_session_info": self.qa_session_info
        }
        
        return rfp_doc
    
    def generate_evaluation_template(self) -> Dict:
        """Generate an evaluation template for reviewing vendor proposals."""
        evaluation_template = {
            "rfp_reference": self.rfp_reference,
            "evaluation_criteria": [
                {
                    "criterion": criterion,
                    "description": details["description"],
                    "weight": details["weight"],
                    "max_score": 10,
                    "scoring_guide": self._get_scoring_guide(criterion)
                }
                for criterion, details in self.evaluation_criteria.items()
            ],
            "vendor_comparison_table": {
                "headers": ["Vendor", "Technical Competence", "Cost Competitiveness", "Past Experience", 
                           "Project Timeline", "Innovation", "Total Score", "Ranking"],
                "vendors": []
            }
        }
        
        return evaluation_template
    
    def _get_scoring_guide(self, criterion: str) -> str:
        """Get a scoring guide for a specific criterion."""
        guides = {
            "technical_competence": "Score from 1-10 based on relevance of approach, methodology, and technical skills",
            "cost_competitiveness": "Score from 1-10 based on value for money, pricing transparency, and competitiveness",
            "past_experience": "Score from 1-10 based on relevant experience, case studies, and client references",
            "project_timeline": "Score from 1-10 based on feasibility, milestone planning, and resource allocation",
            "innovation": "Score from 1-10 based on creativity, added value, and innovative approaches"
        }
        return guides.get(criterion, "Score from 1-10 based on the criterion description")
    
    def save_to_json(self, filepath: str):
        """Save the RFP to a JSON file."""
        rfp_doc = self.generate_rfp_document()
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(rfp_doc, f, indent=2, ensure_ascii=False, default=str)
    
    def load_from_json(self, filepath: str):
        """Load an RFP from a JSON file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update attributes based on loaded data
        self.company_name = data.get("company_name", self.company_name)
        self.rfp_date = data.get("rfp_date", self.rfp_date)
        self.rfp_reference = data.get("rfp_reference", self.rfp_reference)
        self.contact_person = data.get("contact_person", self.contact_person)
        self.contact_info = data.get("contact_info", self.contact_info)
        self.project_description = data.get("project_description", self.project_description)
        self.content_requirements = data.get("content_requirements", self.content_requirements)
        self.evaluation_criteria = data.get("evaluation_criteria", self.evaluation_criteria)
        self.timeline = data.get("rfp_timeline", self.timeline)
        self.required_proposal_content = data.get("required_proposal_content", self.required_proposal_content)
        self.attachments = data.get("attachments", self.attachments)
        self.terms_conditions = data.get("terms_conditions", self.terms_conditions)
        self.budget_expectations = data.get("budget_expectations", self.budget_expectations)
        self.vendor_qualifications = data.get("vendor_qualifications", self.vendor_qualifications)
        self.submission_guidelines = data.get("submission_guidelines", self.submission_guidelines)


def create_sample_rfp() -> RequestForProposal:
    """Create a sample RFP with example data."""
    rfp = RequestForProposal(company_name="Sample RFP Oy", year=2026)
    
    # Set RFP details
    rfp.rfp_reference = "RFP-2026-001"
    rfp.contact_person = "Matti Meikäläinen"
    rfp.contact_info = "matti.meikalainen@samplecompany.fi, p. 050 123 4567"
    
    # Set project details
    rfp.set_project_details(
        title="Digital Marketing Campaign for New Product Launch",
        overview="Request for a comprehensive digital marketing campaign to promote our new product line.",
        scope="Development and execution of a 3-month digital marketing campaign including social media, content marketing, and paid advertising.",
        location="Primarily online with some local events in Tampere area"
    )
    
    # Add project objectives
    rfp.add_project_objective("Increase brand awareness for new product line")
    rfp.add_project_objective("Generate qualified leads for sales team")
    rfp.add_project_objective("Establish digital presence in target markets")
    
    # Add deliverables
    rfp.add_deliverable("Social media strategy and content calendar")
    rfp.add_deliverable("Paid advertising campaigns (Google Ads, Facebook Ads)")
    rfp.add_deliverable("Monthly performance reports")
    rfp.add_deliverable("Campaign optimization recommendations")
    
    # Set evaluation criteria with weights that sum to 1.0
    rfp.set_evaluation_criterion("technical_competence", 0.30, "Technical competence and approach")
    rfp.set_evaluation_criterion("cost_competitiveness", 0.25, "Cost competitiveness and value for money")
    rfp.set_evaluation_criterion("past_experience", 0.20, "Relevant past experience and references")
    rfp.set_evaluation_criterion("project_timeline", 0.15, "Project timeline and feasibility")
    rfp.set_evaluation_criterion("innovation", 0.10, "Innovation and added value")
    
    # Set RFP process timeline
    rfp.set_timeline_milestone("qa_session_date", "2026-03-15")
    rfp.set_timeline_milestone("proposal_deadline", "2026-03-30")
    rfp.set_timeline_milestone("award_notification", "2026-04-15")
    rfp.set_timeline_milestone("project_start_date", "2026-05-01")
    
    # Set budget expectations
    rfp.set_budget_range(30000, 50000)  # €30,000 - €50,000
    rfp.budget_expectations["payment_schedule_preference"] = "Quarterly payments based on milestones"
    
    # Set vendor qualifications
    rfp.set_vendor_qualification("minimum_experience_years", 5)
    rfp.set_vendor_qualification("relevant_project_examples", 3)
    rfp.vendor_qualifications["certifications_required"] = ["Google Ads Certified", "Facebook Blueprint Certified"]
    
    # Add attachments
    rfp.attachments = [
        "Company profile document",
        "Detailed project requirements",
        "Previous campaign results",
        "Brand guidelines"
    ]
    
    # Set terms and conditions
    rfp.terms_conditions = {
        "contract_duration": "3 months with option for extension",
        "intellectual_property": "All created content becomes property of Sample RFP Oy",
        "termination_clause": "Either party can terminate with 30 days notice",
        "confidentiality": "Strict confidentiality agreement required"
    }
    
    # Set submission guidelines
    rfp.submission_guidelines["submission_method"] = "Submit via secure portal at https://samplecompany.fi/rfp-submission"
    rfp.submission_guidelines["number_of_copies"] = 1  # Electronic only
    
    return rfp


if __name__ == "__main__":
    # Example usage
    print("L2 Tarjouspyyntö - Request for Proposal Tool")
    print("=" * 50)
    
    # Create a sample RFP
    sample_rfp = create_sample_rfp()
    
    # Generate and display the RFP document
    rfp_doc = sample_rfp.generate_rfp_document()
    
    print(f"\nCompany: {rfp_doc['company_name']}")
    print(f"RFP Date: {rfp_doc['rfp_date']}")
    print(f"RFP Reference: {rfp_doc['rfp_reference']}")
    print(f"Contact: {rfp_doc['contact_person']}")
    print(f"Contact Info: {rfp_doc['contact_info']}")
    
    print(f"\nProject: {rfp_doc['project_description']['title']}")
    print(f"Overview: {rfp_doc['project_description']['overview']}")
    print(f"Scope: {rfp_doc['project_description']['scope']}")
    print(f"Location: {rfp_doc['project_description']['location']}")
    
    print(f"\nProject Objectives:")
    for obj in rfp_doc['project_description']['objectives']:
        print(f"  - {obj}")
    
    print(f"\nProject Deliverables:")
    for deliv in rfp_doc['project_description']['deliverables']:
        print(f"  - {deliv['name']}: {deliv['description']}")
    
    print(f"\nEvaluation Criteria (Total Weight: {rfp_doc['evaluation_criteria_total_weight']:.0%}):")
    for crit, details in rfp_doc['evaluation_criteria'].items():
        print(f"  {details['description']}: {details['weight']:.0%}")
    
    print(f"\nBudget Expectations:")
    budget = rfp_doc['budget_expectations']
    print(f"  Range: €{budget['estimated_budget_range_min']:,.2f} - €{budget['estimated_budget_range_max']:,.2f}")
    print(f"  Flexibility: {budget['budget_flexibility']}")
    print(f"  Payment Schedule: {budget['payment_schedule_preference']}")
    
    print(f"\nVendor Qualifications:")
    qual = rfp_doc['vendor_qualifications']
    print(f"  Minimum Experience: {qual['minimum_experience_years']} years")
    print(f"  Relevant Examples Required: {qual['relevant_project_examples']}")
    print(f"  Certifications Required: {', '.join(qual['certifications_required'])}")
    print(f"  Financial Stability Proof Required: {qual['financial_stability_proof']}")
    
    print(f"\nTimeline:")
    timeline = rfp_doc['rfp_timeline']
    print(f"  RFP Issue Date: {timeline['rfp_issue_date']}")
    print(f"  Q&A Session: {timeline['qa_session_date']}")
    print(f"  Proposal Deadline: {timeline['proposal_deadline']}")
    print(f"  Award Notification: {timeline['award_notification']}")
    print(f"  Project Start: {timeline['project_start_date']}")
    
    print(f"\nSubmission Guidelines:")
    sub_guidelines = rfp_doc['submission_guidelines']
    print(f"  Format: {sub_guidelines['submission_format']}")
    print(f"  Copies: {sub_guidelines['number_of_copies']}")
    print(f"  Method: {sub_guidelines['submission_method']}")
    
    print(f"\nAttachments:")
    for attachment in rfp_doc['attachments']:
        print(f"  - {attachment}")
    
    # Generate an evaluation template
    print(f"\nGenerating evaluation template...")
    eval_template = sample_rfp.generate_evaluation_template()
    print(f"Evaluation template created with {len(eval_template['evaluation_criteria'])} criteria")
    
    # Example vendor evaluation
    print(f"\nExample Vendor Evaluation:")
    vendor_scores = {
        "technical_competence": 8,
        "cost_competitiveness": 7,
        "past_experience": 9,
        "project_timeline": 8,
        "innovation": 7
    }
    
    evaluation = sample_rfp.evaluate_proposal("Digital Agency Oy", vendor_scores)
    print(f"  Vendor: {evaluation['vendor_name']}")
    print(f"  Total Score: {evaluation['total_score']:.2f}")
    print(f"  Weighted Scores:")
    for criterion, scores in evaluation['weighted_scores'].items():
        desc = rfp_doc['evaluation_criteria'][criterion]['description']
        print(f"    {desc}: {scores['raw_score']}/10 * {scores['weight']:.0%} = {scores['weighted_score']:.2f}")
    
    # Save the RFP to a JSON file
    sample_rfp.save_to_json("sample_request_for_proposal.json")
    print(f"\nRFP saved to 'sample_request_for_proposal.json'")