"""
Data structure for search-engine metadata extracted from documentation files.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json
from datetime import datetime


@dataclass
class Metadata:
    """
    Represents search-engine metadata for a documentation file.
    """
    source_file: str
    title: str
    description: str
    tags: List[str]
    categories: List[str]
    related_files: List[str]
    creation_date: str
    last_modified: str
    author: str
    version: str
    relevance_score: float
    content_type: str  # e.g., "procedure", "regulation", "form", "guidance"
    business_domains: List[str]  # e.g., ["finance", "tax", "compliance"]
    difficulty_level: str  # e.g., "beginner", "intermediate", "advanced"
    estimated_reading_time: int  # in minutes
    word_count: int
    language: str
    keywords: List[str]  # High-level keywords for search
    related_entities: List[str]  # ECS entities mentioned
    related_components: List[str]  # ECS components mentioned
    related_systems: List[str]  # ECS systems mentioned
    related_constraints: List[str]  # Constraint IDs mentioned
    custom_fields: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        if self.custom_fields is None:
            self.custom_fields = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the metadata to a dictionary."""
        return {
            "source_file": self.source_file,
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "categories": self.categories,
            "related_files": self.related_files,
            "creation_date": self.creation_date,
            "last_modified": self.last_modified,
            "author": self.author,
            "version": self.version,
            "relevance_score": self.relevance_score,
            "content_type": self.content_type,
            "business_domains": self.business_domains,
            "difficulty_level": self.difficulty_level,
            "estimated_reading_time": self.estimated_reading_time,
            "word_count": self.word_count,
            "language": self.language,
            "keywords": self.keywords,
            "related_entities": self.related_entities,
            "related_components": self.related_components,
            "related_systems": self.related_systems,
            "related_constraints": self.related_constraints,
            "custom_fields": self.custom_fields
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Metadata':
        """Create a Metadata instance from a dictionary."""
        return cls(
            source_file=data["source_file"],
            title=data["title"],
            description=data["description"],
            tags=data["tags"],
            categories=data["categories"],
            related_files=data["related_files"],
            creation_date=data["creation_date"],
            last_modified=data["last_modified"],
            author=data["author"],
            version=data["version"],
            relevance_score=data["relevance_score"],
            content_type=data["content_type"],
            business_domains=data["business_domains"],
            difficulty_level=data["difficulty_level"],
            estimated_reading_time=data["estimated_reading_time"],
            word_count=data["word_count"],
            language=data["language"],
            keywords=data["keywords"],
            related_entities=data["related_entities"],
            related_components=data["related_components"],
            related_systems=data["related_systems"],
            related_constraints=data["related_constraints"],
            custom_fields=data.get("custom_fields", {})
        )


@dataclass
class MetadataCollection:
    """
    Collection of metadata for multiple documentation files.
    """
    metadata_entries: List[Metadata]
    collection_date: str
    total_files: int
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the collection to a dictionary."""
        return {
            "collection_date": self.collection_date,
            "total_files": self.total_files,
            "metadata_entries": [meta.to_dict() for meta in self.metadata_entries]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'MetadataCollection':
        """Create a MetadataCollection instance from a dictionary."""
        metadata_entries = [Metadata.from_dict(meta_data) for meta_data in data["metadata_entries"]]
        return cls(
            metadata_entries=metadata_entries,
            collection_date=data["collection_date"],
            total_files=data["total_files"]
        )
    
    def add_metadata(self, metadata: Metadata) -> None:
        """Add metadata to the collection."""
        self.metadata_entries.append(metadata)
        self.total_files = len(self.metadata_entries)
    
    def get_by_category(self, category: str) -> List[Metadata]:
        """Get metadata entries by category."""
        return [meta for meta in self.metadata_entries if category in meta.categories]
    
    def get_by_business_domain(self, domain: str) -> List[Metadata]:
        """Get metadata entries by business domain."""
        return [meta for meta in self.metadata_entries if domain in meta.business_domains]
    
    def get_by_content_type(self, content_type: str) -> List[Metadata]:
        """Get metadata entries by content type."""
        return [meta for meta in self.metadata_entries if meta.content_type == content_type]
    
    def search_by_keyword(self, keyword: str) -> List[Metadata]:
        """Search metadata entries by keyword."""
        return [meta for meta in self.metadata_entries if keyword.lower() in [kw.lower() for kw in meta.keywords]]