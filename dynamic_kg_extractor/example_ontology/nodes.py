from typing import Literal

from base_ontology.node import BaseNode
from pydantic import Field, create_model

SözleşmeNode = create_model(
    "SözleşmeNode",
    başlık=(str | None, Field(default=None, description="Sözleşme başlığı, ilk sayfada bulunur")),
    tür=(str | None, Field(default=None, description="Sözleşme türü (örneğin: kira sözleşmesi, satış sözleşmesi)")),
    amaç=(str | None, Field(default=None, description="Sözleşmenin amacı")),
    bağlı_olduğu_kanun=(str | None, Field(default=None, description="Sözleşmenin bağlı olduğu kanun")),
    bağlı_olduğu_yönetmelik=(str | None, Field(default=None, description="Sözleşmenin bağlı olduğu yönetmelik")),
    bağlı_olduğu_yönerge=(str | None, Field(default=None, description="Sözleşmenin bağlı olduğu yönerge")),
    __base__=BaseNode,
)

KiraSüresiNode = create_model(
    "KiraSüresiNode",
    başlangıç_tarihi=(str | None, Field(default=str, description="Kira sözleşmesinin başlangıç tarihi (format: YYYY-MM-DD)")),
    kira_süresi=(int | None, Field(default=None, description="Kira süresi (ay cinsinden), x ay şeklinde yaz")),
    bitiş_tarihi=(str | None, Field(default=None, description="Kira sözleşmesinin bitiş tarihi (format: YYYY-MM-DD), başlangıç tarihi ve kira süresi verilmişse bu alan otomatik hesaplanır")),
    erken_bitebilir=(bool | None, Field(default=None, description="Kira sözleşmesi normal bitiş tarihinden farklılık gösterebilir mi?")),
    erken_bitebilir_açıklaması=(str | None, Field(default=None, description="Kira sözleşmesinin bitiş tarihi değişiklik gösterebilir ise açıklaması")),
    __base__=BaseNode,
)


TarafNode = create_model(
    "TarafNode",
    ad=(str | None, Field(default=None, description="Tarafın adı")),
    ünvan=(str | None, Field(default=None, description="Tarafın unvanı")),
    vergi_no=(str | None, Field(default=None, description="Tarafın vergi numarası")),
    mersis_no=(str | None, Field(default=None, description="Tarafın mersis numarası (mersis no)")),
    vkkn=(str | None, Field(default=None, description="Tarafın VKKN numarası")),
    tc_kimlik=(str | None, Field(default=None, description="Tarafın TC kimlik numarası")),
    adres=(str | None, Field(default=None, description="Tarafın adresi")),
    telefon=(str | None, Field(default=None, description="Tarafın telefon numarası")),
    e_posta=(str | None, Field(default=None, description="Tarafın e-posta adresi")),
    __base__=BaseNode,
)

KiracıNode = create_model("KiracıNode", __base__=TarafNode)
KirayaVerenNode = create_model("KirayaVerenNode", __base__=TarafNode)
KefilNode = create_model("KefilNode", __base__=TarafNode)

TaşınmazNode = create_model(
    "TaşınmazNode",
    adres=(str | None, Field(default=None, description="Kiralanan taşınmazın tam adresi")),
    şehir=(str | None, Field(default=None, description="Kiralanan taşınmazın bulunduğu şehir")),
    metrekare=(float | None, Field(default=None, description="Kiralanan taşınmazın büyüklüğü (m² cinsinden)")),
    tip=(str | None, Field(default=None, description="Taşınmaz türü (örneğin: daire, ofis, depo)")),
    kullanım_amacı=(str | None, Field(default=None, description="Taşınmazın kullanım amacı (örneğin: konut, ticari)")),
    __base__=BaseNode,
)

FinansalUnsurNode = create_model(
    "FinansalUnsurNode",
    type=(Literal["KiraBedeli", "DepozitoBedeli", "AidatBedeli", "Fatura", "Diğer"] | None, Field(default=None, description="Finansal unsur türü")),
    ödemesi_kime_ait=(Literal["Kiracı", "KirayaVeren", "Ortak", "Diğer"] | None, Field(default=None, description="Finansal unsur kimin tarafından ödenecek?")),
    açıklama=(str | None, Field(default=None, description="Finansal unsur açıklaması")),
    miktar=(float | None, Field(default=None, description="Finansal unsur miktarı")),
    birim=(str | None, Field(default=None, description="Finansal unsur miktarının birimi (örneğin: TL, USD)")),
    ödeme_sıklığı=(str | None, Field(default=None, description="Finansal unsur ödeme sıklığı (örneğin: aylık, yıllık)")),
    temerrüt_hali=(str | None, Field(default=None, description="Finansal unsurun temerrüde düşülmesi durumunda uygulanacak hükümler")),
    __base__=BaseNode,
)

TeminatMaddesiNode = create_model(
    "TeminatMaddesiNode",
    teminat_türü=(str | None, Field(default=None, description="Teminat türü")),
    teminat_miktarı=(float | None, Field(default=None, description="Teminat miktarı")),
    teminat_birim=(str | None, Field(default=None, description="Teminat miktarının birimi")),
    teminat_iadesi=(str | None, Field(default=None, description="Teminatın iadesi ile ilgili hükümle nelerdir?")),
    __base__=BaseNode,
)

FesihMaddesiNode = create_model(
    "FesihMaddesiNode",
    fesih_koşulları=(str | None, Field(default=None, description="Fesih koşulları nelerdir? Ne durumlarda sözleşme fesih edilebilir?")),
    fesih_ihbar_süresi=(str | None, Field(default=None, description="Fesih ihbar süresi ne kadar?")),
    temmerüt_hali=(str | None, Field(default=None, description="Fesih temerrüdü ne durumlarda gerçekleşir?")),
    __base__=BaseNode,
)


NODE_DICT = {
    SözleşmeNode.__name__: (SözleşmeNode, False, "sözleşme node"),
    KiraSüresiNode.__name__: (KiraSüresiNode, False, "kira süresi node"),
    KiracıNode.__name__: (KiracıNode, True, "kiracı nodes"),
    KirayaVerenNode.__name__: (KirayaVerenNode, False, "kiraya_veren"),
    KefilNode.__name__: (KefilNode, True, "kefil nodes"),
    TaşınmazNode.__name__: (TaşınmazNode, False, "taşınmaz node"),
    FinansalUnsurNode.__name__: (FinansalUnsurNode, True, "finansal unsur nodes"),
    TeminatMaddesiNode.__name__: (TeminatMaddesiNode, True, "teminat maddesi nodes"),
    FesihMaddesiNode.__name__: (FesihMaddesiNode, True, "fesih maddesi nodes"),
}
