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

    source_url TEXT UNIQUE,
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

    opportunity_score FLOAT,

    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
"""


CREATE_PRICE_HISTORY_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS price_history (

    id SERIAL PRIMARY KEY,

    property_source_url TEXT,
    property_id TEXT,

    price_eur FLOAT,
    price_by_m2 FLOAT,

    recorded_at TIMESTAMP DEFAULT NOW()
);
"""


CREATE_INGESTION_LOGS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS ingestion_logs (

    id SERIAL PRIMARY KEY,

    source_name TEXT,
    status TEXT,
    total_raw INTEGER,
    total_normalized INTEGER,
    total_filtered INTEGER,
    total_saved INTEGER,

    message TEXT,

    created_at TIMESTAMP DEFAULT NOW()
);
"""


CREATE_SOURCES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS sources (

    id SERIAL PRIMARY KEY,

    source_name TEXT UNIQUE,
    source_type TEXT,
    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT NOW()
);
"""


CREATE_INDEXES_SQL = [
    "CREATE INDEX IF NOT EXISTS idx_properties_city ON properties(city);",
    "CREATE INDEX IF NOT EXISTS idx_properties_zone ON properties(zone);",
    "CREATE INDEX IF NOT EXISTS idx_properties_price ON properties(price_eur);",
    "CREATE INDEX IF NOT EXISTS idx_properties_score ON properties(opportunity_score);",
    "CREATE INDEX IF NOT EXISTS idx_properties_source ON properties(source_name);",
    "CREATE INDEX IF NOT EXISTS idx_price_history_url ON price_history(property_source_url);"
]


def init_database():

    engine = get_engine()

    with engine.connect() as connection:

        connection.execute(text(CREATE_PROPERTIES_TABLE_SQL))
        connection.execute(text(CREATE_PRICE_HISTORY_TABLE_SQL))
        connection.execute(text(CREATE_INGESTION_LOGS_TABLE_SQL))
        connection.execute(text(CREATE_SOURCES_TABLE_SQL))

        for index_sql in CREATE_INDEXES_SQL:
            connection.execute(text(index_sql))

        connection.commit()

    print("\nBase de datos inicializada correctamente.")
    print("Tablas creadas/verificadas:")
    print("- properties")
    print("- price_history")
    print("- ingestion_logs")
    print("- sources")


if __name__ == "__main__":
    init_database()