"""
============================================================
CostaBlancaFinder AI
Central Configuration
============================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]


# ============================================================
# ENVIRONMENT VARIABLES
# ============================================================

ENV_FILE = PROJECT_ROOT / "config" / ".env"

load_dotenv(ENV_FILE)


# ============================================================
# GENERAL CONFIG
# ============================================================

PROJECT_NAME = os.getenv("PROJECT_NAME", "CostaBlancaFinder")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"


# ============================================================
# PATHS
# ============================================================

RAW_DATA_PATH = PROJECT_ROOT / os.getenv(
    "RAW_DATA_PATH",
    "02_DATA_IA/raw_data"
)

PROCESSED_DATA_PATH = PROJECT_ROOT / os.getenv(
    "PROCESSED_DATA_PATH",
    "02_DATA_IA/processed_data"
)

RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)


RAW_RENTALS_JSON = RAW_DATA_PATH / "rentals_raw.json"

CLEAN_RENTALS_CSV = PROCESSED_DATA_PATH / "rentals_clean.csv"

TOP_OPPORTUNITIES_CSV = PROCESSED_DATA_PATH / "top_opportunities.csv"

EXECUTIVE_SUMMARY_MD = PROCESSED_DATA_PATH / "executive_summary.md"


# ============================================================
# DEFAULT SEARCH
# ============================================================

DEFAULT_SEARCH_LOCATION = os.getenv(
    "DEFAULT_SEARCH_LOCATION",
    "Costa Blanca"
)

DEFAULT_IDEALISTA_URL = os.getenv(
    "DEFAULT_IDEALISTA_URL",
    "https://www.idealista.com/alquiler-viviendas/alicante-alacant-alicante/"
)

DEFAULT_MAX_ITEMS = int(
    os.getenv("DEFAULT_MAX_ITEMS", "50")
)


# ============================================================
# APIFY CONFIG
# ============================================================

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN", "").strip()

APIFY_DATASET_ID = os.getenv("APIFY_DATASET_ID", "").strip()

APIFY_IDEALISTA_ACTOR_ID = os.getenv(
    "APIFY_IDEALISTA_ACTOR_ID",
    ""
).strip()

APIFY_FOTOCASA_ACTOR_ID = os.getenv(
    "APIFY_FOTOCASA_ACTOR_ID",
    ""
).strip()

APIFY_HABITACLIA_ACTOR_ID = os.getenv(
    "APIFY_HABITACLIA_ACTOR_ID",
    ""
).strip()


# ============================================================
# OFFICIAL API CONFIG
# ============================================================

IDEALISTA_API_KEY = os.getenv("IDEALISTA_API_KEY", "").strip()
IDEALISTA_API_SECRET = os.getenv("IDEALISTA_API_SECRET", "").strip()

FOTOCASA_API_KEY = os.getenv("FOTOCASA_API_KEY", "").strip()

HABITACLIA_API_KEY = os.getenv("HABITACLIA_API_KEY", "").strip()


# ============================================================
# VALIDATION HELPERS
# ============================================================

def has_apify_config() -> bool:
    """
    Verifica si existe configuración mínima de Apify.
    """
    return bool(APIFY_API_TOKEN)


def has_idealista_apify_config() -> bool:
    """
    Verifica si existe configuración mínima para Idealista vía Apify.
    """
    return bool(APIFY_API_TOKEN and APIFY_IDEALISTA_ACTOR_ID)


def print_config_status() -> None:
    """
    Muestra estado básico de configuración sin revelar secretos.
    """
    print("============================================================")
    print("CostaBlancaFinder AI - Config Status")
    print("============================================================")
    print(f"PROJECT_ROOT: {PROJECT_ROOT}")
    print(f"ENV_FILE: {ENV_FILE}")
    print(f"ENVIRONMENT: {ENVIRONMENT}")
    print(f"RAW_DATA_PATH: {RAW_DATA_PATH}")
    print(f"PROCESSED_DATA_PATH: {PROCESSED_DATA_PATH}")
    print(f"APIFY_API_TOKEN: {'OK' if APIFY_API_TOKEN else 'MISSING'}")
    print(
        "APIFY_IDEALISTA_ACTOR_ID: "
        f"{'OK' if APIFY_IDEALISTA_ACTOR_ID else 'MISSING'}"
    )
    print("============================================================")