# ============================================================
# CostaBlancaFinder AI
# Real Properties Data Validator
# ============================================================

import pandas as pd

INPUT_FILE = "02_DATA_IA/raw_data/propiedades_reales_pendientes.csv"

REQUIRED_COLUMNS = [
    "capture_date",
    "title",
    "city",
    "zone",
    "price_eur",
    "area_m2",
    "rooms",
    "bathrooms",
    "property_type",
    "source_name",
    "source_url",
    "notes",
    "status"
]


def validate_columns(df: pd.DataFrame):
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Faltan columnas obligatorias: {missing_columns}"
        )


def validate_required_values(df: pd.DataFrame):
    required_values = [
        "title",
        "city",
        "zone",
        "price_eur",
        "area_m2",
        "rooms",
        "source_url"
    ]

    for column in required_values:
        if df[column].isnull().any():
            raise ValueError(
                f"Hay valores vacíos en la columna: {column}"
            )


def main():
    df = pd.read_csv(INPUT_FILE)

    validate_columns(df)

    if df.empty:
        print("El archivo existe, pero todavía no contiene propiedades.")
        return

    validate_required_values(df)

    print("Validación correcta.")
    print(f"Propiedades validadas: {len(df)}")


if __name__ == "__main__":
    main()