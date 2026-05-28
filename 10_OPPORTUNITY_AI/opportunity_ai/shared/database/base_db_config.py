"""
============================================================
CostaBlancaFinder AI
Database Configuration
============================================================
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine


ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / "config" / ".env"

load_dotenv(ENV_FILE)


DATABASE_URL = os.getenv("DATABASE_URL", "").strip()


def get_database_url() -> str:
    if not DATABASE_URL:
        raise ValueError(
            "DATABASE_URL no está configurado en config/.env"
        )

    return DATABASE_URL


def get_engine():
    return create_engine(
        get_database_url(),
        echo=False,
        future=True
    )