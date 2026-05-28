"""
============================================================
OpportunityAI Platform
PostgreSQL Connection
============================================================
Author: George Apolo Gallardo
Project: OpportunityAI Platform
Created: 2026
============================================================
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine


PROJECT_ROOT = Path(__file__).resolve().parents[4]
ENV_PATH = PROJECT_ROOT / "config" / ".env"

load_dotenv(ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(f"DATABASE_URL not found. Checked: {ENV_PATH}")

engine = create_engine(DATABASE_URL)


def get_postgres_engine():
    return engine
