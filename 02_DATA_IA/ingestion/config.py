"""
============================================================
CostaBlancaFinder AI
Central Configuration
============================================================

Objetivo:
Centralizar toda la configuración del pipeline
de ingesta y procesamiento.

Ventajas:
- evita hardcodear rutas
- facilita escalabilidad
- facilita despliegues
- facilita mantenimiento
============================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# ============================================================
# LOAD ENV
# ============================================================

load_dotenv("config/.env")


# ============================================================
# PROJECT
# ============================================================

PROJECT_NAME = os.getenv(
    "PROJECT_NAME",
    "CostaBlancaFinder"
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
) == "True"


# ============================================================
# DATA PATHS
# ============================================================

RAW_DATA_PATH = Path(
    os.getenv(
        "RAW_DATA_PATH",
        "02_DATA_IA/raw_data"
    )
)

PROCESSED_DATA_PATH = Path(
    os.getenv(
        "PROCESSED_DATA_PATH",
        "02_DATA_IA/processed_data"
    )
)


# ============================================================
# OUTPUT FILES
# ============================================================

RAW_RENTALS_JSON = RAW_DATA_PATH / "rentals_raw.json"

CLEAN_RENTALS_CSV = (
    PROCESSED_DATA_PATH / "rentals_clean.csv"
)


# ============================================================
# SEARCH CONFIG
# ============================================================

DEFAULT_SEARCH_LOCATION = "Costa Blanca"


# ============================================================
# APIFY
# ============================================================

APIFY_API_TOKEN = os.getenv(
    "APIFY_API_TOKEN",
    ""
).strip()

APIFY_DATASET_ID = os.getenv(
    "APIFY_DATASET_ID",
    ""
).strip()


# ============================================================
# IDEALISTA
# ============================================================

IDEALISTA_API_KEY = os.getenv(
    "IDEALISTA_API_KEY",
    ""
).strip()

IDEALISTA_API_SECRET = os.getenv(
    "IDEALISTA_API_SECRET",
    ""
).strip()