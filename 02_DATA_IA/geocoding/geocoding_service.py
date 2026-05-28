"""
============================================================
CostaBlancaFinder AI
Geocoding Service
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Geocoding service responsible for enriching real estate
records with approximate latitude and longitude based on
city and zone information. This module enables geospatial
analytics, intelligent maps, GeoAI, clustering and future
location-based recommendations.

Architecture:
PropTech + AI + GeoAI + PostgreSQL + Supabase

Created:
2026

Status:
MVP / Production-oriented architecture
============================================================
"""

import pandas as pd


# ============================================================
# STATIC LOCATION KNOWLEDGE BASE
# ============================================================

LOCATION_COORDINATES = {
    "Alicante": {
        "default": (38.3452, -0.4810),
        "Centro": (38.3452, -0.4810),
        "Benalúa": (38.3390, -0.4930),
        "Playa San Juan": (38.3688, -0.4080),
    },
    "Villajoyosa": {
        "default": (38.5075, -0.2335),
        "Centro": (38.5075, -0.2335),
    },
    "Benidorm": {
        "default": (38.5411, -0.1225),
        "Playa Levante": (38.5357, -0.1129),
    },
}


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(value: str) -> str:
    """
    Normalizes text values used for geocoding lookup.
    """

    if value is None:
        return ""

    return str(value).strip()


# ============================================================
# GET COORDINATES
# ============================================================

def get_coordinates(
    city: str,
    zone: str = None
) -> tuple:
    """
    Returns approximate coordinates based on city and zone.
    """

    city = normalize_text(city)
    zone = normalize_text(zone)

    if city not in LOCATION_COORDINATES:
        return None, None

    city_data = LOCATION_COORDINATES[city]

    if zone in city_data:
        return city_data[zone]

    return city_data.get("default", (None, None))


# ============================================================
# ENRICH DATAFRAME
# ============================================================

def enrich_with_coordinates(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Adds latitude and longitude to a property DataFrame
    when coordinates are missing.
    """

    if df.empty:
        return df

    enriched_df = df.copy()

    if "latitude" not in enriched_df.columns:
        enriched_df["latitude"] = None

    if "longitude" not in enriched_df.columns:
        enriched_df["longitude"] = None

    for index, row in enriched_df.iterrows():

        current_lat = row.get("latitude")
        current_lon = row.get("longitude")

        if pd.notna(current_lat) and pd.notna(current_lon):
            continue

        latitude, longitude = get_coordinates(
            city=row.get("city"),
            zone=row.get("zone")
        )

        enriched_df.at[index, "latitude"] = latitude
        enriched_df.at[index, "longitude"] = longitude

    return enriched_df