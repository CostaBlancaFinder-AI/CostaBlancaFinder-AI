"""
============================================================
CostaBlancaFinder AI
Recommendations API Routes
============================================================
"""

from fastapi import APIRouter

from services.recommendation_service import (
    load_recommendations,
    has_recommendations,
)

# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


# ============================================================
# GET RECOMMENDATIONS
# ============================================================

@router.get("/")
def get_recommendations():
    """
    Devuelve recomendaciones IA.
    """

    recommendations = load_recommendations()

    if not has_recommendations(recommendations):
        return {
            "message": "No hay recomendaciones"
        }

    return recommendations.head(10).to_dict(
        orient="records"
    )