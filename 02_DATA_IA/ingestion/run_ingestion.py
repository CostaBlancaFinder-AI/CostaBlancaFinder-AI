"""
============================================================
CostaBlancaFinder AI
Main Ingestion Pipeline
============================================================

Objetivo:
Ejecutar la ingesta automática de propiedades desde
diferentes fuentes inmobiliarias.

Flujo:

API / SCRAPER
      ↓
JSON bruto
      ↓
Normalización universal
      ↓
CSV limpio
============================================================
"""

from pathlib import Path

from clients.idealista_client import search_rentals
from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv


# ============================================================
# CONFIG
# ============================================================

SEARCH_LOCATION = "Costa Blanca"

RAW_OUTPUT_PATH = Path(
    "02_DATA_IA/raw_data/rentals_raw.json"
)

CSV_OUTPUT_PATH = Path(
    "02_DATA_IA/processed_data/rentals_clean.csv"
)


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

    # ========================================================
    # FETCH RAW DATA
    # ========================================================

    raw_properties = search_rentals(SEARCH_LOCATION)

    if not raw_properties:
        print("\nNo se han obtenido propiedades.")
        return

    print(f"\nPropiedades obtenidas: {len(raw_properties)}")

    # ========================================================
    # SAVE RAW JSON
    # ========================================================

    save_json(
        raw_properties,
        RAW_OUTPUT_PATH
    )

    print(f"\nJSON bruto guardado en:")
    print(RAW_OUTPUT_PATH)

    # ========================================================
    # NORMALIZE DATA
    # ========================================================

    normalized_df = normalize_properties(
        raw_properties,
        source_name="idealista"
    )

    print("\nDatos normalizados correctamente.")

    # ========================================================
    # SAVE CLEAN CSV
    # ========================================================

    save_csv(
        normalized_df,
        CSV_OUTPUT_PATH
    )

    print(f"\nCSV limpio guardado en:")
    print(CSV_OUTPUT_PATH)

    print("\nPipeline finalizado correctamente.")


# ============================================================
# ENTRYPOINT
# ============================================================

if __name__ == "__main__":
    main()