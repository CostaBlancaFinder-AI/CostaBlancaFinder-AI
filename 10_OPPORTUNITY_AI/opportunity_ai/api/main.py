"""
============================================================
OpportunityAI Platform
FastAPI Main Application
============================================================
Author: George Apolo Gallardo
Project: OpportunityAI Platform
Created: 2026
============================================================
"""

from fastapi import FastAPI

from opportunity_ai.api.routes.real_estate_routes import router as real_estate_router


app = FastAPI(
    title="OpportunityAI Platform API",
    description="Global AI platform for opportunity detection across multiple verticals.",
    version="0.1.0"
)

app.include_router(real_estate_router)


@app.get("/")
def root():
    return {
        "platform": "OpportunityAI",
        "status": "running",
        "available_verticals": ["real_estate"]
    }
