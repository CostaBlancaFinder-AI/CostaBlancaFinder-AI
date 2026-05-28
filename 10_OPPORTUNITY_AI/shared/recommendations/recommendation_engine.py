# ============================================================
# CostaBlancaFinder AI
# Recommendation Engine V2
# ============================================================

import pandas as pd

from ml.recommenders.recommendation_engine import (
    generate_recommendations
)

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

INPUT_FILE = (
    "02_DATA_IA/processed_data/"
    "rentals_enriched.csv"
)

OUTPUT_FILE = (
    "02_DATA_IA/recommendations/"
    "recommended_properties.csv"
)

MAX_PRICE = 800
MIN_ROOMS = 2
MIN_LIFESTYLE = 8
TOP_N = 10


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

def load_dataset() -> pd.DataFrame:
    """
    Carga dataset enriquecido.
    """

    return pd.read_csv(INPUT_FILE)


# ------------------------------------------------------------
# FILTER DATA
# ------------------------------------------------------------

def filter_properties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra propiedades según preferencias.
    """

    filtered = df[
        (df["price_eur"] <= MAX_PRICE)
        &
        (df["rooms"] >= MIN_ROOMS)
        &
        (df["lifestyle_score"] >= MIN_LIFESTYLE)
    ]

    return filtered


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

def main():
    """
    Ejecuta el Recommendation Engine.
    """

    df = load_dataset()

    filtered = filter_properties(df)

    recommendations = generate_recommendations(
        filtered,
        top_n=TOP_N
    )

    recommendations.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("===================================")
    print("CostaBlancaFinder AI Recommendations")
    print("===================================")

    print(recommendations[[
        "city",
        "zone",
        "price_eur",
        "rooms",
        "lifestyle_score",
        "opportunity_score"
    ]])

    print("\nArchivo generado:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()