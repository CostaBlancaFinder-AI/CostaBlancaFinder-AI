"""
============================================================
CostaBlancaFinder AI
Idealista API Client
============================================================
"""

import os
from dotenv import load_dotenv

load_dotenv("config/.env")


class IdealistaClient:
    """
    Cliente base para futura conexión con Idealista API.
    """

    def __init__(self):
        self.api_key = os.getenv("IDEALISTA_API_KEY")
        self.api_secret = os.getenv("IDEALISTA_API_SECRET")

    def search_rentals(self, location: str):
        """
        Placeholder para búsqueda de alquileres.
        """

        print(f"Buscando alquileres en Idealista para: {location}")

        return []