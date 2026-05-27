"""
============================================================
CostaBlancaFinder AI
Central Configuration
============================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv("config/.env")


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


RAW_RENTALS_JSON = RAW_DATA_PATH / "rentals_raw.json"

CLEAN_RENTALS_CSV = (
    PROCESSED_DATA_PATH / "rentals_clean.csv"
)

TOP_OPPORTUNITIES_CSV = (
    PROCESSED_DATA_PATH / "top_opportunities.csv"
)


DEFAULT_SEARCH_LOCATION = "Costa Blanca"


APIFY_API_TOKEN = os.getenv(
    "APIFY_API_TOKEN",
    ""
).strip()

APIFY_DATASET_ID = os.getenv(
    "APIFY_DATASET_ID",
    ""
).strip()


IDEALISTA_API_KEY = os.getenv(
    "IDEALISTA_API_KEY",
    ""
).strip()

IDEALISTA_API_SECRET = os.getenv(
    "IDEALISTA_API_SECRET",
    ""
).strip()