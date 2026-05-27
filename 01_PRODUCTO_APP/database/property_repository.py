"""
============================================================
CostaBlancaFinder AI
Property Repository
============================================================

Objetivo:
Cargar las propiedades procesadas por el pipeline de IA
para mostrarlas en el dashboard Streamlit.
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
            f"No existe el archivo de propiedades: {RENTALS_CLEAN_CSV}"
        )

    df = pd.read_csv(RENTALS_CLEAN_CSV)

    numeric_columns = [
        "price_eur",
        "area_m2",
        "rooms",
        "bathrooms",
        "price_score",
        "area_score",
        "rooms_score",
        "opportunity_score"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    if "price_m2" not in df.columns:
        df["price_m2"] = df["price_eur"] / df["area_m2"]

    return df