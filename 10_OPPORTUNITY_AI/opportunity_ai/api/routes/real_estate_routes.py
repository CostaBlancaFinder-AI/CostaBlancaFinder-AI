"""
============================================================
OpportunityAI Platform
Real Estate API Routes
============================================================
Author: George Apolo Gallardo
Project: OpportunityAI Platform / CostaBlancaFinder AI
Created: 2026
============================================================
"""

from fastapi import APIRouter

from opportunity_ai.verticals.real_estate.services.opportunity_service import (
    RealEstateOpportunityService,
)


router = APIRouter(prefix="/real-estate", tags=["Real Estate"])


@router.get("/summary")
def get_real_estate_summary():
    service = RealEstateOpportunityService()
    return service.get_summary()


@router.get("/top-opportunities")
def get_top_opportunities(limit: int = 20):
    service = RealEstateOpportunityService()
    df = service.get_top_opportunities(limit=limit)
    return df.to_dict(orient="records")
