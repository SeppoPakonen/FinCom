"""
Data structure for keywords extracted from documentation files.
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json


@dataclass
class Keyword:
    """
    Represents a keyword extracted from a documentation file.
    """
    term: str
    frequency: int
    relevance: float
    category: str
    tags: List[str]
    source_file: str
    position_in_text: Optional[int] = None
    related_keywords: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.related_keywords is None:
            self.related_keywords = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the keyword to a dictionary."""
        return {
            "term": self.term,
            "frequency": self.frequency,
            "relevance": self.relevance,
            "category": self.category,
            "tags": self.tags,
            "source_file": self.source_file,
            "position_in_text": self.position_in_text,
            "related_keywords": self.related_keywords
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Keyword':
        """Create a Keyword instance from a dictionary."""
        return cls(
            term=data["term"],
            frequency=data["frequency"],
            relevance=data["relevance"],
            category=data["category"],
            tags=data["tags"],
            source_file=data["source_file"],
            position_in_text=data.get("position_in_text"),
            related_keywords=data.get("related_keywords", [])
        )


@dataclass
class KeywordCollection:
    """
    Collection of keywords from a single documentation file.
    """
    source_file: str
    keywords: List[Keyword]
    total_word_count: int
    extraction_date: str
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the collection to a dictionary."""
        return {
            "source_file": self.source_file,
            "total_word_count": self.total_word_count,
            "extraction_date": self.extraction_date,
            "keywords": [kw.to_dict() for kw in self.keywords]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'KeywordCollection':
        """Create a KeywordCollection instance from a dictionary."""
        keywords = [Keyword.from_dict(kw_data) for kw_data in data["keywords"]]
        return cls(
            source_file=data["source_file"],
            keywords=keywords,
            total_word_count=data["total_word_count"],
            extraction_date=data["extraction_date"]
        )
    
    def add_keyword(self, keyword: Keyword) -> None:
        """Add a keyword to the collection."""
        self.keywords.append(keyword)
    
    def get_by_category(self, category: str) -> List[Keyword]:
        """Get keywords by category."""
        return [kw for kw in self.keywords if kw.category == category]
    
    def get_by_relevance_threshold(self, threshold: float) -> List[Keyword]:
        """Get keywords with relevance above threshold."""
        return [kw for kw in self.keywords if kw.relevance >= threshold]