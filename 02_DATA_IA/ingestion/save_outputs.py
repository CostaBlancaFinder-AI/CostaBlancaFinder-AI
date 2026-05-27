"""
============================================================
CostaBlancaFinder AI
Output Saver Utility
============================================================

Objetivo:
Guardar datos en formatos estándar:

1. JSON bruto
2. CSV limpio
============================================================
"""

import json
from pathlib import Path
from typing import Any, Union

import pandas as pd


# ============================================================
# ENSURE PARENT FOLDER
# ============================================================

def ensure_parent_folder(
    file_path: Union[str, Path]
) -> None:
    """
    Crea carpeta padre si no existe.
    """

    Path(file_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# SAVE JSON
# ============================================================

def save_json(
    data: Any,
    output_path: Union[str, Path]
) -> None:
    """
    Guarda datos en JSON.
    """

    ensure_parent_folder(output_path)

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


# ============================================================
# SAVE CSV
# ============================================================

def save_csv(
    data: pd.DataFrame,
    output_path: Union[str, Path]
) -> None:
    """
    Guarda DataFrame en CSV.
    """

    ensure_parent_folder(output_path)

    data.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )