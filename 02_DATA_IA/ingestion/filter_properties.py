"""
============================================================
CostaBlancaFinder AI
Property Filtering
============================================================
"""

from typing import Optional

import pandas as pd


def filter_properties(
    df: pd.DataFrame,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    min_rooms: Optional[int] = None,
    min_area: Optional[int] = None,
    city: Optional[str] = None
) -> pd.DataFrame:
    """
    Filtra propiedades según criterios básicos.
    """

    if df.empty:
        return df

    filtered_df = df.copy()

    if min_price is not None and "price_eur" in filtered_df.columns:
        filtered_df = filtered_df[
            filtered_df["price_eur"] >= min_price
        ]

    if max_price is not None and "price_eur" in filtered_df.columns:
        filtered_df = filtered_df[
            filtered_df["price_eur"] <= max_price
        ]

    if min_rooms is not None and "rooms" in filtered_df.columns:
        filtered_df = filtered_df[
            filtered_df["rooms"] >= min_rooms
        ]

    if min_area is not None and "area_m2" in filtered_df.columns:
        filtered_df = filtered_df[
            filtered_df["area_m2"] >= min_area
        ]

    if city is not None and "city" in filtered_df.columns:
        filtered_df = filtered_df[
            filtered_df["city"].str.lower() == city.lower()
        ]

    return filtered_df.reset_index(drop=True)