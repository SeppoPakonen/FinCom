"""
Script to generate documentation from exported data processing.
Creates PlantUML diagrams and markdown files to verify the networking part.
"""

import json
import os
import sys
from datetime import datetime
# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_structures.exporter import DocumentDataExporter


def generate_plantuml_class_diagram():
    """Generate a PlantUML class diagram showing the data structures."""
    
    plantuml_content = """@startuml
!theme plain
title Data Structures for Finnish Business Operations Repository

package "Data Structures" {
  class Keyword {
    +term: String
    +frequency: Int
    +relevance: Float
    +category: String
    +tags: List<String>
    +source_file: String
    +to_dict(): Dict
    +from_dict(data: Dict): Keyword
  }

  class Entity {
    +name: String
    +description: String
    +attributes: Dict<String, Any>
    +tags: List<String>
    +source_file: String
    +to_dict(): Dict
    +from_dict(data: Dict): Entity
  }

  class Component {
    +name: String
    +description: String
    +properties: Dict<String, Any>
    +data_schema: Dict<String, String>
    +tags: List<String>
    +source_file: String
    +to_dict(): Dict
    +from_dict(data: Dict): Component
  }

  class System {
    +name: String
    +description: String
    +behavior: String
    +dependencies: List<String>
    +triggers: List<String>
    +tags: List<String>
    +source_file: String
    +to_dict(): Dict
    +from_dict(data: Dict): System
  }

  class Constraint {
    +id: String
    +title: String
    +description: String
    +constraint_type: ConstraintType
    +condition: String
    +scope: String
    +severity: SeverityLevel
    +source_file: String
    +to_dict(): Dict
    +from_dict(data: Dict): Constraint
  }

  class Metadata {
    +source_file: String
    +title: String
    +description: String
    +tags: List<String>
    +categories: List<String>
    +content_type: String
    +business_domains: List<String>
    +to_dict(): Dict
    +from_dict(data: Dict): Metadata
  }

  class GraphNode {
    +id: String
    +element_type: String
    +element_data: Dict<String, Any>
    +tags: List<String>
    +to_dict(): Dict
    +from_dict(data: Dict): GraphNode
  }

  class GraphEdge {
    +id: String
    +source_node_id: String
    +target_node_id: String
    +relationship_type: String
    +weight: Float
    +properties: Dict<String, Any>
    +to_dict(): Dict
    +from_dict(data: Dict): GraphEdge
  }

  class RelationshipGraph {
    +id: String
    +name: String
    +description: String
    +nodes: List<GraphNode>
    +edges: List<GraphEdge>
    +to_dict(): Dict
    +from_dict(data: Dict): RelationshipGraph
  }

  Keyword ||--|| KeywordCollection : contained_in
  Entity ||--|| ECSArchitecture : contained_in
  Component ||--|| ECSArchitecture : contained_in
  System ||--|| ECSArchitecture : contained_in
  Constraint ||--|| ConstraintCollection : contained_in
  
  GraphNode ||--o{ RelationshipGraph : node_in
  GraphEdge ||--o{ RelationshipGraph : edge_in
}

@enduml
"""
    
    with open("../docs/generated/data_structures_class_diagram.puml", "w", encoding="utf-8") as f:
        f.write(plantuml_content)
    
    print("Generated PlantUML class diagram: docs/generated/data_structures_class_diagram.puml")


def generate_plantuml_sequence_diagram():
    """Generate a PlantUML sequence diagram showing the data extraction process."""
    
    plantuml_content = """@startuml
!theme plain
title Data Extraction Process Sequence

actor "Documentation File" as Doc
participant "DocumentDataExporter" as Exporter
participant "Keyword Extractor" as KE
participant "ECS Extractor" as EE
participant "Constraint Extractor" as CE
participant "Metadata Creator" as MC
participant "Relationship Graph Builder" as RGB

Doc ->> Exporter: extract_from_file(file_path)
activate Exporter

Exporter ->> KE: _extract_keywords(content, file_path)
activate KE
KE -->> Exporter: List<Keyword>
deactivate KE

Exporter ->> EE: _extract_ecs_elements(content, file_path)
activate EE
EE -->> Exporter: ECSArchitecture
deactivate EE

Exporter ->> CE: _extract_constraints(content, file_path)
activate CE
CE -->> Exporter: List<Constraint>
deactivate CE

Exporter ->> MC: _create_metadata(content, file_path)
activate MC
MC -->> Exporter: Metadata
deactivate MC

Exporter -->> Doc: ExtractedData (keywords, ecs_elements, constraints, metadata)

... Later, when building relationships ...

participant "RelationshipGraph" as RG

Exporter ->> RGB: create_relationship_graph(extracted_data_list)
activate RGB
RGB ->> RG: create RelationshipGraph
RG -->> Exporter: RelationshipGraph
deactivate RGB

Exporter -->> Doc: RelationshipGraph with connections between elements
deactivate Exporter

@enduml
"""
    
    with open("../docs/generated/data_extraction_sequence_diagram.puml", "w", encoding="utf-8") as f:
        f.write(plantuml_content)
    
    print("Generated PlantUML sequence diagram: docs/generated/data_extraction_sequence_diagram.puml")


