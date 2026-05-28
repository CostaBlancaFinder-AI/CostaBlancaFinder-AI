"""
============================================================
OpportunityAI Platform
Real Estate Pipeline
============================================================
Author: George Apolo Gallardo
Project: CostaBlancaFinder AI / OpportunityAI Platform

Description:
Production-oriented real estate pipeline for CostaBlancaFinder AI.
It uses the universal PipelineEngine and initially reads from the
current legacy processed data to avoid breaking the existing MVP.

Created: 2026
Status: MVP integration layer
============================================================
"""

import pandas as pd

from opportunity_ai.core_engine.pipeline_engine import PipelineEngine
from opportunity_ai.verticals.real_estate.real_estate_config import (
    DEFAULT_CLEAN_DATA_FILE,
    DEFAULT_TOP_OPPORTUNITIES_FILE,
)


def load_clean_real_estate_data(data=None):
    """
    Loads current clean real estate data from the existing MVP output.
    """
    print(f"Loading data from: {DEFAULT_CLEAN_DATA_FILE}")

    if not DEFAULT_CLEAN_DATA_FILE.exists():
        print("Clean data file not found. Returning empty DataFrame.")
        return pd.DataFrame()

    return pd.read_csv(DEFAULT_CLEAN_DATA_FILE)


def validate_data(df: pd.DataFrame):
    """
    Basic validation for real estate opportunity data.
    """
    print("Validating real estate data...")

    if df.empty:
        print("No data available.")
        return df

    print(f"Rows loaded: {len(df)}")
    print(f"Columns: {list(df.columns)}")

    return df


def select_top_opportunities(df: pd.DataFrame):
    """
    Selects top opportunities using opportunity_score if available.
    """
    print("Selecting top real estate opportunities...")

    if df.empty:
        return df

    if "opportunity_score" in df.columns:
        return df.sort_values(by="opportunity_score", ascending=False).head(20)

    print("opportunity_score column not found. Returning first 20 rows.")
    return df.head(20)


def export_top_opportunities(df: pd.DataFrame):
    """
    Exports top opportunities to the legacy output file for compatibility.
    """
    print(f"Exporting top opportunities to: {DEFAULT_TOP_OPPORTUNITIES_FILE}")

    if df.empty:
        print("No opportunities to export.")
        return df

    DEFAULT_TOP_OPPORTUNITIES_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DEFAULT_TOP_OPPORTUNITIES_FILE, index=False)

    return df


def build_real_estate_pipeline():
    """
    Builds the CostaBlancaFinder AI real estate pipeline.
    """
    pipeline = PipelineEngine("CostaBlancaFinder AI Real Estate Pipeline")

    pipeline.add_step("load_clean_real_estate_data", load_clean_real_estate_data)
    pipeline.add_step("validate_data", validate_data)
    pipeline.add_step("select_top_opportunities", select_top_opportunities)
    pipeline.add_step("export_top_opportunities", export_top_opportunities)

    return pipeline


if __name__ == "__main__":
    pipeline = build_real_estate_pipeline()
    result = pipeline.run()
    print("Final result preview:")
    print(result.head() if hasattr(result, "head") else result)
