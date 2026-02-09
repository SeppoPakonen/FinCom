"""
Script to generate individual task files for each English documentation file from db_eng.
This creates a task tracking system for all English files that need processing.
"""

import os
from pathlib import Path

def generate_task_files_for_db_eng():
    # Get all English documentation files from the original db_eng directory
    source_dir = Path("/common/active/sblo/Dev/Manager/DummyMusicCompany/db_eng")
    doc_files = list(source_dir.rglob("*.md"))
    
    # Create task directory if it doesn't exist
    task_dir = Path("/common/active/sblo/Dev/FinCom/plan/manual_processing/tasks")
    task_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Found {len(doc_files)} English documentation files in db_eng to create tasks for")

    for i, doc_file in enumerate(doc_files, 1):
        # Get just the filename
        filename = doc_file.name
        
        # Create a safe filename for the task file
        safe_name = filename.replace(" ", "_").replace(".", "_").replace("-", "_").replace("(", "_").replace(")", "_")
        task_file_path = task_dir / f"task_process_{safe_name}.md"
        
        # Get the relative path from the source directory
        relative_path = doc_file.relative_to(source_dir)
        
        # Create task content
        content = f"""# Task: Process Documentation File

## File Information
- **File**: `{filename}`
- **Source Directory**: `/common/active/sblo/Dev/Manager/DummyMusicCompany/db_eng/`
- **Relative Path**: `{relative_path}`
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
- This file is part of the Finnish Business Operations Repository (English version)
- All processing should maintain Finnish business context while using English for system elements
- Follow the same pattern as previously processed files
- Ensure ECS elements properly represent the business concepts in the document

## Next Steps
1. Read and understand the content of `{filename}`
2. Extract relevant keywords with frequencies and relevance scores
3. Identify entities, components, and systems in the document
4. Extract any constraints or requirements mentioned
5. Add appropriate metadata for search optimization
6. Save processed data to JSON format
7. Update this task file to COMPLETED status
"""
        
        # Write the task file
        with open(task_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        if i % 50 == 0:
            print(f"  Created {i} task files so far...")
    
    print(f"\nTotal task files created: {len(doc_files)}")
    print(f"All task files are in: {task_dir}")
    
    # Create a master tracker
    master_tracker_path = Path("/common/active/sblo/Dev/FinCom/plan/manual_processing/master_tracker.md")
    with open(master_tracker_path, 'w', encoding='utf-8') as f:
        f.write(f"""# Master Tracker for Manual Documentation Processing

## Overview
This file tracks the progress of manually processing all English documentation files from the db_eng directory in the Finnish Business Operations Repository. Each file needs to be processed to add keywords, ECS elements, constraints, and search-engine metadata.

## Total Files to Process
- **Total Documentation Files**: {len(doc_files)}
- **Already Processed**: 0
- **Remaining to Process**: {len(doc_files)}
- **Completion Rate**: 0.0%

## Processing Status
- **Not Started**: {len(doc_files)} files
- **In Progress**: 0 files
- **Completed**: 0 files

## Progress Tracking
Each file has a corresponding task file in `/plan/manual_processing/tasks/` directory that tracks its individual processing status.

## Next Steps
1. Process remaining {len(doc_files)} documentation files systematically
2. Update individual task files as each file is processed
3. Update this master tracker periodically
4. Generate processed data files in `processed_docs/` directory
5. Ensure all data structures are properly validated

## Quality Assurance
- All processed files must have keywords, ECS elements, constraints, and metadata
- Cross-verification between related documents
- Validation of all data structures
- Proper relationship mapping between elements
""")
    
    print(f"Master tracker updated at: {master_tracker_path}")


if __name__ == "__main__":
    generate_task_files_for_db_eng()