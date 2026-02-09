"""
Example script to demonstrate data extraction from documentation files.
This creates example exported data from a sample documentation file.
"""

import json
import sys
import os
from datetime import datetime
# Add the current directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures.exporter import DocumentDataExporter
from data_structures.keyword import KeywordCollection
from data_structures.ecs_elements import ECSArchitecture
from data_structures.constraint import ConstraintCollection
from data_structures.metadata import Metadata
from data_structures.relationships import RelationshipGraph


def create_example_export():
    """Create example exported data from a documentation file."""
    
    # Initialize the exporter
    exporter = DocumentDataExporter()
    
    # Extract data from the example file
    file_path = "../docs/business_forms/company_formation_example.md"
    extracted_data = exporter.extract_from_file(file_path)
    
    # Print the extracted data to see the structure
    print("Extracted data structure:")
    print(json.dumps(extracted_data, indent=2, ensure_ascii=False))
    
    # Save the extracted data
    exporter.save_extracted_data("../examples/exported_data")
    
    print(f"\nExtracted data saved to ../examples/exported_data/")
    
    # Create a relationship graph
    graph = exporter.create_relationship_graph([extracted_data])
    
    # Save the relationship graph
    graph_path = "../examples/exported_data/relationship_graph.json"
    with open(graph_path, 'w', encoding='utf-8') as f:
        json.dump(graph.to_dict(), f, ensure_ascii=False, indent=2)
    
    print(f"Relationship graph saved to {graph_path}")
    
    return extracted_data, graph


def create_second_connected_example():
    """Create a second example that connects to the first one."""
    
    # Create a second documentation file that relates to the first
    second_doc_content = """# Managing Company Finances in Finland

## Overview
This document explains how to manage finances for a Finnish limited liability company (Oy).

## Key Financial Requirements
- Maintain proper accounting records
- File annual financial statements
- Pay corporate tax (20% of profits)
- Register for VAT if turnover exceeds €10,000 annually

## Banking
- Open a business bank account in Finland
- Separate business and personal finances
- Keep detailed transaction records

## Tax Obligations
- Corporate income tax: 20% of profits
- VAT registration required above €10,000 annual turnover
- Payroll taxes for employees

## Compliance
- Annual financial statements must be filed with PRH
- Auditing requirements for larger companies
- Board members responsible for financial oversight

## Important Constraints
- Financial statements must be filed annually
- Companies with turnover > €800,000 require auditing
- Directors liable for unpaid taxes in certain circumstances
"""
    
    # Write the second example file
    with open("../docs/business_forms/company_finance_example.md", "w", encoding="utf-8") as f:
        f.write(second_doc_content)
    
    # Extract data from the second file
    exporter = DocumentDataExporter()
    extracted_data2 = exporter.extract_from_file("../docs/business_forms/company_finance_example.md")
    
    # Save the second extracted data
    exporter.save_extracted_data("../examples/exported_data")
    
    print("Second example data extracted and saved.")
    
    # Create a combined relationship graph
    import json
    first_data_path = "../examples/exported_data/docs_business_forms_company_formation_example_md.json"
    if os.path.exists(first_data_path):
        with open(first_data_path, "r", encoding="utf-8") as f:
            first_data = json.load(f)
        combined_graph = exporter.create_relationship_graph([first_data, extracted_data2])
    else:
        # If the first file doesn't exist, just create graph for the second
        combined_graph = exporter.create_relationship_graph([extracted_data2])
    
    # Save the combined relationship graph
    graph_path = "../examples/exported_data/combined_relationship_graph.json"
    with open(graph_path, 'w', encoding='utf-8') as f:
        json.dump(combined_graph.to_dict(), f, ensure_ascii=False, indent=2)
    
    print(f"Combined relationship graph saved to {graph_path}")
    
    return extracted_data2, combined_graph


if __name__ == "__main__":
    print("Creating example exported data...")
    
    # Create first example
    first_data, first_graph = create_example_export()
    
    print("\n" + "="*50)
    print("Creating second connected example...")
    
    # Create second example that connects to the first
    second_data, combined_graph = create_second_connected_example()
    
    print("\n" + "="*50)
    print("Example creation completed!")
    print("Files created:")
    print("- ../docs/business_forms/company_formation_example.md")
    print("- ../docs/business_forms/company_finance_example.md")
    print("- ../examples/exported_data/docs_business_forms_company_formation_example_md.json")
    print("- ../examples/exported_data/docs_business_forms_company_finance_example_md.json")
    print("- ../examples/exported_data/relationship_graph.json")
    print("- ../examples/exported_data/combined_relationship_graph.json")