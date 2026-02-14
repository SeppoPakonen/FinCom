# Finnish Business Operations Repository - Documentation

## Overview

This repository contains English documentation files from the Finnish Business Operations Repository, systematically processed to enhance them with structured data elements:

- **Keywords** with relevance scores and categories
- **ECS Elements** (Entities, Components, Systems) for business architecture
- **Constraints** with types and severity levels
- **Metadata** for search-engine optimization

## Repository Structure

```
├── docs/                          # Original documentation files
│   ├── dataset_documentation.md   # Comprehensive dataset documentation
│   ├── dataset_documentation_website.md  # Main documentation website
│   ├── index.md                   # Documentation index
│   └── diagrams/                  # PlantUML diagrams and generated images
├── processed_docs/               # Processed JSON files with enhanced data
├── plan/                         # Processing plans and trackers
│   └── manual_processing/        # Manual processing tasks and tracker
├── src/                          # Source code for processing scripts
└── README.md                     # This file
```

## Data Model

The processed data follows a structured model:

### Keywords
- Term: The keyword itself
- Frequency: How often it appears in the document
- Relevance: Relevance score (0.0-1.0)
- Category: Business term category
- Tags: Additional tags for classification

### ECS Architecture
- **Entities**: Actors, organizations, roles mentioned in the document
- **Components**: Attributes, properties, and data elements
- **Systems**: Processes, operations, and functions described

### Constraints
- ID: Unique identifier for the constraint
- Title: Brief title of the constraint
- Description: Detailed description
- Type: Regulatory, financial, procedural, etc.
- Severity: Info, warning, error, or critical level
- Scope: The domain where the constraint applies

### Metadata
- Title: Document title
- Description: Brief description
- Tags: Classification tags
- Categories: Business domain categories
- Related files: Cross-references to other documents
- Business domains: Specific business areas covered
- Difficulty level: Complexity assessment
- Estimated reading time
- Language: Document language
- Keywords: Top keywords from the document
- Related entities/components/systems/constraints

## Usage

The processed files can be used for:

- Search and retrieval of business information
- Automated compliance checking
- Business process modeling
- Knowledge graph construction
- Business intelligence applications

## Processing Methodology

The documentation files were processed using a systematic approach:

1. Identification of English content in the Finnish Business Operations Repository
2. Extraction of keywords with relevance scoring
3. Identification of ECS elements (entities, components, systems)
4. Extraction of constraints with types and severity levels
5. Addition of comprehensive metadata
6. Validation of all data structures
7. Relationship mapping between elements

## Quality Assurance

All processed files have been validated to ensure:

- Proper data structure formatting
- Correct relationships between elements
- Accurate metadata capture
- Cross-references with other documents

## License

This dataset is provided under the terms specified in the LICENSE file in the repository root.

## Contact

For questions about this dataset, please contact the maintainers through the project's issue tracker.