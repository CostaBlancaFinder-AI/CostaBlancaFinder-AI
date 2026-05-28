from opportunity_ai.verticals.real_estate.repositories.real_estate_repository import (
    RealEstateRepository
)

repo = RealEstateRepository()

print("Testing DB connection...")
print(repo.test_connection())

print("\nLoading properties...")
df = repo.get_properties(limit=5)
print(df.head())
print(f"Rows loaded: {len(df)}")

print("\nLoading top opportunities...")
top_df = repo.get_top_opportunities(limit=5)
print(top_df.head())
print(f"Top opportunities loaded: {len(top_df)}")
