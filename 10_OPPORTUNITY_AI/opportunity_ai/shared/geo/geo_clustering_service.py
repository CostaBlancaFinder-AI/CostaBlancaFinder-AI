"""
============================================================
CostaBlancaFinder AI
Geo Clustering Service
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Service layer for detecting geographic clusters of real estate
opportunities using latitude, longitude and opportunity score.

Architecture:
PropTech + AI + GeoAI + PostgreSQL + Supabase + Streamlit

Created:
2026

Status:
MVP / Production-oriented architecture
============================================================
"""

import pandas as pd


def detect_geo_clusters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detects simple opportunity clusters based on city and zone.
    """

    if df.empty:
        return pd.DataFrame()

    required_columns = [
        "city",
        "zone",
        "opportunity_score",
        "price_eur",
        "area_m2"
    ]

    for column in required_columns:
        if column not in df.columns:
            return pd.DataFrame()

    clusters_df = (
        df.groupby(["city", "zone"])
        .agg(
            total_properties=("title", "count"),
            avg_opportunity_score=("opportunity_score", "mean"),
            avg_price=("price_eur", "mean"),
            avg_area=("area_m2", "mean")
        )
        .reset_index()
    )

    clusters_df["avg_opportunity_score"] = (
        clusters_df["avg_opportunity_score"].round(2)
    )

    clusters_df["avg_price"] = (
        clusters_df["avg_price"].round(2)
    )

    clusters_df["avg_area"] = (
        clusters_df["avg_area"].round(2)
    )

    clusters_df = clusters_df.sort_values(
        by="avg_opportunity_score",
        ascending=False
    )

    return clusters_df