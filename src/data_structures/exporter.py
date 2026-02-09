"""
Main handler for exporting and processing data from documentation files.
"""

import os
import json
from typing import Dict, Any, List, Optional, Union
from datetime import datetime
from .keyword import Keyword, KeywordCollection
from .ecs_elements import Entity, Component, System, ECSArchitecture
from .constraint import Constraint, ConstraintCollection, ConstraintType, SeverityLevel
from .metadata import Metadata, MetadataCollection
from .relationships import Relationship, RelationshipType, RelationshipGraph, GraphNode, GraphEdge


class DocumentDataExporter:
    """
    Main class for extracting and handling data from documentation files.
    """
    
    def __init__(self, docs_dir: str = "docs"):
        self.docs_dir = docs_dir
        self.extracted_data = {}
    
    def extract_from_file(self, file_path: str) -> Dict[str, Any]:
        """
        Extract all data types from a single documentation file.
        
        Args:
            file_path: Path to the documentation file
            
        Returns:
            Dictionary containing all extracted data
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract different data types
        keywords = self._extract_keywords(content, file_path)
        ecs_arch = self._extract_ecs_elements(content, file_path)
        constraints = self._extract_constraints(content, file_path)
        metadata = self._create_metadata(content, file_path)
        
        # Package all extracted data
        result = {
            "file_path": file_path,
            "keywords": [kw.to_dict() for kw in keywords],
            "ecs_elements": ecs_arch.to_dict(),
            "constraints": [con.to_dict() for con in constraints],
            "metadata": metadata.to_dict(),
            "extraction_date": datetime.now().isoformat()
        }
        
        self.extracted_data[file_path] = result
        return result
    
    def _extract_keywords(self, content: str, file_path: str) -> List[Keyword]:
        """
        Extract keywords from the content.
        This is a simplified implementation - in practice, this would use NLP techniques.
        """
        import re
        
        # Simple keyword extraction based on common business terms
        common_terms = [
            'business', 'company', 'corporation', 'enterprise', 'organization',
            'registration', 'formation', 'establishment', 'incorporation',
            'tax', 'taxation', 'vat', 'income', 'profit', 'loss', 'revenue',
            'finance', 'accounting', 'budget', 'cash', 'investment',
            'compliance', 'regulation', 'requirement', 'obligation',
            'employment', 'work', 'salary', 'benefit', 'insurance',
            'contract', 'agreement', 'partnership', 'shareholder',
            'report', 'declaration', 'form', 'application', 'notification'
        ]
        
        content_lower = content.lower()
        found_keywords = []
        
        for term in common_terms:
            if term in content_lower:
                count = content_lower.count(term)
                # Calculate relevance based on frequency and length of document
                relevance = min(count * 10.0 / len(content.split()), 1.0)
                
                keyword = Keyword(
                    term=term,
                    frequency=count,
                    relevance=relevance,
                    category="business_term",
                    tags=["automated_extraction"],
                    source_file=file_path
                )
                found_keywords.append(keyword)
        
        # Also extract capitalized words that might be specific terms
        capitalized_words = re.findall(r'\b[A-Z][A-Za-z]{3,}\b', content[:2000])  # First 2000 chars
        for word in capitalized_words:
            if len(word) > 3 and word.lower() not in [kw.term.lower() for kw in found_keywords]:
                count = len(re.findall(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE))
                relevance = min(count * 5.0 / len(content.split()), 1.0)
                
                keyword = Keyword(
                    term=word,
                    frequency=count,
                    relevance=relevance,
                    category="proper_noun",
                    tags=["capitalized_term"],
                    source_file=file_path
                )
                found_keywords.append(keyword)
        
        return found_keywords
    
    def _extract_ecs_elements(self, content: str, file_path: str) -> ECSArchitecture:
        """
        Extract ECS elements from the content.
        This identifies entities, components, and systems mentioned in the document.
        """
        import re
        
        # Look for entity-like terms (actors, organizations, roles)
        entity_patterns = [
            r'(?:the\s+)?([A-Z][a-z]+\s+[A-Z][a-z]+)(?:\s+(?:is|are|was|were))',  # "Company Name is"
            r'(?:as\s+)?(?:a|an)\s+([A-Z][a-z]+)(?:\s+(?:representative|officer|director|employee))',  # "as a Director"
            r'(?:the\s+)?([A-Z][a-z]+)(?:\s+(?:must|shall|should|needs to))',  # "Company must"
        ]
        
        entities = []
        for pattern in entity_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                entity = Entity(
                    name=match.strip(),
                    description=f"Entity identified in {file_path}",
                    attributes={"source_document": file_path},
                    tags=["automated_extraction"],
                    source_file=file_path
                )
                entities.append(entity)
        
        # Look for component-like terms (attributes, properties)
        component_patterns = [
            r'(?:the\s+)?([A-Z][a-z]*\s*[A-Z][a-z]*)\s+(?:of|for)\s+',  # "Registration Date of"
            r'(?:with\s+)?(?:the\s+)?([A-Z][a-z]+)\s+(?:of|for)',  # "Amount of"
        ]
        
        components = []
        for pattern in component_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                component = Component(
                    name=match.strip(),
                    description=f"Component identified in {file_path}",
                    properties={"source_document": file_path},
                    data_schema={"value": "string"},
                    tags=["automated_extraction"],
                    source_file=file_path
                )
                components.append(component)
        
        # Look for system-like terms (processes, operations)
        system_patterns = [
            r'(?:the\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:process|procedure|system)',  # "Registration Process"
            r'(?:to\s+)?([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\s+(?:must|shall|requires)',  # "Filing must"
        ]
        
        systems = []
        for pattern in system_patterns:
            matches = re.findall(pattern, content)
            for match in matches:
                system = System(
                    name=match.strip(),
                    description=f"System/process identified in {file_path}",
                    behavior="Behavior to be defined manually",
                    dependencies=[],
                    triggers=[],
                    tags=["automated_extraction"],
                    source_file=file_path
                )
                systems.append(system)
        
        return ECSArchitecture(
            source_file=file_path,
            entities=entities,
            components=components,
            systems=systems,
            extraction_date=datetime.now().isoformat()
        )
    
    def _extract_constraints(self, content: str, file_path: str) -> List[Constraint]:
        """
        Extract constraints from the content.
        Identifies regulatory, financial, procedural, etc. constraints.
        """
        import re
        
        constraints = []
        
        # Look for constraint-indicating phrases
        constraint_indicators = [
            (r'(?:must|shall|required|need to|has to|obliged to)', ConstraintType.COMPLIANCE),
            (r'(?:within\s+\d+\s+(?:days|weeks|months|years))', ConstraintType.TEMPORAL),
            (r'(?:minimum|at least|not less than)\s+(\d+)', ConstraintType.FINANCIAL),
            (r'(?:maximum|at most|not more than|up to)\s+(\d+)', ConstraintType.RESOURCE),
            (r'(?:before|after|by)\s+(?:the|each|every)', ConstraintType.TEMPORAL),
        ]
        
        for pattern, c_type in constraint_indicators:
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches[:3]:  # Limit to first 3 matches to avoid spam
                constraint_id = f"{file_path.replace('/', '_').replace('.', '_')}_{len(constraints)+1}"
                
                constraint = Constraint(
                    id=constraint_id,
                    title=f"Automatically detected {c_type.value} constraint",
                    description=f"Constraint found in {file_path}: {match}",
                    constraint_type=c_type,
                    condition=match if isinstance(match, str) else str(match),
                    scope="document_specific",
                    severity=SeverityLevel.WARNING,
                    source_file=file_path,
                    tags=["automated_extraction", c_type.value]
                )
                constraints.append(constraint)
        
        return constraints
    
    def _create_metadata(self, content: str, file_path: str) -> Metadata:
        """
        Create metadata for the document.
        """
        import re
        
        # Extract title from first heading or filename
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else os.path.basename(file_path)
        
        # Estimate reading time (200 words per minute)
        word_count = len(content.split())
        reading_time = max(1, word_count // 200)
        
        # Determine content type based on keywords
        content_type = "guidance"
        if any(term in content.lower() for term in ["form", "template", "fill", "submit"]):
            content_type = "form"
        elif any(term in content.lower() for term in ["law", "act", "section", "paragraph", "regulation"]):
            content_type = "regulation"
        elif any(term in content.lower() for term in ["procedure", "step", "how to", "process"]):
            content_type = "procedure"
        
        # Identify business domains
        business_domains = []
        if any(term in content.lower() for term in ["tax", "vat", "income", "revenue"]):
            business_domains.append("tax")
        if any(term in content.lower() for term in ["finance", "budget", "investment", "cash"]):
            business_domains.append("finance")
        if any(term in content.lower() for term in ["compliance", "requirement", "obligation"]):
            business_domains.append("compliance")
        
        return Metadata(
            source_file=file_path,
            title=title,
            description=content[:200] + "..." if len(content) > 200 else content,
            tags=["automated_extraction"],
            categories=[content_type],
            related_files=[],
            creation_date=datetime.now().isoformat(),
            last_modified=datetime.now().isoformat(),
            author="automated_extraction",
            version="1.0",
            relevance_score=0.5,
            content_type=content_type,
            business_domains=business_domains,
            difficulty_level="intermediate",  # Default, to be adjusted manually
            estimated_reading_time=reading_time,
            word_count=word_count,
            language="en",
            keywords=[],  # Will be populated from extracted keywords
            related_entities=[],  # Will be populated from ECS entities
            related_components=[],  # Will be populated from ECS components
            related_systems=[],  # Will be populated from ECS systems
            related_constraints=[]  # Will be populated from constraints
        )
    
    def create_relationship_graph(self, extracted_data_list: List[Dict[str, Any]]) -> RelationshipGraph:
        """
        Create a relationship graph connecting different data elements across files.
        
        Args:
            extracted_data_list: List of extracted data from multiple files
            
        Returns:
            RelationshipGraph connecting the data elements
        """
        nodes = []
        edges = []
        
        # Create nodes for each data element
        node_counter = 0
        
        for data in extracted_data_list:
            file_path = data["file_path"]
            
            # Create a node for the file itself
            file_node = GraphNode(
                id=f"file_{node_counter}",
                element_type="file",
                element_data={
                    "path": file_path,
                    "extraction_date": data["extraction_date"]
                },
                tags=["file_node"]
            )
            nodes.append(file_node)
            file_node_id = file_node.id
            node_counter += 1
            
            # Create nodes for keywords
            for i, kw_data in enumerate(data["keywords"]):
                kw_node = GraphNode(
                    id=f"keyword_{node_counter}",
                    element_type="keyword",
                    element_data=kw_data,
                    tags=["keyword_node"]
                )
                nodes.append(kw_node)
                
                # Connect keyword to file
                edge = GraphEdge(
                    id=f"edge_{len(edges)}",
                    source_node_id=kw_node.id,
                    target_node_id=file_node_id,
                    relationship_type="CONTAINS",
                    weight=0.7,
                    properties={"relationship_subtype": "keyword_in_file"}
                )
                edges.append(edge)
                node_counter += 1
            
            # Create nodes for ECS elements
            ecs_data = data["ecs_elements"]
            for entity_data in ecs_data["entities"]:
                entity_node = GraphNode(
                    id=f"entity_{node_counter}",
                    element_type="entity",
                    element_data=entity_data,
                    tags=["entity_node"]
                )
                nodes.append(entity_node)
                
                # Connect entity to file
                edge = GraphEdge(
                    id=f"edge_{len(edges)}",
                    source_node_id=entity_node.id,
                    target_node_id=file_node_id,
                    relationship_type="MENTIONS",
                    weight=0.8,
                    properties={"relationship_subtype": "entity_mentioned_in_file"}
                )
                edges.append(edge)
                node_counter += 1
            
            for component_data in ecs_data["components"]:
                component_node = GraphNode(
                    id=f"component_{node_counter}",
                    element_type="component",
                    element_data=component_data,
                    tags=["component_node"]
                )
                nodes.append(component_node)
                
                # Connect component to file
                edge = GraphEdge(
                    id=f"edge_{len(edges)}",
                    source_node_id=component_node.id,
                    target_node_id=file_node_id,
                    relationship_type="MENTIONS",
                    weight=0.8,
                    properties={"relationship_subtype": "component_mentioned_in_file"}
                )
                edges.append(edge)
                node_counter += 1
            
            for system_data in ecs_data["systems"]:
                system_node = GraphNode(
                    id=f"system_{node_counter}",
                    element_type="system",
                    element_data=system_data,
                    tags=["system_node"]
                )
                nodes.append(system_node)
                
                # Connect system to file
                edge = GraphEdge(
                    id=f"edge_{len(edges)}",
                    source_node_id=system_node.id,
                    target_node_id=file_node_id,
                    relationship_type="MENTIONS",
                    weight=0.8,
                    properties={"relationship_subtype": "system_mentioned_in_file"}
                )
                edges.append(edge)
                node_counter += 1
            
            # Create nodes for constraints
            for i, con_data in enumerate(data["constraints"]):
                con_node = GraphNode(
                    id=f"constraint_{node_counter}",
                    element_type="constraint",
                    element_data=con_data,
                    tags=["constraint_node"]
                )
                nodes.append(con_node)
                
                # Connect constraint to file
                edge = GraphEdge(
                    id=f"edge_{len(edges)}",
                    source_node_id=con_node.id,
                    target_node_id=file_node_id,
                    relationship_type="DEFINED_IN",
                    weight=0.9,
                    properties={"relationship_subtype": "constraint_defined_in_file"}
                )
                edges.append(edge)
                node_counter += 1
        
        # Create inter-file relationships based on shared keywords
        self._create_inter_file_relationships(nodes, edges)
        
        return RelationshipGraph(
            id="relationship_graph_1",
            name="Cross-Document Relationships",
            description="Relationships between data elements across different documentation files",
            nodes=nodes,
            edges=edges,
            creation_date=datetime.now().isoformat(),
            tags=["cross_document", "automated_generation"]
        )
    
    def _create_inter_file_relationships(self, nodes: List[GraphNode], edges: List[GraphEdge]) -> None:
        """
        Create relationships between elements from different files.
        """
        # Group nodes by type
        keyword_nodes = [n for n in nodes if n.element_type == "keyword"]
        file_nodes = [n for n in nodes if n.element_type == "file"]
        
        # Create relationships between files that share common keywords
        for i, kw_node1 in enumerate(keyword_nodes):
            kw_term1 = kw_node1.element_data.get("term", "")
            
            for j, kw_node2 in enumerate(keyword_nodes[i+1:], i+1):
                kw_term2 = kw_node2.element_data.get("term", "")
                
                if kw_term1.lower() == kw_term2.lower() and kw_term1 != "":
                    # Find the files associated with these keywords
                    file_node1 = self._find_associated_file(kw_node1, nodes, edges)
                    file_node2 = self._find_associated_file(kw_node2, nodes, edges)
                    
                    if file_node1 and file_node2 and file_node1.id != file_node2.id:
                        # Create a relationship between the files based on shared keyword
                        edge = GraphEdge(
                            id=f"edge_{len(edges)}",
                            source_node_id=file_node1.id,
                            target_node_id=file_node2.id,
                            relationship_type="RELATED_BY_KEYWORD",
                            weight=kw_node1.element_data.get("relevance", 0.5),
                            properties={
                                "relationship_subtype": "shares_keyword",
                                "keyword": kw_term1
                            }
                        )
                        edges.append(edge)
    
    def _find_associated_file(self, node: GraphNode, all_nodes: List[GraphNode], all_edges: List[GraphEdge]) -> Optional[GraphNode]:
        """
        Find the file node associated with a given node through edges.
        """
        for edge in all_edges:
            if edge.source_node_id == node.id:
                target_node = next((n for n in all_nodes if n.id == edge.target_node_id), None)
                if target_node and target_node.element_type == "file":
                    return target_node
            elif edge.target_node_id == node.id:
                source_node = next((n for n in all_nodes if n.id == edge.source_node_id), None)
                if source_node and source_node.element_type == "file":
                    return source_node
        return None
    
    def save_extracted_data(self, output_dir: str = "exported_data") -> None:
        """
        Save all extracted data to JSON files.
        """
        os.makedirs(output_dir, exist_ok=True)
        
        for file_path, data in self.extracted_data.items():
            # Create a safe filename
            safe_filename = file_path.replace("/", "_").replace("\\", "_").replace(":", "_")
            output_path = os.path.join(output_dir, f"{safe_filename}.json")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_extracted_data(self, input_dir: str = "exported_data") -> None:
        """
        Load extracted data from JSON files.
        """
        for filename in os.listdir(input_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(input_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    original_path = data["file_path"]
                    self.extracted_data[original_path] = data


# Example usage and testing
if __name__ == "__main__":
    # This would be used to test the data extraction
    print("DocumentDataExporter class defined successfully.")
    print("Use extract_from_file() method to extract data from documentation files.")