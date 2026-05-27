"""
============================================================
CostaBlancaFinder AI
Output Saver Utility
============================================================
"""

import json
from pathlib import Path
from typing import Any, Union

import pandas as pd


# ============================================================
# PATHS
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = ROOT_DIR / "02_DATA_IA" / "raw_data"

REAL_DATA_DIR = RAW_DATA_DIR / "real"
MOCK_DATA_DIR = RAW_DATA_DIR / "mock"

REAL_DATA_DIR.mkdir(parents=True, exist_ok=True)
MOCK_DATA_DIR.mkdir(parents=True, exist_ok=True)

REAL_JSON_PATH = (
    REAL_DATA_DIR / "rentals_real_latest.json"
)

MOCK_JSON_PATH = (
    MOCK_DATA_DIR / "rentals_mock_latest.json"
)


# ============================================================
# ENSURE PARENT FOLDER
# ============================================================

def ensure_parent_folder(
    file_path: Union[str, Path]
) -> None:

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# DETECT MOCK DATA
# ============================================================

def is_mock_data(data: Any) -> bool:

    if not isinstance(data, list):
        return False

    if not data:
        return False

    source_names = {
        item.get("source_name", "")
        for item in data
        if isinstance(item, dict)
    }

    return "idealista_mock" in source_names


# ============================================================
# SAVE JSON
# ============================================================

def save_json(
    data: Any,
    output_path: Union[str, Path]
) -> None:

    ensure_parent_folder(output_path)

    # --------------------------------------------------------
    # MAIN JSON
    # --------------------------------------------------------

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    # --------------------------------------------------------
    # REAL / MOCK BACKUP
    # --------------------------------------------------------

    try:

        if is_mock_data(data):

            with open(
                MOCK_JSON_PATH,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            print(
                f"Backup MOCK guardado en: "
                f"{MOCK_JSON_PATH}"
            )

        else:

            with open(
                REAL_JSON_PATH,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            print(
                f"Backup REAL guardado en: "
                f"{REAL_JSON_PATH}"
            )

    except Exception as error:

        print("Error generando backup JSON:")
        print(error)


# ============================================================
# SAVE CSV
# ============================================================

def save_csv(
    data: pd.DataFrame,
    output_path: Union[str, Path]
) -> None:

    ensure_parent_folder(output_path)

    data.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )