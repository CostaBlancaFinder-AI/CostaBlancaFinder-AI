"""
============================================================
OpportunityAI Platform
Real Estate Config
============================================================
Author: George Apolo Gallardo
Project: CostaBlancaFinder AI / OpportunityAI Platform
Created: 2026
============================================================
"""

from pathlib import Path

REAL_ESTATE_ROOT = Path(__file__).resolve().parent

DATA_DIR = REAL_ESTATE_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
REPORTS_DIR = DATA_DIR / "reports"

LEGACY_PROCESSED_DATA_DIR = Path("02_DATA_IA/processed_data")
LEGACY_RAW_DATA_DIR = Path("02_DATA_IA/raw_data")

DEFAULT_CLEAN_DATA_FILE = LEGACY_PROCESSED_DATA_DIR / "rentals_clean.csv"
DEFAULT_SCORED_DATA_FILE = LEGACY_PROCESSED_DATA_DIR / "rentals_scored.csv"
DEFAULT_TOP_OPPORTUNITIES_FILE = LEGACY_PROCESSED_DATA_DIR / "top_opportunities.csv"
