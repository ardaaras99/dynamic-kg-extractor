from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation


class LLMOptions(str, Enum):
    OPENAI_O3_MINI = "o3-mini-2025-01-31"
    OPENAI_GPT4_O1 = "gpt-4o-2024-08-06"


@dataclass
class NodeExtractorConfig:
    file_path: Path
    node_dict: dict[str, tuple[type[BaseNode], bool, str]]
    llm_model_name: LLMOptions


@dataclass
class RelationExtractorConfig:
    relation_dict: dict[str, type[BaseRelation]]
    llm_model_name: LLMOptions
