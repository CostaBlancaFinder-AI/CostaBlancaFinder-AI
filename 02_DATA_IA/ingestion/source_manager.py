"""
============================================================
CostaBlancaFinder AI
Source Manager
============================================================
"""

import sys
from pathlib import Path

from clients.idealista_client import search_rentals
from config import DEFAULT_SEARCH_LOCATION


ROOT_DIR = Path(__file__).resolve().parents[2]
REAL_CONNECTORS_DIR = ROOT_DIR / "02_DATA_IA" / "real_connectors"

sys.path.append(str(REAL_CONNECTORS_DIR))

from real_source_manager import fetch_all_real_sources


def attach_source(properties: list, source_name: str) -> list:
    """
    Añade source_name a cada propiedad.
    """

    enriched = []

    for item in properties:
        item_copy = item.copy()

        if not item_copy.get("source_name"):
            item_copy["source_name"] = source_name

        enriched.append(item_copy)

    return enriched


def fetch_from_real_sources() -> list:
    """
    Obtiene propiedades desde conectores reales.
    """

    print("\nBuscando propiedades en fuentes reales...")

    try:
        properties = fetch_all_real_sources()

        if not properties:
            print("No se recibieron propiedades reales.")
            return []

        print(f"Propiedades reales obtenidas: {len(properties)}")

        return properties

    except Exception as error:
        print("Error obteniendo fuentes reales:")
        print(error)
        return []


def fetch_from_idealista_mock() -> list:
    """
    Obtiene propiedades desde Idealista Mock.
    """

    print("\nActivando fallback MOCK...")

    properties = search_rentals(DEFAULT_SEARCH_LOCATION)

    properties = attach_source(
        properties,
        "idealista_mock"
    )

    print(f"Propiedades mock obtenidas: {len(properties)}")

    return properties


def fetch_all_properties() -> tuple:
    """
    Obtiene propiedades desde fuentes reales.
    Si no hay datos reales, usa mock como fallback.
    """

    real_properties = fetch_from_real_sources()

    if real_properties:
        print("\nFuentes reales activas.")
        all_properties = real_properties
    else:
        print("\nNo se obtuvieron datos reales.")
        print("Usando fallback Idealista Mock.")
        all_properties = fetch_from_idealista_mock()

    active_sources = sorted(
        list(
            set(
                item.get("source_name", "unknown")
                for item in all_properties
            )
        )
    )

    print(f"Fuentes activas: {active_sources}")
    print(f"Total propiedades cargadas: {len(all_properties)}")

    return all_properties, active_sources