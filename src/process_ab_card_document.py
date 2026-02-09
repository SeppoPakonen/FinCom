"""
Script to manually process the AB-Card documentation file and add keywords, ECS elements, constraints, and metadata.
"""

import json
import sys
import os
from datetime import datetime

# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.keyword import Keyword, KeywordCollection
from data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from data_structures.metadata import Metadata


def process_ab_card_document():
    """
    Manually process the AB-Card document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/AB-Card.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: AB-Card.md")
    print("="*50)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="AB card",
            frequency=15,
            relevance=0.95,
            category="qualification",
            tags=["manual_extraction", "professional_qualification"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=10
        ),
        Keyword(
            term="computer user qualification",
            frequency=8,
            relevance=0.9,
            category="qualification",
            tags=["manual_extraction", "professional_certification"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=50
        ),
        Keyword(
            term="professional competence",
            frequency=7,
            relevance=0.85,
            category="competence",
            tags=["manual_extraction", "skills_assessment"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=100
        ),
        Keyword(
            term="qualification requirements",
            frequency=6,
            relevance=0.8,
            category="requirement",
            tags=["manual_extraction", "certification_process"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=150
        ),
        Keyword(
            term="demonstration of skills",
            frequency=9,
            relevance=0.9,
            category="assessment",
            tags=["manual_extraction", "competency_evaluation"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=200
        ),
        Keyword(
            term="professional development",
            frequency=5,
            relevance=0.75,
            category="development",
            tags=["manual_extraction", "career_advancement"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=250
        ),
        Keyword(
            term="ICT skills",
            frequency=12,
            relevance=0.9,
            category="technical_skill",
            tags=["manual_extraction", "digital_competence"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=300
        ),
        Keyword(
            term="office software",
            frequency=10,
            relevance=0.85,
            category="software",
            tags=["manual_extraction", "productivity_tools"],
            source_file="../docs/business_forms/AB-Card.md",
            position_in_text=350
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/AB-Card.md",
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
            name="Computer User (AB Card Holder)",
            description="Professional with computer user qualification",
            attributes={
                "qualification_level": "professional",
                "skills_demonstrated": ["office_software", "ict_fundamentals", "digital_literacy"],
                "certification_status": "verified"
            },
            tags=["professional", "qualified_user"],
            source_file="../docs/business_forms/AB-Card.md",
            relationships={
                "possesses": ["AB_Card_Certification"],
                "demonstrates": ["Computer_Competencies"],
                "uses": ["Office_Software"]
            }
        ),
        Entity(
            name="Assessment Body",
            description="Organization responsible for evaluating AB card qualifications",
            attributes={
                "responsibilities": ["evaluate_skills", "verify_competence", "issue_certificates"],
                "standards_applied": ["professional_standards", "qualification_criteria"]
            },
            tags=["evaluator", "certifier"],
            source_file="../docs/business_forms/AB-Card.md",
            relationships={
                "evaluates": ["Computer_Users"],
                "issues": ["AB_Card_Certifications"],
                "maintains": ["Qualification_Standards"]
            }
        ),
        Entity(
            name="Office Software Suite",
            description="Software applications for productivity and business tasks",
            attributes={
                "components": ["word_processor", "spreadsheet", "presentation", "database"],
                "purposes": ["document_creation", "data_analysis", "presentations", "information_management"]
            },
            tags=["software", "productivity_tool"],
            source_file="../docs/business_forms/AB-Card.md",
            relationships={
                "used_by": ["Computer_Users"],
                "evaluated_in": ["AB_Card_Assessment"]
            }
        ),
        Entity(
            name="Professional Qualification Standard",
            description="Standard defining requirements for AB card certification",
            attributes={
                "criteria": ["skill_levels", "knowledge_areas", "competency_domains"],
                "assessment_methods": ["practical_tasks", "theoretical_tests", "portfolio_review"]
            },
            tags=["standard", "requirement"],
            source_file="../docs/business_forms/AB-Card.md",
            relationships={
                "defines": ["AB_Card_Requirements"],
                "evaluated_by": ["Assessment_Bodies"],
                "achieved_by": ["Computer_Users"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="AB Card Certification",
            description="Formal recognition of computer user competence",
            properties={
                "validity_period": "typically_no_expiry",
                "issuing_authority": "authorized_assessment_body",
                "recognition": "nationally_recognized"
            },
            data_schema={
                "validity_period": "string",
                "issuing_authority": "string",
                "recognition": "string"
            },
            tags=["certification", "credential"],
            source_file="../docs/business_forms/AB-Card.md"
        ),
        Component(
            name="Computer Competencies",
            description="Specific ICT skills evaluated in AB card assessment",
            properties={
                "skill_areas": ["word_processing", "spreadsheets", "presentations", "database_management", "information_retrieval"],
                "proficiency_levels": ["basic", "intermediate", "advanced"]
            },
            data_schema={
                "skill_areas": "list[string]",
                "proficiency_levels": "list[string]"
            },
            tags=["competency", "skill_set"],
            source_file="../docs/business_forms/AB-Card.md"
        ),
        Component(
            name="Demonstration of Skills Process",
            description="Method for evaluating computer user competencies",
            properties={
                "evaluation_type": "practical_demonstration",
                "assessment_criteria": ["accuracy", "efficiency", "problem_solving"],
                "required_tasks": ["document_creation", "data_analysis", "presentation_preparation"]
            },
            data_schema={
                "evaluation_type": "string",
                "assessment_criteria": "list[string]",
                "required_tasks": "list[string]"
            },
            tags=["assessment", "evaluation"],
            source_file="../docs/business_forms/AB-Card.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="AB Card Qualification System",
            description="Process for obtaining and maintaining AB card certification",
            behavior=(
                "1. Applicant prepares portfolio of evidence\n"
                "2. Applicant registers for assessment\n"
                "3. Assessment body evaluates competencies\n"
                "4. Practical demonstration of skills is conducted\n"
                "5. Certificate is issued if requirements are met\n"
                "6. Competence is maintained through continuous learning"
            ),
            dependencies=[
                "Computer Competencies",
                "Demonstration of Skills Process",
                "Professional Qualification Standard"
            ],
            triggers=["application_for_certification"],
            tags=["qualification_process", "certification_system"],
            source_file="../docs/business_forms/AB-Card.md"
        ),
        System(
            name="ICT Skills Assessment Framework",
            description="Framework for evaluating ICT competencies",
            behavior=(
                "1. Define competency requirements\n"
                "2. Create assessment tasks\n"
                "3. Evaluate practical skills\n"
                "4. Verify theoretical knowledge\n"
                "5. Issue certification based on results\n"
                "6. Maintain quality standards"
            ),
            dependencies=[
                "Office Software Suite",
                "Professional Qualification Standard"
            ],
            triggers=["qualification_assessment"],
            tags=["assessment_framework", "competency_evaluation"],
            source_file="../docs/business_forms/AB-Card.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/AB-Card.md",
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
            id="constraint_ab_card_requirements",
            title="AB Card Qualification Requirements",
            description="Applicant must demonstrate proficiency in all required skill areas",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="all_required_skills_demonstrated == True",
            scope="qualification_assessment",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Card.md",
            tags=["qualification", "compliance"],
            related_constraints=[],
            validation_logic="check_skill_demonstration(completed_tasks, required_tasks)",
            error_message="All required skills must be demonstrated for AB card certification"
        ),
        Constraint(
            id="constraint_office_software_proficiency",
            title="Office Software Proficiency Requirement",
            description="Applicant must show intermediate to advanced proficiency in office software",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="office_software_proficiency_level >= 'intermediate'",
            scope="skill_assessment",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Card.md",
            tags=["software", "proficiency"],
            related_constraints=["constraint_ab_card_requirements"],
            validation_logic="evaluate_software_proficiency(skill_level)",
            error_message="Intermediate or advanced proficiency in office software required"
        ),
        Constraint(
            id="constraint_demonstration_accuracy",
            title="Accuracy in Practical Demonstration",
            description="Tasks must be completed with high accuracy during assessment",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="task_accuracy_rate >= 0.9",
            scope="assessment_process",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/AB-Card.md",
            tags=["performance", "accuracy"],
            related_constraints=["constraint_ab_card_requirements"],
            validation_logic="calculate_accuracy_score(correct_answers, total_questions)",
            error_message="Tasks must be completed with at least 90% accuracy"
        ),
        Constraint(
            id="constraint_portfolio_content",
            title="Portfolio Content Requirements",
            description="Portfolio must contain evidence of all required competencies",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="all_competency_evidence_present == True",
            scope="portfolio_assessment",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/AB-Card.md",
            tags=["portfolio", "evidence"],
            related_constraints=["constraint_ab_card_requirements"],
            validation_logic="verify_portfolio_content(portfolio, required_evidence)",
            error_message="Portfolio must contain evidence for all required competencies"
        ),
        Constraint(
            id="constraint_assessment_timing",
            title="Assessment Timing Requirements",
            description="Assessment must be completed within specified timeframe",
            constraint_type=ConstraintType.TEMPORAL,
            condition="assessment_completed_within_deadline == True",
            scope="assessment_process",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/AB-Card.md",
            tags=["timing", "deadline"],
            related_constraints=[],
            validation_logic="check_assessment_deadline(completion_time, deadline)",
            error_message="Assessment must be completed within specified timeframe"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/AB-Card.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/AB-Card.md",
        title="AB Card - Computer User Qualification Requirements",
        description="Documentation outlining requirements for AB card computer user qualification, including skill areas, assessment methods, and certification process",
        tags=["AB card", "computer qualification", "ICT skills", "professional certification", "office software", "competency assessment"],
        categories=["qualification", "certification", "ICT", "professional development"],
        related_files=["AB-Kortti.md", "Computer User AB Card Qualification Content and Objectives.md"],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.92,
        content_type="qualification_guide",
        business_domains=["education", "professional_certification", "ICT"],
        difficulty_level="intermediate",
        estimated_reading_time=4,
        word_count=len(content.split()),
        language="en",
        keywords=["AB card", "computer user", "qualification", "ICT", "office software", "competency", "assessment", "professional"],
        related_entities=["Computer User", "Assessment Body", "Office Software Suite", "Professional Qualification Standard"],
        related_components=["AB Card Certification", "Computer Competencies", "Demonstration of Skills Process"],
        related_systems=["AB Card Qualification System", "ICT Skills Assessment Framework"],
        related_constraints=["constraint_ab_card_requirements", "constraint_office_software_proficiency", "constraint_demonstration_accuracy"],
        custom_fields={
            "qualification_type": "professional",
            "assessment_method": "practical_demonstration",
            "target_audience": ["students", "professionals", "job_seekers"],
            "prerequisites": ["basic_computer_literacy"],
            "certification_body": "authorized_assessment_organization"
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
    with open("../processed_docs/ab_card_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: ../processed_docs/ab_card_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_ab_card_document()