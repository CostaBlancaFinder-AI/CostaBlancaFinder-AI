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
→ Filtros automáticos
→ Scoring de oportunidad
→ CSV limpio
→ Top oportunidades
============================================================
"""

from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv
from source_manager import fetch_all_properties
from deduplicate import deduplicate_properties
from filter_properties import filter_properties
from score_properties import score_properties
from export_opportunities import export_top_opportunities
from config import (
    DEFAULT_SEARCH_LOCATION,
    RAW_RENTALS_JSON,
    CLEAN_RENTALS_CSV,
    TOP_OPPORTUNITIES_CSV
)


def main():
    """
    Ejecuta pipeline completo de ingesta multifuente.
    """

    print("=" * 60)
    print("CostaBlancaFinder AI - Multi-Source Ingestion Pipeline")
    print("=" * 60)

    print(f"\nBuscando alquileres en: {DEFAULT_SEARCH_LOCATION}")

    raw_properties, active_sources = fetch_all_properties()

    if not raw_properties:
        print("\nNo se han obtenido propiedades.")
        return

    print(f"\nPropiedades obtenidas: {len(raw_properties)}")
    print(f"Fuentes activas: {active_sources}")

    save_json(
        raw_properties,
        RAW_RENTALS_JSON
    )

    print("\nJSON bruto guardado en:")
    print(RAW_RENTALS_JSON)

    normalized_df = normalize_properties(
        raw_properties,
        source_name="+".join(active_sources)
    )

    print("\nDatos normalizados correctamente.")
    print(f"Registros normalizados: {len(normalized_df)}")

    deduplicated_df = deduplicate_properties(
        normalized_df
    )

    print("\nDuplicados eliminados correctamente.")
    print(f"Registros tras deduplicación: {len(deduplicated_df)}")

    filtered_df = filter_properties(
        deduplicated_df,
        min_price=600,
        max_price=1500,
        min_rooms=1,
        min_area=40
    )

    print("\nFiltros aplicados correctamente.")
    print(f"Registros finales filtrados: {len(filtered_df)}")

    scored_df = score_properties(
        filtered_df
    )

    print("\nScoring aplicado correctamente.")
    print(f"Registros con scoring: {len(scored_df)}")

    save_csv(
        scored_df,
        CLEAN_RENTALS_CSV
    )

    print("\nCSV limpio con scoring guardado en:")
    print(CLEAN_RENTALS_CSV)

    export_top_opportunities(
        scored_df,
        TOP_OPPORTUNITIES_CSV,
        top_n=10
    )

    print("\nPipeline multifuente finalizado correctamente.")


if __name__ == "__main__":
    main()