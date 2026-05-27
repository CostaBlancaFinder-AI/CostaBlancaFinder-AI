"""
============================================================
CostaBlancaFinder AI
Apify Client
============================================================

Objetivo:
Cliente de conexión con Apify para obtener datos reales
desde datasets generados por actores/scrapers.

Estado actual:
- Preparado para API real de Apify.
- No rompe el pipeline si falta token o dataset.
============================================================
"""

import requests

from config import APIFY_API_TOKEN


def is_apify_configured() -> bool:
    """
    Comprueba si existe token de Apify configurado.
    """

    return bool(APIFY_API_TOKEN)


def fetch_dataset_items(dataset_id: str) -> list:
    """
    Descarga items de un dataset de Apify.
    """

    print("\n[Apify Client]")

    if not is_apify_configured():
        print("APIFY_API_TOKEN no configurado.")
        return []

    if not dataset_id:
        print("APIFY_DATASET_ID no proporcionado.")
        return []

    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"

    params = {
        "token": APIFY_API_TOKEN,
        "clean": "true",
        "format": "json"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        items = response.json()

        print(f"Items obtenidos desde Apify: {len(items)}")

        return items

    except requests.exceptions.RequestException as error:
        print("Error al conectar con Apify:")
        print(error)
        return []


if __name__ == "__main__":
    print("Apify configurado:", is_apify_configured())