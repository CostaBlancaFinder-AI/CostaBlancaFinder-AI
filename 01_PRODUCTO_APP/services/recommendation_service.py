"""
============================================================
CostaBlancaFinder AI
Recommendation Service
============================================================

Objetivo:
Centralizar la carga y gestión de recomendaciones IA.

Este módulo evita que el dashboard Streamlit cargue
directamente archivos CSV de recomendaciones.

Arquitectura:
Frontend Streamlit
    ↓
Recommendation Service
    ↓
Dataset de recomendaciones

Futuro:
- recomendaciones personalizadas
- filtros por perfil de usuario
- ranking avanzado
- integración con modelos ML
- conexión con base de datos
============================================================
"""

import pandas as pd


# ============================================================
# LOAD RECOMMENDATIONS
# ============================================================

def load_recommendations(recommendations_path) -> pd.DataFrame:
    """
    Carga el dataset de recomendaciones IA.
    """

    return pd.read_csv(recommendations_path)


# ============================================================
# CHECK RECOMMENDATIONS
# ============================================================

def has_recommendations(df: pd.DataFrame) -> bool:
    """
    Comprueba si existen recomendaciones disponibles.
    """

    return not df.empty