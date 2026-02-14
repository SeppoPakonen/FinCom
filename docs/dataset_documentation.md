# Dataset Documentation: Finnish Business Operations Repository

## Overview

This documentation provides a comprehensive overview of the Finnish Business Operations Repository dataset, which contains English documentation files with processed business information including keywords, ECS elements, constraints, and metadata.

## Table of Contents

1. [Dataset Structure](#dataset-structure)
2. [Data Models](#data-models)
3. [Relationships](#relationships)
4. [Processing Pipeline](#processing-pipeline)
5. [Business Context](#business-context)
6. [Usage Guidelines](#usage-guidelines)

## Dataset Structure

The dataset consists of processed documentation files that contain structured business information. Each document has been enhanced with:

- Keywords with relevance scores and categories
- ECS elements (Entities, Components, Systems)
- Constraints with types and severity levels
- Comprehensive metadata for search optimization

```plantuml
@startuml
package "Finnish Business Operations Repository" {
  folder "docs" as docs {
    note bottom : Contains original documentation files
  }
  
  folder "processed_docs" as proc {
    note bottom : Contains processed JSON files with enhanced data
  }
  
  folder "plan" as plan {
    folder "manual_processing" as mp {
      folder "tasks" as tasks {
        note bottom : Individual processing task files
      }
      file "master_tracker.md" as tracker {
        note bottom : Tracks overall processing progress
      }
    }
  }
  
  folder "src" as src {
    note bottom : Source code for processing scripts
  }
  
  docs --> proc : "processed to"
  tasks --> proc : "tracks processing of"
  tracker --> proc : "monitors progress of"
  src --> proc : "generates"
}
@enduml
```

## Data Models

The dataset uses several core data models to structure business information:

### Keyword Model

Keywords are extracted business terms with relevance scores and categories.

```plantuml
@startuml
class Keyword {
  - term: String
  - frequency: Integer
  - relevance: Float
  - category: String
  - tags: List<String>
  - source_file: String
  - position_in_text: Integer
  - related_keywords: List<String>
  
  + to_dict(): Dict
  + calculate_relevance(): Float
}

class KeywordCollection {
  - source_file: String
  - keywords: List<Keyword>
  - total_word_count: Integer
  - extraction_date: String
  
  + add_keyword(keyword: Keyword): void
  + get_by_category(category: String): List<Keyword>
  + get_top_relevant(count: Integer): List<Keyword>
}
@enduml
```

### ECS Architecture Model

The ECS (Entity-Component-System) model represents business architecture elements.

```plantuml
@startuml
class Entity {
  - name: String
  - description: String
  - attributes: Dict
  - tags: List<String>
  - source_file: String
  - relationships: Dict
  
  + add_attribute(key: String, value: Any): void
  + get_attribute(key: String): Any
}

class Component {
  - name: String
  - description: String
  - properties: Dict
  - data_schema: Dict
  - tags: List<String>
  - source_file: String
  
  + update_property(key: String, value: Any): void
  + validate_data(data: Any): Boolean
}

class System {
  - name: String
  - description: String
  - behavior: String
  - dependencies: List<String>
  - triggers: List<String>
  - tags: List<String>
  - source_file: String
  
  + execute(): void
  + add_dependency(dep: String): void
}

class ECSArchitecture {
  - source_file: String
  - entities: List<Entity>
  - components: List<Component>
  - systems: List<System>
  - extraction_date: String
  
  + add_entity(entity: Entity): void
  + add_component(component: Component): void
  + add_system(system: System): void
  + get_relationships(): Dict
}
@enduml
```

### Constraint Model

Constraints represent regulatory, financial, procedural, and other business limitations.

```plantuml
@startuml
class Constraint {
  - id: String
  - title: String
  - description: String
  - constraint_type: ConstraintType
  - condition: String
  - scope: String
  - severity: SeverityLevel
  - source_file: String
  - tags: List<String>
  - related_constraints: List<String>
  - validation_logic: String
  - error_message: String
  
  + validate(): Boolean
  + get_violation_details(): String
}

enum ConstraintType {
  REGULATORY
  FINANCIAL
  PROCEDURAL
  TEMPORAL
  RESOURCE
}

enum SeverityLevel {
  INFO
  WARNING
  ERROR
  CRITICAL
}

class ConstraintCollection {
  - source_file: String
  - constraints: List<Constraint>
  - extraction_date: String
  
  + add_constraint(constraint: Constraint): void
  + get_by_type(type: ConstraintType): List<Constraint>
  + get_by_severity(level: SeverityLevel): List<Constraint>
}
@enduml
```

### Metadata Model

Metadata provides search-engine optimization and business domain information.

```plantuml
@startuml
class Metadata {
  - source_file: String
  - title: String
  - description: String
  - tags: List<String>
  - categories: List<String>
  - related_files: List<String>
  - creation_date: String
  - last_modified: String
  - author: String
  - version: String
  - relevance_score: Float
  - content_type: String
  - business_domains: List<String>
  - difficulty_level: String
  - estimated_reading_time: Integer
  - word_count: Integer
  - language: String
  - keywords: List<String>
  - related_entities: List<String>
  - related_components: List<String>
  - related_systems: List<String>
  - related_constraints: List<String>
  - custom_fields: Dict
  
  + add_tag(tag: String): void
  + add_category(category: String): void
  + update_field(field: String, value: Any): void
}
@enduml
```

## Relationships

The dataset elements are interconnected through various relationships:

```plantuml
@startuml
class Document {
  - filename: String
  - content: String
  - processing_date: String
}

Document ||--o{ KeywordCollection : contains
Document ||--o{ ECSArchitecture : implements
Document ||--o{ ConstraintCollection : has
Document ||--o{ Metadata : has

KeywordCollection ||--o{ Keyword : contains
ECSArchitecture ||--o{ Entity : contains
ECSArchitecture ||--o{ Component : contains
ECSArchitecture ||--o{ System : contains
ConstraintCollection ||--o{ Constraint : contains

Keyword }|--|{ Keyword : related_to
Entity }|--|{ Component : has
Component }|--|{ System : used_by
Constraint }|--|{ Document : applies_to

note top of Document
  Each document is processed to extract
  keywords, ECS elements, constraints,
  and metadata
end note

note bottom of ECSArchitecture
  ECS elements represent the business
  architecture described in the document
end note
@enduml
```

## Processing Pipeline

The following diagram shows the processing pipeline used to transform raw documentation files into structured data:

```plantuml
@startuml
start

:Load raw documentation file;

if (Is file in English?) then (yes)
  :Extract keywords;
  :Identify ECS elements;
  :Extract constraints;
  :Add metadata;
  :Validate data structures;
  :Save processed JSON file;
  :Create task tracking file;
else (no)
  :Skip file;
endif

if (More files to process?) then (yes)
  :Continue processing;
else (no)
  :Update master tracker;
  :Generate consolidated data;
endif

stop
@enduml
```

## Business Context

The dataset maintains Finnish business context while using English for system elements:

```plantuml
@startuml
package "Finnish Business Context" {
  rectangle "Finnish Legal Framework" as FLF
  rectangle "Finnish Tax Regulations" as FTR
  rectangle "Finnish Business Forms" as FBF
  rectangle "Finnish Industry Standards" as FIS
}

package "English System Elements" {
  rectangle "Keywords (English)" as KE
  rectangle "ECS Architecture (English)" as EECS
  rectangle "Constraints (English)" as EC
  rectangle "Metadata (English)" as EM
}

FLF --> KE : "Provides context for"
FTR --> EC : "Defines constraints for"
FBF --> EECS : "Implements architecture for"
FIS --> EM : "Influences metadata for"

note top of FLF
  All processing maintains
  Finnish business context
  while using English for
  system elements
end note
@enduml
```

## Usage Guidelines

The processed dataset can be used for:

- Search and retrieval of business information
- Automated compliance checking
- Business process modeling
- Knowledge graph construction
- Business intelligence applications

For more information on how to use the dataset, refer to the individual processed files in the `processed_docs` directory.