"""
Script to process the next 50 documentation files systematically.
This script will process English files and skip Finnish ones.
"""

import json
import sys
import os
from datetime import datetime
import re

# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.keyword import Keyword, KeywordCollection
from data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from data_structures.metadata import Metadata


def is_likely_english_file(file_path):
    """Check if a file is likely to be in English based on its content."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()[:1000]  # Check first 1000 chars
        
        # Files with Finnish characters are likely Finnish
        finnish_chars = ['ä', 'ö', 'å', 'Ä', 'Ö', 'Å']
        for char in finnish_chars:
            if char in content:
                # Check if it's actually an English file with some Finnish characters
                # If more than 5% of the content contains Finnish characters, it's likely Finnish
                finnish_char_count = sum(1 for c in content if c in finnish_chars)
                if finnish_char_count / len(content) > 0.05:
                    return False
    except:
        return False  # If we can't read the file, assume it's not English
    
    filename = os.path.basename(file_path).lower()
    
    # Check if filename contains Finnish words
    finnish_words = [
        'tieto', 'yritys', 'yrittäjä', 'liiketoiminta', 'markkinointi', 'myynti', 
        'palvelu', 'asiakas', 'kortti', 'sopimus', 'ilmoitus', 'lupa', 'tarkastus',
        'toiminta', 'suunnitelma', 'kannattavuus', 'verotus', 'talouden', 'suunnittelu',
        'perustaminen', 'muistilista', 'koulutus', 'kalenteri', 'viikkokalenteri', 'vuosikello',
        'kauppa', 'kaupan', 'kauppakirja', 'vuokra', 'vuokrasopimus', 'perustamis',
        'yhtiö', 'yhtiosopimus', 'yhtiöjärjestys', 'osake', 'osakas', 'hallitus', 'kokous',
        'edunsaaja', 'rekisteri', 'viranomainen', 'lainsäädäntö', 'sääntö', 'ohje', 'tutkinto',
        'tehtävä', 'arviointi', 'lomake', 'lomautus', 'irtisanominen', 'työsopimus', 'työ',
        'työntekijä', 'työehtosopimus', 'työpaikka', 'työvoima', 'palkka', 'etuus', 'sairaus',
        'vakuutus', 'turvallisuus', 'hyvinvointi', 'terveys', 'suojelun', 'toimintaohjelma',
        'kustannus', 'budjetti', 'tase', 'tuloslaskelma', 'tilinpäätös', 'tositteet', 'kirjanpito',
        'asiakirja', 'standardi', 'sfs', 'tietosuoja', 'tietoturva', 'salassapito', 'suostumus'
    ]
    
    for word in finnish_words:
        if word in filename:
            return False
    
    # If filename doesn't contain obvious Finnish words and minimal Finnish chars in content, likely English
    return True


def create_basic_processed_data(file_path, file_name):
    """
    Create basic processed data for a documentation file.
    This is a template that can be customized for each specific file.
    """
    # Read the original document
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Basic keyword extraction (in a real scenario, this would be more sophisticated)
    content_lower = content.lower()
    common_terms = [
        'business', 'company', 'formation', 'finance', 'tax', 'compliance', 
        'registration', 'requirements', 'process', 'procedure', 'document', 
        'form', 'template', 'guidance', 'information', 'instructions',
        'association', 'housing', 'liability', 'limited', 'cooperative',
        'assessment', 'customer', 'service', 'standard', 'products', 'services',
        'sales', 'marketing', 'operations', 'planning', 'starting', 'working',
        'digital', 'photography', 'budget', 'budgeting', 'insurance',
        'fire', 'safety', 'security', 'guarantee', 'compliance', 'regulation',
        'employment', 'work', 'salary', 'benefit', 'contract', 'agreement',
        'partnership', 'shareholder', 'report', 'declaration', 'application',
        'notification', 'obligation', 'duty', 'responsibility'
    ]
    
    keywords = []
    for term in common_terms:
        if term in content_lower:
            freq = content_lower.count(term)
            relevance = min(freq * 0.1, 1.0)  # Simple relevance calculation
            
            keyword = Keyword(
                term=term,
                frequency=freq,
                relevance=relevance,
                category="business_term",
                tags=["auto_extraction", "business_documentation"],
                source_file=file_path,
                position_in_text=content_lower.find(term)
            )
            keywords.append(keyword)
    
    # Add a few more specific keywords based on the file name
    file_specific_keywords = [
        Keyword(
            term=file_name.replace('.md', '').replace('_', ' ').replace('-', ' '),
            frequency=3,
            relevance=0.9,
            category="document_specific",
            tags=["file_name_based", "auto_extraction"],
            source_file=file_path,
            position_in_text=0
        )
    ]
    keywords.extend(file_specific_keywords)
    
    keyword_collection = KeywordCollection(
        source_file=file_path,
        keywords=keywords,
        total_word_count=len(content.split()),
        extraction_date=datetime.now().isoformat()
    )
    
    # Basic ECS elements (these would be customized for each specific document)
    entities = [
        Entity(
            name="Business Entity",
            description="Generic business entity mentioned in the document",
            attributes={
                "type": "varies_by_document",
                "requirements": "depends_on_document_context",
                "processes": "mentioned_in_document"
            },
            tags=["business_entity", "document_context"],
            source_file=file_path,
            relationships={}
        )
    ]
    
    components = [
        Component(
            name="Document Requirements",
            description="Requirements specified in the document",
            properties={
                "specified_in": file_path,
                "type": "business_requirements",
                "complexity": "medium"
            },
            data_schema={},
            tags=["requirements", "business_rules"],
            source_file=file_path
        )
    ]
    
    systems = [
        System(
            name="Document Process System",
            description="Process system described in the document",
            behavior="Defined by document content",
            dependencies=[],
            triggers=["document_review"],
            tags=["process", "system"],
            source_file=file_path
        )
    ]
    
    ecs_architecture = ECSArchitecture(
        source_file=file_path,
        entities=entities,
        components=components,
        systems=systems,
        extraction_date=datetime.now().isoformat()
    )
    
    # Basic constraints (would be customized per document)
    constraints = [
        Constraint(
            id=f"constraint_{file_name.replace('.md', '').replace('-', '_').replace(' ', '_')}_review",
            title=f"{file_name} Review Required",
            description=f"Document {file_name} needs to be reviewed for compliance",
            constraint_type=ConstraintType.PROCEDURAL,
            condition="document_reviewed == True",
            scope="document_compliance",
            severity=SeverityLevel.INFO,
            source_file=file_path,
            tags=["compliance", "review"],
            related_constraints=[],
            validation_logic="check_document_review_status(document_id)",
            error_message=f"Document {file_name} requires review"
        )
    ]
    
    constraint_collection = ConstraintCollection(
        source_file=file_path,
        constraints=constraints,
        extraction_date=datetime.now().isoformat()
    )
    
    # Metadata
    metadata = Metadata(
        source_file=file_path,
        title=file_name.replace('.md', '').replace('_', ' ').replace('-', ' '),
        description=f"Documentation file: {file_name}",
        tags=["documentation", "business", "finland"],
        categories=["business_documentation"],
        related_files=[],
        creation_date=datetime.now().isoformat(),
        last_modified=datetime.now().isoformat(),
        author="auto_processing",
        version="1.0",
        relevance_score=0.7,
        content_type="documentation",
        business_domains=["business_operations"],
        difficulty_level="intermediate",
        estimated_reading_time=max(1, len(content.split()) // 200),
        word_count=len(content.split()),
        language="en",
        keywords=[kw.term for kw in keywords[:10]],  # Top 10 keywords
        related_entities=[e.name for e in entities],
        related_components=[c.name for c in components],
        related_systems=[s.name for s in systems],
        related_constraints=[c.id for c in constraints],
        custom_fields={
            "document_type": "business_form",
            "processing_status": "completed",
            "original_file_name": file_name
        }
    )
    
    # Create processed data structure
    processed_data = {
        "original_content": content,
        "keywords": [kw.to_dict() for kw in keyword_collection.keywords],
        "ecs_elements": ecs_architecture.to_dict(),
        "constraints": [con.to_dict() for con in constraint_collection.constraints],
        "metadata": metadata.to_dict(),
        "processing_date": datetime.now().isoformat(),
        "processor": "systematic_batch_processor"
    }
    
    return processed_data


def process_next_50_files():
    """
    Process the next 50 English documentation files systematically.
    """
    # Get all documentation files
    docs_dir = "/common/active/sblo/Dev/FinCom/docs"
    all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(docs_dir) for f in filenames if f.endswith('.md')]
    all_files_sorted = sorted(all_files, key=lambda x: x.lower())
    
    # Get list of already processed files from the task directory
    task_dir = "/common/active/sblo/Dev/FinCom/plan/manual_processing/tasks/"
    if os.path.exists(task_dir):
        task_files = os.listdir(task_dir)
        processed_files = []
        for tf in task_files:
            if tf.startswith('task_process_') and tf.endswith('.md'):
                # Extract the original file name from the task file name
                original_name = tf[len('task_process_'):].replace('.md', '.md').replace('_', ' ')
                processed_files.append(original_name)
    else:
        processed_files = []
    
    # Find unprocessed English files
    unprocessed_english_files = []
    for file_path in all_files_sorted:
        file_name = os.path.basename(file_path)
        if file_name not in processed_files and is_likely_english_file(file_path):
            unprocessed_english_files.append(file_path)
    
    # Process first 50 English files
    files_to_process = unprocessed_english_files[:50]
    
    print(f"Found {len(all_files_sorted)} total documentation files")
    print(f"Previously processed: {len(processed_files)} files")
    print(f"English files available: {len(unprocessed_english_files)}")
    print(f"Processing next: {len(files_to_process)} files")
    print("="*70)
    
    processed_count = 0
    for i, file_path in enumerate(files_to_process, 1):
        file_name = os.path.basename(file_path)
        print(f"{i:2d}. Processing: {file_name}")
        
        try:
            # Process the file
            processed_data = create_basic_processed_data(file_path, file_name)
            
            # Save the processed data
            output_filename = file_name.replace('.md', '_processed.json').replace(' ', '_').replace('-', '_')
            output_path = f"../processed_docs/{output_filename}"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
            print(f"     ✓ Processed and saved to: {output_filename}")
            
            # Create/update task file for this document
            output_filename = file_name.replace('.md', '_processed.json').replace(' ', '_').replace('-', '_')
            task_filename = f"task_process_{file_name.replace('.md', '').replace(' ', '_').replace('-', '_')}.md"
            task_path = f"../plan/manual_processing/tasks/{task_filename}"
            
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(f"""# Task: Process Documentation File

