# Example Usage of Data Export and Networking System

## Overview
This document demonstrates how to use the data export and networking system in the Finnish Business Operations Repository.

## Data Extraction Process

### 1. Single File Extraction
```python
from src.data_structures.exporter import DocumentDataExporter

# Initialize the exporter
exporter = DocumentDataExporter()

# Extract data from a documentation file
file_path = "docs/business_forms/company_formation_example.md"
extracted_data = exporter.extract_from_file(file_path)

# The extracted_data contains:
# - keywords: List of important terms from the document
# - ecs_elements: Entities, Components, and Systems identified
# - constraints: Regulatory and procedural constraints
# - metadata: Information for search engine optimization
```

### 2. Multiple File Processing
```python
# Process multiple files and create a relationship graph
extracted_data_list = []
for file_path in ["file1.md", "file2.md", "file3.md"]:
    data = exporter.extract_from_file(file_path)
    extracted_data_list.append(data)

# Create a relationship graph connecting all elements
graph = exporter.create_relationship_graph(extracted_data_list)
```

## Data Structure Examples

### Keyword Example
```json
{
  "term": "company",
  "frequency": 5,
  "relevance": 0.8,
  "category": "business_term",
  "tags": ["automated_extraction"],
  "source_file": "docs/business_forms/company_formation_example.md"
}
```

### Entity Example
```json
{
  "name": "Shareholder",
  "description": "An owner of company shares",
  "attributes": {
    "voting_rights": "proportional to shares held",
    "liability": "limited to investment"
  },
  "tags": ["automated_extraction"],
  "source_file": "docs/business_forms/company_formation_example.md"
}
```

### Constraint Example
```json
{
  "id": "company_formation_min_capital",
  "title": "Minimum Share Capital Requirement",
  "description": "Finnish Oy companies must have minimum €2,500 share capital",
  "constraint_type": "financial",
  "condition": "share_capital >= 2500",
  "scope": "company_registration",
  "severity": "critical",
  "source_file": "docs/business_forms/company_formation_example.md"
}
```

## Relationship Graph Structure

The relationship graph connects different data elements across files:

- **Nodes**: Represent individual data elements (keywords, entities, constraints, etc.)
- **Edges**: Represent relationships between elements
- **Relationship Types**: Include dependency, reference, similarity, causation, etc.

## Networking Capabilities

### 1. Cross-Document Linking
Documents with shared keywords or entities are automatically linked, enabling:
- Discovery of related procedures
- Identification of interconnected processes
- Comprehensive constraint checking

### 2. ECS Integration
Entities, Components, and Systems are connected to show:
- Which entities participate in which systems
- How components relate to entities
- Dependencies between different systems

### 3. Constraint Networks
Related constraints are linked to enable:
- Validation of constraint combinations
- Identification of conflicting requirements
- Comprehensive compliance checking

## Verification

The system includes verification capabilities to ensure:
- All extracted elements are properly connected
- Relationships are meaningful and accurate
- Constraint networks are consistent
- Cross-document links are relevant
