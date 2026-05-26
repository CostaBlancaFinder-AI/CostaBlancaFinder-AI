"""
============================================================
CostaBlancaFinder AI
FastAPI Backend
============================================================
"""

from fastapi import FastAPI

from api.routes.properties import router as properties_router
from api.routes.recommendations import router as recommendations_router


# ============================================================
# CREATE APP
# ============================================================

app = FastAPI(
    title="CostaBlancaFinder AI",
    version="1.0.0"
)


# ============================================================
# ROOT ENDPOINT
# ============================================================

@app.get("/")
def root():
    """
    Endpoint principal API.
    """

    return {
        "message": "CostaBlancaFinder AI API funcionando"
    }


# ============================================================
# ROUTES
# ============================================================

app.include_router(properties_router)
app.include_router(recommendations_router)