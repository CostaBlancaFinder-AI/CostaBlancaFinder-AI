"""
CostaBlancaFinder AI
Central Project Configuration
"""

from pathlib import Path


# =========================================================
# ROOT PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parents[2]


# =========================================================
# DATASETS
# =========================================================

RAW_DATASET = BASE_DIR / "02_DATA_IA/datasets/rentals_raw.csv"

SCORED_DATASET = (
    BASE_DIR / "02_DATA_IA/processed_data/rentals_scored_v2.csv"
)

ENRICHED_DATASET = (
    BASE_DIR / "02_DATA_IA/processed_data/rentals_enriched.csv"
)

RECOMMENDATIONS_DATASET = (
    BASE_DIR / "02_DATA_IA/recommendations/recommended_properties.csv"
)
OSM_LOCATIONS_DATASET = (
    BASE_DIR / "02_DATA_IA/datasets/osm_locations.csv"
)

# =========================================================
# LOGS
# =========================================================

PIPELINE_LOG = (
    BASE_DIR / "03_AUTOMATIZACIONES/logs/pipeline.log"
)


# =========================================================
# APP CONFIG
# =========================================================

APP_NAME = "CostaBlancaFinder AI"

APP_VERSION = "0.1 MVP"

DEFAULT_CITY = "Villajoyosa"


# =========================================================
# FUTURE APIs
# =========================================================

IDEALISTA_API = None

OPENAI_API = None

TELEGRAM_BOT_TOKEN = None


# =========================================================
# FUTURE DATABASE
# =========================================================

POSTGRESQL_URL = None

SUPABASE_URL = None