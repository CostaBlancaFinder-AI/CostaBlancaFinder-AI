# ============================================================
# CostaBlancaFinder AI
# OpenStreetMap Locations Connector
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# DATOS INICIALES
# ------------------------------------------------------------

locations = [
    {
        "city": "Villajoyosa",
        "type": "beach",
        "name": "Playa Centro",
        "latitude": 38.5070,
        "longitude": -0.2310
    },
    {
        "city": "Benidorm",
        "type": "beach",
        "name": "Playa Levante",
        "latitude": 38.5362,
        "longitude": -0.1225
    },
    {
        "city": "Finestrat",
        "type": "mountain",
        "name": "Puig Campana",
        "latitude": 38.5890,
        "longitude": -0.2870
    }
]

# ------------------------------------------------------------
# DATAFRAME
# ------------------------------------------------------------

df = pd.DataFrame(locations)

# ------------------------------------------------------------
# EXPORTACIÓN
# ------------------------------------------------------------

output_path = "02_DATA_IA/datasets/osm_locations.csv"

df.to_csv(output_path, index=False)

# ------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------

print("OpenStreetMap dataset generado.")
print(df)