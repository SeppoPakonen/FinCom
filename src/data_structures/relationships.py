"""
Data structures for relationships and networks between different data elements.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Union
import json
from enum import Enum
from .keyword import Keyword, KeywordCollection
from .ecs_elements import Entity, Component, System, ECSArchitecture
from .constraint import Constraint, ConstraintCollection
from .metadata import Metadata


class RelationshipType(Enum):
    """Types of relationships between data elements."""
    DEPENDENCY = "dependency"
    REFERENCE = "reference"
    SIMILARITY = "similarity"
    CAUSATION = "causation"
    CONTAINMENT = "containment"
    CONSTRAINT = "constraint"
    EXECUTION_ORDER = "execution_order"
    INFORMATION_FLOW = "information_flow"


@dataclass
class Relationship:
    """
    Represents a relationship between two data elements.
    """
    id: str
    source_element_id: str
    target_element_id: str
    relationship_type: RelationshipType
    strength: float  # 0.0 to 1.0
    description: str
    source_type: str  # e.g., "keyword", "entity", "constraint", "metadata"
    target_type: str  # e.g., "keyword", "entity", "constraint", "metadata"
    tags: List[str]
    creation_date: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the relationship to a dictionary."""
        return {
            "id": self.id,
            "source_element_id": self.source_element_id,
            "target_element_id": self.target_element_id,
            "relationship_type": self.relationship_type.value,
            "strength": self.strength,
            "description": self.description,
            "source_type": self.source_type,
            "target_type": self.target_type,
            "tags": self.tags,
            "creation_date": self.creation_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Relationship':
        """Create a Relationship instance from a dictionary."""
        return cls(
            id=data["id"],
            source_element_id=data["source_element_id"],
            target_element_id=data["target_element_id"],
            relationship_type=RelationshipType(data["relationship_type"]),
            strength=data["strength"],
            description=data["description"],
            source_type=data["source_type"],
            target_type=data["target_type"],
            tags=data["tags"],
            creation_date=data["creation_date"]
        )


@dataclass
class GraphNode:
    """
    Represents a node in the relationship graph.
    """
    id: str
    element_type: str  # e.g., "keyword", "entity", "constraint", "metadata"
    element_data: Dict[str, Any]  # The actual data of the element
    tags: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary."""
        return {
            "id": self.id,
            "element_type": self.element_type,
            "element_data": self.element_data,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GraphNode':
        """Create a GraphNode instance from a dictionary."""
        return cls(
            id=data["id"],
            element_type=data["element_type"],
            element_data=data["element_data"],
            tags=data["tags"]
        )


@dataclass
class GraphEdge:
    """
    Represents an edge in the relationship graph.
    """
    id: str
    source_node_id: str
    target_node_id: str
    relationship_type: str
    weight: float
    properties: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the edge to a dictionary."""
        return {
            "id": self.id,
            "source_node_id": self.source_node_id,
            "target_node_id": self.target_node_id,
            "relationship_type": self.relationship_type,
            "weight": self.weight,
            "properties": self.properties
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GraphEdge':
        """Create a GraphEdge instance from a dictionary."""
        return cls(
            id=data["id"],
            source_node_id=data["source_node_id"],
            target_node_id=data["target_node_id"],
            relationship_type=data["relationship_type"],
            weight=data["weight"],
            properties=data["properties"]
        )


@dataclass
class RelationshipGraph:
    """
    Represents a graph of relationships between different data elements.
    """
    id: str
    name: str
    description: str
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    creation_date: str
    tags: List[str]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the graph to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "creation_date": self.creation_date,
            "tags": self.tags,
            "nodes": [node.to_dict() for node in self.nodes],
            "edges": [edge.to_dict() for edge in self.edges]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RelationshipGraph':
        """Create a RelationshipGraph instance from a dictionary."""
        nodes = [GraphNode.from_dict(node_data) for node_data in data["nodes"]]
        edges = [GraphEdge.from_dict(edge_data) for edge_data in data["edges"]]
        
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            nodes=nodes,
            edges=edges,
            creation_date=data["creation_date"],
            tags=data["tags"]
        )
    
    def add_node(self, node: GraphNode) -> None:
        """Add a node to the graph."""
        self.nodes.append(node)
    
    def add_edge(self, edge: GraphEdge) -> None:
        """Add an edge to the graph."""
        self.edges.append(edge)
    
    def get_node_by_id(self, node_id: str) -> Optional[GraphNode]:
        """Get a node by its ID."""
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None
    
    def get_neighbors(self, node_id: str) -> List[GraphNode]:
        """Get all neighbors of a node."""
        neighbors = []
        for edge in self.edges:
            if edge.source_node_id == node_id:
                target_node = self.get_node_by_id(edge.target_node_id)
                if target_node:
                    neighbors.append(target_node)
            elif edge.target_node_id == node_id:
                source_node = self.get_node_by_id(edge.source_node_id)
                if source_node:
                    neighbors.append(source_node)
        return neighbors
    
    def get_nodes_by_type(self, element_type: str) -> List[GraphNode]:
        """Get all nodes of a specific type."""
        return [node for node in self.nodes if node.element_type == element_type]
    
    def get_edges_by_relationship_type(self, rel_type: str) -> List[GraphEdge]:
        """Get all edges of a specific relationship type."""
        return [edge for edge in self.edges if edge.relationship_type == rel_type]