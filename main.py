# %%

from pathlib import Path

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation

from dynamic_kg_extractor.example_ontology.nodes import NODE_DICT
from dynamic_kg_extractor.example_ontology.relations import RELATION_DICT
from dynamic_kg_extractor.models.configurations import LLMOptions, NodeExtractorConfig, RelationExtractorConfig
from dynamic_kg_extractor.models.node_extractor import NodeExtractor
from dynamic_kg_extractor.models.relation_model import RelationExtractor
from dynamic_kg_extractor.visualization import KnowledgeGraphVisualizer

# %%
#! 0. Configure the followings to make sure everything works
OPENAI_API_KEY = "create .env folder and read it"
file_path = Path("data/short.pdf")  # Path to the PDF file
node_dict: dict[str, tuple[type[BaseNode], bool, str]] = NODE_DICT
relation_dict: dict[str, type[BaseRelation]] = RELATION_DICT
# %%
#! 1. Extract Nodes from pdf with the given NODE_DICT
node_extractor = NodeExtractor(config=NodeExtractorConfig(file_path=file_path, node_dict=node_dict, llm_model_name=LLMOptions.OPENAI_O3_MINI))
extracted_nodes = node_extractor.pipeline()
# %%
#! 2. Pass the extracted nodes to relation extractor
relation_extractor = RelationExtractor(config=RelationExtractorConfig(relation_dict=relation_dict, llm_model_name=LLMOptions.OPENAI_O3_MINI))
extracted_relations = relation_extractor.pipeline(extracted_nodes=extracted_nodes)
# %%
#! 3. Visualize the extracted nodes and relations
vis = KnowledgeGraphVisualizer()
vis.create_visualization(nodes=extracted_nodes, relations=extracted_relations)
# %%
