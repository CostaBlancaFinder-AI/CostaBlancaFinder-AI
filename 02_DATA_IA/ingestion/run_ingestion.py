"""
============================================================
CostaBlancaFinder AI
Main Ingestion Pipeline
============================================================

Flujo:
Multi-source ingestion
→ JSON bruto
→ Normalización universal
→ Deduplicación básica
→ CSV limpio
============================================================
"""

from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv
from source_manager import fetch_all_properties
from deduplicate import deduplicate_properties
from config import (
    DEFAULT_SEARCH_LOCATION,
    RAW_RENTALS_JSON,
    CLEAN_RENTALS_CSV
)


def main():
    """
    Ejecuta pipeline completo de ingesta multifuente.
    """

    print("=" * 60)
    print("CostaBlancaFinder AI - Multi-Source Ingestion Pipeline")
    print("=" * 60)

    print(f"\nBuscando alquileres en: {DEFAULT_SEARCH_LOCATION}")

    # ========================================================
    # FETCH RAW DATA FROM ALL SOURCES
    # ========================================================

    raw_properties, active_sources = fetch_all_properties()

    if not raw_properties:
        print("\nNo se han obtenido propiedades.")
        return

    print(f"\nPropiedades obtenidas: {len(raw_properties)}")
    print(f"Fuentes activas: {active_sources}")

    # ========================================================
    # SAVE RAW JSON
    # ========================================================

    save_json(
        raw_properties,
        RAW_RENTALS_JSON
    )

    print("\nJSON bruto guardado en:")
    print(RAW_RENTALS_JSON)

    # ========================================================
    # NORMALIZE DATA
    # ========================================================

    normalized_df = normalize_properties(
        raw_properties,
        source_name="+".join(active_sources)
    )

    print("\nDatos normalizados correctamente.")
    print(f"Registros normalizados: {len(normalized_df)}")

    # ========================================================
    # DEDUPLICATE DATA
    # ========================================================

    deduplicated_df = deduplicate_properties(
        normalized_df
    )

    print("\nDuplicados eliminados correctamente.")
    print(f"Registros finales: {len(deduplicated_df)}")

    # ========================================================
    # SAVE CLEAN CSV
    # ========================================================

    save_csv(
        deduplicated_df,
        CLEAN_RENTALS_CSV
    )

    print("\nCSV limpio guardado en:")
    print(CLEAN_RENTALS_CSV)

    print("\nPipeline multifuente finalizado correctamente.")


if __name__ == "__main__":
    main()