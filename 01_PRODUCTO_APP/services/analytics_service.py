"""
============================================================
CostaBlancaFinder AI
Analytics Service
============================================================

Objetivo:
Centralizar métricas, KPIs y cálculos analíticos
del dashboard Streamlit.

Este módulo evita mezclar lógica de negocio
con interfaz gráfica.

Arquitectura:
Frontend (Streamlit)
    ↓
Analytics Service
    ↓
Datasets procesados

Futuro:
- métricas avanzadas
- predicción tendencias
- análisis temporal
- KPIs IA
- analytics para inversores
============================================================
"""

import pandas as pd


# ============================================================
# KPI: TOTAL PROPERTIES
# ============================================================

def get_total_properties(df: pd.DataFrame) -> int:
    """
    Devuelve número total de propiedades.
    """

    return len(df)


# ============================================================
# KPI: AVERAGE PRICE
# ============================================================

def get_average_price(df: pd.DataFrame) -> float:
    """
    Devuelve precio promedio.
    """

    return round(df["price_eur"].mean(), 2)


# ============================================================
# KPI: BEST OPPORTUNITY
# ============================================================

def get_best_opportunity(df: pd.DataFrame):
    """
    Devuelve propiedad con mayor opportunity score.
    """

    return df.sort_values(
        by="opportunity_score",
        ascending=False
    ).iloc[0]


# ============================================================
# KPI: CITY DISTRIBUTION
# ============================================================

def get_city_distribution(df: pd.DataFrame):
    """
    Distribución de propiedades por ciudad.
    """

    return df["city"].value_counts()