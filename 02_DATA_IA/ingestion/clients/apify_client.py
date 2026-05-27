"""
============================================================
CostaBlancaFinder AI
Apify Client
============================================================

Objetivo:
Preparar la conexión con Apify para obtener datos reales
desde actores/scrapers de portales inmobiliarios.

Este cliente:
- Lee APIFY_API_TOKEN desde config/.env
- Permite comprobar si Apify está configurado
- Puede descargar items desde un dataset de Apify
- No rompe el pipeline si falta configuración
============================================================
"""

import os
import requests
from dotenv import load_dotenv


load_dotenv("config/.env")

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN", "").strip()


def is_apify_configured() -> bool:
    """
    Comprueba si existe token de Apify configurado.
    """

    return bool(APIFY_API_TOKEN)


def fetch_dataset_items(dataset_id: str) -> list:
    """
    Descarga items de un dataset de Apify.

    Parámetros:
    - dataset_id: ID del dataset generado por un actor de Apify.

    Retorna:
    - Lista de propiedades en formato JSON/dict.
    """

    if not is_apify_configured():
        print("\n[Apify Client]")
        print("APIFY_API_TOKEN no configurado.")
        return []

    if not dataset_id:
        print("\n[Apify Client]")
        print("DATASET_ID no proporcionado.")
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

        return response.json()

    except requests.exceptions.RequestException as error:
        print("\n[Apify Client]")
        print("Error al conectar con Apify:")
        print(error)
        return []


if __name__ == "__main__":
    print("Apify configurado:", is_apify_configured())