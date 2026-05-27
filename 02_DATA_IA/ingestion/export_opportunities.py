"""
============================================================
CostaBlancaFinder AI
Opportunity Exporter
============================================================
"""

import pandas as pd


def export_top_opportunities(
    df: pd.DataFrame,
    output_path,
    top_n: int = 10
) -> None:
    """
    Exporta las mejores oportunidades según opportunity_score.
    """

    if df.empty:
        print("No hay propiedades para exportar.")
        return

    if "opportunity_score" not in df.columns:
        print("No existe la columna opportunity_score.")
        return

    top_df = df.sort_values(
        by="opportunity_score",
        ascending=False
    ).head(top_n)

    top_df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"Top oportunidades exportadas en: {output_path}")