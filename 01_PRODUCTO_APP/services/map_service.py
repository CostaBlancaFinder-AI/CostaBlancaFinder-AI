"""
============================================================
CostaBlancaFinder AI
Map Service
============================================================

Objetivo:
Centralizar la lógica geográfica y visualización de mapas.

Este módulo evita que Streamlit gestione directamente Folium
y deja preparada la futura evolución GIS / GeoAI.
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
    Crea un mapa base centrado en la Costa Blanca.
    """

    return folium.Map(
        location=[latitude, longitude],
        zoom_start=zoom_start
    )


# ============================================================
# ADD LOCATION MARKERS
# ============================================================

def add_location_markers(
    map_object,
    locations_df: pd.DataFrame
):
    """
    Añade marcadores geográficos al mapa.
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
                f"Falta la columna obligatoria en localizaciones: {column}"
            )

    for _, row in locations_df.iterrows():

        folium.Marker(
            location=[
                row["latitude"],
                row["longitude"]
            ],
            popup=f"{row['name']} ({row['city']})",
            tooltip=row["type"]
        ).add_to(map_object)

    return map_object