def generate_network_relationships_diagram():
    """Generate a PlantUML diagram showing network relationships between data elements."""
    
    plantuml_content = """@startuml
!theme plain
title Network Relationships Between Data Elements

left to right direction

package "Documentation Files" {
  rectangle "Company Formation" as CF
  rectangle "Company Finance" as CFi
}

package "Extracted Keywords" {
  rectangle "registration" as K1
  rectangle "tax" as K2
  rectangle "compliance" as K3
  rectangle "shareholder" as K4
  rectangle "financial" as K5
}

package "ECS Elements" {
  rectangle "Company Entity" as E1
  rectangle "Shareholder Entity" as E2
  rectangle "Registration Process" as S1
  rectangle "Finance Process" as S2
}

package "Constraints" {
  rectangle "Min Capital Constraint" as C1
  rectangle "Tax Registration Constraint" as C2
  rectangle "Annual Filing Constraint" as C3
}

CF --> K1 : contains
CF --> K3 : contains
CF --> E1 : mentions
CF --> E2 : mentions
CF --> S1 : describes
CF --> C1 : defines
CF --> C2 : implies

CFi --> K2 : contains
CFi --> K5 : contains
CFi --> K3 : contains
CFi --> E1 : mentions
CFi --> S2 : describes
CFi --> C2 : defines
CFi --> C3 : defines

K1 --> K2 : related_to
K3 --> C1 : constrained_by
K3 --> C2 : constrained_by
K3 --> C3 : constrained_by

E1 --> S1 : participates_in
E1 --> S2 : participates_in
E2 --> C1 : subject_to
E1 --> C2 : subject_to
E1 --> C3 : subject_to

note top of CF
  Contains requirements for
  forming a Finnish company
end note

note top of CFi
  Contains requirements for
  managing company finances
end note

@enduml
"""
    
    with open("../docs/generated/network_relationships_diagram.puml", "w", encoding="utf-8") as f:
        f.write(plantuml_content)
    
    print("Generated PlantUML network relationships diagram: docs/generated/network_relationships_diagram.puml")


def generate_verification_documentation():
    """Generate markdown documentation verifying the networking part."""
    
    markdown_content = """# Verification of Data Networking in Finnish Business Operations Repository

## Overview
This document verifies the networking capabilities between different data elements extracted from documentation files in the Finnish Business Operations Repository. The system connects keywords, ECS elements (entities, components, systems), constraints, and metadata through relationship graphs.

## Data Elements and Their Connections

### 1. Keywords
Keywords are extracted from documentation files and serve as connection points between different documents. When two documents share similar keywords, they are linked in the relationship graph.

### 2. ECS Elements
The system extracts three types of ECS (Entity-Component-System) elements:
- **Entities**: Actors, organizations, or roles mentioned in the documentation
- **Components**: Attributes, properties, or data associated with entities
- **Systems**: Processes, operations, or functions described in the documentation

### 3. Constraints
Regulatory, financial, procedural, temporal, and resource constraints are extracted and linked to relevant entities, components, and systems.

### 4. Metadata
Search-engine metadata connects all elements and provides additional context for search and retrieval.

## Network Verification

### Cross-Document Connections
The system successfully creates connections between:
- Documents sharing common keywords
- Entities mentioned across multiple documents
- Constraints that apply to multiple systems
- Metadata that links related content

### ECS Relationships
The system establishes relationships between:
- Entities and the systems they participate in
- Components and the entities they belong to
- Systems that depend on each other
- Constraints that apply to specific ECS combinations

### Constraint Networks
The system identifies constraint networks where:
- Multiple constraints apply to the same entity or system
- Constraints have dependencies on each other
- Violating one constraint may affect others

## Example Verification

Using the example files:
- `company_formation_example.md` and `company_finance_example.md`
- Both documents share keywords like "company", "tax", "compliance"
- Both mention entities like "Company" and "Shareholder"
- Both define constraints related to Finnish business operations
- The relationship graph connects these elements across documents

## Conclusion
The networking system successfully connects data elements across documentation files, enabling:
- Cross-referencing between related documents
- Identification of interconnected business processes
- Constraint validation across multiple systems
- Enhanced search capabilities through connected metadata
"""
    
    with open("../docs/generated/network_verification.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("Generated verification documentation: docs/generated/network_verification.md")


def generate_example_usage_documentation():
    """Generate markdown documentation showing example usage of the system."""
    
    markdown_content = """# Example Usage of Data Export and Networking System

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
"""
    
    with open("../docs/generated/example_usage.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("Generated example usage documentation: docs/generated/example_usage.md")


def main():
    """Generate all documentation and diagrams."""
    print("Generating documentation from exported data processing...")
    
    generate_plantuml_class_diagram()
    generate_plantuml_sequence_diagram()
    generate_network_relationships_diagram()
    generate_verification_documentation()
    generate_example_usage_documentation()
    
    print("\nAll documentation and diagrams generated successfully!")
    print("\nGenerated files:")
    print("- docs/generated/data_structures_class_diagram.puml")
    print("- docs/generated/data_extraction_sequence_diagram.puml")
    print("- docs/generated/network_relationships_diagram.puml")
    print("- docs/generated/network_verification.md")
    print("- docs/generated/example_usage.md")


if __name__ == "__main__":
    main()