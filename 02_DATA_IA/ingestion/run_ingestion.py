"""
============================================================
CostaBlancaFinder AI
Main Ingestion Pipeline
============================================================
"""

from normalizers.property_normalizer import normalize_properties
from save_outputs import save_json, save_csv
from source_manager import fetch_all_properties
from deduplicate import deduplicate_properties
from filter_properties import filter_properties
from score_properties import score_properties
from export_opportunities import export_top_opportunities
from export_summary import export_executive_summary

from config import (
    DEFAULT_SEARCH_LOCATION,
    RAW_RENTALS_JSON,
    CLEAN_RENTALS_CSV,
    TOP_OPPORTUNITIES_CSV,
    EXECUTIVE_SUMMARY_MD
)


def main():

    print("=" * 60)
    print("CostaBlancaFinder AI - Multi-Source Ingestion Pipeline")
    print("=" * 60)

    print(f"\nBuscando alquileres en: {DEFAULT_SEARCH_LOCATION}")

    # ========================================================
    # FETCH PROPERTIES
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

    save_json(raw_properties, RAW_RENTALS_JSON)

    print("\nJSON bruto guardado en:")
    print(RAW_RENTALS_JSON)

    # ========================================================
    # NORMALIZATION
    # ========================================================

    normalized_df = normalize_properties(
        raw_properties,
        source_name="+".join(active_sources)
    )

    print("\nDatos normalizados correctamente.")
    print(f"Registros normalizados: {len(normalized_df)}")

    if normalized_df.empty:
        print("\nERROR: DataFrame normalizado vacío.")
        return

    # ========================================================
    # DEDUPLICATION
    # ========================================================

    deduplicated_df = deduplicate_properties(
        normalized_df
    )

    print("\nDuplicados eliminados correctamente.")
    print(
        f"Registros tras deduplicación: "
        f"{len(deduplicated_df)}"
    )

    if deduplicated_df.empty:
        print("\nERROR: DataFrame vacío tras deduplicación.")
        return

    # ========================================================
    # FILTERS
    # ========================================================

    filtered_df = filter_properties(
        deduplicated_df,
        min_price=600,
        max_price=1500,
        min_rooms=1,
        min_area=40
    )

    print("\nFiltros aplicados correctamente.")
    print(
        f"Registros finales filtrados: "
        f"{len(filtered_df)}"
    )

    if filtered_df.empty:
        print("\nWARNING: No quedan propiedades tras filtros.")
        return

    # ========================================================
    # SCORING
    # ========================================================

    scored_df = score_properties(filtered_df)

    print("\nScoring aplicado correctamente.")
    print(
        f"Registros con scoring: "
        f"{len(scored_df)}"
    )

    if scored_df.empty:
        print("\nERROR: DataFrame vacío tras scoring.")
        return

    # ========================================================
    # SAVE CLEAN CSV
    # ========================================================

    save_csv(scored_df, CLEAN_RENTALS_CSV)

    print("\nCSV limpio con scoring guardado en:")
    print(CLEAN_RENTALS_CSV)

    # ========================================================
    # EXPORT OPPORTUNITIES
    # ========================================================

    export_top_opportunities(
        scored_df,
        TOP_OPPORTUNITIES_CSV,
        top_n=10
    )

    print("\nTop oportunidades exportadas en:")
    print(TOP_OPPORTUNITIES_CSV)

    # ========================================================
    # EXECUTIVE SUMMARY
    # ========================================================

    export_executive_summary(
        scored_df,
        EXECUTIVE_SUMMARY_MD,
        top_n=5
    )

    print("\nResumen ejecutivo exportado en:")
    print(EXECUTIVE_SUMMARY_MD)

    # ========================================================
    # PIPELINE COMPLETE
    # ========================================================

    print("\n====================================================")
    print("PIPELINE MULTIFUENTE FINALIZADO CORRECTAMENTE")
    print("====================================================")


if __name__ == "__main__":
    main()