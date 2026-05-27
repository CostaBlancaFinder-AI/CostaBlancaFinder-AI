"""
============================================================
CostaBlancaFinder AI
Real Source Manager
============================================================

Objetivo:
Centralizar la ejecución de conectores reales.

Fuentes previstas:
- Idealista vía Apify
- Fotocasa vía Apify
- Habitaclia vía Apify
============================================================
"""

from apify_idealista import fetch_idealista_properties
from apify_fotocasa import fetch_fotocasa_properties
from apify_habitaclia import fetch_habitaclia_properties


def attach_source(properties: list, source_name: str) -> list:
    """
    Añade source_name a cada propiedad.
    """

    enriched = []

    for item in properties:
        item_copy = item.copy()
        item_copy["source_name"] = source_name
        enriched.append(item_copy)

    return enriched


def fetch_all_real_sources() -> list:
    """
    Ejecuta todos los conectores reales disponibles.
    """

    all_properties = []

    idealista_properties = fetch_idealista_properties()
    all_properties.extend(
        attach_source(idealista_properties, "idealista_apify")
    )

    fotocasa_properties = fetch_fotocasa_properties()
    all_properties.extend(
        attach_source(fotocasa_properties, "fotocasa_apify")
    )

    habitaclia_properties = fetch_habitaclia_properties()
    all_properties.extend(
        attach_source(habitaclia_properties, "habitaclia_apify")
    )

    return all_properties


if __name__ == "__main__":
    properties = fetch_all_real_sources()
    print(f"\nTotal propiedades reales obtenidas: {len(properties)}")