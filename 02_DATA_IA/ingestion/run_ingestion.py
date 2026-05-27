"""
============================================================
CostaBlancaFinder AI
Ingestion Pipeline
============================================================
"""

from clients.idealista_client import IdealistaClient
from normalizers.property_normalizer import normalize_properties

OUTPUT_FILE = "02_DATA_IA/datasets/rentals_raw.csv"


def main():
    client = IdealistaClient()

    raw_properties = client.search_rentals(
        location="Costa Blanca"
    )

    df = normalize_properties(
        raw_properties=raw_properties,
        source_name="Idealista"
    )

    if df.empty:
        print("No se han obtenido propiedades desde la API.")
        return

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("Ingesta completada.")
    print(f"Archivo generado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()