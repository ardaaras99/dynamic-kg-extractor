from base_ontology.relation import BaseRelation
from pydantic import Field, create_model

from dynamic_kg_extractor.example_ontology.nodes import FesihMaddesiNode, FinansalUnsurNode, KefilNode, KiracıNode, KiraSüresiNode, KirayaVerenNode, SözleşmeNode, TaşınmazNode, TeminatMaddesiNode

KiracıTarafıVardır = create_model(
    "KiracıTarafıVardır",
    label=(str, Field(default="KiracıTarafıVardır")),
    source_node=(SözleşmeNode, ...),
    target_node=(KiracıNode, ...),
    __base__=BaseRelation,
)

KirayaVerenTarafıVardır = create_model(
    "KirayaVerenTarafıVardır",
    label=(str, Field(default="KirayaVerenTarafıVardır")),
    source_node=(SözleşmeNode, ...),
    target_node=(KirayaVerenNode, ...),
    __base__=BaseRelation,
)

KefilTarafıVardır = create_model(
    "KefilTarafıVardır",
    label=(str, Field(default="KefilTarafıVardır")),
    source_node=(SözleşmeNode, ...),
    target_node=(KefilNode, ...),
    __base__=BaseRelation,
)

FinansalUnsuraSahiptir = create_model(
    "FinansalUnsuraSahiptir",
    label=(str, Field(default="FinansalUnsuraSahiptir")),
    source_node=(SözleşmeNode, ...),
    target_node=(FinansalUnsurNode, ...),
    __base__=BaseRelation,
)

SüreyeSahiptir = create_model(
    "SüreyeSahiptir",
    label=(str, Field(default="SüreyeSahiptir")),
    source_node=(SözleşmeNode, ...),
    target_node=(KiraSüresiNode, ...),
    __base__=BaseRelation,
)

FesihMaddesineSahiptir = create_model(
    "FesihMaddesineSahiptir",
    label=(str, Field(default="FesihMaddesineSahiptir")),
    source_node=(SözleşmeNode, ...),
    target_node=(FesihMaddesiNode, ...),
    __base__=BaseRelation,
)

TeminatMaddesineSahiptir = create_model(
    "TeminatMaddesineSahiptir",
    label=(str, Field(default="TeminatMaddesineSahiptir")),
    source_node=(SözleşmeNode, ...),
    target_node=(TeminatMaddesiNode, ...),
    __base__=BaseRelation,
)
SüresiniEtkiler = create_model(
    "SüresiniEtkiler",
    label=(str, Field(default="SüresiniEtkiler")),
    source_node=(FesihMaddesiNode, ...),
    target_node=(KiraSüresiNode, ...),
    __base__=BaseRelation,
)

KiracıÖdemekleYükümlüdür = create_model(
    "KiracıÖdemekleYükümlüdür",
    label=(str, Field(default="KiracıÖdemekleYükümlüdür")),
    source_node=(KiracıNode, ...),
    target_node=(FinansalUnsurNode, ...),
    __base__=BaseRelation,
)

KiracıTaşınmazıKullanır = create_model(
    "KiracıTaşınmazıKullanır",
    label=(str, Field(default="KiracıTaşınmazıKullanır")),
    source_node=(KiracıNode, ...),
    target_node=(TaşınmazNode, ...),
    __base__=BaseRelation,
)

RELATION_DICT = {
    KiracıTarafıVardır.__name__: KiracıTarafıVardır,
    KirayaVerenTarafıVardır.__name__: KirayaVerenTarafıVardır,
    KefilTarafıVardır.__name__: KefilTarafıVardır,
    FinansalUnsuraSahiptir.__name__: FinansalUnsuraSahiptir,
    SüreyeSahiptir.__name__: SüreyeSahiptir,
    FesihMaddesineSahiptir.__name__: FesihMaddesineSahiptir,
    TeminatMaddesineSahiptir.__name__: TeminatMaddesineSahiptir,
    SüresiniEtkiler.__name__: SüresiniEtkiler,
    KiracıÖdemekleYükümlüdür.__name__: KiracıÖdemekleYükümlüdür,
    KiracıTaşınmazıKullanır.__name__: KiracıTaşınmazıKullanır,
}
