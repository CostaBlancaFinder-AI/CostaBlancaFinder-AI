"""
============================================================
OpportunityAI Platform
Real Estate Repository
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI / OpportunityAI Platform

Description:
PostgreSQL repository for the Real Estate vertical.
Provides database access methods for properties and opportunities.

Created:
2026

Status:
MVP database repository
============================================================
"""

import pandas as pd
from sqlalchemy import text

from opportunity_ai.shared.database.postgres_connection import get_postgres_engine


class RealEstateRepository:
    """
    Repository for real estate properties stored in PostgreSQL/Supabase.
    """

    def __init__(self):
        self.engine = get_postgres_engine()

    def test_connection(self):
        """
        Tests PostgreSQL connection.
        """
        with self.engine.connect() as conn:
            result = conn.execute(text("SELECT NOW();"))
            return result.fetchone()

    def get_properties(self, limit: int = 100):
        """
        Returns properties from the properties table.
        """
        query = text("""
            SELECT *
            FROM properties
            LIMIT :limit
        """)

        with self.engine.connect() as conn:
            df = pd.read_sql(query, conn, params={"limit": limit})

        return df

    def get_top_opportunities(self, limit: int = 20):
        """
        Returns top properties ordered by opportunity_score.
        """
        query = text("""
            SELECT *
            FROM properties
            WHERE opportunity_score IS NOT NULL
            ORDER BY opportunity_score DESC
            LIMIT :limit
        """)

        with self.engine.connect() as conn:
            df = pd.read_sql(query, conn, params={"limit": limit})

        return df
