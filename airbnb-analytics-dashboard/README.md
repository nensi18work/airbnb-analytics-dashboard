# Airbnb Analytics Dashboard

A Power BI dashboard analyzing Airbnb listing data (price, availability,
room type, and host activity) at a neighborhood level.

## Project Structure

```
airbnb-analytics-dashboard/
├── data/
│   ├── raw/                # Original/source data (Inside Airbnb schema)
│   │   └── listings.csv
│   └── processed/          # Cleaned data used by the Power BI file
│       └── listings_clean.csv
├── scripts/
│   ├── generate_sample_data.py   # Creates a synthetic sample dataset
│   └── clean_data.py             # Cleans raw data -> processed data
├── docs/
│   └── data_dictionary.md
├── AirbnbDashboard.pbix    # (add this yourself from Power BI Desktop)
└── README.md
```

## Data Source

This project is structured to use data in the same schema as
[Inside Airbnb](http://insideairbnb.com/get-the-data/). Two options:

1. **Real data**: Download `listings.csv` for a city of your choice from
   Inside Airbnb and place it in `data/raw/`.
2. **Sample data**: Run `python scripts/generate_sample_data.py` to generate
   a realistic synthetic dataset with the same columns, useful for building
   and testing the dashboard without waiting on a download.

## Workflow

1. Get raw data into `data/raw/listings.csv` (real or generated).
2. Run `python scripts/clean_data.py` to produce `data/processed/listings_clean.csv`.
3. Open `AirbnbDashboard.pbix` in Power BI Desktop and point the data source
   at `data/processed/listings_clean.csv`.
4. Build/refresh visuals, save the .pbix, and commit your changes.

## Notes on Power BI + Git

`.pbix` files are binary, so Git can track *that a change happened* but not
*what* changed inside the report. For meaningful diffs, consider saving as a
Power BI Project (`.pbip`) if your Power BI Desktop version supports it —
this breaks the report into readable JSON/text files.
