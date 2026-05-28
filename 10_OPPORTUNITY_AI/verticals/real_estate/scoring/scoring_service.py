"""
============================================================
CostaBlancaFinder AI
Scoring Service
============================================================
"""

import pandas as pd


# ============================================================
# OPPORTUNITY LEVEL
# ============================================================

def get_opportunity_level(score: float) -> str:

    if score >= 90:
        return "EXCELLENT"

    if score >= 75:
        return "GREAT"

    if score >= 60:
        return "GOOD"

    if score >= 40:
        return "AVERAGE"

    return "BASIC"


# ============================================================
# BEST OPPORTUNITY
# ============================================================

def get_best_opportunity_from_df(df: pd.DataFrame):

    if df.empty:
        return None

    best = df.sort_values(
        by="opportunity_score",
        ascending=False
    ).iloc[0]

    return best


# ============================================================
# TOP OPPORTUNITIES
# ============================================================

def get_top_opportunities(
    df: pd.DataFrame,
    top_n: int = 3
) -> pd.DataFrame:

    if df.empty:
        return df

    top_df = df.sort_values(
        by="opportunity_score",
        ascending=False
    ).head(top_n).copy()

    top_df["opportunity_level"] = (
        top_df["opportunity_score"]
        .apply(get_opportunity_level)
    )

    return top_df


# ============================================================
# AVERAGE OPPORTUNITY SCORE
# ============================================================

def get_average_opportunity_score(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["opportunity_score"].mean(),
        2
    )


# ============================================================
# AVERAGE VALUE SCORE
# ============================================================

def get_average_value_score(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["value_score"].mean(),
        2
    )


# ============================================================
# AVERAGE COMFORT SCORE
# ============================================================

def get_average_comfort_score(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["comfort_score"].mean(),
        2
    )


# ============================================================
# AVERAGE QUALITY SCORE
# ============================================================

def get_average_quality_score(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["quality_score"].mean(),
        2
    )


# ============================================================
# AVERAGE PRICE PER M2
# ============================================================

def get_average_price_m2(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    column = (
        "price_by_m2"
        if "price_by_m2" in df.columns
        else "price_m2"
    )

    return round(
        df[column].fillna(0).mean(),
        2
    )


# ============================================================
# AVERAGE PRICE
# ============================================================

def get_average_price(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["price_eur"].mean(),
        2
    )


# ============================================================
# AVERAGE PRICE FILTERED
# ============================================================

def get_average_price_from_df(df: pd.DataFrame) -> float:

    if df.empty:
        return 0

    return round(
        df["price_eur"].mean(),
        2
    )