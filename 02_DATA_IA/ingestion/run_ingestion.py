"""
============================================================
CostaBlancaFinder AI
Main Ingestion Pipeline
============================================================

Flujo:
API/SCRAPER → JSON bruto → Normalización → CSV limpio
============================================================
"""

from clients.apify_client import fetch_dataset_items, is_apify_configured
from clients.idealista_client import search_rentals
from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv
from config import (
    DEFAULT_SEARCH_LOCATION,
    APIFY_DATASET_ID,
    RAW_RENTALS_JSON,
    CLEAN_RENTALS_CSV
)


def fetch_properties() -> tuple:
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

    raw_properties = search_rentals(DEFAULT_SEARCH_LOCATION)

    return raw_properties, "idealista_mock"


def main():
    """
    Ejecuta pipeline completo de ingesta.
    """

    print("=" * 60)
    print("CostaBlancaFinder AI - Ingestion Pipeline")
    print("=" * 60)

    print(f"\nBuscando alquileres en: {DEFAULT_SEARCH_LOCATION}")

    raw_properties, source_name = fetch_properties()

    if not raw_properties:
        print("\nNo se han obtenido propiedades.")
        return

    print(f"\nPropiedades obtenidas: {len(raw_properties)}")
    print(f"Fuente: {source_name}")

    save_json(raw_properties, RAW_RENTALS_JSON)

    print("\nJSON bruto guardado en:")
    print(RAW_RENTALS_JSON)

    normalized_df = normalize_properties(
        raw_properties,
        source_name=source_name
    )

    print("\nDatos normalizados correctamente.")

    save_csv(normalized_df, CLEAN_RENTALS_CSV)

    print("\nCSV limpio guardado en:")
    print(CLEAN_RENTALS_CSV)

    print("\nPipeline finalizado correctamente.")


if __name__ == "__main__":
    main()