"""
============================================================
CostaBlancaFinder AI
Property Deduplication
============================================================

Objetivo:
Eliminar duplicados básicos en el dataset normalizado.

Primera versión:
- elimina duplicados por URL
- elimina duplicados por combinación:
  title + city + price_eur + area_m2
============================================================
"""

import pandas as pd


def deduplicate_properties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina duplicados básicos de propiedades.
    """

    if df.empty:
        return df

    df_clean = df.copy()

    if "source_url" in df_clean.columns:
        df_clean = df_clean.drop_duplicates(
            subset=["source_url"],
            keep="first"
        )

    duplicate_columns = [
        "title",
        "city",
        "price_eur",
        "area_m2"
    ]

    available_columns = [
        column for column in duplicate_columns
        if column in df_clean.columns
    ]

    if available_columns:
        df_clean = df_clean.drop_duplicates(
            subset=available_columns,
            keep="first"
        )

    return df_clean.reset_index(drop=True)