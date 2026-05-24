import pandas as pd

INPUT_FILE = "02_DATA_IA/datasets/rentals_raw.csv"
OUTPUT_FILE = "02_DATA_IA/processed_data/rentals_scored.csv"

df = pd.read_csv(INPUT_FILE)

df["price_m2"] = df["price_eur"] / df["area_m2"]

def calculate_score(row):
    score = 0

    if row["price_m2"] < 10:
        score += 40
    elif row["price_m2"] < 13:
        score += 25
    else:
        score += 10

    if row["city"] in ["Villajoyosa", "Benidorm", "Finestrat"]:
        score += 20

    if row["rooms"] >= 2:
        score += 20

    if "playa" in row["title"].lower() or "vistas mar" in row["title"].lower():
        score += 20

    return score

df["opportunity_score"] = df.apply(calculate_score, axis=1)

df = df.sort_values(by="opportunity_score", ascending=False)

df.to_csv(OUTPUT_FILE, index=False)

print("Scoring finalizado.")
print(df[["city", "zone", "price_eur", "area_m2", "price_m2", "opportunity_score"]])