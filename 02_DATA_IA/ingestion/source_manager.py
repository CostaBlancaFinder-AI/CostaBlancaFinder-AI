"""
============================================================
CostaBlancaFinder AI
Source Manager
============================================================
"""

from clients.apify_client import fetch_dataset_items, is_apify_configured
from clients.idealista_client import search_rentals
from config import APIFY_DATASET_ID, DEFAULT_SEARCH_LOCATION


def attach_source(properties: list, source_name: str) -> list:
    """
    Añade el nombre de la fuente a cada propiedad.
    """

    enriched = []

    for item in properties:
        item_copy = item.copy()
        item_copy["source_name"] = source_name
        enriched.append(item_copy)

    return enriched


def fetch_from_apify() -> list:
    """
    Obtiene propiedades desde Apify.
    """

    if not is_apify_configured():
        return []

    if not APIFY_DATASET_ID:
        return []

    properties = fetch_dataset_items(APIFY_DATASET_ID)

    return attach_source(properties, "apify")


def fetch_from_idealista() -> list:
    """
    Obtiene propiedades desde Idealista Mock/API.
    """

    properties = search_rentals(DEFAULT_SEARCH_LOCATION)

    return attach_source(properties, "idealista_mock")


def fetch_all_properties() -> tuple:
    """
    Obtiene propiedades desde todas las fuentes disponibles.
    """

    all_properties = []

    sources = [
        fetch_from_apify,
        fetch_from_idealista
    ]

    for source_fetcher in sources:
        properties = source_fetcher()

        if properties:
            all_properties.extend(properties)

    active_sources = sorted(
        list(set(
            item.get("source_name", "unknown")
            for item in all_properties
        ))
    )

    return all_properties, active_sources