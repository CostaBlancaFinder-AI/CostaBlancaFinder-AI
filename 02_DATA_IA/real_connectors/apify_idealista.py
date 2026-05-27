"""
============================================================
CostaBlancaFinder AI
Apify Idealista Connector
============================================================

Objetivo:
Preparar el conector real para obtener propiedades de
Idealista mediante Apify.

Estado actual:
- Estructura preparada.
- No lanza todavía actores automáticamente.
- Lee configuración desde ingestion/config.py.
- Devuelve lista vacía si no hay configuración real.
============================================================
"""

import sys
from pathlib import Path

import requests


ROOT_DIR = Path(__file__).resolve().parents[2]
INGESTION_DIR = ROOT_DIR / "02_DATA_IA" / "ingestion"

sys.path.append(str(INGESTION_DIR))

from config import APIFY_API_TOKEN


APIFY_IDEALISTA_ACTOR_ID = ""


def is_configured() -> bool:
    """
    Comprueba si el conector tiene configuración mínima.
    """

    return bool(APIFY_API_TOKEN and APIFY_IDEALISTA_ACTOR_ID)


def fetch_idealista_properties() -> list:
    """
    Obtiene propiedades reales desde Idealista vía Apify.

    En esta primera versión, si no hay actor configurado,
    devuelve lista vacía sin romper el sistema.
    """

    print("\n[Real Connector] Apify Idealista")

    if not APIFY_API_TOKEN:
        print("APIFY_API_TOKEN no configurado.")
        return []

    if not APIFY_IDEALISTA_ACTOR_ID:
        print("APIFY_IDEALISTA_ACTOR_ID no configurado todavía.")
        return []

    print("Conector preparado, pero ejecución de actor pendiente.")

    return []


if __name__ == "__main__":
    properties = fetch_idealista_properties()
    print(f"Propiedades obtenidas: {len(properties)}")