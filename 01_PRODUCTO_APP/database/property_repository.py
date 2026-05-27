"""
============================================================
CostaBlancaFinder AI
Property Repository
============================================================
"""

from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DATA_PATH = (
    ROOT_DIR / "02_DATA_IA" / "processed_data"
)

RENTALS_CLEAN_CSV = (
    PROCESSED_DATA_PATH / "rentals_clean.csv"
)


def load_properties() -> pd.DataFrame:
    """
    Carga el dataset limpio generado por el pipeline.
    """

    if not RENTALS_CLEAN_CSV.exists():
        raise FileNotFoundError(
            f"No existe el archivo: {RENTALS_CLEAN_CSV}"
        )

    df = pd.read_csv(RENTALS_CLEAN_CSV)

    # ========================================================
    # NUMERIC COLUMNS
    # ========================================================

    numeric_columns = [
        "price_eur",
        "price_by_m2",
        "area_m2",
        "rooms",
        "bathrooms",
        "price_score",
        "price_m2_score",
        "area_score",
        "rooms_score",
        "value_score",
        "comfort_score",
        "quality_score",
        "opportunity_score"
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    # ========================================================
    # FALLBACK PRICE_BY_M2
    # ========================================================

    if "price_by_m2" not in df.columns:

        df["price_by_m2"] = (
            df["price_eur"] / df["area_m2"]
        )

    # ========================================================
    # CLEAN DIVISION ERRORS
    # ========================================================

    df["price_by_m2"] = (
        df["price_by_m2"]
        .replace([float("inf"), -float("inf")], 0)
        .fillna(0)
    )

    return df