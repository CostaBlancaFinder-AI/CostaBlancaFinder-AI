# ============================================================
# CostaBlancaFinder AI
# Opportunity Scoring Agent V2
# ============================================================

import pandas as pd

from ml.scoring.opportunity_model import (
    calculate_price_score,
    calculate_location_score,
    calculate_room_score,
    calculate_tourism_score,
    classify_opportunity_level,
    calculate_opportunity_score,
)

# ------------------------------------------------------------
# CONFIGURACIÓN
# ------------------------------------------------------------

INPUT_FILE = "02_DATA_IA/datasets/rentals_raw.csv"
OUTPUT_FILE = "02_DATA_IA/processed_data/rentals_scored_v2.csv"


# ------------------------------------------------------------
# FEATURE ENGINEERING
# ------------------------------------------------------------

def calculate_price_m2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula precio por metro cuadrado.
    """

    df["price_m2"] = df["price_eur"] / df["area_m2"]

    return df


# ------------------------------------------------------------
# SCORING PIPELINE
# ------------------------------------------------------------

def apply_scoring(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todo el proceso de scoring sobre el dataset.
    """

    df = calculate_price_m2(df)

    df["price_score"] = df["price_m2"].apply(calculate_price_score)
    df["location_score"] = df["city"].apply(calculate_location_score)
    df["room_score"] = df["rooms"].apply(calculate_room_score)
    df["tourism_score"] = df["title"].apply(calculate_tourism_score)

    df["opportunity_score"] = df.apply(
        lambda row: calculate_opportunity_score(
            price_score=row["price_score"],
            location_score=row["location_score"],
            room_score=row["room_score"],
            tourism_score=row["tourism_score"]
        ),
        axis=1
    )

    df["opportunity_level"] = df["opportunity_score"].apply(
        classify_opportunity_level
    )

    df = df.sort_values(
        by="opportunity_score",
        ascending=False
    )

    return df


# ------------------------------------------------------------
# MAIN EXECUTION
# ------------------------------------------------------------

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