"""
============================================================
CostaBlancaFinder AI
Executive Summary Exporter
============================================================

Objetivo:
Generar un resumen ejecutivo en Markdown con las mejores
oportunidades inmobiliarias detectadas.
============================================================
"""

from datetime import datetime

import pandas as pd


def export_executive_summary(
    df: pd.DataFrame,
    output_path,
    top_n: int = 5
) -> None:
    """
    Exporta un resumen ejecutivo en formato Markdown.
    """

    if df.empty:
        print("No hay datos para generar resumen ejecutivo.")
        return

    if "opportunity_score" not in df.columns:
        print("No existe la columna opportunity_score.")
        return

    top_df = df.sort_values(
        by="opportunity_score",
        ascending=False
    ).head(top_n)

    lines = []

    lines.append("# CostaBlancaFinder AI — Resumen Ejecutivo")
    lines.append("")
    lines.append(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append(f"Propiedades analizadas: {len(df)}")
    lines.append(f"Top oportunidades mostradas: {len(top_df)}")
    lines.append("")
    lines.append("## Mejores oportunidades detectadas")
    lines.append("")

    for index, row in top_df.iterrows():
        lines.append(f"### {index + 1}. {row.get('title', 'Sin título')}")
        lines.append("")
        lines.append(f"- Ciudad: {row.get('city', 'N/D')}")
        lines.append(f"- Zona: {row.get('zone', 'N/D')}")
        lines.append(f"- Precio: {row.get('price_eur', 'N/D')} €")
        lines.append(f"- Superficie: {row.get('area_m2', 'N/D')} m²")
        lines.append(f"- Habitaciones: {row.get('rooms', 'N/D')}")
        lines.append(f"- Baños: {row.get('bathrooms', 'N/D')}")
        lines.append(f"- Tipo: {row.get('property_type', 'N/D')}")
        lines.append(f"- Fuente: {row.get('source_name', 'N/D')}")
        lines.append(f"- Score oportunidad: {round(row.get('opportunity_score', 0), 4)}")
        lines.append(f"- URL: {row.get('source_url', 'N/D')}")
        lines.append("")

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    print(f"Resumen ejecutivo exportado en: {output_path}")