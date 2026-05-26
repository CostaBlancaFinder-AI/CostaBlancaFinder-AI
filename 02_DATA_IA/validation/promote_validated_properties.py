# ============================================================
# CostaBlancaFinder AI
# Promote Validated Real Properties
# ============================================================

import pandas as pd

INPUT_FILE = "02_DATA_IA/raw_data/propiedades_reales_pendientes.csv"
OUTPUT_FILE = "02_DATA_IA/datasets/rentals_real_sample.csv"

OUTPUT_COLUMNS = [
    "title",
    "city",
    "zone",
    "price_eur",
    "area_m2",
    "rooms",
    "bathrooms",
    "property_type",
    "source_url",
    "source_name"
]


def main():
    df = pd.read_csv(INPUT_FILE)

    if df.empty:
        print("No hay propiedades pendientes.")
        return

    validated = df[df["status"] == "validated"]

    if validated.empty:
        print("No hay propiedades validadas para promover.")
        return

    final_df = validated[OUTPUT_COLUMNS]

    final_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Propiedades validadas promovidas correctamente.")
    print(f"Total promovidas: {len(final_df)}")
    print(f"Archivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()