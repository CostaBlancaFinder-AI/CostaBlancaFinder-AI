"""
============================================================
CostaBlancaFinder AI
Property Database Repository
============================================================
"""

import pandas as pd

from sqlalchemy import text

from db_config import get_engine


TABLE_NAME = "properties"


def delete_existing_properties(df: pd.DataFrame):
    """
    Evita duplicados eliminando registros ya existentes
    por source_url antes de insertar.
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
                DELETE FROM {TABLE_NAME}
                WHERE source_url = ANY(:urls)
                """
            ),
            {"urls": urls}
        )

        connection.commit()


def save_properties_to_db(df: pd.DataFrame):

    if df.empty:
        print("DataFrame vacío.")
        return

    clean_df = df.copy()

    delete_existing_properties(clean_df)

    engine = get_engine()

    clean_df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(
        f"\nPropiedades guardadas/actualizadas en PostgreSQL: "
        f"{len(clean_df)}"
    )


def count_properties():

    engine = get_engine()

    with engine.connect() as connection:

        result = connection.execute(
            text(
                f"SELECT COUNT(*) FROM {TABLE_NAME}"
            )
        )

        total = result.scalar()

    return total