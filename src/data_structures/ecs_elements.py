"""
Data structures for ECS (Entity-Component-System) elements extracted from documentation files.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Set
import json


@dataclass
class Entity:
    """
    Represents an entity in the ECS architecture.
    """
    name: str
    description: str
    attributes: Dict[str, Any]
    tags: List[str]
    source_file: str
    relationships: Optional[Dict[str, List[str]]] = None
    
    def __post_init__(self):
        if self.relationships is None:
            self.relationships = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the entity to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "attributes": self.attributes,
            "tags": self.tags,
            "source_file": self.source_file,
            "relationships": self.relationships
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Entity':
        """Create an Entity instance from a dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            attributes=data["attributes"],
            tags=data["tags"],
            source_file=data["source_file"],
            relationships=data.get("relationships", {})
        )


@dataclass
class Component:
    """
    Represents a component in the ECS architecture.
    """
    name: str
    description: str
    properties: Dict[str, Any]
    data_schema: Dict[str, str]  # Maps property name to type
    tags: List[str]
    source_file: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the component to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "properties": self.properties,
            "data_schema": self.data_schema,
            "tags": self.tags,
            "source_file": self.source_file
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Component':
        """Create a Component instance from a dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            properties=data["properties"],
            data_schema=data["data_schema"],
            tags=data["tags"],
            source_file=data["source_file"]
        )


@dataclass
class System:
    """
    Represents a system in the ECS architecture.
    """
    name: str
    description: str
    behavior: str  # Description of what the system does
    dependencies: List[str]  # Names of required components
    triggers: List[str]  # Events that trigger the system
    tags: List[str]
    source_file: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the system to a dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "behavior": self.behavior,
            "dependencies": self.dependencies,
            "triggers": self.triggers,
            "tags": self.tags,
            "source_file": self.source_file
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'System':
        """Create a System instance from a dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            behavior=data["behavior"],
            dependencies=data["dependencies"],
            triggers=data["triggers"],
            tags=data["tags"],
            source_file=data["source_file"]
        )


@dataclass
class ECSArchitecture:
    """
    Complete ECS architecture extracted from a documentation file.
    """
    source_file: str
    entities: List[Entity]
    components: List[Component]
    systems: List[System]
    extraction_date: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the ECS architecture to a dictionary."""
        return {
            "source_file": self.source_file,
            "extraction_date": self.extraction_date,
            "entities": [ent.to_dict() for ent in self.entities],
            "components": [comp.to_dict() for comp in self.components],
            "systems": [sys.to_dict() for sys in self.systems]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ECSArchitecture':
        """Create an ECSArchitecture instance from a dictionary."""
        entities = [Entity.from_dict(ent_data) for ent_data in data["entities"]]
        components = [Component.from_dict(comp_data) for comp_data in data["components"]]
        systems = [System.from_dict(sys_data) for sys_data in data["systems"]]
        
        return cls(
            source_file=data["source_file"],
            entities=entities,
            components=components,
            systems=systems,
            extraction_date=data["extraction_date"]
        )
    
    def get_entity_by_name(self, name: str) -> Optional[Entity]:
        """Get an entity by name."""
        for entity in self.entities:
            if entity.name == name:
                return entity
        return None
    
    def get_component_by_name(self, name: str) -> Optional[Component]:
        """Get a component by name."""
        for component in self.components:
            if component.name == name:
                return component
        return None
    
    def get_system_by_name(self, name: str) -> Optional[System]:
        """Get a system by name."""
        for system in self.systems:
            if system.name == name:
                return system
        return None