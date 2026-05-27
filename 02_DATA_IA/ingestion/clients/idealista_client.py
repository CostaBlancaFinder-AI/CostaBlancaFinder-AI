"""
============================================================
CostaBlancaFinder AI
Idealista Client
============================================================
"""

import os
from dotenv import load_dotenv


load_dotenv("config/.env")

IDEALISTA_API_KEY = os.getenv("IDEALISTA_API_KEY", "").strip()
IDEALISTA_API_SECRET = os.getenv("IDEALISTA_API_SECRET", "").strip()


MOCK_PROPERTIES = [
    {
        "title": "Apartamento moderno en Villajoyosa",
        "city": "Villajoyosa",
        "zone": "Centro",
        "price_eur": 950,
        "area_m2": 85,
        "rooms": 2,
        "bathrooms": 1,
        "property_type": "apartment",
        "source_url": "https://www.idealista.com/mock1"
    },
    {
        "title": "Ático con vistas al mar en Benidorm",
        "city": "Benidorm",
        "zone": "Playa Levante",
        "price_eur": 1450,
        "area_m2": 110,
        "rooms": 3,
        "bathrooms": 2,
        "property_type": "penthouse",
        "source_url": "https://www.idealista.com/mock2"
    },
    {
        "title": "Estudio económico en Alicante",
        "city": "Alicante",
        "zone": "Centro",
        "price_eur": 650,
        "area_m2": 45,
        "rooms": 1,
        "bathrooms": 1,
        "property_type": "studio",
        "source_url": "https://www.idealista.com/mock3"
    }
]


def search_rentals(location: str) -> list:
    """
    Busca alquileres en una localización.

    Si no hay credenciales reales completas, usa MOCK DATA.
    """

    print("\n[Idealista Client]")
    print(f"Buscando alquileres en: {location}")

    if not IDEALISTA_API_KEY or not IDEALISTA_API_SECRET:
        print("\nModo MOCK activado.")
        print("No hay credenciales reales completas de Idealista.")
        return MOCK_PROPERTIES

    print("\nAPI REAL pendiente de implementación.")
    print("Usando MOCK DATA temporalmente para no romper el pipeline.")

    return MOCK_PROPERTIES


if __name__ == "__main__":
    properties = search_rentals("Costa Blanca")
    print(f"\nPropiedades encontradas: {len(properties)}")