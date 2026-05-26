"""
============================================================
CostaBlancaFinder AI
Recommendation Service
============================================================

Objetivo:
Centralizar la gestión de recomendaciones IA.

Arquitectura:
Frontend Streamlit
    ↓
Recommendation Service
    ↓
Recommendation Repository
    ↓
Dataset de recomendaciones
============================================================
"""

import pandas as pd

from database.recommendation_repository import load_recommendations_data


# ============================================================
# LOAD RECOMMENDATIONS
# ============================================================

def load_recommendations() -> pd.DataFrame:
    """
    Carga el dataset de recomendaciones IA desde el repository.
    """

    return load_recommendations_data()


# ============================================================
# CHECK RECOMMENDATIONS
# ============================================================

def has_recommendations(df: pd.DataFrame) -> bool:
    """
    Comprueba si existen recomendaciones disponibles.
    """

    return df is not None and not df.empty