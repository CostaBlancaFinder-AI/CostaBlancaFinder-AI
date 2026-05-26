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
# FUNCIONES DE SCORING
# ------------------------------------------------------------

def calculate_price_m2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula precio por metro cuadrado.
    """

    df["price_m2"] = df["price_eur"] / df["area_m2"]

    return df


def calculate_price_score(price_m2: float) -> int:
    """
    Puntúa la oportunidad según precio por m².
    """

    if price_m2 < 10:
        return 40
    elif price_m2 < 13:
        return 25
    elif price_m2 < 16:
        return 15
    else:
        return 5


def calculate_location_score(city: str) -> int:
    """
    Puntúa la ubicación según ciudades premium.
    """

    premium_locations = [
        "Villajoyosa",
        "Benidorm",
        "Finestrat",
        "Altea"
    ]

    if city in premium_locations:
        return 20

    return 10


def calculate_room_score(rooms: int) -> int:
    """
    Puntúa según número de habitaciones.
    """

    if rooms >= 3:
        return 20
    elif rooms == 2:
        return 15
    else:
        return 8


def calculate_tourism_score(title: str) -> int:
    """
    Puntúa atractivo turístico según palabras clave.
    """

    title = str(title).lower()

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


def classify_opportunity_level(score: int) -> str:
    """
    Clasifica el nivel de oportunidad.
    """

    if score >= 85:
        return "High Opportunity"

    if score >= 65:
        return "Medium Opportunity"

    return "Low Opportunity"


def apply_scoring(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todo el proceso de scoring sobre el dataset.
    """

    df = calculate_price_m2(df)

    df["price_score"] = df["price_m2"].apply(calculate_price_score)
    df["location_score"] = df["city"].apply(calculate_location_score)
    df["room_score"] = df["rooms"].apply(calculate_room_score)
    df["tourism_score"] = df["title"].apply(calculate_tourism_score)

    df["opportunity_score"] = (
        df["price_score"]
        + df["location_score"]
        + df["room_score"]
        + df["tourism_score"]
    )

    df["opportunity_level"] = df["opportunity_score"].apply(
        classify_opportunity_level
    )

    df = df.sort_values(
        by="opportunity_score",
        ascending=False
    )

    return df


def main():
    """
    Ejecuta el Opportunity Scoring Agent V2.
    """

    df = pd.read_csv(INPUT_FILE)

    df = apply_scoring(df)

    df.to_csv(OUTPUT_FILE, index=False)

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


if __name__ == "__main__":
    main()