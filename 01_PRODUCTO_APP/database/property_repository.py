"""
============================================================
CostaBlancaFinder AI
Property Repository
============================================================
"""

import sys
from pathlib import Path

import pandas as pd
from sqlalchemy import text


ROOT_DIR = Path(__file__).resolve().parents[2]

DATABASE_DIR = ROOT_DIR / "02_DATA_IA" / "database"

sys.path.append(str(DATABASE_DIR))

from db_config import get_engine


TABLE_NAME = "properties"


def load_properties() -> pd.DataFrame:
    """
    Carga propiedades directamente desde PostgreSQL/Supabase.
    """

    engine = get_engine()

    query = text(
        f"""
        SELECT *
        FROM {TABLE_NAME}
        ORDER BY opportunity_score DESC
        """
    )

    df = pd.read_sql(query, engine)

    if df.empty:
        return df

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
    # CLEAN NaN / INF
    # ========================================================

    if "price_by_m2" in df.columns:

        df["price_by_m2"] = (
            df["price_by_m2"]
            .replace(
                [float("inf"), -float("inf")],
                0
            )
            .fillna(0)
        )

    return df