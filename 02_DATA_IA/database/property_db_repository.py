"""
============================================================
CostaBlancaFinder AI
Property Database Repository
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Enterprise-grade repository layer responsible for persisting
processed real estate opportunities into PostgreSQL/Supabase,
avoiding duplicates and maintaining price history records.

Architecture:
PropTech + AI + PostgreSQL + Supabase + Streamlit

Created:
2026

Status:
MVP / Production-oriented architecture
============================================================
"""

import pandas as pd

from sqlalchemy import text

from db_config import get_engine


PROPERTIES_TABLE = "properties"
PRICE_HISTORY_TABLE = "price_history"


# ============================================================
# DATA CLEANING
# ============================================================

def prepare_dataframe_for_db(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares the DataFrame before database persistence.
    """

    clean_df = df.copy()

    clean_df = clean_df.where(
        pd.notnull(clean_df),
        None
    )

    return clean_df


# ============================================================
# PRICE HISTORY
# ============================================================

def save_price_history(df: pd.DataFrame) -> None:
    """
    Stores price history for each property execution.
    """

    if df.empty:
        return

    required_columns = [
        "source_url",
        "property_id",
        "price_eur",
        "price_by_m2"
    ]

    for column in required_columns:
        if column not in df.columns:
            return

    history_df = df[required_columns].copy()

    history_df = history_df.rename(
        columns={
            "source_url": "property_source_url"
        }
    )

    engine = get_engine()

    history_df.to_sql(
        PRICE_HISTORY_TABLE,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(
        f"Histórico de precios guardado: {len(history_df)} registros"
    )


# ============================================================
# DEDUPLICATION
# ============================================================

def delete_existing_properties(df: pd.DataFrame) -> None:
    """
    Avoids duplicated active records by deleting existing
    properties with the same source_url before inserting
    the updated version.
    """

    if df.empty or "source_url" not in df.columns:
        return

    urls = (
        df["source_url"]
        .dropna()
        .unique()
        .tolist()
    )

    if not urls:
        return

    engine = get_engine()

    with engine.connect() as connection:

        connection.execute(
            text(
                f"""
                DELETE FROM {PROPERTIES_TABLE}
                WHERE source_url = ANY(:urls)
                """
            ),
            {"urls": urls}
        )

        connection.commit()


# ============================================================
# MAIN SAVE FUNCTION
# ============================================================

def save_properties_to_db(df: pd.DataFrame) -> None:
    """
    Saves scored properties into PostgreSQL/Supabase and
    records their price history.
    """

    if df.empty:
        print("DataFrame vacío. No se guardan propiedades.")
        return

    clean_df = prepare_dataframe_for_db(df)

    save_price_history(clean_df)

    delete_existing_properties(clean_df)

    engine = get_engine()

    clean_df.to_sql(
        PROPERTIES_TABLE,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(
        f"\nPropiedades guardadas/actualizadas en PostgreSQL: "
        f"{len(clean_df)}"
    )


# ============================================================
# COUNTERS
# ============================================================

def count_properties() -> int:
    """
    Returns the number of active properties stored.
    """

    engine = get_engine()

    with engine.connect() as connection:

        result = connection.execute(
            text(
                f"SELECT COUNT(*) FROM {PROPERTIES_TABLE}"
            )
        )

        total = result.scalar()

    return total


def count_price_history() -> int:
    """
    Returns the number of price history records stored.
    """

    engine = get_engine()

    with engine.connect() as connection:

        result = connection.execute(
            text(
                f"SELECT COUNT(*) FROM {PRICE_HISTORY_TABLE}"
            )
        )

        total = result.scalar()

    return total