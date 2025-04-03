from dataclasses import dataclass
from itertools import product
from typing import Any

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from dynamic_kg_extractor.models.configurations import RelationExtractorConfig


class HasRelation(BaseModel):
    value: bool = Field(default=False, description="Bu iki node arasında bir ilişki var mı?")
    reason: str | None = Field(default=None, description="Bu kararı vermenizin sebebi nedir?")
    attributes: dict[str, Any] = Field(default_factory=lambda: {}, description="Bu ilişkinin özellikleri")


@dataclass
class ChainInputforRelation:
    input_text: str
    source_node: BaseNode
    target_node: BaseNode
    candidate_relation: str | None = Field(default=None, description="İlişki adayı")


class RelationExtractor:
    def __init__(self, config: RelationExtractorConfig) -> None:
        self.config = config

        self.llm = ChatOpenAI(model=config.llm_model_name.value)

        self.has_relation_parser = PydanticOutputParser(pydantic_object=HasRelation)

        self.prompt_template = self._create_prompt()
        self.chain = self.prompt_template | self.llm

    def pipeline(self, extracted_nodes: list[BaseNode]) -> list[BaseRelation]:
        extracted_relations: list[BaseRelation] = []

        for _, relation_class in self.config.relation_dict.items():
            source_nodes, target_nodes = self._filter_nodes_by_class(extracted_nodes, relation_class)
            if not source_nodes or not target_nodes:
                continue
            else:
                self._process_relation(source_nodes, target_nodes, relation_class, extracted_relations)
        return extracted_relations

    def _filter_nodes_by_class(self, extracted_nodes: list[BaseNode], relation_class: type[BaseRelation]) -> tuple[list[BaseNode], list[BaseNode]]:
        source_class_name = relation_class.model_fields["source_node"].annotation.__name__
        target_class_name = relation_class.model_fields["target_node"].annotation.__name__
        source_nodes = [node for node in extracted_nodes if node.__class__.__name__ == source_class_name]
        target_nodes = [node for node in extracted_nodes if node.__class__.__name__ == target_class_name]
        return source_nodes, target_nodes

    def _process_relation(self, source_nodes: list[BaseNode], target_nodes: list[BaseNode], relation_class: type[BaseRelation], found_relations: list[BaseRelation]) -> None:
        source_class_name = relation_class.model_fields["source_node"].annotation.__name__
        target_class_name = relation_class.model_fields["target_node"].annotation.__name__
        print(f"There are total of {len(source_nodes)} {source_class_name} and {len(target_nodes)} {target_class_name} nodes.")
        print(f"Trying for the relation: {source_class_name} -> {relation_class.__name__} -> {target_class_name}")
        for source_node, target_node in product(source_nodes, target_nodes):
            has_relation = self._check_relation(source_node, target_node, relation_class.__name__)
            if has_relation.value:
                print(f"Relation found between {source_class_name} and {target_class_name} with the relation {relation_class.__name__}")
                found_relations.append(
                    relation_class(
                        source_node=source_node,
                        target_node=target_node,
                        attributes=has_relation.attributes,
                        reason=has_relation.reason,
                    )
                )
        print("******************", end="\n\n")

    def _check_relation(self, source_node: BaseNode, target_node: BaseNode, candidate_relation: str) -> HasRelation:
        chain_input = ChainInputforRelation(
            input_text=" ".join([source_node.reference_text, target_node.reference_text]),
            source_node=source_node,
            target_node=target_node,
            candidate_relation=candidate_relation,
        )
        content = str(self.chain.invoke(input=chain_input.__dict__).content)
        has_relation_pydantic_instance = self.has_relation_parser.parse(content)
        return has_relation_pydantic_instance

    def _create_prompt(self) -> PromptTemplate:
        template = """
            Aşağıda yer alan iki node arasında candidate olarak verilen ilişki var mıdır? Texte bakarak karar veriniz:
            Text: {input_text}
            target_node: {target_node}
            source_node: {source_node}
            candidate relation: {candidate_relation}
            {format_instructions}
        """
        return PromptTemplate(
            template=template,
            input_variables=["input_text", "target_node", "source_node", "candidate_relation"],
            partial_variables={"format_instructions": self.has_relation_parser.get_format_instructions()},
        )
