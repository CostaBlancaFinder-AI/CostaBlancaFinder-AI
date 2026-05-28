from opportunity_ai.verticals.real_estate.services.opportunity_service import (
    RealEstateOpportunityService
)

service = RealEstateOpportunityService()

print("Opportunity summary:")
print(service.get_summary())

print("\nTop opportunities:")
df = service.get_top_opportunities(limit=5)
print(df.head())
