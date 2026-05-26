"""
============================================================
CostaBlancaFinder AI
Properties API Routes
============================================================
"""

from fastapi import APIRouter

from database.property_repository import load_properties

# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)


# ============================================================
# GET PROPERTIES
# ============================================================

@router.get("/")
def get_properties():
    """
    Devuelve propiedades inmobiliarias.
    """

    df = load_properties()

    return df.head(20).to_dict(
        orient="records"
    )