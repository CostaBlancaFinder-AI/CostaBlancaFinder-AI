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
Property Repository
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

from database.property_repository import load_properties


# ============================================================
# KPI: TOTAL PROPERTIES
# ============================================================

def get_total_properties() -> int:
    """
    Devuelve número total de propiedades.
    """

    df = load_properties()

    return len(df)


# ============================================================
# KPI: AVERAGE PRICE
# ============================================================

def get_average_price() -> float:
    """
    Devuelve precio promedio.
    """

    df = load_properties()

    return round(df["price_eur"].mean(), 2)


# ============================================================
# KPI: BEST OPPORTUNITY
# ============================================================

def get_best_opportunity():
    """
    Devuelve propiedad con mayor opportunity score.
    """

    df = load_properties()

    return df.sort_values(
        by="opportunity_score",
        ascending=False
    ).iloc[0]


# ============================================================
# KPI: CITY DISTRIBUTION
# ============================================================

def get_city_distribution():
    """
    Distribución de propiedades por ciudad.
    """

    df = load_properties()

    return df["city"].value_counts()