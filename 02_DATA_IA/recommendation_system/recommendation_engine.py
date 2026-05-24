# ============================================================
# CostaBlancaFinder AI
# Recommendation Engine V1
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

df = pd.read_csv(
    "02_DATA_IA/processed_data/rentals_enriched.csv"
)

# ------------------------------------------------------------
# USER PREFERENCES
# ------------------------------------------------------------

MAX_PRICE = 800
MIN_ROOMS = 2
MIN_LIFESTYLE = 8

# ------------------------------------------------------------
# FILTERING
# ------------------------------------------------------------

recommended = df[
    (df["price_eur"] <= MAX_PRICE)
    &
    (df["rooms"] >= MIN_ROOMS)
    &
    (df["lifestyle_score"] >= MIN_LIFESTYLE)
]

# ------------------------------------------------------------
# SORT
# ------------------------------------------------------------

recommended = recommended.sort_values(
    by="opportunity_score",
    ascending=False
)

# ------------------------------------------------------------
# EXPORT
# ------------------------------------------------------------

output_path = (
    "02_DATA_IA/recommendations/"
    "recommended_properties.csv"
)

recommended.to_csv(
    output_path,
    index=False
)

# ------------------------------------------------------------
# RESULTS
# ------------------------------------------------------------

print("===================================")
print("CostaBlancaFinder AI Recommendations")
print("===================================")

print(recommended[[
    "city",
    "zone",
    "price_eur",
    "rooms",
    "lifestyle_score",
    "opportunity_score"
]])

print("\nArchivo generado:")
print(output_path)