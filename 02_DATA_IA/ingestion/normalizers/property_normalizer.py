"""
============================================================
CostaBlancaFinder AI
Universal Property Normalizer
============================================================

Objetivo:
Convertir propiedades procedentes de diferentes fuentes
inmobiliarias al formato estándar del proyecto.

Fuentes previstas:
- Idealista
- Fotocasa
- Habitaclia
- Properstar
- Apify
- Otros agregadores
============================================================
"""

import pandas as pd


STANDARD_COLUMNS = [
    "title",
    "city",
    "zone",
    "price_eur",
    "area_m2",
    "rooms",
    "bathrooms",
    "property_type",
    "source_url",
    "source_name"
]


def get_first_available(item: dict, possible_keys: list):
    """
    Devuelve el primer valor disponible dentro de una lista
    de posibles nombres de campo.
    """

    for key in possible_keys:
        value = item.get(key)

        if value not in [None, ""]:
            return value

    return None


def normalize_property(item: dict, source_name: str) -> dict:
    """
    Normaliza una única propiedad.
    """

    return {
        "title": get_first_available(
            item,
            ["title", "name", "headline"]
        ),
        "city": get_first_available(
            item,
            ["city", "municipality", "location"]
        ),
        "zone": get_first_available(
            item,
            ["zone", "district", "neighborhood", "areaName"]
        ),
        "price_eur": get_first_available(
            item,
            ["price_eur", "price", "rent_price", "monthlyPrice"]
        ),
        "area_m2": get_first_available(
            item,
            ["area_m2", "size", "area", "surface", "m2"]
        ),
        "rooms": get_first_available(
            item,
            ["rooms", "bedrooms", "numRooms"]
        ),
        "bathrooms": get_first_available(
            item,
            ["bathrooms", "bathroomsNumber", "numBathrooms"]
        ),
        "property_type": get_first_available(
            item,
            ["property_type", "propertyType", "type", "typology"]
        ),
        "source_url": get_first_available(
            item,
            ["source_url", "url", "detailUrl", "link"]
        ),
        "source_name": item.get("source_name", source_name)
    }


def normalize_properties(raw_properties: list, source_name: str) -> pd.DataFrame:
    """
    Normaliza una lista de propiedades al formato estándar.
    """

    normalized = []

    for item in raw_properties:
        normalized.append(
            normalize_property(
                item=item,
                source_name=source_name
            )
        )

    return pd.DataFrame(
        normalized,
        columns=STANDARD_COLUMNS
    )