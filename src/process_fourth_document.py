"""
Script to manually process the Finnish marketing fundamentals documentation file (already in English) and add keywords, ECS elements, constraints, and metadata.
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


def process_marketing_fundamentals_finnish_document():
    """
    Manually process the marketing fundamentals Finnish document (already in English) to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: 2025 Markkinointi_perusteet_kilpailukeinot.md")
    print("="*70)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="marketing fundamentals",
            frequency=15,
            relevance=0.95,
            category="marketing",
            tags=["manual_extraction", "marketing_fundamentals"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=10
        ),
        Keyword(
            term="marketing competition methods",
            frequency=8,
            relevance=0.9,
            category="strategy",
            tags=["manual_extraction", "competitive_analysis"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=50
        ),
        Keyword(
            term="7P model",
            frequency=12,
            relevance=0.85,
            category="marketing",
            tags=["manual_extraction", "marketing_framework"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=100
        ),
        Keyword(
            term="marketing planning tools",
            frequency=6,
            relevance=0.8,
            category="tools",
            tags=["manual_extraction", "planning"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=150
        ),
        Keyword(
            term="service design",
            frequency=7,
            relevance=0.85,
            category="design",
            tags=["manual_extraction", "service_development"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=200
        ),
        Keyword(
            term="marketing communication",
            frequency=9,
            relevance=0.9,
            category="communication",
            tags=["manual_extraction", "marketing_channels"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=250
        ),
        Keyword(
            term="sustainability",
            frequency=5,
            relevance=0.75,
            category="business_principle",
            tags=["manual_extraction", "sustainable_practices"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=300
        ),
        Keyword(
            term="lean methodology",
            frequency=4,
            relevance=0.7,
            category="methodology",
            tags=["manual_extraction", "efficiency"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            position_in_text=350
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
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
            name="Marketing Department",
            description="Team responsible for implementing marketing strategies and communication",
            attributes={
                "responsibilities": ["service_design", "pricing", "marketing_communication", "distribution_arrangement"],
                "skills_required": ["strategic_thinking", "creative_problem_solving", "analytical_skills"],
                "tools_used": ["marketing_planning_tools", "analytics_platforms", "crm_systems"]
            },
            tags=["department", "marketing_team"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            relationships={
                "implements": ["Marketing_Strategies"],
                "communicates_to": ["Market"],
                "designs": ["Service_Experiences"]
            }
        ),
        Entity(
            name="Customer",
            description="Target of marketing efforts who engages in transactions",
            attributes={
                "characteristics": ["needs", "preferences", "buying_behavior"],
                "objectives": ["fulfill_personal_objectives", "obtain_value"],
                "interaction_type": ["transaction_based", "relationship_based"]
            },
            tags=["target_audience", "customer_segment"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            relationships={
                "engages_with": ["Marketing_Department"],
                "purchases": ["Products_Services"],
                "fulfills_objectives_through": ["Transactions"]
            }
        ),
        Entity(
            name="Company",
            description="Organization implementing marketing processes",
            attributes={
                "functions": ["service_design", "pricing", "marketing_communication", "distribution"],
                "goals": ["profitability", "market_share", "customer_satisfaction"],
                "approach": ["agile", "lean", "sustainability_focused"]
            },
            tags=["organization", "business_entity"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            relationships={
                "conducts": ["Marketing_Processes"],
                "interacts_with": ["Customers"],
                "implements": ["7P_Model"]
            }
        ),
        Entity(
            name="Market",
            description="Environment where marketing activities take place",
            attributes={
                "participants": ["companies", "customers", "competitors"],
                "dynamics": ["competition", "demand_fluctuations", "trend_shifts"],
                "requirements": ["visibility", "accessibility", "relevance"]
            },
            tags=["environment", "market_space"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            relationships={
                "receives": ["Marketing_Communication"],
                "influences": ["Pricing_Strategies"],
                "shapes": ["Distribution_Methods"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="Service Design",
            description="Process of creating services that meet customer needs",
            properties={
                "elements": ["functionality", "user_experience", "accessibility"],
                "considerations": ["customer_journey", "touchpoints", "value_creation"],
                "outcomes": ["customer_satisfaction", "market_fit"]
            },
            data_schema={
                "elements": "list[string]",
                "considerations": "list[string]",
                "outcomes": "list[string]"
            },
            tags=["design_process", "service_development"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md"
        ),
        Component(
            name="Pricing Strategy",
            description="Approach to setting prices for products and services",
            properties={
                "factors": ["cost", "competition", "perceived_value"],
                "models": ["cost_plus", "value_based", "competition_based"],
                "objectives": ["profitability", "market_penetration", "competitive_positioning"]
            },
            data_schema={
                "factors": "list[string]",
                "models": "list[string]",
                "objectives": "list[string]"
            },
            tags=["pricing", "revenue_strategy"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md"
        ),
        Component(
            name="Marketing Communication",
            description="Methods of conveying value proposition to the market",
            properties={
                "channels": ["traditional", "digital", "social_media", "direct"],
                "messages": ["promotional", "educational", "brand_building"],
                "objectives": ["awareness", "engagement", "conversion"]
            },
            data_schema={
                "channels": "list[string]",
                "messages": "list[string]",
                "objectives": "list[string]"
            },
            tags=["communication", "marketing_channels"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="Marketing Process System",
            description="Comprehensive system for planning and implementing marketing activities",
            behavior=(
                "1. Plan ideas as products\n"
                "2. Price products appropriately\n"
                "3. Communicate to the market\n"
                "4. Arrange distribution\n"
                "5. Monitor and adjust based on feedback"
            ),
            dependencies=[
                "Service Design",
                "Pricing Strategy",
                "Marketing Communication"
            ],
            triggers=["new_product_development", "market_change", "competitive_action"],
            tags=["process", "marketing_system"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md"
        ),
        System(
            name="7P Model Implementation Framework",
            description="Framework for implementing the 7P marketing model",
            behavior=(
                "1. Define Product offering\n"
                "2. Set Pricing strategy\n"
                "3. Plan Place (distribution)\n"
                "4. Develop Promotion strategy\n"
                "5. Organize People (staff)\n"
                "6. Implement Processes\n"
                "7. Create Physical Evidence"
            ),
            dependencies=[
                "Service Design",
                "Pricing Strategy",
                "Marketing Communication"
            ],
            triggers=["marketing_strategy_review", "service_expansion", "market_entry"],
            tags=["framework", "marketing_model"],
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
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
            id="constraint_marketing_agility",
            title="Marketing Agility Requirement",
            description="Marketing should be agile (lean) sustainability-focused rather than reckless spending",
            constraint_type=ConstraintType.PROCEDURAL,
            condition="marketing_approach == 'agile_sustainable'",
            scope="marketing_methodology",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            tags=["methodology", "sustainability", "efficiency"],
            related_constraints=[],
            validation_logic="check_marketing_approach(approach)",
            error_message="Marketing should follow agile and sustainable practices"
        ),
        Constraint(
            id="constraint_customer_interaction",
            title="Customer Interaction Focus",
            description="Marketing is about human interaction with the goal of conducting transactions that fulfill parties' objectives",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="marketing_activities_include_customer_interaction == True",
            scope="marketing_philosophy",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            tags=["interaction", "customer_focus", "transaction"],
            related_constraints=[],
            validation_logic="validate_customer_interaction_elements(activity)",
            error_message="Marketing activities must focus on customer interaction and transaction fulfillment"
        ),
        Constraint(
            id="constraint_service_design_completeness",
            title="Service Design Completeness",
            description="Service design should encompass everything done in the company",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="service_design_comprehensiveness_score >= 0.8",
            scope="service_development",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            tags=["service_design", "completeness", "integration"],
            related_constraints=["constraint_marketing_agility"],
            validation_logic="evaluate_service_design_coverage(design)",
            error_message="Service design should encompass all company activities"
        ),
        Constraint(
            id="constraint_marketing_definition",
            title="Marketing Definition Adherence",
            description="Marketing encompasses planning and implementing products, pricing, communication and distribution",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="marketing_scope.includes(['product', 'price', 'promotion', 'place'])",
            scope="marketing_scope",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            tags=["definition", "scope", "completeness"],
            related_constraints=["constraint_customer_interaction"],
            validation_logic="verify_marketing_scope(scope)",
            error_message="Marketing activities must cover all 4Ps (Product, Price, Place, Promotion)"
        ),
        Constraint(
            id="constraint_7p_expansion",
            title="7P Model Expansion",
            description="Traditional 4P model should be expanded to 7P model for better service business consideration",
            constraint_type=ConstraintType.PROCEDURAL,
            condition="marketing_model == '7P' or marketing_model == 'expanded_4P'",
            scope="marketing_framework",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
            tags=["framework", "expansion", "service_business"],
            related_constraints=["constraint_marketing_definition"],
            validation_logic="check_marketing_model(model)",
            error_message="Use 7P model instead of traditional 4P for service businesses"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/2025 Markkinointi_perusteet_kilpailukeinot.md",
        title="Marketing Fundamentals and Competition Methods (2025)",
        description="Documentation compiling key information about marketing fundamentals, competition methods (4P/7P) and marketing planning tools",
        tags=["marketing", "fundamentals", "competition", "7P_model", "2025", "business_growth"],
        categories=["marketing", "strategy", "competitive_analysis"],
        related_files=["2025 Marketing Fundamentals and Competitive Strategies.md"],  # English version
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.94,
        content_type="guide",
        business_domains=["marketing", "strategy", "service_design"],
        difficulty_level="intermediate",
        estimated_reading_time=10,
        word_count=len(content.split()),
        language="en",
        keywords=["marketing", "fundamentals", "competition", "4P", "7P", "2025", "business", "growth", "planning"],
        related_entities=["Marketing Department", "Customer", "Company", "Market"],
        related_components=["Service Design", "Pricing Strategy", "Marketing Communication"],
        related_systems=["Marketing Process System", "7P Model Implementation Framework"],
        related_constraints=["constraint_marketing_agility", "constraint_customer_interaction", "constraint_service_design_completeness"],
        custom_fields={
            "target_audience": ["marketing_professionals", "business_owners", "strategic_planners"],
            "prerequisites": ["basic_business_knowledge"],
            "follow_up_steps": ["implement_marketing_strategy", "monitor_performance", "adjust_approach"]
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
    with open("../processed_docs/marketing_fundamentals_finnish_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: ../processed_docs/marketing_fundamentals_finnish_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_marketing_fundamentals_finnish_document()