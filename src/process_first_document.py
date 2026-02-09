"""
Script to manually process documentation files and add keywords, ECS elements, constraints, and metadata.
This is the first step in the manual processing phase.
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


def process_company_formation_document():
    """
    Manually process the company formation document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/company_formation_example.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: company_formation_example.md")
    print("="*60)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="company formation",
            frequency=8,
            relevance=0.9,
            category="procedure",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=10
        ),
        Keyword(
            term="limited liability company",
            frequency=5,
            relevance=0.95,
            category="business_structure",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=50
        ),
        Keyword(
            term="Oy",
            frequency=3,
            relevance=0.85,
            category="business_structure",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=100
        ),
        Keyword(
            term="registration",
            frequency=6,
            relevance=0.8,
            category="procedure",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=200
        ),
        Keyword(
            term="minimum share capital",
            frequency=4,
            relevance=0.95,
            category="financial_requirement",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=300
        ),
        Keyword(
            term="Articles of Association",
            frequency=4,
            relevance=0.9,
            category="legal_document",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=400
        ),
        Keyword(
            term="tax obligations",
            frequency=3,
            relevance=0.85,
            category="compliance",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=500
        ),
        Keyword(
            term="compliance requirements",
            frequency=3,
            relevance=0.9,
            category="compliance",
            tags=["manual_extraction", "business_formation"],
            source_file="../docs/business_forms/company_formation_example.md",
            position_in_text=600
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/company_formation_example.md",
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
            name="Limited Liability Company (Oy)",
            description="A Finnish limited liability company structure",
            attributes={
                "minimum_share_capital": "€2,500",
                "shareholders_required": 1,
                "registered_office_required": True,
                "finnish_director_resident_required": True
            },
            tags=["business_structure", "legal_entity"],
            source_file="../docs/business_forms/company_formation_example.md",
            relationships={
                "has_shareholders": ["Shareholder"],
                "managed_by": ["Director"],
                "registered_with": ["Patent and Registration Office (PRH)"]
            }
        ),
        Entity(
            name="Shareholder",
            description="Owner of shares in the limited liability company",
            attributes={
                "voting_rights": "proportional to shares held",
                "liability": "limited to investment amount"
            },
            tags=["role", "ownership"],
            source_file="../docs/business_forms/company_formation_example.md",
            relationships={
                "owns_shares_in": ["Limited Liability Company (Oy)"],
                "participates_in": ["Shareholders_Meeting"]
            }
        ),
        Entity(
            name="Director",
            description="Person responsible for managing the company",
            attributes={
                "residency_requirement": "Must be Finnish resident",
                "fiduciary_duty": True
            },
            tags=["role", "management"],
            source_file="../docs/business_forms/company_formation_example.md",
            relationships={
                "manages": ["Limited Liability Company (Oy)"],
                "reports_to": ["Shareholders_Meeting"]
            }
        ),
        Entity(
            name="Patent and Registration Office (PRH)",
            description="Finnish authority responsible for company registrations",
            attributes={
                "responsibility": "Company registration and record keeping",
                "jurisdiction": "Finland"
            },
            tags=["authority", "regulator"],
            source_file="../docs/business_forms/company_formation_example.md",
            relationships={
                "registers": ["Limited Liability Company (Oy)"],
                "receives_documents_from": ["Company_Representative"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="Share Capital",
            description="Financial capital invested in the company",
            properties={
                "amount": "€2,500 minimum",
                "currency": "EUR",
                "requirement": "Must be deposited before registration"
            },
            data_schema={
                "amount": "float",
                "currency": "string",
                "requirement": "string"
            },
            tags=["financial", "requirement"],
            source_file="../docs/business_forms/company_formation_example.md"
        ),
        Component(
            name="Articles of Association",
            description="Legal document defining company structure and operations",
            properties={
                "purpose": "Define company's purpose and governance",
                "required": True,
                "content": ["Company name", "Purpose", "Share structure", "Governance rules"]
            },
            data_schema={
                "purpose": "string",
                "required": "boolean",
                "content": "list[string]"
            },
            tags=["legal_document", "requirement"],
            source_file="../docs/business_forms/company_formation_example.md"
        ),
        Component(
            name="Registered Office Address",
            description="Official address of the company in Finland",
            properties={
                "requirement": True,
                "location": "Must be in Finland",
                "purpose": "Official correspondence address"
            },
            data_schema={
                "requirement": "boolean",
                "location": "string",
                "purpose": "string"
            },
            tags=["requirement", "address"],
            source_file="../docs/business_forms/company_formation_example.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="Company Registration Process",
            description="Step-by-step process for registering a limited liability company in Finland",
            behavior=(
                "1. Prepare Articles of Association\n"
                "2. Deposit minimum share capital\n"
                "3. Submit registration to Patent and Registration Office (PRH)\n"
                "4. Await confirmation (typically 2-3 weeks)"
            ),
            dependencies=[
                "Articles of Association",
                "Share Capital",
                "Registered Office Address",
                "Identity Verification"
            ],
            triggers=["Company Formation Request"],
            tags=["process", "procedure"],
            source_file="../docs/business_forms/company_formation_example.md"
        ),
        System(
            name="Tax Registration Process",
            description="Process for registering tax obligations after company formation",
            behavior=(
                "1. Register for VAT if annual turnover exceeds €10,000\n"
                "2. Register for corporate tax (20% of profits)\n"
                "3. Set up payroll tax system if employees are hired"
            ),
            dependencies=[
                "Company Registration Confirmation",
                "Estimated Turnover Projection"
            ],
            triggers=["Company Registration Complete"],
            tags=["process", "tax_compliance"],
            source_file="../docs/business_forms/company_formation_example.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/company_formation_example.md",
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
            id="constraint_min_share_capital",
            title="Minimum Share Capital Requirement",
            description="Finnish Oy companies must have minimum €2,500 share capital deposited before registration",
            constraint_type=ConstraintType.FINANCIAL,
            condition="share_capital >= 2500",
            scope="company_registration",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/company_formation_example.md",
            tags=["financial", "requirement", "registration"],
            related_constraints=["constraint_registered_office_address"],
            validation_logic="check_monetary_amount(currency='EUR', amount >= 2500)",
            error_message="Minimum share capital of €2,500 not met"
        ),
        Constraint(
            id="constraint_registered_office_address",
            title="Finnish Registered Office Address Required",
            description="A Finnish registered office address is mandatory for Oy companies",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="registered_office_address.country == 'Finland'",
            scope="company_registration",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/company_formation_example.md",
            tags=["compliance", "requirement", "registration"],
            related_constraints=["constraint_min_share_capital"],
            validation_logic="check_address_country(address, country='Finland')",
            error_message="Finnish registered office address is required"
        ),
        Constraint(
            id="constraint_director_residency",
            title="Finnish Resident Director Required",
            description="The company must have at least one director who is a resident of Finland",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="any(director.resident_of == 'Finland' for director in directors)",
            scope="company_governance",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/company_formation_example.md",
            tags=["compliance", "governance", "requirement"],
            related_constraints=[],
            validation_logic="check_director_residency(directors)",
            error_message="At least one director must be a Finnish resident"
        ),
        Constraint(
            id="constraint_vat_registration_turnover",
            title="VAT Registration Threshold",
            description="New companies must register for VAT if annual turnover exceeds €10,000",
            constraint_type=ConstraintType.REGULATORY,
            condition="annual_turnover > 10000",
            scope="tax_obligation",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/company_formation_example.md",
            tags=["tax", "compliance", "threshold"],
            related_constraints=[],
            validation_logic="check_annual_turnover(turnover)",
            error_message="VAT registration required for turnover exceeding €10,000"
        ),
        Constraint(
            id="constraint_annual_filing",
            title="Annual Financial Statements Filing",
            description="Companies must file annual financial statements",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="annual_filing_required == True",
            scope="compliance_reporting",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/company_formation_example.md",
            tags=["compliance", "reporting", "annual"],
            related_constraints=[],
            validation_logic="check_annual_filing_status(year)",
            error_message="Annual financial statements must be filed"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/company_formation_example.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/company_formation_example.md",
        title="Company Formation Requirements in Finland",
        description="Documentation outlining the requirements for forming a limited liability company (Oy) in Finland",
        tags=["company_formation", "finnish_business", "oy", "registration", "requirements"],
        categories=["procedure", "legal_requirements", "business_formation"],
        related_files=["../docs/business_forms/company_finance_example.md"],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.95,
        content_type="procedure",
        business_domains=["legal", "tax", "compliance"],
        difficulty_level="intermediate",
        estimated_reading_time=5,
        word_count=len(content.split()),
        language="en",
        keywords=["company", "formation", "finland", "oy", "registration", "requirements"],
        related_entities=["Limited Liability Company (Oy)", "Shareholder", "Director"],
        related_components=["Share Capital", "Articles of Association", "Registered Office Address"],
        related_systems=["Company Registration Process", "Tax Registration Process"],
        related_constraints=["constraint_min_share_capital", "constraint_registered_office_address", "constraint_director_residency"],
        custom_fields={
            "target_audience": ["entrepreneurs", "business_founders"],
            "prerequisites": ["business_idea", "initial_capital"],
            "follow_up_steps": ["tax_registration", "bank_account_setup"]
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
    with open("../processed_docs/company_formation_example_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: processed_docs/company_formation_example_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_company_formation_document()