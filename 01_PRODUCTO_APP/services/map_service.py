"""
============================================================
CostaBlancaFinder AI
Map Service
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Centralized geospatial visualization service responsible for
interactive Folium maps, intelligent property markers,
GeoAI visualization and future GIS integrations.

Architecture:
PropTech + AI + GeoAI + Folium + Streamlit

Created:
2026

Status:
MVP / Production-oriented architecture
============================================================
"""

import folium
import pandas as pd


# ============================================================
# CREATE BASE MAP
# ============================================================

def create_base_map(
    latitude: float = 38.5400,
    longitude: float = -0.1300,
    zoom_start: int = 10
):
    """
    Creates a base map centered on Costa Blanca.
    """

    return folium.Map(
        location=[latitude, longitude],
        zoom_start=zoom_start,
        tiles="OpenStreetMap"
    )


# ============================================================
# ADD LOCATION MARKERS
# ============================================================

def add_location_markers(
    map_object,
    locations_df: pd.DataFrame
):
    """
    Adds generic location markers.
    """

    if locations_df is None or locations_df.empty:
        return map_object

    required_columns = [
        "latitude",
        "longitude",
        "name",
        "city",
        "type"
    ]

    for column in required_columns:

        if column not in locations_df.columns:

            raise ValueError(
                f"Missing required location column: {column}"
            )

    for _, row in locations_df.iterrows():

        folium.Marker(
            location=[
                row["latitude"],
                row["longitude"]
            ],
            popup=f"{row['name']} ({row['city']})",
            tooltip=row["type"],
            icon=folium.Icon(
                color="blue",
                icon="info-sign"
            )
        ).add_to(map_object)

    return map_object


# ============================================================
# GET MARKER COLOR
# ============================================================

def get_marker_color(opportunity_score: float) -> str:
    """
    Returns marker color based on opportunity score.
    """

    if opportunity_score >= 80:
        return "green"

    if opportunity_score >= 60:
        return "blue"

    if opportunity_score >= 40:
        return "orange"

    return "red"


# ============================================================
# ADD PROPERTY MARKERS
# ============================================================

def add_property_markers(
    map_object,
    properties_df: pd.DataFrame
):
    """
    Adds intelligent property markers to the map.
    """

    if properties_df is None or properties_df.empty:
        return map_object

    required_columns = [
        "latitude",
        "longitude",
        "title",
        "city",
        "price_eur",
        "opportunity_score"
    ]

    for column in required_columns:

        if column not in properties_df.columns:

            raise ValueError(
                f"Missing required property column: {column}"
            )

    clean_df = properties_df.dropna(
        subset=["latitude", "longitude"]
    )

    for _, row in clean_df.iterrows():

        marker_color = get_marker_color(
            row["opportunity_score"]
        )

        popup_html = f"""
        <b>{row['title']}</b><br>
        📍 {row['city']}<br>
        💰 {row['price_eur']} €<br>
        📊 Score: {round(row['opportunity_score'], 2)}
        """

        folium.Marker(
            location=[
                row["latitude"],
                row["longitude"]
            ],
            popup=popup_html,
            tooltip=row["title"],
            icon=folium.Icon(
                color=marker_color,
                icon="home"
            )
        ).add_to(map_object)

    return map_object