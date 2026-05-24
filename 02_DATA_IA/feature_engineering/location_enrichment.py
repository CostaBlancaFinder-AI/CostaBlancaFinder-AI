# ============================================================
# CostaBlancaFinder AI
# Location Enrichment Engine
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# CARGA DATOS
# ------------------------------------------------------------

rentals = pd.read_csv(
    "02_DATA_IA/processed_data/rentals_scored_v2.csv"
)

locations = pd.read_csv(
    "02_DATA_IA/datasets/osm_locations.csv"
)

# ------------------------------------------------------------
# ENRIQUECIMIENTO SIMPLE
# ------------------------------------------------------------

city_scores = {
    "Villajoyosa": 9,
    "Benidorm": 8,
    "Finestrat": 8,
    "Altea": 10
}

rentals["lifestyle_score"] = rentals["city"].map(
    city_scores
)

# ------------------------------------------------------------
# EXPORTACIÓN
# ------------------------------------------------------------

output_path = (
    "02_DATA_IA/processed_data/"
    "rentals_enriched.csv"
)

rentals.to_csv(
    output_path,
    index=False
)

print("Location enrichment finalizado.")
print(rentals[[
    "city",
    "zone",
    "lifestyle_score"
]])