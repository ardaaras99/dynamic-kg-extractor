# %%

from pathlib import Path

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation

from dynamic_kg_extractor.models.configurations import (
    LLMOptions,
    NodeExtractorConfig,
    RelationExtractorConfig,
)
from dynamic_kg_extractor.models.node_extractor import NodeExtractor
from dynamic_kg_extractor.models.relation_model import RelationExtractor
from dynamic_kg_extractor.visualization import KnowledgeGraphVisualizer

# 0. Configure the followings to make sure everything works
OPENAI_API_KEY = ...
NODE_DICT: dict[str, tuple[type[BaseNode], bool, str]] = {}
RELATION_DICT: dict[str, type[BaseRelation]] = {}
file_path = Path("path/to/your/pdf/file.pdf")  # Path to the PDF file

# %%
# 1. Extrac Nodes from pdf with the given NODE_DICT

node_extractor_config = NodeExtractorConfig(
    file_path=file_path,
    node_dict=NODE_DICT,
    llm_model_name=LLMOptions.OPENAI_O3_MINI,
)
extracted_nodes = NodeExtractor(config=node_extractor_config).pipeline()
# %%
# 2. Pass the extracted nodes to relation extractor
relation_extractor_config = RelationExtractorConfig(
    relation_dict=RELATION_DICT,
    llm_model_name=LLMOptions.OPENAI_O3_MINI,
)

relation_extractor = RelationExtractor(config=relation_extractor_config)
extracted_relations = relation_extractor.pipeline(extracted_nodes=extracted_nodes)
# %%
# 3. Visualize the extracted nodes and relations
vis = KnowledgeGraphVisualizer()
vis.create_visualization(nodes=extracted_nodes, relations=extracted_relations)
