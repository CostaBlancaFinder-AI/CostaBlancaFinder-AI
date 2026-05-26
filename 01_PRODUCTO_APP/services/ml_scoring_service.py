"""
============================================================
CostaBlancaFinder AI
ML Scoring Service
============================================================

Objetivo:
Conectar la capa de servicios con los modelos ML de scoring.

Arquitectura:
Frontend / Pipeline
    ↓
ML Scoring Service
    ↓
ML Opportunity Model
============================================================
"""

from ml.scoring.opportunity_model import (
    calculate_opportunity_score,
    classify_opportunity,
)


def calculate_property_opportunity(
    price_m2: float,
    lifestyle_score: float,
    tourism_score: float
) -> dict:
    """
    Calcula score y clasificación de oportunidad para una propiedad.
    """

    score = calculate_opportunity_score(
        price_m2=price_m2,
        lifestyle_score=lifestyle_score,
        tourism_score=tourism_score
    )

    level = classify_opportunity(score)

    return {
        "opportunity_score": score,
        "opportunity_level": level
    }