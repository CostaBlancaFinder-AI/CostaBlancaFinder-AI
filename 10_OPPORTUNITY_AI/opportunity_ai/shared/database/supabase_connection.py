import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import create_client


PROJECT_ROOT = Path(__file__).resolve().parents[4]
ENV_PATH = PROJECT_ROOT / "config" / ".env"

load_dotenv(ENV_PATH)


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        f"SUPABASE_URL or SUPABASE_KEY not found. Checked: {ENV_PATH}"
    )


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_supabase_client():
    return supabase
