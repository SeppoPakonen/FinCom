"""
Script to manually process the second documentation file and add keywords, ECS elements, constraints, and metadata.
This continues the manual processing phase.
"""

import json
import sys
import os
from datetime import datetime

# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.keyword import Keyword, KeywordCollection
from data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from data_structures.metadata import Metadata


def process_company_finance_document():
    """
    Manually process the company finance document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/company_finance_example.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: company_finance_example.md")
    print("="*60)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="company finance",
            frequency=7,
            relevance=0.9,
            category="finance",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=10
        ),
        Keyword(
            term="financial management",
            frequency=5,
            relevance=0.85,
            category="finance",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=50
        ),
        Keyword(
            term="accounting records",
            frequency=4,
            relevance=0.8,
            category="compliance",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=100
        ),
        Keyword(
            term="annual financial statements",
            frequency=6,
            relevance=0.95,
            category="compliance",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=200
        ),
        Keyword(
            term="corporate tax",
            frequency=5,
            relevance=0.9,
            category="tax",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=300
        ),
        Keyword(
            term="VAT registration",
            frequency=4,
            relevance=0.85,
            category="tax",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=400
        ),
        Keyword(
            term="payroll taxes",
            frequency=3,
            relevance=0.8,
            category="tax",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=500
        ),
        Keyword(
            term="business banking",
            frequency=3,
            relevance=0.75,
            category="finance",
            tags=["manual_extraction", "business_finance"],
            source_file="../docs/business_forms/company_finance_example.md",
            position_in_text=600
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/company_finance_example.md",
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
            name="Finnish Limited Liability Company (Oy)",
            description="A Finnish limited liability company structure",
            attributes={
                "tax_obligations": ["corporate_tax", "vat", "payroll_tax"],
                "reporting_requirements": ["annual_financial_statements"],
                "auditing_requirements": "if_revenue_over_800k_eur"
            },
            tags=["business_structure", "legal_entity", "tax_obligation"],
            source_file="../docs/business_forms/company_finance_example.md",
            relationships={
                "files_reports_with": ["PRH"],
                "pays_taxes_to": ["Tax_Administration"],
                "employs": ["Employees"]
            }
        ),
        Entity(
            name="Tax Administration",
            description="Finnish tax authority responsible for collecting taxes",
            attributes={
                "responsibilities": ["collect_corporate_tax", "manage_vat_system", "process_tax_returns"],
                "jurisdiction": "Finland"
            },
            tags=["authority", "tax_administrator"],
            source_file="../docs/business_forms/company_finance_example.md",
            relationships={
                "collects_from": ["Finnish Limited Liability Company (Oy)"],
                "receives_filings_from": ["Company_Representative"]
            }
        ),
        Entity(
            name="Employees",
            description="People employed by the company",
            attributes={
                "tax_implications": ["payroll_taxes", "social_security_contributions"],
                "reporting_requirements": ["employment_details"]
            },
            tags=["role", "human_resources"],
            source_file="../docs/business_forms/company_finance_example.md",
            relationships={
                "paid_by": ["Finnish Limited Liability Company (Oy)"],
                "generate_tax_obligations_for": ["Finnish Limited Liability Company (Oy)"]
            }
        ),
        Entity(
            name="Auditors",
            description="Professionals who audit company financial statements",
            attributes={
                "requirement": "if_company_meets_certain_size_criteria",
                "responsibility": "verify_accuracy_of_financial_statements"
            },
            tags=["role", "compliance", "verification"],
            source_file="../docs/business_forms/company_finance_example.md",
            relationships={
                "audit": ["Finnish Limited Liability Company (Oy)"],
                "report_to": ["PRH", "Shareholders"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="Accounting Records",
            description="Detailed records of all financial transactions",
            properties={
                "requirement": "Mandatory for all companies",
                "retention_period": "7 years",
                "content": ["income", "expenses", "assets", "liabilities"]
            },
            data_schema={
                "requirement": "string",
                "retention_period": "string",
                "content": "list[string]"
            },
            tags=["compliance", "record_keeping"],
            source_file="../docs/business_forms/company_finance_example.md"
        ),
        Component(
            name="Annual Financial Statements",
            description="Yearly financial report required by law",
            properties={
                "deadline": "by certain date following fiscal year",
                "required_for": "all_companies",
                "content": ["balance_sheet", "income_statement", "notes"]
            },
            data_schema={
                "deadline": "string",
                "required_for": "string",
                "content": "list[string]"
            },
            tags=["compliance", "reporting"],
            source_file="../docs/business_forms/company_finance_example.md"
        ),
        Component(
            name="Transaction Records",
            description="Detailed records of business transactions",
            properties={
                "requirement": "Mandatory for tax purposes",
                "detail_level": "sufficient_to_verify_income_and_expenses",
                "format": "can_be_electronic_or_paper"
            },
            data_schema={
                "requirement": "string",
                "detail_level": "string",
                "format": "string"
            },
            tags=["compliance", "record_keeping"],
            source_file="../docs/business_forms/company_finance_example.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="Financial Reporting System",
            description="Processes for maintaining accounting records and preparing financial statements",
            behavior=(
                "1. Record all financial transactions\n"
                "2. Maintain proper accounting records\n"
                "3. Prepare annual financial statements\n"
                "4. File statements with PRH\n"
                "5. Conduct audit if required"
            ),
            dependencies=[
                "Accounting Records",
                "Transaction Records",
                "Annual Financial Statements"
            ],
            triggers=["end_of_fiscal_year"],
            tags=["process", "compliance"],
            source_file="../docs/business_forms/company_finance_example.md"
        ),
        System(
            name="Tax Compliance System",
            description="Processes for meeting tax obligations",
            behavior=(
                "1. Calculate corporate tax (20% of profits)\n"
                "2. Register for VAT if turnover > €10,000 annually\n"
                "3. Calculate and pay payroll taxes for employees\n"
                "4. File tax returns on schedule\n"
                "5. Maintain tax documentation"
            ),
            dependencies=[
                "Annual Financial Statements",
                "Payroll Records",
                "Revenue Tracking"
            ],
            triggers=["monthly", "annually"],
            tags=["process", "tax_compliance"],
            source_file="../docs/business_forms/company_finance_example.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/company_finance_example.md",
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
            id="constraint_annual_financial_statements",
            title="Annual Financial Statements Filing",
            description="Companies must file annual financial statements with PRH",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="annual_financial_statements_filed == True",
            scope="compliance_reporting",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/company_finance_example.md",
            tags=["compliance", "reporting", "annual"],
            related_constraints=["constraint_auditing_requirements"],
            validation_logic="check_annual_filing_status(company_id, year)",
            error_message="Annual financial statements must be filed with PRH"
        ),
        Constraint(
            id="constraint_auditing_requirements",
            title="Auditing Requirements",
            description="Companies with revenue > €800,000 require auditing",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="revenue <= 800000 or (revenue > 800000 and audit_conducted == True)",
            scope="compliance_verification",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/company_finance_example.md",
            tags=["compliance", "verification", "auditing"],
            related_constraints=["constraint_annual_financial_statements"],
            validation_logic="check_auditing_requirement(revenue, audit_status)",
            error_message="Companies with revenue over €800,000 must undergo auditing"
        ),
        Constraint(
            id="constraint_directors_liability",
            title="Directors Liability for Unpaid Taxes",
            description="Directors liable for unpaid taxes in certain circumstances",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="taxes_paid == True or director_liability_acknowledged == True",
            scope="governance",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/company_finance_example.md",
            tags=["governance", "liability", "tax_compliance"],
            related_constraints=[],
            validation_logic="check_tax_payment_status_and_director_liability(tax_records)",
            error_message="Directors may be liable for unpaid taxes"
        ),
        Constraint(
            id="constraint_vat_registration",
            title="VAT Registration Threshold",
            description="Companies must register for VAT if annual turnover exceeds €10,000",
            constraint_type=ConstraintType.REGULATORY,
            condition="annual_turnover <= 10000 or vat_registration_completed == True",
            scope="tax_obligation",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/company_finance_example.md",
            tags=["tax", "compliance", "threshold"],
            related_constraints=["constraint_corporate_tax_rate"],
            validation_logic="check_vat_registration_requirement(annual_turnover)",
            error_message="VAT registration required for turnover exceeding €10,000"
        ),
        Constraint(
            id="constraint_corporate_tax_rate",
            title="Corporate Tax Rate",
            description="Corporate tax rate is 20% of profits",
            constraint_type=ConstraintType.REGULATORY,
            condition="corporate_tax_rate == 0.20",
            scope="tax_calculation",
            severity=SeverityLevel.INFO,
            source_file="../docs/business_forms/company_finance_example.md",
            tags=["tax", "calculation", "rate"],
            related_constraints=["constraint_vat_registration"],
            validation_logic="validate_corporate_tax_calculation(profit, tax_amount)",
            error_message="Corporate tax should be calculated at 20% of profit"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/company_finance_example.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/company_finance_example.md",
        title="Managing Company Finances in Finland",
        description="Documentation explaining how to manage finances for a Finnish limited liability company (Oy)",
        tags=["company_finance", "finnish_business", "oy", "financial_management", "tax_obligations"],
        categories=["finance", "tax", "compliance"],
        related_files=["company_formation_example.md"],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.95,
        content_type="procedure",
        business_domains=["finance", "tax", "compliance"],
        difficulty_level="intermediate",
        estimated_reading_time=6,
        word_count=len(content.split()),
        language="en",
        keywords=["company", "finance", "finland", "oy", "financial_management", "tax", "compliance"],
        related_entities=["Finnish Limited Liability Company (Oy)", "Tax Administration", "Employees"],
        related_components=["Accounting Records", "Annual Financial Statements", "Transaction Records"],
        related_systems=["Financial Reporting System", "Tax Compliance System"],
        related_constraints=["constraint_annual_financial_statements", "constraint_vat_registration", "constraint_corporate_tax_rate"],
        custom_fields={
            "target_audience": ["business_owners", "finance_managers", "accountants"],
            "prerequisites": ["company_registration"],
            "follow_up_steps": ["tax_registration", "accounting_setup"]
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
    with open("../processed_docs/company_finance_example_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: ../processed_docs/company_finance_example_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_company_finance_document()