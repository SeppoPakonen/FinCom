#!/usr/bin/env python3
"""
Script to generate individual task files for each documentation file
that needs to be manually processed.
"""

import os
from pathlib import Path

def generate_task_files():
    # Get all documentation files
    docs_dir = Path("/common/active/sblo/Dev/FinCom/docs")
    doc_files = list(docs_dir.rglob("*.md"))
    
    # Filter out the already processed files
    already_processed = [
        "company_formation_example.md",
        "company_finance_example.md"
    ]
    
    task_dir = Path("/common/active/sblo/Dev/FinCom/plan/manual_processing/tasks")
    
    count = 0
    for doc_file in doc_files:
        # Get just the filename
        filename = doc_file.name
        
        # Skip already processed files
        if filename in already_processed:
            continue
            
        # Create a safe filename for the task file
        safe_name = filename.replace(" ", "_").replace(".", "_").replace("-", "_")
        task_file_path = task_dir / f"task_process_{safe_name}.md"
        
        # Get the relative path from the docs directory
        relative_path = doc_file.relative_to(docs_dir)
        
        # Create task content
        content = f"""# Task: Process Documentation File

## File Information
- **File**: `{relative_path}`
- **Source Directory**: `{docs_dir}`
- **Status**: Pending

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
- This file is part of the Finnish Business Operations Repository
- All processing should maintain Finnish business context while using English for system elements
- Follow the same pattern as previously processed files
"""
        
        # Write the task file
        with open(task_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        count += 1
        print(f"Created task file: {task_file_path.name}")
    
    print(f"\nTotal task files created: {count}")
    print(f"Already processed files skipped: {len(already_processed)}")

if __name__ == "__main__":
    generate_task_files()