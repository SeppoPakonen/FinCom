"""
Script to manually process the ABC of Working Life Rules and Obligations documentation file and add keywords, ECS elements, constraints, and metadata.
"""

import json
import sys
import os
from datetime import datetime

# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_structures.keyword import Keyword, KeywordCollection
from src.data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from src.data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from src.data_structures.metadata import Metadata


def process_abc_working_life_document():
    """
    Manually process the ABC of Working Life Rules and Obligations document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/ABC of Working Life Rules and Obligations.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: ABC of Working Life Rules and Obligations.md")
    print("="*70)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="working life rules",
            frequency=12,
            relevance=0.95,
            category="regulation",
            tags=["manual_extraction", "employment_legislation"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=10
        ),
        Keyword(
            term="employment obligations",
            frequency=10,
            relevance=0.9,
            category="compliance",
            tags=["manual_extraction", "employment_law"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=45
        ),
        Keyword(
            term="labor legislation",
            frequency=8,
            relevance=0.85,
            category="regulation",
            tags=["manual_extraction", "employment_law"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=80
        ),
        Keyword(
            term="workplace safety",
            frequency=9,
            relevance=0.9,
            category="safety",
            tags=["manual_extraction", "occupational_safety"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=120
        ),
        Keyword(
            term="employment contracts",
            frequency=7,
            relevance=0.85,
            category="legal_document",
            tags=["manual_extraction", "employment_agreement"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=160
        ),
        Keyword(
            term="working hours",
            frequency=6,
            relevance=0.8,
            category="regulation",
            tags=["manual_extraction", "work_schedule"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=200
        ),
        Keyword(
            term="vacation rights",
            frequency=5,
            relevance=0.75,
            category="employee_benefit",
            tags=["manual_extraction", "leave_entitlement"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=240
        ),
        Keyword(
            term="salary obligations",
            frequency=6,
            relevance=0.8,
            category="financial_requirement",
            tags=["manual_extraction", "compensation"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            position_in_text=280
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
        keywords=keywords,
        total_word_count=len(content.split()),
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(keywords)} keywords")
    
    # 2. Identify and map ECS elements
    print("2. Adding ECS elements...")
    
    # Entities
    entities = [
        Entity(
            name="Employer",
            description="Organization or individual that employs workers",
            attributes={
                "responsibilities": ["provide_safe_workplace", "pay_salary", "follow_employment_law"],
                "obligations": ["comply_with_working_hours", "grant_vacation_rights", "ensure_workplace_safety"],
                "rights": ["expect_work_performance", "manage_business_operations"]
            },
            tags=["business_actor", "employment_relationship"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            relationships={
                "employs": ["Employee"],
                "signs": ["Employment_Contract"],
                "provides": ["Salary", "Benefits"]
            }
        ),
        Entity(
            name="Employee",
            description="Individual who performs work for compensation",
            attributes={
                "rights": ["receive_salary", "vacation", "safe_workplace"],
                "obligations": ["perform_work", "follow_company_rules", "maintain_confidentiality"],
                "protections": ["non_discrimination", "workplace_safety", "fair_treatment"]
            },
            tags=["business_actor", "employment_relationship"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            relationships={
                "works_for": ["Employer"],
                "signs": ["Employment_Contract"],
                "receives": ["Salary", "Benefits"]
            }
        ),
        Entity(
            name="Employment Contract",
            description="Legal agreement between employer and employee",
            attributes={
                "required_elements": ["job_description", "salary", "working_hours", "vacation_accrual"],
                "legal_basis": "Employment Contracts Act",
                "modification_process": "mutual_agreement_required"
            },
            tags=["legal_document", "employment_relationship"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            relationships={
                "binds": ["Employer", "Employee"],
                "specifies": ["Terms_and_Conditions"],
                "defines": ["Rights_and_Obligations"]
            }
        ),
        Entity(
            name="Occupational Safety Authority",
            description="Government body responsible for workplace safety oversight",
            attributes={
                "jurisdiction": "national",
                "responsibilities": ["inspect_workplaces", "enforce_safety_regulations", "investigate_accidents"],
                "powers": ["issue_fines", "order_improvements", "close_unsafe_workplaces"]
            },
            tags=["regulatory_body", "safety_enforcement"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            relationships={
                "oversees": ["Workplace_Safety"],
                "inspects": ["Employer_Facilities"],
                "enforces": ["Safety_Regulations"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="Employment Terms and Conditions",
            description="Specific terms that govern the employment relationship",
            properties={
                "working_hours": "typically_8_hours_per_day",
                "overtime_rules": "compensation_or_time_off_required",
                "break_requirements": "minimum_breaks_based_on_duration",
                "remote_work_policy": "may_be_negotiated"
            },
            data_schema={
                "working_hours": "string",
                "overtime_rules": "string",
                "break_requirements": "string",
                "remote_work_policy": "string"
            },
            tags=["employment_terms", "work_conditions"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md"
        ),
        Component(
            name="Vacation Entitlement Calculation",
            description="Method for calculating employee vacation entitlements",
            properties={
                "accrual_rate": "2.5_days_per_month_worked",
                "minimum_entitlement": "24_working_days_annually",
                "carry_over_rules": "up_to_1_year_maximum",
                "planning_requirements": "mutual_agreement_with_employee"
            },
            data_schema={
                "accrual_rate": "string",
                "minimum_entitlement": "string",
                "carry_over_rules": "string",
                "planning_requirements": "string"
            },
            tags=["benefits_calculation", "leave_entitlement"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md"
        ),
        Component(
            name="Workplace Safety Requirements",
            description="Safety measures that must be implemented in the workplace",
            properties={
                "risk_assessment": "required_annually_or_when_conditions_change",
                "safety_equipment": "provided_by_employer_at_no_cost_to_employee",
                "training_requirements": "completed_before_starting_work",
                "incident_reporting": "mandatory_for_employers"
            },
            data_schema={
                "risk_assessment": "string",
                "safety_equipment": "string",
                "training_requirements": "string",
                "incident_reporting": "string"
            },
            tags=["safety_measures", "compliance_requirements"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="Employment Relationship Management System",
            description="System for managing the employment relationship from hiring to termination",
            behavior=(
                "1. Employer and Employee sign Employment Contract\n"
                "2. Employee begins work following agreed terms\n"
                "3. Salary and benefits are provided according to contract\n"
                "4. Vacation and leave are granted as per legislation\n"
                "5. Workplace safety measures are maintained\n"
                "6. Employment relationship ends through proper procedures"
            ),
            dependencies=[
                "Employment Contract",
                "Employment Terms and Conditions",
                "Vacation Entitlement Calculation"
            ],
            triggers=["hiring_decision", "contract_signing", "employment_end"],
            tags=["employment_process", "relationship_management"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md"
        ),
        System(
            name="Workplace Safety Compliance System",
            description="System for ensuring compliance with occupational safety regulations",
            behavior=(
                "1. Conduct initial risk assessment\n"
                "2. Implement required safety measures\n"
                "3. Provide safety training to employees\n"
                "4. Monitor safety compliance continuously\n"
                "5. Report incidents as required\n"
                "6. Update safety measures based on findings"
            ),
            dependencies=[
                "Workplace Safety Requirements",
                "Occupational Safety Authority"
            ],
            triggers=["new_employees", "changed_conditions", "accidents"],
            tags=["safety_compliance", "regulatory_adherence"],
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
        entities=entities,
        components=components,
        systems=systems,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(entities)} entities, {len(components)} components, {len(systems)} systems")
    
    # 3. Extract and document constraints
    print("3. Adding constraints...")
    constraints = [
        Constraint(
            id="constraint_working_hours_limit",
            title="Working Hours Limit",
            description="Daily working hours cannot exceed 8 hours on average over a 4-month period",
            constraint_type=ConstraintType.REGULATORY,
            condition="avg_daily_hours_over_4_months <= 8",
            scope="employment_compliance",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            tags=["working_hours", "compliance"],
            related_constraints=["constraint_overtime_compensation"],
            validation_logic="calculate_avg_daily_hours(work_hours, period)",
            error_message="Average daily working hours cannot exceed 8 hours over a 4-month period"
        ),
        Constraint(
            id="constraint_minimum_vacation_entitlement",
            title="Minimum Vacation Entitlement",
            description="Employees must receive at least 24 working days of vacation annually",
            constraint_type=ConstraintType.REGULATORY,
            condition="annual_vacation_days >= 24",
            scope="employee_benefits",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            tags=["vacation", "employee_rights"],
            related_constraints=[],
            validation_logic="calculate_vacation_entitlement(employee_service_years)",
            error_message="Employees must receive at least 24 working days of vacation annually"
        ),
        Constraint(
            id="constraint_occupational_safety_training",
            title="Occupational Safety Training Requirement",
            description="All employees must complete safety training before starting work",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="safety_training_completed == True",
            scope="workplace_safety",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            tags=["safety", "training", "compliance"],
            related_constraints=["constraint_workplace_safety_measures"],
            validation_logic="verify_training_completion(employee_id)",
            error_message="All employees must complete safety training before starting work"
        ),
        Constraint(
            id="constraint_employment_contract_writing",
            title="Written Employment Contract Requirement",
            description="Employment contracts must be in writing for positions lasting more than 2 months",
            constraint_type=ConstraintType.REGULATORY,
            condition="contract_duration > 2_months or contract_written == True",
            scope="employment_legislation",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            tags=["contract", "writing_requirement", "compliance"],
            related_constraints=[],
            validation_logic="check_contract_duration_and_format(contract)",
            error_message="Employment contracts must be in writing for positions lasting more than 2 months"
        ),
        Constraint(
            id="constraint_salary_payment_timing",
            title="Salary Payment Timing",
            description="Salaries must be paid at least monthly and within 10 days of payment period end",
            constraint_type=ConstraintType.FINANCIAL,
            condition="salary_paid_within_10_days_of_period_end == True",
            scope="compensation_compliance",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
            tags=["salary", "payment_timing", "compliance"],
            related_constraints=[],
            validation_logic="verify_salary_payment_timing(payment_date, period_end)",
            error_message="Salaries must be paid within 10 days of payment period end"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/ABC of Working Life Rules and Obligations.md",
        title="ABC of Working Life Rules and Obligations",
        description="Comprehensive guide to Finnish employment legislation, workplace safety requirements, and employee-employer obligations",
        tags=["employment_legislation", "working_life", "finnish_law", "employee_rights", "employer_obligations", "workplace_safety", "vacation_rights", "working_hours"],
        categories=["employment_law", "workplace_safety", "compliance"],
        related_files=["Employment Contracts Act", "Occupational Safety and Health Act", "Working Hours Act"],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.95,
        content_type="regulatory_guide",
        business_domains=["human_resources", "employment", "compliance"],
        difficulty_level="intermediate",
        estimated_reading_time=6,
        word_count=len(content.split()),
        language="en",
        keywords=["working_life", "rules", "obligations", "employment", "finland", "legislation", "safety", "contracts"],
        related_entities=["Employer", "Employee", "Employment Contract", "Occupational Safety Authority"],
        related_components=["Employment Terms and Conditions", "Vacation Entitlement Calculation", "Workplace Safety Requirements"],
        related_systems=["Employment Relationship Management System", "Workplace Safety Compliance System"],
        related_constraints=["constraint_working_hours_limit", "constraint_minimum_vacation_entitlement", "constraint_occupational_safety_training"],
        custom_fields={
            "target_audience": ["employers", "employees", "hr_professionals", "business_owners"],
            "prerequisites": ["basic_understanding_of_employment_relationship"],
            "follow_up_steps": ["implement_safety_measures", "draft_employment_contracts", "establish_vacation_planning_process"]
        }
    )
    
    print("   Added search-engine metadata")
    
    # Save the processed data
    processed_data = {
        "original_content": content,
        "keywords": [kw.to_dict() for kw in keyword_collection.keywords],
        "ecs_elements": ecs_architecture.to_dict(),
        "constraints": [con.to_dict() for con in constraint_collection.constraints],
        "metadata": metadata.to_dict(),
        "processing_date": datetime.now().isoformat(),
        "processor": "manual"
    }
    
    # Write processed data to a new file
    with open("../processed_docs/abc_working_life_rules_obligations_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: ../processed_docs/abc_working_life_rules_obligations_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_abc_working_life_document()