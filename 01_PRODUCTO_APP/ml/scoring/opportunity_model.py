"""
============================================================
CostaBlancaFinder AI
Opportunity Scoring Model
============================================================

Objetivo:
Centralizar la lógica de scoring IA inmobiliario.

Este módulo representa la futura capa ML del sistema.

Futuro:
- machine learning
- weighting dinámico
- modelos predictivos
- scoring IA avanzado
- XAI
============================================================
"""

import pandas as pd


# ============================================================
# CALCULATE OPPORTUNITY SCORE
# ============================================================

def calculate_opportunity_score(
    price_m2: float,
    lifestyle_score: float,
    tourism_score: float
) -> float:
    """
    Calcula un score simple de oportunidad inmobiliaria.
    """

    if price_m2 <= 0:
        return 0

    score = (
        (lifestyle_score * 0.4) +
        (tourism_score * 0.4) +
        ((10000 / price_m2) * 0.2)
    )

    return round(score, 2)


# ============================================================
# CLASSIFY OPPORTUNITY
# ============================================================

def classify_opportunity(score: float) -> str:
    """
    Clasifica el nivel de oportunidad.
    """

    if score >= 8:
        return "Excelente"

    if score >= 6:
        return "Alta"

    if score >= 4:
        return "Media"

    return "Baja"