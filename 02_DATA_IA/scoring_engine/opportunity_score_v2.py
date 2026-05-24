# ============================================================
# CostaBlancaFinder AI
# Opportunity Scoring Agent V2
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# CONFIGURACIÓN
# ------------------------------------------------------------

INPUT_FILE = "02_DATA_IA/datasets/rentals_raw.csv"
OUTPUT_FILE = "02_DATA_IA/processed_data/rentals_scored_v2.csv"

# ------------------------------------------------------------
# CARGA DE DATOS
# ------------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

# ------------------------------------------------------------
# FEATURE ENGINEERING
# ------------------------------------------------------------

df["price_m2"] = df["price_eur"] / df["area_m2"]

# ------------------------------------------------------------
# FUNCIONES DE SCORING
# ------------------------------------------------------------

def price_score(price_m2):
    if price_m2 < 10:
        return 40
    elif price_m2 < 13:
        return 25
    elif price_m2 < 16:
        return 15
    else:
        return 5


def location_score(city):
    premium_locations = ["Villajoyosa", "Benidorm", "Finestrat", "Altea"]
    if city in premium_locations:
        return 20
    return 10


def room_score(rooms):
    if rooms >= 3:
        return 20
    elif rooms == 2:
        return 15
    else:
        return 8


def tourism_score(title):
    title = title.lower()

    keywords = [
        "playa",
        "vistas mar",
        "mar",
        "turístico",
        "cala",
        "centro"
    ]

    score = 0

    for keyword in keywords:
        if keyword in title:
            score += 5

    return min(score, 20)


# ------------------------------------------------------------
# APLICACIÓN DEL AGENTE DE SCORING
# ------------------------------------------------------------

df["price_score"] = df["price_m2"].apply(price_score)
df["location_score"] = df["city"].apply(location_score)
df["room_score"] = df["rooms"].apply(room_score)
df["tourism_score"] = df["title"].apply(tourism_score)

df["opportunity_score"] = (
    df["price_score"]
    + df["location_score"]
    + df["room_score"]
    + df["tourism_score"]
)

# ------------------------------------------------------------
# CLASIFICACIÓN
# ------------------------------------------------------------

def opportunity_level(score):
    if score >= 85:
        return "High Opportunity"
    elif score >= 65:
        return "Medium Opportunity"
    else:
        return "Low Opportunity"


df["opportunity_level"] = df["opportunity_score"].apply(opportunity_level)

# ------------------------------------------------------------
# EXPORTACIÓN
# ------------------------------------------------------------

df = df.sort_values(
    by="opportunity_score",
    ascending=False
)

df.to_csv(OUTPUT_FILE, index=False)

# ------------------------------------------------------------
# RESULTADOS
# ------------------------------------------------------------

print("Opportunity Scoring Agent V2 finalizado.")
print(df[[
    "city",
    "zone",
    "price_eur",
    "area_m2",
    "price_m2",
    "price_score",
    "location_score",
    "room_score",
    "tourism_score",
    "opportunity_score",
    "opportunity_level"
]])