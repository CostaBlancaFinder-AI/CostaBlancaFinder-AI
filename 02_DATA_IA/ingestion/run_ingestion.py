"""
============================================================
CostaBlancaFinder AI
Main Ingestion Pipeline
============================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv

from clients.apify_client import fetch_dataset_items, is_apify_configured
from clients.idealista_client import search_rentals
from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv("config/.env")


# ============================================================
# CONFIG
# ============================================================

SEARCH_LOCATION = "Costa Blanca"

APIFY_DATASET_ID = os.getenv("APIFY_DATASET_ID", "").strip()

RAW_OUTPUT_PATH = Path("02_DATA_IA/raw_data/rentals_raw.json")
CSV_OUTPUT_PATH = Path("02_DATA_IA/processed_data/rentals_clean.csv")


# ============================================================
# FETCH DATA
# ============================================================

def fetch_properties() -> tuple[list, str]:
    """
    Obtiene propiedades desde la mejor fuente disponible.
    """

    if is_apify_configured() and APIFY_DATASET_ID:
        print("\nFuente seleccionada: Apify")
        raw_properties = fetch_dataset_items(APIFY_DATASET_ID)

        if raw_properties:
            return raw_properties, "apify"

        print("Apify no devolvió datos. Se usará fallback Idealista Mock.")

    print("\nFuente seleccionada: Idealista Mock")
    raw_properties = search_rentals(SEARCH_LOCATION)

    return raw_properties, "idealista_mock"


# ============================================================
# MAIN PIPELINE
# ============================================================

def main():
    """
    Ejecuta pipeline completo de ingesta.
    """

    print("=" * 60)
    print("CostaBlancaFinder AI - Ingestion Pipeline")
    print("=" * 60)

    print(f"\nBuscando alquileres en: {SEARCH_LOCATION}")

    raw_properties, source_name = fetch_properties()

    if not raw_properties:
        print("\nNo se han obtenido propiedades.")
        return

    print(f"\nPropiedades obtenidas: {len(raw_properties)}")
    print(f"Fuente: {source_name}")

    save_json(raw_properties, RAW_OUTPUT_PATH)

    print("\nJSON bruto guardado en:")
    print(RAW_OUTPUT_PATH)

    normalized_df = normalize_properties(
        raw_properties,
        source_name=source_name
    )

    print("\nDatos normalizados correctamente.")

    save_csv(normalized_df, CSV_OUTPUT_PATH)

    print("\nCSV limpio guardado en:")
    print(CSV_OUTPUT_PATH)

    print("\nPipeline finalizado correctamente.")


# ============================================================
# ENTRYPOINT
# ============================================================

if __name__ == "__main__":
    main()