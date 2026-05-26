"""
============================================================
CostaBlancaFinder AI
Scoring Service
============================================================

Objetivo:
Centralizar la lógica de ranking y puntuación de oportunidades.

Este módulo evita que el frontend calcule directamente rankings,
mejores oportunidades o medias de score.

Arquitectura:
Frontend Streamlit
    ↓
Scoring Service
    ↓
DataFrame filtrado
============================================================
"""

import pandas as pd


# ============================================================
# BEST OPPORTUNITY
# ============================================================

def get_best_opportunity_from_df(df: pd.DataFrame):
    """
    Devuelve la propiedad con mayor opportunity_score
    a partir de un DataFrame filtrado.
    """

    if df.empty:
        return None

    return df.sort_values(
        by="opportunity_score",
        ascending=False
    ).iloc[0]


# ============================================================
# TOP OPPORTUNITIES
# ============================================================

def get_top_opportunities(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """
    Devuelve las mejores oportunidades según opportunity_score.
    """

    if df.empty:
        return df

    return df.sort_values(
        by="opportunity_score",
        ascending=False
    ).head(top_n)


# ============================================================
# AVERAGE SCORE
# ============================================================

def get_average_opportunity_score(df: pd.DataFrame) -> float:
    """
    Calcula el score medio de oportunidad.
    """

    if df.empty:
        return 0

    return round(df["opportunity_score"].mean(), 2)


# ============================================================
# AVERAGE PRICE PER M2
# ============================================================

def get_average_price_m2(df: pd.DataFrame) -> float:
    """
    Calcula el precio medio por metro cuadrado.
    """

    if df.empty:
        return 0

    return round(df["price_m2"].mean(), 2)