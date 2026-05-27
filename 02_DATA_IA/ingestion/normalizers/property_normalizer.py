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
            "title": item.get("title"),
            "city": item.get("city"),
            "zone": item.get("zone"),
            "price_eur": item.get("price_eur"),
            "area_m2": item.get("area_m2"),
            "rooms": item.get("rooms"),
            "bathrooms": item.get("bathrooms"),
            "property_type": item.get("property_type"),
            "source_url": item.get("source_url"),
            "source_name": source_name
        })

    return pd.DataFrame(normalized, columns=STANDARD_COLUMNS)