"""
============================================================
CostaBlancaFinder AI
Opportunity Scoring Model
============================================================

Objetivo:
Centralizar la lógica de scoring inmobiliario reutilizable.

Este módulo pertenece a la capa ML del sistema y puede ser usado por:
- pipelines
- servicios
- futuros modelos predictivos
- backend FastAPI
============================================================
"""


def calculate_price_score(price_m2: float) -> int:
    if price_m2 < 10:
        return 40
    elif price_m2 < 13:
        return 25
    elif price_m2 < 16:
        return 15
    else:
        return 5


def calculate_location_score(city: str) -> int:
    premium_locations = [
        "Villajoyosa",
        "Benidorm",
        "Finestrat",
        "Altea"
    ]

    if city in premium_locations:
        return 20

    return 10


def calculate_room_score(rooms: int) -> int:
    if rooms >= 3:
        return 20
    elif rooms == 2:
        return 15
    else:
        return 8


def calculate_tourism_score(title: str) -> int:
    title = str(title).lower()

    keywords = [
        "playa",
        "vistas mar",
        "mar",
        "turístico",
        "cala",
        "centro"
    ]

    score = 0

    for keyword in keywords:
        if keyword in title:
            score += 5

    return min(score, 20)


def classify_opportunity_level(score: int) -> str:
    if score >= 85:
        return "High Opportunity"

    if score >= 65:
        return "Medium Opportunity"

    return "Low Opportunity"


def calculate_opportunity_score(
    price_score: int,
    location_score: int,
    room_score: int,
    tourism_score: int
) -> int:
    return (
        price_score
        + location_score
        + room_score
        + tourism_score
    )