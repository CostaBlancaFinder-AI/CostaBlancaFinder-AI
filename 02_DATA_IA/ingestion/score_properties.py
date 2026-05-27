"""
============================================================
CostaBlancaFinder AI
Property Scoring V2
============================================================
"""

import pandas as pd


def min_max_score(series: pd.Series, inverse: bool = False) -> pd.Series:
    if series.empty:
        return series

    numeric = pd.to_numeric(series, errors="coerce").fillna(0)

    min_value = numeric.min()
    max_value = numeric.max()

    if min_value == max_value:
        return pd.Series([1.0] * len(numeric), index=numeric.index)

    score = (numeric - min_value) / (max_value - min_value)

    if inverse:
        score = 1 - score

    return score


def bool_score(series: pd.Series) -> pd.Series:
    return series.fillna(False).astype(bool).astype(int)


def score_properties(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    scored_df = df.copy()

    scored_df["price_score"] = min_max_score(
        scored_df["price_eur"],
        inverse=True
    )

    scored_df["area_score"] = min_max_score(
        scored_df["area_m2"]
    )

    scored_df["rooms_score"] = min_max_score(
        scored_df["rooms"]
    )

    scored_df["price_m2_score"] = min_max_score(
        scored_df["price_by_m2"],
        inverse=True
    )

    scored_df["comfort_score"] = (
        bool_score(scored_df.get("has_lift", False)) * 0.20 +
        bool_score(scored_df.get("has_terrace", False)) * 0.20 +
        bool_score(scored_df.get("has_air_conditioning", False)) * 0.20 +
        bool_score(scored_df.get("has_parking", False)) * 0.20 +
        bool_score(scored_df.get("has_swimming_pool", False)) * 0.10 +
        bool_score(scored_df.get("has_garden", False)) * 0.10
    )

    scored_df["photo_score"] = min_max_score(
        scored_df.get("num_photos", pd.Series([0] * len(scored_df)))
    )

    scored_df["opportunity_score"] = (
        scored_df["price_score"] * 0.30 +
        scored_df["price_m2_score"] * 0.20 +
        scored_df["area_score"] * 0.20 +
        scored_df["rooms_score"] * 0.10 +
        scored_df["comfort_score"] * 0.15 +
        scored_df["photo_score"] * 0.05
    )

    scored_df["opportunity_score"] = (
        scored_df["opportunity_score"] * 100
    ).round(2)

    scored_df = scored_df.sort_values(
        by="opportunity_score",
        ascending=False
    )

    return scored_df.reset_index(drop=True)