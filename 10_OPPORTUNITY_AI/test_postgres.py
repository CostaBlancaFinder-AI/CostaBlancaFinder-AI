from sqlalchemy import text
from opportunity_ai.shared.database.postgres_connection import get_postgres_engine

engine = get_postgres_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT NOW();"))
    print("PostgreSQL connection OK")
    print(result.fetchone())
