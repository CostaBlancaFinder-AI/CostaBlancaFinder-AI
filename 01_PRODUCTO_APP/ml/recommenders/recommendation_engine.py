"""
============================================================
CostaBlancaFinder AI
Recommendation Engine
============================================================

Objetivo:
Motor IA de recomendación inmobiliaria.

Este módulo centraliza:
- ranking IA
- recomendaciones
- scoring combinado
- futura IA semántica
============================================================
"""

import pandas as pd


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    df: pd.DataFrame,
    top_n: int = 10
) -> pd.DataFrame:
    """
    Genera recomendaciones inmobiliarias.
    """

    if df is None or df.empty:
        return pd.DataFrame()

    required_columns = [
        "opportunity_score"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Falta columna requerida: {column}"
            )

    recommendations = df.sort_values(
        by="opportunity_score",
        ascending=False
    ).head(top_n)

    return recommendations