"""
============================================================
OpportunityAI Platform
Real Estate Pipeline
============================================================
Author: George Apolo Gallardo
Project: CostaBlancaFinder AI / OpportunityAI Platform
Created: 2026
Status: PostgreSQL integrated pipeline
============================================================
"""

from opportunity_ai.core_engine.pipeline_engine import PipelineEngine
from opportunity_ai.verticals.real_estate.repositories.real_estate_repository import (
    RealEstateRepository,
)


def load_from_database(data=None):
    print("Loading real estate data from PostgreSQL...")
    repo = RealEstateRepository()
    return repo.get_properties(limit=500)


def validate_data(df):
    print("Validating real estate data...")

    if df.empty:
        print("No data available.")
        return df

    print(f"Rows loaded: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    return df


def select_top_opportunities(df):
    print("Selecting top real estate opportunities...")

    if df.empty:
        return df

    if "opportunity_score" in df.columns:
        return df.sort_values(by="opportunity_score", ascending=False).head(20)

    return df.head(20)


def build_real_estate_pipeline():
    pipeline = PipelineEngine("CostaBlancaFinder AI PostgreSQL Pipeline")
    pipeline.add_step("load_from_database", load_from_database)
    pipeline.add_step("validate_data", validate_data)
    pipeline.add_step("select_top_opportunities", select_top_opportunities)
    return pipeline


if __name__ == "__main__":
    pipeline = build_real_estate_pipeline()
    result = pipeline.run()
    print("Final result preview:")
    print(result.head() if hasattr(result, "head") else result)
