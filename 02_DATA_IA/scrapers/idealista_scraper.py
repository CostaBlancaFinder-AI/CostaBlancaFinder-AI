# ============================================================
# CostaBlancaFinder AI
# Idealista Scraper Placeholder
# ============================================================

import pandas as pd

print("Idealista scraper placeholder ejecutado.")

print(
    "Actualmente se usa dataset manual en "
    "02_DATA_IA/datasets/rentals_raw.csv"
)

df = pd.read_csv("02_DATA_IA/datasets/rentals_raw.csv")

print("Dataset manual cargado correctamente.")
print(df[["city", "zone", "price_eur"]])