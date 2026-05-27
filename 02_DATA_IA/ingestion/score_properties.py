"""
============================================================
CostaBlancaFinder AI
Property Scoring
============================================================

Objetivo:
Asignar una puntuación básica a cada propiedad para ordenar
las mejores oportunidades.

Primera versión:
- menor precio = mejor
- mayor superficie = mejor
- más habitaciones = mejor
============================================================
"""

import pandas as pd


def min_max_score(series: pd.Series, inverse: bool = False) -> pd.Series:
    """
    Normaliza una columna numérica entre 0 y 1.
    """

    if series.empty:
        return series

    min_value = series.min()
    max_value = series.max()

    if min_value == max_value:
        return pd.Series([1.0] * len(series), index=series.index)

    score = (series - min_value) / (max_value - min_value)

    if inverse:
        score = 1 - score

    return score


def score_properties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula scoring básico de oportunidad.
    """

    if df.empty:
        return df

    scored_df = df.copy()

    scored_df["price_score"] = min_max_score(
        scored_df["price_eur"],
        inverse=True
    )

    scored_df["area_score"] = min_max_score(
        scored_df["area_m2"],
        inverse=False
    )

    scored_df["rooms_score"] = min_max_score(
        scored_df["rooms"],
        inverse=False
    )

    scored_df["opportunity_score"] = (
        scored_df["price_score"] * 0.50 +
        scored_df["area_score"] * 0.30 +
        scored_df["rooms_score"] * 0.20
    )

    scored_df = scored_df.sort_values(
        by="opportunity_score",
        ascending=False
    )

    return scored_df.reset_index(drop=True)