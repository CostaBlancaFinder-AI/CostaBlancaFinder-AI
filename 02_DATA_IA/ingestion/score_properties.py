"""
============================================================
CostaBlancaFinder AI
Property Scoring V3
============================================================

Objetivo:
Asignar una puntuación inteligente de oportunidad
a propiedades inmobiliarias reales.

Scoring basado en:
- value_score
- comfort_score
- quality_score
============================================================
"""

import pandas as pd


# ============================================================
# NORMALIZATION HELPERS
# ============================================================

def min_max_score(
    series: pd.Series,
    inverse: bool = False
) -> pd.Series:

    if series.empty:
        return series

    numeric = pd.to_numeric(
        series,
        errors="coerce"
    ).fillna(0)

    min_value = numeric.min()
    max_value = numeric.max()

    if min_value == max_value:
        return pd.Series(
            [1.0] * len(numeric),
            index=numeric.index
        )

    score = (
        (numeric - min_value)
        / (max_value - min_value)
    )

    if inverse:
        score = 1 - score

    return score


def bool_score(series: pd.Series) -> pd.Series:
    return (
        series
        .fillna(False)
        .astype(bool)
        .astype(int)
    )


# ============================================================
# COMPLETENESS SCORE
# ============================================================

def completeness_score(row) -> float:

    important_fields = [
        "price_eur",
        "area_m2",
        "rooms",
        "description",
        "thumbnail"
    ]

    filled = sum(
        1 for field in important_fields
        if pd.notna(row.get(field))
        and row.get(field) not in ["", 0]
    )

    return filled / len(important_fields)


# ============================================================
# MAIN SCORING FUNCTION
# ============================================================

def score_properties(df: pd.DataFrame) -> pd.DataFrame:

    if df.empty:
        return df

    scored_df = df.copy()

    # ========================================================
    # VALUE FEATURES
    # ========================================================

    scored_df["price_score"] = min_max_score(
        scored_df["price_eur"],
        inverse=True
    )

    scored_df["price_m2_score"] = min_max_score(
        scored_df["price_by_m2"],
        inverse=True
    )

    scored_df["area_score"] = min_max_score(
        scored_df["area_m2"]
    )

    scored_df["rooms_score"] = min_max_score(
        scored_df["rooms"]
    )

    # ========================================================
    # VALUE SCORE
    # ========================================================

    scored_df["value_score"] = (
        scored_df["price_score"] * 0.40 +
        scored_df["price_m2_score"] * 0.35 +
        scored_df["area_score"] * 0.15 +
        scored_df["rooms_score"] * 0.10
    )

    # ========================================================
    # COMFORT SCORE
    # ========================================================

    scored_df["comfort_score"] = (
        bool_score(
            scored_df.get(
                "has_air_conditioning",
                False
            )
        ) * 0.30 +

        bool_score(
            scored_df.get(
                "has_terrace",
                False
            )
        ) * 0.25 +

        bool_score(
            scored_df.get(
                "has_lift",
                False
            )
        ) * 0.20 +

        bool_score(
            scored_df.get(
                "has_parking",
                False
            )
        ) * 0.15 +

        bool_score(
            scored_df.get(
                "has_swimming_pool",
                False
            )
        ) * 0.07 +

        bool_score(
            scored_df.get(
                "has_garden",
                False
            )
        ) * 0.03
    )

    # ========================================================
    # QUALITY FEATURES
    # ========================================================

    scored_df["photo_score"] = min_max_score(
        scored_df.get(
            "num_photos",
            pd.Series([0] * len(scored_df))
        )
    )

    scored_df["description_length"] = (
        scored_df["description"]
        .fillna("")
        .astype(str)
        .str.len()
    )

    scored_df["description_score"] = min_max_score(
        scored_df["description_length"]
    )

    scored_df["completeness_score"] = (
        scored_df.apply(
            completeness_score,
            axis=1
        )
    )

    # ========================================================
    # QUALITY SCORE
    # ========================================================

    scored_df["quality_score"] = (
        scored_df["photo_score"] * 0.40 +
        scored_df["description_score"] * 0.30 +
        scored_df["completeness_score"] * 0.30
    )

    # ========================================================
    # FINAL OPPORTUNITY SCORE
    # ========================================================

    scored_df["opportunity_score"] = (
        scored_df["value_score"] * 0.60 +
        scored_df["comfort_score"] * 0.25 +
        scored_df["quality_score"] * 0.15
    )

    scored_df["opportunity_score"] = (
        scored_df["opportunity_score"] * 100
    ).round(2)

    # ========================================================
    # SORT RESULTS
    # ========================================================

    scored_df = scored_df.sort_values(
        by="opportunity_score",
        ascending=False
    )

    return scored_df.reset_index(drop=True)