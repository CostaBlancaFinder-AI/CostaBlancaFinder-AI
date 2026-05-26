"""
============================================================
CostaBlancaFinder AI
Map Service
============================================================

Objetivo:
Centralizar la lógica geográfica y visualización
de mapas inteligentes.

Este módulo evita que Streamlit gestione
directamente Folium y la lógica GIS.

Futuro:
- heatmaps
- clustering geográfico
- zonas calientes
- scoring geoespacial
- integración OpenStreetMap
- rutas turísticas
- IA geográfica
============================================================
"""

import folium
import pandas as pd


# ============================================================
# CREATE BASE MAP
# ============================================================

def create_base_map():
    """
    Crea mapa base Costa Blanca.
    """

    map_center = [38.5400, -0.1300]

    return folium.Map(
        location=map_center,
        zoom_start=10
    )


# ============================================================
# ADD LOCATION MARKERS
# ============================================================

def add_location_markers(map_object, locations_df):
    """
    Añade marcadores al mapa.
    """

    for _, row in locations_df.iterrows():

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['name']} ({row['city']})",
            tooltip=row["type"]
        ).add_to(map_object)

    return map_object