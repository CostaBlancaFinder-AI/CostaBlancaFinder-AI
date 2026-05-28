"""
============================================================
CostaBlancaFinder AI
Source Manager
============================================================
"""

import sys
import json
from pathlib import Path

from clients.idealista_client import search_rentals
from config import (
    DEFAULT_SEARCH_LOCATION,
    RAW_RENTALS_JSON
)


ROOT_DIR = Path(__file__).resolve().parents[2]
REAL_CONNECTORS_DIR = ROOT_DIR / "02_DATA_IA" / "real_connectors"

sys.path.append(str(REAL_CONNECTORS_DIR))

from real_source_manager import fetch_all_real_sources


def attach_source(properties: list, source_name: str) -> list:
    enriched = []

    for item in properties:
        item_copy = item.copy()

        if not item_copy.get("source_name"):
            item_copy["source_name"] = source_name

        enriched.append(item_copy)

    return enriched


def fetch_from_real_sources() -> list:
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


def fetch_from_cached_real_json() -> list:
    """
    Usa el último rentals_raw.json real guardado si Apify falla.
    """

    print("\nBuscando fallback con JSON real guardado...")

    if not RAW_RENTALS_JSON.exists():
        print("No existe rentals_raw.json previo.")
        return []

    try:
        with open(RAW_RENTALS_JSON, "r", encoding="utf-8") as file:
            properties = json.load(file)

        if not properties:
            print("El JSON previo está vacío.")
            return []

        source_names = {
            item.get("source_name", "")
            for item in properties
        }

        if "idealista_mock" in source_names:
            print("El JSON previo es MOCK. No se usará como real.")
            return []

        print(
            f"Fallback real cargado desde JSON: "
            f"{len(properties)} propiedades"
        )

        return properties

    except Exception as error:
        print("Error leyendo JSON real guardado:")
        print(error)
        return []


def fetch_from_idealista_mock() -> list:
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
    Prioridad:
    1. Fuentes reales Apify/API
    2. JSON real guardado anterior
    3. Mock
    """

    real_properties = fetch_from_real_sources()

    if real_properties:
        print("\nFuentes reales activas.")
        all_properties = real_properties

    else:
        cached_properties = fetch_from_cached_real_json()

        if cached_properties:
            print("\nUsando fallback con datos reales guardados.")
            all_properties = cached_properties

        else:
            print("\nNo se obtuvieron datos reales ni cache real.")
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