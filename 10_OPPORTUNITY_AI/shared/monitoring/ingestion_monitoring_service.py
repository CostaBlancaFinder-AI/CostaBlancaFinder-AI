"""
============================================================
CostaBlancaFinder AI
Ingestion Monitoring Service
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI

Description:
Service layer responsible for reading ingestion execution logs
from PostgreSQL/Supabase and exposing pipeline monitoring
metrics to the Streamlit dashboard.

Architecture:
PropTech + AI + PostgreSQL + Supabase + Streamlit

Created:
2026

Status:
MVP / Production-oriented architecture
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


def load_ingestion_logs(limit: int = 10) -> pd.DataFrame:
    """
    Loads the latest ingestion execution logs.
    """

    engine = get_engine()

    query = text(
        """
        SELECT
            source_name,
            status,
            total_raw,
            total_normalized,
            total_filtered,
            total_saved,
            message,
            created_at
        FROM ingestion_logs
        ORDER BY created_at DESC
        LIMIT :limit
        """
    )

    return pd.read_sql(
        query,
        engine,
        params={"limit": limit}
    )


def get_last_ingestion_status() -> str:
    """
    Returns the status of the latest ingestion execution.
    """

    logs = load_ingestion_logs(limit=1)

    if logs.empty:
        return "NO DATA"

    return logs.iloc[0]["status"]


def get_last_ingestion_summary() -> dict:
    """
    Returns the latest ingestion execution as a dictionary.
    """

    logs = load_ingestion_logs(limit=1)

    if logs.empty:
        return {
            "status": "NO DATA",
            "source_name": "N/A",
            "total_raw": 0,
            "total_normalized": 0,
            "total_filtered": 0,
            "total_saved": 0,
            "message": "No ingestion logs available.",
            "created_at": None
        }

    return logs.iloc[0].to_dict()