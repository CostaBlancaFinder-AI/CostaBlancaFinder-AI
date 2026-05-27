"""
============================================================
CostaBlancaFinder AI
Ingestion Report
============================================================

Objetivo:
Generar un resumen rápido del CSV limpio generado por
el pipeline de ingesta.
============================================================
"""

import pandas as pd

from config import CLEAN_RENTALS_CSV


def generate_report() -> None:
    """
    Genera informe básico del dataset limpio.
    """

    print("=" * 60)
    print("CostaBlancaFinder AI - Ingestion Report")
    print("=" * 60)

    if not CLEAN_RENTALS_CSV.exists():
        print(f"No existe el archivo: {CLEAN_RENTALS_CSV}")
        return

    df = pd.read_csv(CLEAN_RENTALS_CSV)

    if df.empty:
        print("El dataset está vacío.")
        return

    print(f"\nArchivo analizado: {CLEAN_RENTALS_CSV}")
    print(f"Filas: {len(df)}")
    print(f"Columnas: {len(df.columns)}")

    print("\nColumnas disponibles:")
    for column in df.columns:
        print(f"- {column}")

    if "source_name" in df.columns:
        print("\nFuentes:")
        print(df["source_name"].value_counts())

    if "city" in df.columns:
        print("\nCiudades:")
        print(df["city"].value_counts())

    if "price_eur" in df.columns:
        print("\nPrecio:")
        print(df["price_eur"].describe())

    if "area_m2" in df.columns:
        print("\nSuperficie:")
        print(df["area_m2"].describe())

    print("\nInforme finalizado correctamente.")


if __name__ == "__main__":
    generate_report()