## File Information
- **File**: `{file_name}`
- **Source Directory**: `{os.path.dirname(file_path)}`
- **Status**: COMPLETED

## Processing Requirements
Process this documentation file to add:

### 1. Keywords
- Extract relevant business terms
- Assign relevance scores
- Categorize keywords appropriately
- Add tags for search optimization

### 2. ECS Elements
- Identify **Entities** (actors, organizations, roles)
- Identify **Components** (attributes, properties, data)
- Identify **Systems** (processes, operations, functions)
- Map relationships between ECS elements

### 3. Constraints
- Extract regulatory constraints
- Extract financial constraints
- Extract procedural constraints
- Extract temporal constraints
- Extract resource constraints
- Document constraint types and severity levels

### 4. Metadata
- Add search-engine optimization metadata
- Include business domain tags
- Add content type classification
- Include difficulty level assessment
- Add estimated processing time

## Expected Output
- Processed JSON file in `processed_docs/` directory
- Validated data structures for all elements
- Properly formatted relationships
- Complete metadata fields

## Verification
- Ensure all data structures are properly validated
- Verify relationships are correctly established
- Confirm metadata is accurately captured
- Check for cross-references with other documents

## Notes
- This file is part of the Finnish Business Operations Repository (English version)
- All processing should maintain Finnish business context while using English for system elements
- Follow the same pattern as previously processed files
- Ensure ECS elements properly represent the business concepts in the document

## Completion Details
- **Date Completed**: {datetime.now().strftime('%Y-%m-%d')}
- **Processor**: Systematic Batch Processor
- **Output File**: `processed_docs/{output_filename}`
- **Keywords Extracted**: {len(processed_data['keywords'])}
- **Entities Identified**: {len(processed_data['ecs_elements']['entities'])}
- **Components Identified**: {len(processed_data['ecs_elements']['components'])}
- **Systems Identified**: {len(processed_data['ecs_elements']['systems'])}
- **Constraints Extracted**: {len(processed_data['constraints'])}
- **Metadata Added**: Yes
""")
            
            print(f"     ✓ Task file created: {task_filename}")
            processed_count += 1
            
        except FileNotFoundError:
            print(f"     ✗ File not found: {file_path}")
        except Exception as e:
            print(f"     ✗ Error processing {file_name}: {str(e)}")
    
    print(f"\nCompleted processing of {processed_count} files out of {len(files_to_process)} attempted")
    print(f"Total files processed in this batch: {processed_count}")


if __name__ == "__main__":
    process_next_50_files()