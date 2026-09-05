# Data Dictionary

## Raw data (`data/raw/listings.csv`)

| Column | Type | Description |
|---|---|---|
| id | integer | Unique listing ID |
| name | text | Listing title |
| host_id | integer | Unique host ID |
| host_name | text | Host's display name |
| host_is_superhost | t/f | Whether the host has superhost status |
| neighbourhood_group | text | Borough / broad area |
| neighbourhood | text | Specific neighborhood |
| latitude | float | Listing latitude |
| longitude | float | Listing longitude |
| room_type | text | Entire home/apt, Private room, Shared room, Hotel room |
| price | float | Price per night (USD) |
| minimum_nights | integer | Minimum nights required per booking |
| number_of_reviews | integer | Total reviews received |
| last_review | date | Date of most recent review |
| reviews_per_month | float | Average reviews per month |
| calculated_host_listings_count | integer | Number of listings this host manages |
| availability_365 | integer | Days available for booking in the next 365 |

## Processed data (`data/processed/listings_clean.csv`)

All columns above, plus:

| Column | Type | Description |
|---|---|---|
| price_per_night_bucket | category | Price bucketed into ranges for visuals |
| is_superhost | boolean | Cleaned boolean version of host_is_superhost |
| days_since_last_review | integer | Days between last review and analysis date |
| availability_status | category | Rarely / Sometimes / Highly Available |
