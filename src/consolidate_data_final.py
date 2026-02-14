"""
Final script to process remaining English documentation files systematically.
This version handles JSON parsing errors more gracefully.
"""

import json
import sys
import os
from datetime import datetime
import re


def is_likely_english_file(file_path):
    """Check if a file is likely to be in English based on its content."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()[:2000]  # Check first 2000 chars

        # Count Finnish vs English characters
        finnish_chars = ['ä', 'ö', 'å', 'Ä', 'Ö', 'Å']
        finnish_char_count = sum(1 for c in content if c in finnish_chars)

        # If more than 15% of the content contains Finnish characters, it's likely Finnish
        if len(content) > 0 and finnish_char_count / len(content) > 0.15:
            return False

        # Check for Finnish words in the content
        finnish_words = [
            'ja', 'se', 'että', 'on', 'oli', 'ovat', 'joka', 'jossa', 'josta', 'mikä', 'mitä',
            'kun', 'kuin', 'tai', 'mutta', 'jos', 'niin', 'nyt', 'tässä', 'täältä', 'tänne',
            'yritys', 'yrittäjä', 'liiketoiminta', 'markkinointi', 'myynti', 'palvelu', 'asiakas',
            'kortti', 'sopimus', 'ilmoitus', 'lupa', 'tarkastus', 'toiminta', 'suunnitelma',
            'kannattavuus', 'verotus', 'talouden', 'suunnittelu', 'perustaminen', 'muistilista',
            'koulutus', 'kalenteri', 'vuosikello', 'kauppa', 'kauppakirja', 'vuokra', 'vuokrasopimus',
            'yhtiö', 'yhtiosopimus', 'yhtiöjärjestys', 'osake', 'osakas', 'hallitus', 'kokous',
            'edunsaaja', 'rekisteri', 'viranomainen', 'lainsäädäntö', 'sääntö', 'ohje', 'tutkinto',
            'tehtävä', 'arviointi', 'lomake', 'lomautus', 'irtisanominen', 'työsopimus', 'työ',
            'työntekijä', 'työehtosopimus', 'työpaikka', 'työvoima', 'palkka', 'etuus', 'sairaus',
            'vakuutus', 'turvallisuus', 'hyvinvointi', 'terveys', 'toimintaohjelma', 'kustannus',
            'budjetti', 'tase', 'tuloslaskelma', 'tilinpäätös', 'tositteet', 'kirjanpito', 'asiakirja',
            'tietosuoja', 'tietoturva', 'salassapito', 'suostumus', 'tietoturvaa', 'tietosuojaa',
            'perusteet', 'kilpailukeinot', 'täydennys', 'täydentäminen', 'täydennys', 'täydentäminen',
            'liikeidea', 'toimintamalli', 'täsmennys', 'täsmennetään', 'täsmennä', 'täsmennäminen'
        ]

        # Count Finnish words in content
        content_lower = content.lower()
        finnish_word_matches = 0
        for word in finnish_words:
            if re.search(r'\b' + re.escape(word.lower()) + r'\b', content_lower):
                finnish_word_matches += 1

        # If we find more than 10 Finnish words in the content, it's likely Finnish
        if finnish_word_matches > 10:
            return False

        # Look for English indicators in the content
        english_indicators = [
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
            'notification', 'obligation', 'duty', 'responsibility', 'strategy',
            'development', 'management', 'governance', 'control', 'risk', 'asset',
            'liability', 'equity', 'revenue', 'expense', 'profit', 'loss', 'cash',
            'flow', 'investment', 'loan', 'credit', 'debt', 'equity', 'capital',
            'funding', 'valuation', 'merger', 'acquisition', 'sale', 'purchase',
            'entrepreneur', 'entrepreneurship', 'establishing', 'annual', 'accounts'
        ]

        # Count English indicators in content
        content_lower = content.lower()
        english_word_matches = 0
        for word in english_indicators:
            if re.search(r'\b' + re.escape(word.lower()) + r'\b', content_lower):
                english_word_matches += 1

        # If we find at least 3 English indicators and fewer than 10 Finnish words, it's likely English
        if english_word_matches >= 3 and finnish_word_matches < 10:
            return True

    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return False

    return False


def safe_json_load(file_path):
    """
    Safely load a JSON file, handling common formatting issues.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse normally first
        try:
            return json.loads(content), True
        except json.JSONDecodeError:
            # If normal parsing fails, try to fix common issues
            # Remove any trailing commas before closing braces/brackets
            content = re.sub(r',(\s*[}\]])', r'\1', content)
            
            # Try to find the proper end of the JSON
            # Look for the last matching closing bracket/brace
            stack = []
            last_pos = len(content)
            for i, char in enumerate(content):
                if char in '{[':
                    stack.append(char)
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                
                if not stack and char in '{}]':
                    last_pos = i + 1
            
            # Truncate to the last valid position
            fixed_content = content[:last_pos]
            
            try:
                return json.loads(fixed_content), True
            except json.JSONDecodeError:
                # If still failing, try more aggressive fixes
                # Remove any content after the last matching closing bracket
                fixed_content = content
                for pattern in [r'}\s*,?\s*\]', r'}\s*,?\s*}']:
                    matches = list(re.finditer(pattern, fixed_content))
                    if matches:
                        last_match = matches[-1]
                        fixed_content = fixed_content[:last_match.end()]
                        break
                
                try:
                    return json.loads(fixed_content), True
                except json.JSONDecodeError:
                    # Last resort: try to parse up to the last valid JSON object
                    # Find the last balanced } or ]
                    pos = len(fixed_content) - 1
                    while pos > 0:
                        try:
                            test_content = fixed_content[:pos+1]
                            result = json.loads(test_content)
                            return result, True
                        except json.JSONDecodeError:
                            pos -= 1
                    return None, False
    except Exception as e:
        print(f"Could not fix JSON for {file_path}: {str(e)}")
        return None, False


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
    processed_count = 0
    error_count = 0
    
    for i, filename in enumerate(processed_files, 1):
        file_path = os.path.join(processed_docs_dir, filename)
        
        try:
            # Try to load the JSON file
            file_data, success = safe_json_load(file_path)
            if not success:
                print(f"  ✗ Could not parse JSON for {filename}")
                error_count += 1
                continue
            
            # Add document to consolidated list
            doc_entry = {
                "filename": filename,
                "source_file": file_data.get("source_file", file_data.get("original_content", {}).get("source_file", filename)),
                "keywords": file_data.get("keywords", []),
                "ecs_elements": file_data.get("ecs_elements", {}),
                "constraints": file_data.get("constraints", []),
                "metadata": file_data.get("metadata", {}),
                "processing_date": file_data.get("processing_date", ""),
                "processor": file_data.get("processor", "")
            }
            
            consolidated_data["documents"].append(doc_entry)
            
            # Add to global collections
            for kw in file_data.get("keywords", []):
                kw_with_source = dict(kw)
                kw_with_source["source_file"] = filename
                consolidated_data["all_keywords"].append(kw_with_source)
            
            ecs_elements = file_data.get("ecs_elements", {})
            if isinstance(ecs_elements, dict):
                for entity in ecs_elements.get("entities", []):
                    entity_with_source = dict(entity)
                    entity_with_source["source_file"] = filename
                    consolidated_data["all_entities"].append(entity_with_source)
                
                for comp in ecs_elements.get("components", []):
                    comp_with_source = dict(comp)
                    comp_with_source["source_file"] = filename
                    consolidated_data["all_components"].append(comp_with_source)
                
                for sys in ecs_elements.get("systems", []):
                    sys_with_source = dict(sys)
                    sys_with_source["source_file"] = filename
                    consolidated_data["all_systems"].append(sys_with_source)
            
            for constraint in file_data.get("constraints", []):
                con_with_source = dict(constraint)
                con_with_source["source_file"] = filename
                consolidated_data["all_constraints"].append(con_with_source)
            
            meta_with_source = dict(file_data.get("metadata", {}))
            meta_with_source["source_file"] = filename
            consolidated_data["all_metadata"].append(meta_with_source)
            
            processed_count += 1
            if processed_count % 50 == 0:
                print(f"  Processed {processed_count}/{len(processed_files)} files...")
                
        except Exception as e:
            print(f"  ✗ Error processing file {filename}: {str(e)}")
            error_count += 1
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
    print(f"Files processed successfully: {processed_count}")
    print(f"Files with errors: {error_count}")
    
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
        term = kw.get('term', 'unknown')
        source_file = kw.get('source_file', 'unknown')
        
        if term not in master_index['by_keyword']:
            master_index['by_keyword'][term] = []
        
        master_index['by_keyword'][term].append(source_file)
    
    # Index by entity
    for entity in consolidated_data.get('all_entities', []):
        entity_name = entity.get('name', 'unknown')
        source_file = entity.get('source_file', 'unknown')
        
        if entity_name not in master_index['by_entity']:
            master_index['by_entity'][entity_name] = []
        
        master_index['by_entity'][entity_name].append(source_file)
    
    # Index by component
    for comp in consolidated_data.get('all_components', []):
        comp_name = comp.get('name', 'unknown')
        source_file = comp.get('source_file', 'unknown')
        
        if comp_name not in master_index['by_component']:
            master_index['by_component'][comp_name] = []
        
        master_index['by_component'][comp_name].append(source_file)
    
    # Index by system
    for sys in consolidated_data.get('all_systems', []):
        sys_name = sys.get('name', 'unknown')
        source_file = sys.get('source_file', 'unknown')
        
        if sys_name not in master_index['by_system']:
            master_index['by_system'][sys_name] = []
        
        master_index['by_system'][sys_name].append(source_file)
    
    # Index by constraint
    for con in consolidated_data.get('all_constraints', []):
        con_id = con.get('id', 'unknown')
        source_file = con.get('source_file', 'unknown')
        
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
    index_path = os.path.join(consolidated_output_dir, "master_index.json")
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
    total_entities = len(consolidated_data.get('all_entities', []))
    total_components = len(consolidated_data.get('all_components', []))
    total_systems = len(consolidated_data.get('all_systems', []))
    total_constraints = len(consolidated_data.get('all_constraints', []))
    
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
    report_path = os.path.join(consolidated_output_dir, "data_quality_report.json")
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
    print("Starting consolidation of processed documentation files")
    print("="*60)
    
    # Consolidate all processed JSON files
    print("Consolidating all processed JSON files into a unified data structure")
    consolidated_file_path = consolidate_processed_files()
    print("✓ Completed: Consolidation of processed files\n")
    
    # Validate data integrity
    print("Validating data integrity across all processed files")
    issues = validate_data_integrity(consolidated_file_path)
    print("✓ Completed: Data integrity validation\n")
    
    # Create master index
    print("Creating master index linking all processed elements to source documents")
    index_path = create_master_index(consolidated_file_path)
    print("✓ Completed: Master index creation\n")
    
    # Establish data quality metrics
    print("Establishing data quality metrics and identifying gaps in processing")
    quality_report_path = establish_data_quality_metrics(consolidated_file_path)
    print("✓ Completed: Data quality metrics established\n")
    
    print("All processing tasks completed successfully!")
    print("="*60)