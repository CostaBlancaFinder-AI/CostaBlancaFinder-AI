"""
============================================================
CostaBlancaFinder AI
Output Validator
============================================================

Objetivo:
Validar que los archivos generados por el pipeline existen
y contienen datos correctos.
============================================================
"""

import pandas as pd

from config import RAW_RENTALS_JSON, CLEAN_RENTALS_CSV


def validate_outputs() -> bool:
    """
    Valida la existencia y contenido básico de los outputs.
    """

    print("\nValidando outputs del pipeline...")

    if not RAW_RENTALS_JSON.exists():
        print(f"No existe JSON bruto: {RAW_RENTALS_JSON}")
        return False

    if not CLEAN_RENTALS_CSV.exists():
        print(f"No existe CSV limpio: {CLEAN_RENTALS_CSV}")
        return False

    df = pd.read_csv(CLEAN_RENTALS_CSV)

    if df.empty:
        print("El CSV limpio está vacío.")
        return False

    print(f"JSON encontrado: {RAW_RENTALS_JSON}")
    print(f"CSV encontrado: {CLEAN_RENTALS_CSV}")
    print(f"Filas en CSV: {len(df)}")
    print(f"Columnas: {list(df.columns)}")

    print("\nValidación correcta.")
    return True


if __name__ == "__main__":
    validate_outputs()