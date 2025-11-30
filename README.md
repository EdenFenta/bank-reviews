# Bank App Reviews – Task 1

This repository collects and preprocesses Google Play Store reviews for Ethiopian banking mobile applications.  
Task-1 focuses on:
1. Scraping reviews
2. Cleaning and preparing the dataset for sentiment analysis


## 📌 Task-1 Deliverables

### ✔ 1. Raw Scraped Reviews
Generated file:
``data/reviews_raw.csv``  
Contains:
- bank  
- review_text  
- rating  
- review_date  
- thumbs_up (helpfulness)
- app_version  

### ✔ 2. Scraper Script
File:  
``scrape/scrape_reviews.py``  
Uses **google-play-scraper** to fetch the latest ~500 reviews for each bank app.

Run it using:

python scrape/scrape_reviews.py

### ✔ 3. Preprocessing Script
File:  
``scripts/preprocess.py``  
Cleans and normalizes the scraped data.

Operations include:
- Drop duplicate reviews (bank + review_text)
- Drop rows with missing rating or text
- Normalize dates → `YYYY-MM-DD`
- Remove control characters and trim whitespace
- Save cleaned dataset to:

``data/reviews_clean.csv``

Run it using:

python scripts/preprocess.py

### ✔ 4. Cleaned Dataset
Generated file:
``data/reviews_clean.csv``  
This dataset is ready for sentiment analysis (Task-2).

##  Folder Structure
bank-reviews/
├── scrape/
│ └── scrape_reviews.py
├── scripts/
│ └── preprocess.py
├── data/
│ ├── reviews_raw.csv
│ └── reviews_clean.csv
├── README.md
└── requirements.txt

## How to Set Up

Install dependencies:

pip install -r requirements.txt

Then:

1. Run scraper → generates raw dataset
2. Run preprocessing → generates cleaned dataset


## Apps Covered in Task-1

| Bank | App ID |
|------|---------------------------------------------|
| CBE | `com.combanketh.mobilebanking` |
| Bank of Abyssinia | `com.boa.boaMobileBanking` |
| Dashen Bank | `com.dashen.dashensuperapp` |