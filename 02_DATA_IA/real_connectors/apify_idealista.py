"""
============================================================
CostaBlancaFinder AI
Apify Idealista Connector
============================================================
"""

import sys
from pathlib import Path

from apify_client import ApifyClient


ROOT_DIR = Path(__file__).resolve().parents[2]
INGESTION_DIR = ROOT_DIR / "02_DATA_IA" / "ingestion"

sys.path.append(str(INGESTION_DIR))

from config import (
    APIFY_API_TOKEN,
    APIFY_IDEALISTA_ACTOR_ID,
    DEFAULT_IDEALISTA_URL,
    DEFAULT_MAX_ITEMS
)


def is_configured() -> bool:
    """
    Comprueba si el conector tiene configuración mínima.
    """
    return bool(APIFY_API_TOKEN and APIFY_IDEALISTA_ACTOR_ID)


def fetch_idealista_properties() -> list:
    """
    Obtiene propiedades reales desde Idealista vía Apify.
    """

    print("\n[Real Connector] Apify Idealista")

    if not APIFY_API_TOKEN:
        print("APIFY_API_TOKEN no configurado.")
        return []

    if not APIFY_IDEALISTA_ACTOR_ID:
        print("APIFY_IDEALISTA_ACTOR_ID no configurado.")
        return []

    try:
        print("Conector configurado correctamente.")
        print(f"Actor ID: {APIFY_IDEALISTA_ACTOR_ID}")
        print(f"URL búsqueda: {DEFAULT_IDEALISTA_URL}")
        print(f"Máximo propiedades: {DEFAULT_MAX_ITEMS}")

        client = ApifyClient(APIFY_API_TOKEN)

        run_input = {
            "startUrls": [
                {
                    "url": DEFAULT_IDEALISTA_URL
                }
            ],
            "maxItems": DEFAULT_MAX_ITEMS
        }

        print("Ejecutando actor de Apify...")

        run = client.actor(APIFY_IDEALISTA_ACTOR_ID).call(
            run_input=run_input
        )

        dataset_id = run.get("defaultDatasetId")

        if not dataset_id:
            print("No se ha generado dataset en Apify.")
            return []

        print(f"Dataset generado: {dataset_id}")
        print("Leyendo resultados del dataset...")

        properties = list(
            client.dataset(dataset_id).iterate_items()
        )

        print(f"Propiedades obtenidas desde Apify: {len(properties)}")

        return properties

    except Exception as error:
        print("Error ejecutando conector Apify Idealista:")
        print(error)
        return []


if __name__ == "__main__":
    properties = fetch_idealista_properties()
    print(f"\nPropiedades obtenidas: {len(properties)}")

    if properties:
        print("\nPrimera propiedad:")
        print(properties[0])