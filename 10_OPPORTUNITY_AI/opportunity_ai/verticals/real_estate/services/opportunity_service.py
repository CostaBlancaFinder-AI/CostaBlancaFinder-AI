"""
============================================================
OpportunityAI Platform
Real Estate Opportunity Service
============================================================

Author:
George Apolo Gallardo

Project:
CostaBlancaFinder AI / OpportunityAI Platform

Description:
Service layer for retrieving, ranking and preparing real estate
opportunities from PostgreSQL/Supabase.

Created:
2026

Status:
MVP service layer
============================================================
"""

from opportunity_ai.verticals.real_estate.repositories.real_estate_repository import (
    RealEstateRepository,
)


class RealEstateOpportunityService:
    """
    Business service for real estate opportunities.
    """

    def __init__(self):
        self.repository = RealEstateRepository()

    def get_all_properties(self, limit: int = 100):
        """
        Returns all available properties.
        """
        return self.repository.get_properties(limit=limit)

    def get_top_opportunities(self, limit: int = 20):
        """
        Returns ranked real estate opportunities.
        """
        return self.repository.get_top_opportunities(limit=limit)

    def get_summary(self):
        """
        Returns basic opportunity summary.
        """
        df = self.repository.get_properties(limit=1000)

        if df.empty:
            return {
                "total_properties": 0,
                "avg_opportunity_score": 0,
                "max_opportunity_score": 0,
            }

        return {
            "total_properties": len(df),
            "avg_opportunity_score": round(df["opportunity_score"].mean(), 2)
            if "opportunity_score" in df.columns else None,
            "max_opportunity_score": round(df["opportunity_score"].max(), 2)
            if "opportunity_score" in df.columns else None,
        }
