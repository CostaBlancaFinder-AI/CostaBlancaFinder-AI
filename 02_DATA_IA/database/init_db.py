"""
============================================================
CostaBlancaFinder AI
Database Initialization
============================================================
"""

from sqlalchemy import text

from db_config import get_engine


CREATE_PROPERTIES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS properties (

    id SERIAL PRIMARY KEY,

    property_id TEXT,
    title TEXT,
    description TEXT,

    city TEXT,
    zone TEXT,
    address TEXT,

    price_eur FLOAT,
    price_by_m2 FLOAT,

    area_m2 FLOAT,

    rooms INTEGER,
    bathrooms INTEGER,

    floor TEXT,

    property_type TEXT,
    operation TEXT,

    latitude FLOAT,
    longitude FLOAT,

    thumbnail TEXT,

    num_photos INTEGER,

    has_lift BOOLEAN,
    has_terrace BOOLEAN,
    has_air_conditioning BOOLEAN,
    has_swimming_pool BOOLEAN,
    has_garden BOOLEAN,
    has_parking BOOLEAN,

    source_url TEXT,
    source_name TEXT,

    scraped_at TEXT,

    price_score FLOAT,
    price_m2_score FLOAT,
    area_score FLOAT,
    rooms_score FLOAT,

    value_score FLOAT,
    comfort_score FLOAT,
    photo_score FLOAT,

    description_length FLOAT,
    description_score FLOAT,
    completeness_score FLOAT,
    quality_score FLOAT,

    opportunity_score FLOAT
);
"""


def init_database():

    engine = get_engine()

    with engine.connect() as connection:

        connection.execute(
            text(CREATE_PROPERTIES_TABLE_SQL)
        )

        connection.commit()

    print("\nBase de datos inicializada correctamente.")


if __name__ == "__main__":
    init_database()