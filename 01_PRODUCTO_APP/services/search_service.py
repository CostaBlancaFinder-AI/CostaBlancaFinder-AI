"""
============================================================
CostaBlancaFinder AI
Search Service
============================================================

Objetivo:
Centralizar la lógica de filtrado y búsqueda de propiedades.

Este módulo evita que el dashboard Streamlit mezcle
interfaz visual con lógica de negocio.

Arquitectura:
Frontend Streamlit
    ↓
Search Service
    ↓
Dataset de propiedades

Futuro:
- búsqueda semántica
- filtros avanzados
- búsqueda por perfil de usuario
- ranking personalizado
- integración con embeddings
============================================================
"""

import pandas as pd


# ============================================================
# FILTER PROPERTIES
# ============================================================

def filter_properties(
    df: pd.DataFrame,
    city_filter: str,
    max_price: int,
    min_rooms: int
) -> pd.DataFrame:
    """
    Filtra propiedades por ciudad, precio máximo y habitaciones mínimas.
    """

    if df is None or df.empty:
        return pd.DataFrame()

    required_columns = [
        "city",
        "price_eur",
        "rooms"
    ]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(
                f"Falta la columna obligatoria en el dataset: {column}"
            )

    filtered = df.copy()

    if city_filter != "Todas":
        filtered = filtered[
            filtered["city"] == city_filter
        ]

    filtered = filtered[
        filtered["price_eur"] <= max_price
    ]

    filtered = filtered[
        filtered["rooms"] >= min_rooms
    ]

    return filtered