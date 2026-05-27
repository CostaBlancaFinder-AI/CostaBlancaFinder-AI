"""
============================================================
CostaBlancaFinder AI
Universal Property Normalizer
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


def normalize_properties(raw_properties: list, source_name: str) -> pd.DataFrame:
    """
    Normaliza propiedades de cualquier fuente al formato estándar.
    """

    normalized = []

    for item in raw_properties:
        normalized.append({
            "title": item.get("title") or item.get("name"),
            "city": item.get("city") or item.get("municipality"),
            "zone": item.get("zone") or item.get("district") or item.get("neighborhood"),
            "price_eur": item.get("price_eur") or item.get("price"),
            "area_m2": item.get("area_m2") or item.get("size") or item.get("area"),
            "rooms": item.get("rooms") or item.get("bedrooms"),
            "bathrooms": item.get("bathrooms"),
            "property_type": item.get("property_type") or item.get("propertyType") or item.get("type"),
            "source_url": item.get("source_url") or item.get("url"),
            "source_name": source_name
        })

    return pd.DataFrame(normalized, columns=STANDARD_COLUMNS)