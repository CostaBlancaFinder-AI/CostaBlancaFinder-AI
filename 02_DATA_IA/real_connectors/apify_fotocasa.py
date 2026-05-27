"""
============================================================
CostaBlancaFinder AI
Apify Fotocasa Connector
============================================================

Objetivo:
Preparar el conector real para obtener propiedades de
Fotocasa mediante Apify.
============================================================
"""

import sys
from pathlib import Path

import requests


ROOT_DIR = Path(__file__).resolve().parents[2]
INGESTION_DIR = ROOT_DIR / "02_DATA_IA" / "ingestion"

sys.path.append(str(INGESTION_DIR))

from config import (
    APIFY_API_TOKEN,
    APIFY_FOTOCASA_ACTOR_ID
)


def is_configured() -> bool:
    """
    Comprueba si el conector tiene configuración mínima.
    """

    return bool(
        APIFY_API_TOKEN and
        APIFY_FOTOCASA_ACTOR_ID
    )


def fetch_fotocasa_properties() -> list:
    """
    Obtiene propiedades reales desde Fotocasa vía Apify.

    Si no hay configuración real, devuelve lista vacía.
    """

    print("\n[Real Connector] Apify Fotocasa")

    if not APIFY_API_TOKEN:
        print("APIFY_API_TOKEN no configurado.")
        return []

    if not APIFY_FOTOCASA_ACTOR_ID:
        print("APIFY_FOTOCASA_ACTOR_ID no configurado.")
        return []

    print("Conector configurado correctamente.")
    print("Ejecución real del actor pendiente de implementar.")

    return []


if __name__ == "__main__":
    properties = fetch_fotocasa_properties()
    print(f"Propiedades obtenidas: {len(properties)}")