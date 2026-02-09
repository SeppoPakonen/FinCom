"""
Script to manually process the marketing fundamentals documentation file and add keywords, ECS elements, constraints, and metadata.
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


def process_marketing_fundamentals_document():
    """
    Manually process the marketing fundamentals document to add:
    - Keywords
    - ECS elements (entities, components, systems)
    - Constraints
    - Search-engine metadata
    """
    
    # Read the original document
    with open("../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    print("Processing document: 2025 Marketing Fundamentals and Competitive Strategies.md")
    print("="*70)
    
    # 1. Extract and add keywords
    print("1. Adding keywords...")
    keywords = [
        Keyword(
            term="marketing fundamentals",
            frequency=12,
            relevance=0.95,
            category="marketing",
            tags=["manual_extraction", "marketing_fundamentals"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=15
        ),
        Keyword(
            term="competitive strategies",
            frequency=10,
            relevance=0.9,
            category="strategy",
            tags=["manual_extraction", "competitive_analysis"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=45
        ),
        Keyword(
            term="market research",
            frequency=8,
            relevance=0.85,
            category="research",
            tags=["manual_extraction", "market_analysis"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=80
        ),
        Keyword(
            term="brand positioning",
            frequency=7,
            relevance=0.8,
            category="marketing",
            tags=["manual_extraction", "branding"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=120
        ),
        Keyword(
            term="target audience",
            frequency=9,
            relevance=0.85,
            category="marketing",
            tags=["manual_extraction", "customer_segmentation"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=160
        ),
        Keyword(
            term="digital marketing",
            frequency=6,
            relevance=0.8,
            category="marketing",
            tags=["manual_extraction", "digital_channels"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=200
        ),
        Keyword(
            term="marketing mix",
            frequency=5,
            relevance=0.75,
            category="marketing",
            tags=["manual_extraction", "marketing_framework"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=240
        ),
        Keyword(
            term="SWOT analysis",
            frequency=4,
            relevance=0.7,
            category="analysis",
            tags=["manual_extraction", "strategic_analysis"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            position_in_text=280
        )
    ]
    
    keyword_collection = KeywordCollection(
        source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
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
            name="Marketing Team",
            description="Group responsible for executing marketing strategies",
            attributes={
                "responsibilities": ["market_research", "campaign_development", "brand_management"],
                "skills_required": ["analytical_thinking", "creativity", "communication"],
                "tools_used": ["analytics_platforms", "design_software", "crm_systems"]
            },
            tags=["team", "marketing_department"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            relationships={
                "develops": ["Marketing Campaigns"],
                "analyses": ["Market Data"],
                "implements": ["Marketing Strategies"]
            }
        ),
        Entity(
            name="Target Customer",
            description="Primary audience for marketing efforts",
            attributes={
                "demographics": ["age", "gender", "income", "location"],
                "psychographics": ["interests", "values", "lifestyle"],
                "behavioral_traits": ["purchase_history", "brand_preferences", "channel_preferences"]
            },
            tags=["customer_segment", "audience"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            relationships={
                "receives": ["Marketing Messages"],
                "engages_with": ["Marketing Channels"],
                "purchases": ["Products_Services"]
            }
        ),
        Entity(
            name="Competitor",
            description="Other businesses offering similar products/services",
            attributes={
                "market_position": "relative_to_own_business",
                "strengths": ["product_quality", "pricing", "brand_recognition"],
                "weaknesses": ["service_gaps", "price_points", "market_segments"]
            },
            tags=["competition", "market_analysis"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            relationships={
                "competes_with": ["Own_Business"],
                "targets": ["Similar_Customers"],
                "offers": ["Competing_Products_Services"]
            }
        ),
        Entity(
            name="Marketing Channel",
            description="Medium through which marketing messages are delivered",
            attributes={
                "channel_type": ["digital", "traditional", "social_media", "email"],
                "reach": "potential_customer_base",
                "cost_efficiency": "cost_per_acquisition",
                "engagement_level": "customer_interaction_quality"
            },
            tags=["distribution", "communication"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            relationships={
                "delivers": ["Marketing_Messages"],
                "connects": ["Business_to_Customers"],
                "generates": ["Customer_Insights"]
            }
        )
    ]
    
    # Components
    components = [
        Component(
            name="Market Research Data",
            description="Information gathered about market conditions, customer preferences, and competitor activities",
            properties={
                "data_sources": ["surveys", "analytics", "focus_groups", "sales_data"],
                "collection_method": "primary_or_secondary_research",
                "analysis_type": ["quantitative", "qualitative", "predictive"]
            },
            data_schema={
                "data_sources": "list[string]",
                "collection_method": "string",
                "analysis_type": "list[string]"
            },
            tags=["data", "research", "analysis"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md"
        ),
        Component(
            name="Brand Identity",
            description="Visual and conceptual elements that represent the business",
            properties={
                "visual_elements": ["logo", "color_scheme", "typography"],
                "verbal_elements": ["tagline", "voice", "tone"],
                "core_values": ["trust", "innovation", "quality"]
            },
            data_schema={
                "visual_elements": "list[string]",
                "verbal_elements": "list[string]",
                "core_values": "list[string]"
            },
            tags=["branding", "identity", "positioning"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md"
        ),
        Component(
            name="Marketing Message",
            description="Content designed to communicate value proposition to target audience",
            properties={
                "message_type": ["promotional", "educational", "informative"],
                "tone": ["professional", "casual", "authoritative"],
                "channels": ["social_media", "email", "website", "advertising"]
            },
            data_schema={
                "message_type": "string",
                "tone": "string",
                "channels": "list[string]"
            },
            tags=["content", "communication", "messaging"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md"
        )
    ]
    
    # Systems
    systems = [
        System(
            name="Marketing Strategy Development Process",
            description="Structured approach to developing marketing strategies",
            behavior=(
                "1. Conduct market research and competitive analysis\n"
                "2. Define target audience and value proposition\n"
                "3. Develop brand identity and messaging\n"
                "4. Select marketing channels and tactics\n"
                "5. Set KPIs and measurement methods\n"
                "6. Execute and monitor campaigns\n"
                "7. Analyze results and optimize strategies"
            ),
            dependencies=[
                "Market Research Data",
                "Brand Identity",
                "Marketing Message"
            ],
            triggers=["new_product_launch", "seasonal_campaign", "competitive_response"],
            tags=["process", "strategy", "development"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md"
        ),
        System(
            name="Competitive Analysis Framework",
            description="Methodology for evaluating competitor strengths and weaknesses",
            behavior=(
                "1. Identify direct and indirect competitors\n"
                "2. Analyze competitor products/services\n"
                "3. Evaluate competitor pricing strategies\n"
                "4. Assess competitor marketing approaches\n"
                "5. Identify market gaps and opportunities\n"
                "6. Develop competitive positioning strategies"
            ),
            dependencies=[
                "Market Research Data",
                "Competitor"
            ],
            triggers=["new_competitor_entry", "market_change", "strategic_review"],
            tags=["analysis", "competition", "framework"],
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md"
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
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
            id="constraint_budget_allocation",
            title="Marketing Budget Allocation",
            description="Marketing budget should be allocated according to channel effectiveness and ROI",
            constraint_type=ConstraintType.FINANCIAL,
            condition="budget_allocation_effectiveness_ratio > 0.7",
            scope="marketing_budget",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            tags=["budget", "allocation", "roi"],
            related_constraints=["constraint_roi_measurement"],
            validation_logic="calculate_channel_roi(channel_performance, cost)",
            error_message="Marketing budget allocation should prioritize high-ROI channels"
        ),
        Constraint(
            id="constraint_target_audience_alignment",
            title="Target Audience Alignment",
            description="All marketing messages must align with defined target audience characteristics",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="message_audience_match_score >= 0.8",
            scope="marketing_communication",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            tags=["audience", "alignment", "communication"],
            related_constraints=["constraint_brand_positioning"],
            validation_logic="check_message_audience_alignment(message, target_profile)",
            error_message="Marketing messages must align with target audience profile"
        ),
        Constraint(
            id="constraint_brand_consistency",
            title="Brand Consistency",
            description="All marketing materials must maintain consistent brand identity",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="brand_guideline_adherence_score >= 0.9",
            scope="brand_management",
            severity=SeverityLevel.ERROR,
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            tags=["brand", "consistency", "guidelines"],
            related_constraints=["constraint_brand_positioning"],
            validation_logic="validate_brand_elements(material, brand_guidelines)",
            error_message="Marketing materials must adhere to brand guidelines"
        ),
        Constraint(
            id="constraint_roi_measurement",
            title="ROI Measurement Requirement",
            description="Marketing campaigns must have measurable ROI metrics defined before launch",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="roi_metrics_defined == True",
            scope="campaign_execution",
            severity=SeverityLevel.CRITICAL,
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            tags=["roi", "measurement", "metrics"],
            related_constraints=["constraint_budget_allocation"],
            validation_logic="check_roi_metrics_exist(campaign)",
            error_message="Campaigns must have defined ROI metrics before launch"
        ),
        Constraint(
            id="constraint_competitive_monitoring",
            title="Competitive Monitoring",
            description="Competitor activities should be monitored regularly to inform strategy adjustments",
            constraint_type=ConstraintType.PROCEDURAL,
            condition="competitor_monitoring_frequency >= 'weekly'",
            scope="competitive_intelligence",
            severity=SeverityLevel.WARNING,
            source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
            tags=["monitoring", "competition", "intelligence"],
            related_constraints=[],
            validation_logic="check_monitoring_schedule(activity_log)",
            error_message="Competitor activities should be monitored regularly"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    print(f"   Added {len(constraints)} constraints")
    
    # 4. Add search-engine metadata
    print("4. Adding search-engine metadata...")
    metadata = Metadata(
        source_file="../docs/business_forms/2025 Marketing Fundamentals and Competitive Strategies.md",
        title="Marketing Fundamentals and Competitive Strategies 2025",
        description="Documentation outlining fundamental marketing principles and competitive strategies for businesses",
        tags=["marketing", "fundamentals", "competitive_strategies", "2025", "business_growth"],
        categories=["marketing", "strategy", "competitive_analysis"],
        related_files=["2025 Markkinointi perusteet kilpailukeinot.md"],  # Finnish version
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="manual_processing",
        version="1.0",
        relevance_score=0.92,
        content_type="guide",
        business_domains=["marketing", "strategy", "competitive_analysis"],
        difficulty_level="intermediate",
        estimated_reading_time=8,
        word_count=len(content.split()),
        language="en",
        keywords=["marketing", "fundamentals", "competitive", "strategies", "2025", "business", "growth", "analysis"],
        related_entities=["Marketing Team", "Target Customer", "Competitor", "Marketing Channel"],
        related_components=["Market Research Data", "Brand Identity", "Marketing Message"],
        related_systems=["Marketing Strategy Development Process", "Competitive Analysis Framework"],
        related_constraints=["constraint_budget_allocation", "constraint_target_audience_alignment", "constraint_brand_consistency"],
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
    with open("../processed_docs/marketing_fundamentals_2025_processed.json", "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDocument processed successfully!")
    print(f"- Keywords: {len(keywords)}")
    print(f"- Entities: {len(entities)}")
    print(f"- Components: {len(components)}")
    print(f"- Systems: {len(systems)}")
    print(f"- Constraints: {len(constraints)}")
    print(f"- Metadata: Added")
    print(f"\nProcessed data saved to: processed_docs/marketing_fundamentals_2025_processed.json")
    
    return processed_data


if __name__ == "__main__":
    processed_data = process_marketing_fundamentals_document()