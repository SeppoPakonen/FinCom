"""
Script to consolidate all processed JSON files into a unified data structure.
This script performs Phase 1 of the action plan: Data Integration and Validation.
"""

import json
import os
from datetime import datetime
from pathlib import Path


def consolidate_processed_files():
    """
    Consolidate all processed JSON files into a unified data structure.
    """
    # Define paths
    processed_docs_dir = "/common/active/sblo/Dev/FinCom/processed_docs"
    consolidated_output_dir = "/common/active/sblo/Dev/FinCom/consolidated_data"
    
    # Create output directory if it doesn't exist
    os.makedirs(consolidated_output_dir, exist_ok=True)
    
    # Get all processed JSON files
    processed_files = [f for f in os.listdir(processed_docs_dir) if f.endswith('_processed.json')]
    
    print(f"Found {len(processed_files)} processed JSON files to consolidate")
    
    # Initialize consolidated data structure
    consolidated_data = {
        "metadata": {
            "consolidation_date": datetime.now().isoformat(),
            "total_files_processed": len(processed_files),
            "source_directory": processed_docs_dir,
            "description": "Consolidated data from all processed documentation files"
        },
        "documents": [],
        "all_keywords": [],
        "all_entities": [],
        "all_components": [],
        "all_systems": [],
        "all_constraints": [],
        "all_metadata": []
    }
    
    # Process each file
    for i, filename in enumerate(processed_files, 1):
        file_path = os.path.join(processed_docs_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
            
            # Add document to consolidated list
            doc_entry = {
                "filename": filename,
                "source_file": file_data.get("original_content", {}).get("source_file", filename),
                "keywords": file_data.get("keywords", []),
                "ecs_elements": file_data.get("ecs_elements", {}),
                "constraints": file_data.get("constraints", []),
                "metadata": file_data.get("metadata", {}),
                "processing_date": file_data.get("processing_date", ""),
                "processor": file_data.get("processor", "")
            }
            
            consolidated_data["documents"].append(doc_entry)
            
            # Add to global collections
            consolidated_data["all_keywords"].extend([
                {**kw, "source_file": filename} for kw in file_data.get("keywords", [])
            ])
            
            ecs_elements = file_data.get("ecs_elements", {})
            if isinstance(ecs_elements, dict):
                consolidated_data["all_entities"].extend([
                    {**entity, "source_file": filename} for entity in ecs_elements.get("entities", [])
                ])
                consolidated_data["all_components"].extend([
                    {**comp, "source_file": filename} for comp in ecs_elements.get("components", [])
                ])
                consolidated_data["all_systems"].extend([
                    {**sys, "source_file": filename} for sys in ecs_elements.get("systems", [])
                ])
            
            consolidated_data["all_constraints"].extend([
                {**constraint, "source_file": filename} for constraint in file_data.get("constraints", [])
            ])
            
            consolidated_data["all_metadata"].append({
                **file_data.get("metadata", {}),
                "source_file": filename
            })
            
            if i % 50 == 0:
                print(f"  Processed {i}/{len(processed_files)} files...")
                
        except Exception as e:
            print(f"Error processing file {filename}: {str(e)}")
            continue
    
    # Save the consolidated data
    output_path = os.path.join(consolidated_output_dir, "consolidated_processed_data.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(consolidated_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nConsolidation complete! Created {output_path}")
    print(f"Total documents in consolidated data: {len(consolidated_data['documents'])}")
    print(f"Total keywords in consolidated data: {len(consolidated_data['all_keywords'])}")
    print(f"Total entities in consolidated data: {len(consolidated_data['all_entities'])}")
    print(f"Total components in consolidated data: {len(consolidated_data['all_components'])}")
    print(f"Total systems in consolidated data: {len(consolidated_data['all_systems'])}")
    print(f"Total constraints in consolidated data: {len(consolidated_data['all_constraints'])}")
    
    return output_path


def validate_data_integrity(consolidated_file_path):
    """
    Validate data integrity across all processed files.
    """
    print("\nValidating data integrity...")
    
    with open(consolidated_file_path, 'r', encoding='utf-8') as f:
        consolidated_data = json.load(f)
    
    issues_found = []
    
    # Check for missing required fields in documents
    for doc in consolidated_data['documents']:
        if not doc.get('source_file'):
            issues_found.append(f"Missing source_file in {doc.get('filename', 'unknown')}")
        
        # Check ECS elements structure
        ecs = doc.get('ecs_elements', {})
        if not isinstance(ecs, dict):
            issues_found.append(f"ECS elements not a dict in {doc.get('filename', 'unknown')}")
        else:
            for element_type in ['entities', 'components', 'systems']:
                if element_type not in ecs:
                    issues_found.append(f"Missing {element_type} in ECS for {doc.get('filename', 'unknown')}")
    
    # Check for missing required fields in keywords
    for kw in consolidated_data['all_keywords']:
        required_fields = ['term', 'frequency', 'relevance']
        for field in required_fields:
            if field not in kw:
                issues_found.append(f"Keyword missing {field} in {kw.get('source_file', 'unknown')}")
                break
    
    # Check for missing required fields in constraints
    for con in consolidated_data['all_constraints']:
        required_fields = ['id', 'title', 'description', 'constraint_type', 'severity']
        for field in required_fields:
            if field not in con:
                issues_found.append(f"Constraint missing {field} in {con.get('source_file', 'unknown')}")
                break
    
    print(f"Data integrity validation complete.")
    print(f"Issues found: {len(issues_found)}")
    
    if issues_found:
        print("Sample issues:")
        for issue in issues_found[:10]:  # Show first 10 issues
            print(f"  - {issue}")
    
    return issues_found


def create_master_index(consolidated_file_path):
    """
    Create a master index linking all processed elements to source documents.
    """
    print("\nCreating master index...")
    
    with open(consolidated_file_path, 'r', encoding='utf-8') as f:
        consolidated_data = json.load(f)
    
    # Create index structure
    master_index = {
        "metadata": {
            "index_creation_date": datetime.now().isoformat(),
            "description": "Master index linking all processed elements to source documents"
        },
        "by_document": {},
        "by_keyword": {},
        "by_entity": {},
        "by_component": {},
        "by_system": {},
        "by_constraint": {},
        "by_category": {},
        "by_business_domain": {}
    }
    
    # Index by document
    for doc in consolidated_data['documents']:
        filename = doc['filename']
        master_index['by_document'][filename] = {
            "keywords_count": len(doc.get('keywords', [])),
            "entities_count": len(doc.get('ecs_elements', {}).get('entities', [])),
            "components_count": len(doc.get('ecs_elements', {}).get('components', [])),
            "systems_count": len(doc.get('ecs_elements', {}).get('systems', [])),
            "constraints_count": len(doc.get('constraints', [])),
            "has_metadata": bool(doc.get('metadata'))
        }
    
    # Index by keyword
    for kw in consolidated_data['all_keywords']:
        term = kw['term']
        source_file = kw['source_file']
        
        if term not in master_index['by_keyword']:
            master_index['by_keyword'][term] = []
        
        master_index['by_keyword'][term].append(source_file)
    
    # Index by entity
    for entity in consolidated_data['all_entities']:
        entity_name = entity['name']
        source_file = entity['source_file']
        
        if entity_name not in master_index['by_entity']:
            master_index['by_entity'][entity_name] = []
        
        master_index['by_entity'][entity_name].append(source_file)
    
    # Index by component
    for comp in consolidated_data['all_components']:
        comp_name = comp['name']
        source_file = comp['source_file']
        
        if comp_name not in master_index['by_component']:
            master_index['by_component'][comp_name] = []
        
        master_index['by_component'][comp_name].append(source_file)
    
    # Index by system
    for sys in consolidated_data['all_systems']:
        sys_name = sys['name']
        source_file = sys['source_file']
        
        if sys_name not in master_index['by_system']:
            master_index['by_system'][sys_name] = []
        
        master_index['by_system'][sys_name].append(source_file)
    
    # Index by constraint
    for con in consolidated_data['all_constraints']:
        con_id = con['id']
        source_file = con['source_file']
        
        if con_id not in master_index['by_constraint']:
            master_index['by_constraint'][con_id] = []
        
        master_index['by_constraint'][con_id].append(source_file)
    
    # Index by category and business domain
    for meta in consolidated_data['all_metadata']:
        source_file = meta.get('source_file', 'unknown')
        
        # By category
        categories = meta.get('categories', [])
        for cat in categories:
            if cat not in master_index['by_category']:
                master_index['by_category'][cat] = []
            master_index['by_category'][cat].append(source_file)
        
        # By business domain
        domains = meta.get('business_domains', [])
        for dom in domains:
            if dom not in master_index['by_business_domain']:
                master_index['by_business_domain'][dom] = []
            master_index['by_business_domain'][dom].append(source_file)
    
    # Save the master index
    index_path = os.path.join("/common/active/sblo/Dev/FinCom/consolidated_data", "master_index.json")
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(master_index, f, ensure_ascii=False, indent=2)
    
    print(f"Master index created at {index_path}")
    print(f"Indexed {len(master_index['by_document'])} documents")
    print(f"Indexed {len(master_index['by_keyword'])} unique keywords")
    print(f"Indexed {len(master_index['by_entity'])} unique entities")
    print(f"Indexed {len(master_index['by_component'])} unique components")
    print(f"Indexed {len(master_index['by_system'])} unique systems")
    print(f"Indexed {len(master_index['by_constraint'])} unique constraints")
    
    return index_path


def establish_data_quality_metrics(consolidated_file_path):
    """
    Establish data quality metrics and identify any gaps in processing.
    """
    print("\nEstablishing data quality metrics...")
    
    with open(consolidated_file_path, 'r', encoding='utf-8') as f:
        consolidated_data = json.load(f)
    
    # Calculate metrics
    total_docs = len(consolidated_data['documents'])
    total_keywords = len(consolidated_data['all_keywords'])
    total_entities = len(consolidated_data['all_entities'])
    total_components = len(consolidated_data['all_components'])
    total_systems = len(consolidated_data['all_systems'])
    total_constraints = len(consolidated_data['all_constraints'])
    
    # Calculate averages
    avg_keywords_per_doc = total_keywords / total_docs if total_docs > 0 else 0
    avg_entities_per_doc = total_entities / total_docs if total_docs > 0 else 0
    avg_components_per_doc = total_components / total_docs if total_docs > 0 else 0
    avg_systems_per_doc = total_systems / total_docs if total_docs > 0 else 0
    avg_constraints_per_doc = total_constraints / total_docs if total_docs > 0 else 0
    
    # Identify gaps - documents with no keywords, ECS elements, or constraints
    gaps = {
        "no_keywords": [],
        "no_entities": [],
        "no_components": [],
        "no_systems": [],
        "no_constraints": [],
        "no_metadata": []
    }
    
    for doc in consolidated_data['documents']:
        filename = doc['filename']
        
        if len(doc.get('keywords', [])) == 0:
            gaps['no_keywords'].append(filename)
        
        ecs = doc.get('ecs_elements', {})
        if len(ecs.get('entities', [])) == 0:
            gaps['no_entities'].append(filename)
        
        if len(ecs.get('components', [])) == 0:
            gaps['no_components'].append(filename)
        
        if len(ecs.get('systems', [])) == 0:
            gaps['no_systems'].append(filename)
        
        if len(doc.get('constraints', [])) == 0:
            gaps['no_constraints'].append(filename)
        
        if not doc.get('metadata'):
            gaps['no_metadata'].append(filename)
    
    # Create quality report
    quality_report = {
        "metrics": {
            "total_documents": total_docs,
            "total_keywords": total_keywords,
            "total_entities": total_entities,
            "total_components": total_components,
            "total_systems": total_systems,
            "total_constraints": total_constraints,
            "avg_keywords_per_doc": avg_keywords_per_doc,
            "avg_entities_per_doc": avg_entities_per_doc,
            "avg_components_per_doc": avg_components_per_doc,
            "avg_systems_per_doc": avg_systems_per_doc,
            "avg_constraints_per_doc": avg_constraints_per_doc
        },
        "gaps": gaps,
        "quality_score": 0.0,
        "report_date": datetime.now().isoformat()
    }
    
    # Calculate a simple quality score based on completeness
    total_possible_elements = total_docs * 5  # keywords, entities, components, systems, constraints
    total_actual_elements = (
        len([d for d in consolidated_data['documents'] if len(d.get('keywords', [])) > 0]) +
        len([d for d in consolidated_data['documents'] if len(d.get('ecs_elements', {}).get('entities', [])) > 0]) +
        len([d for d in consolidated_data['documents'] if len(d.get('ecs_elements', {}).get('components', [])) > 0]) +
        len([d for d in consolidated_data['documents'] if len(d.get('ecs_elements', {}).get('systems', [])) > 0]) +
        len([d for d in consolidated_data['documents'] if len(d.get('constraints', [])) > 0])
    )
    
    quality_score = (total_actual_elements / total_possible_elements) * 100 if total_possible_elements > 0 else 0
    quality_report['quality_score'] = round(quality_score, 2)
    
    # Save the quality report
    report_path = os.path.join("/common/active/sblo/Dev/FinCom/consolidated_data", "data_quality_report.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(quality_report, f, ensure_ascii=False, indent=2)
    
    print(f"Data quality report created at {report_path}")
    print(f"Quality score: {quality_score:.2f}%")
    print(f"Gaps identified in {len(gaps['no_keywords'])} documents with no keywords")
    print(f"Gaps identified in {len(gaps['no_entities'])} documents with no entities")
    print(f"Gaps identified in {len(gaps['no_components'])} documents with no components")
    print(f"Gaps identified in {len(gaps['no_systems'])} documents with no systems")
    print(f"Gaps identified in {len(gaps['no_constraints'])} documents with no constraints")
    
    return report_path


if __name__ == "__main__":
    print("Starting Phase 1: Data Integration and Validation")
    print("="*60)
    
    # Task 1: Consolidate all processed JSON files
    print("Task 1: Consolidating all 471 processed JSON files into a unified data structure")
    consolidated_file_path = consolidate_processed_files()
    print("✓ Completed: Consolidation of processed files\n")
    
    # Task 2: Validate data integrity
    print("Task 2: Validating data integrity across all processed files")
    issues = validate_data_integrity(consolidated_file_path)
    print("✓ Completed: Data integrity validation\n")
    
    # Task 3: Create master index
    print("Task 3: Creating master index linking all processed elements to source documents")
    index_path = create_master_index(consolidated_file_path)
    print("✓ Completed: Master index creation\n")
    
    # Task 4: Establish data quality metrics
    print("Task 4: Establishing data quality metrics and identifying gaps in processing")
    quality_report_path = establish_data_quality_metrics(consolidated_file_path)
    print("✓ Completed: Data quality metrics established\n")
    
    print("Phase 1: Data Integration and Validation - COMPLETE")
    print("="*60)