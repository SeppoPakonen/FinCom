"""
Data structure for constraints extracted from documentation files.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json
from enum import Enum


class ConstraintType(Enum):
    """Types of constraints that can be extracted."""
    REGULATORY = "regulatory"
    FINANCIAL = "financial"
    PROCEDURAL = "procedural"
    TEMPORAL = "temporal"
    RESOURCE = "resource"
    COMPLIANCE = "compliance"


class SeverityLevel(Enum):
    """Severity levels for constraints."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass
class Constraint:
    """
    Represents a constraint extracted from a documentation file.
    """
    id: str
    title: str
    description: str
    constraint_type: ConstraintType
    condition: str  # The condition that must be satisfied
    scope: str  # The scope where the constraint applies
    severity: SeverityLevel
    source_file: str
    tags: List[str]
    related_constraints: Optional[List[str]] = None
    validation_logic: Optional[str] = None  # Optional validation code
    error_message: Optional[str] = None
    
    def __post_init__(self):
        if self.related_constraints is None:
            self.related_constraints = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the constraint to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "constraint_type": self.constraint_type.value,
            "condition": self.condition,
            "scope": self.scope,
            "severity": self.severity.value,
            "source_file": self.source_file,
            "tags": self.tags,
            "related_constraints": self.related_constraints,
            "validation_logic": self.validation_logic,
            "error_message": self.error_message
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Constraint':
        """Create a Constraint instance from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            constraint_type=ConstraintType(data["constraint_type"]),
            condition=data["condition"],
            scope=data["scope"],
            severity=SeverityLevel(data["severity"]),
            source_file=data["source_file"],
            tags=data["tags"],
            related_constraints=data.get("related_constraints", []),
            validation_logic=data.get("validation_logic"),
            error_message=data.get("error_message")
        )


@dataclass
class ConstraintCollection:
    """
    Collection of constraints from a single documentation file.
    """
    source_file: str
    constraints: List[Constraint]
    extraction_date: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the collection to a dictionary."""
        return {
            "source_file": self.source_file,
            "extraction_date": self.extraction_date,
            "constraints": [con.to_dict() for con in self.constraints]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConstraintCollection':
        """Create a ConstraintCollection instance from a dictionary."""
        constraints = [Constraint.from_dict(con_data) for con_data in data["constraints"]]
        return cls(
            source_file=data["source_file"],
            constraints=constraints,
            extraction_date=data["extraction_date"]
        )
    
    def add_constraint(self, constraint: Constraint) -> None:
        """Add a constraint to the collection."""
        self.constraints.append(constraint)
    
    def get_by_type(self, constraint_type: ConstraintType) -> List[Constraint]:
        """Get constraints by type."""
        return [con for con in self.constraints if con.constraint_type == constraint_type]
    
    def get_by_severity(self, severity: SeverityLevel) -> List[Constraint]:
        """Get constraints by severity."""
        return [con for con in self.constraints if con.severity == severity]
    
    def get_by_tag(self, tag: str) -> List[Constraint]:
        """Get constraints by tag."""
        return [con for con in self.constraints if tag in con.tags]