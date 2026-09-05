"""
generate_sample_data.py

Generates a synthetic Airbnb listings dataset that mirrors the schema and
general statistical patterns of the Inside Airbnb "listings.csv" file for
New York City. Use this to prototype the Power BI dashboard before (or
instead of) plugging in real Inside Airbnb data.

Run:
    python generate_sample_data.py

Output:
    data/raw/listings.csv
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

N = 5000  # number of synthetic listings

boroughs = {
    "Manhattan": ["Harlem", "Upper West Side", "Chelsea", "East Village",
                  "Financial District", "Midtown", "Hell's Kitchen"],
    "Brooklyn": ["Williamsburg", "Bushwick", "Park Slope", "Bedford-Stuyvesant",
                 "Greenpoint", "Crown Heights", "DUMBO"],
    "Queens": ["Astoria", "Long Island City", "Flushing", "Jamaica", "Ridgewood"],
    "Bronx": ["Fordham", "Riverdale", "Mott Haven"],
    "Staten Island": ["St. George", "Tottenville"],
}

room_types = ["Entire home/apt", "Private room", "Shared room", "Hotel room"]
room_type_weights = [0.52, 0.42, 0.04, 0.02]

# Base price multipliers per borough to keep prices realistic
borough_price_base = {
    "Manhattan": 220,
    "Brooklyn": 150,
    "Queens": 110,
    "Bronx": 85,
    "Staten Island": 95,
}

rows = []
for i in range(1, N + 1):
    borough = np.random.choice(list(boroughs.keys()), p=[0.32, 0.34, 0.20, 0.09, 0.05])
    neighbourhood = np.random.choice(boroughs[borough])
    room_type = np.random.choice(room_types, p=room_type_weights)

    base_price = borough_price_base[borough]
    room_multiplier = {"Entire home/apt": 1.3, "Private room": 0.7,
                        "Shared room": 0.4, "Hotel room": 1.6}[room_type]
    price = max(20, np.random.gamma(shape=4.0, scale=base_price * room_multiplier / 4.0))

    minimum_nights = np.random.choice([1, 2, 3, 5, 7, 14, 30], p=[0.35, 0.2, 0.15, 0.1, 0.1, 0.07, 0.03])
    number_of_reviews = int(np.random.exponential(scale=25))
    reviews_per_month = round(number_of_reviews / np.random.uniform(6, 48), 2) if number_of_reviews > 0 else 0.0
    availability_365 = int(np.clip(np.random.normal(150, 110), 0, 365))
    calculated_host_listings_count = np.random.choice([1, 1, 1, 2, 3, 5, 10], p=[0.55, 0.1, 0.1, 0.1, 0.08, 0.04, 0.03])
    host_is_superhost = np.random.choice(["t", "f"], p=[0.22, 0.78])

    last_review = (
        (datetime(2026, 8, 1) - timedelta(days=int(np.random.exponential(scale=120)))).strftime("%Y-%m-%d")
        if number_of_reviews > 0 else ""
    )

    # rough NYC bounding box, nudged per borough
    borough_coords = {
        "Manhattan": (40.776, -73.971),
        "Brooklyn": (40.678, -73.944),
        "Queens": (40.728, -73.794),
        "Bronx": (40.837, -73.886),
        "Staten Island": (40.579, -74.151),
    }
    lat0, lon0 = borough_coords[borough]
    latitude = round(lat0 + np.random.normal(0, 0.02), 6)
    longitude = round(lon0 + np.random.normal(0, 0.02), 6)

    rows.append({
        "id": 1000000 + i,
        "name": f"{room_type} in {neighbourhood}",
        "host_id": 500000 + (i % 1800),
        "host_name": f"Host{(i % 1800)}",
        "host_is_superhost": host_is_superhost,
        "neighbourhood_group": borough,
        "neighbourhood": neighbourhood,
        "latitude": latitude,
        "longitude": longitude,
        "room_type": room_type,
        "price": round(price, 2),
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "last_review": last_review,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": calculated_host_listings_count,
        "availability_365": availability_365,
    })

df = pd.DataFrame(rows)
df.to_csv("data/raw/listings.csv", index=False)
print(f"Wrote {len(df)} rows to data/raw/listings.csv")
