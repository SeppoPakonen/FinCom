"""
Unit tests for the exported data handling functionality.
"""

import unittest
import json
import os
from src.data_structures.keyword import Keyword, KeywordCollection
from src.data_structures.ecs_elements import Entity, Component, System, ECSArchitecture
from src.data_structures.constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from src.data_structures.metadata import Metadata, MetadataCollection
from src.data_structures.relationships import Relationship, RelationshipType, RelationshipGraph
from src.data_structures.exporter import DocumentDataExporter


class TestExportedDataHandling(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.exporter = DocumentDataExporter()
        
        # Sample data for testing
        self.sample_keyword = Keyword(
            term="test",
            frequency=5,
            relevance=0.8,
            category="test_category",
            tags=["test", "sample"],
            source_file="test.md"
        )
        
        self.sample_entity = Entity(
            name="TestEntity",
            description="A test entity",
            attributes={"key": "value"},
            tags=["test"],
            source_file="test.md"
        )
        
        self.sample_constraint = Constraint(
            id="test_constraint_1",
            title="Test Constraint",
            description="A test constraint",
            constraint_type=ConstraintType.COMPLIANCE,
            condition="test condition",
            scope="test scope",
            severity=SeverityLevel.WARNING,
            source_file="test.md",
            tags=["test"]
        )
        
        self.sample_metadata = Metadata(
            source_file="test.md",
            title="Test Document",
            description="A test document",
            tags=["test"],
            categories=["test"],
            related_files=[],
            creation_date="2023-01-01",
            last_modified="2023-01-01",
            author="test",
            version="1.0",
            relevance_score=0.5,
            content_type="test",
            business_domains=["test"],
            difficulty_level="intermediate",
            estimated_reading_time=5,
            word_count=100,
            language="en",
            keywords=["test"],
            related_entities=["TestEntity"],
            related_components=[],
            related_systems=[],
            related_constraints=["test_constraint_1"]
        )
    
    def test_keyword_serialization(self):
        """Test that Keyword objects can be serialized and deserialized correctly."""
        original_dict = self.sample_keyword.to_dict()
        reconstructed = Keyword.from_dict(original_dict)
        
        self.assertEqual(self.sample_keyword.term, reconstructed.term)
        self.assertEqual(self.sample_keyword.frequency, reconstructed.frequency)
        self.assertEqual(self.sample_keyword.relevance, reconstructed.relevance)
        self.assertEqual(self.sample_keyword.category, reconstructed.category)
        self.assertEqual(self.sample_keyword.tags, reconstructed.tags)
        self.assertEqual(self.sample_keyword.source_file, reconstructed.source_file)
    
    def test_entity_serialization(self):
        """Test that Entity objects can be serialized and deserialized correctly."""
        original_dict = self.sample_entity.to_dict()
        reconstructed = Entity.from_dict(original_dict)
        
        self.assertEqual(self.sample_entity.name, reconstructed.name)
        self.assertEqual(self.sample_entity.description, reconstructed.description)
        self.assertEqual(self.sample_entity.attributes, reconstructed.attributes)
        self.assertEqual(self.sample_entity.tags, reconstructed.tags)
        self.assertEqual(self.sample_entity.source_file, reconstructed.source_file)
    
    def test_constraint_serialization(self):
        """Test that Constraint objects can be serialized and deserialized correctly."""
        original_dict = self.sample_constraint.to_dict()
        reconstructed = Constraint.from_dict(original_dict)
        
        self.assertEqual(self.sample_constraint.id, reconstructed.id)
        self.assertEqual(self.sample_constraint.title, reconstructed.title)
        self.assertEqual(self.sample_constraint.description, reconstructed.description)
        self.assertEqual(self.sample_constraint.constraint_type, reconstructed.constraint_type)
        self.assertEqual(self.sample_constraint.condition, reconstructed.condition)
        self.assertEqual(self.sample_constraint.scope, reconstructed.scope)
        self.assertEqual(self.sample_constraint.severity, reconstructed.severity)
        self.assertEqual(self.sample_constraint.source_file, reconstructed.source_file)
        self.assertEqual(self.sample_constraint.tags, reconstructed.tags)
    
    def test_metadata_serialization(self):
        """Test that Metadata objects can be serialized and deserialized correctly."""
        original_dict = self.sample_metadata.to_dict()
        reconstructed = Metadata.from_dict(original_dict)
        
        self.assertEqual(self.sample_metadata.source_file, reconstructed.source_file)
        self.assertEqual(self.sample_metadata.title, reconstructed.title)
        self.assertEqual(self.sample_metadata.description, reconstructed.description)
        self.assertEqual(self.sample_metadata.tags, reconstructed.tags)
        self.assertEqual(self.sample_metadata.categories, reconstructed.categories)
        self.assertEqual(self.sample_metadata.content_type, reconstructed.content_type)
        self.assertEqual(self.sample_metadata.business_domains, reconstructed.business_domains)
    
    def test_extract_from_existing_file(self):
        """Test extracting data from an existing file."""
        # Use one of our example files
        file_path = "../docs/business_forms/company_formation_example.md"
        if os.path.exists(file_path):
            extracted_data = self.exporter.extract_from_file(file_path)
            
            # Check that we got data back
            self.assertIn("file_path", extracted_data)
            self.assertIn("keywords", extracted_data)
            self.assertIn("ecs_elements", extracted_data)
            self.assertIn("constraints", extracted_data)
            self.assertIn("metadata", extracted_data)
            
            # Check that keywords were extracted
            self.assertIsInstance(extracted_data["keywords"], list)
            
            # Check that ECS elements were extracted
            self.assertIn("entities", extracted_data["ecs_elements"])
            self.assertIn("components", extracted_data["ecs_elements"])
            self.assertIn("systems", extracted_data["ecs_elements"])
            
            # Check that constraints were extracted
            self.assertIsInstance(extracted_data["constraints"], list)
            
            # Check that metadata was extracted
            self.assertIsInstance(extracted_data["metadata"], dict)
        else:
            # Skip this test if the file doesn't exist
            self.skipTest(f"File {file_path} does not exist")
    
    def test_create_relationship_graph(self):
        """Test creating a relationship graph from extracted data."""
        # Use our example files
        file1_path = "../docs/business_forms/company_formation_example.md"
        file2_path = "../docs/business_forms/company_finance_example.md"
        
        if os.path.exists(file1_path) and os.path.exists(file2_path):
            # Extract data from both files
            data1 = self.exporter.extract_from_file(file1_path)
            data2 = self.exporter.extract_from_file(file2_path)
            
            # Create relationship graph
            graph = self.exporter.create_relationship_graph([data1, data2])
            
            # Check that the graph was created
            self.assertIsInstance(graph, RelationshipGraph)
            self.assertGreater(len(graph.nodes), 0)
            self.assertGreater(len(graph.edges), 0)
        else:
            # Skip this test if the files don't exist
            self.skipTest(f"One or both of the files do not exist")


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)