# Bank App Reviews

This repository collects and preprocesses Google Play Store reviews for Ethiopian banking mobile applications.

- **Task-1:** Scraping, cleaning, and translating reviews
- **Task-2:** Sentiment analysis and thematic extraction

##  Task-1 Deliverables

### ✔ 1. Raw Scraped Reviews
Generated file:

```
data/reviews_raw.csv
```

Contains:

- bank
- review_text
- rating
- review_date
- thumbs_up (helpfulness)
- app_version


### ✔ 2. Scraper Script
File:

```
scrape/scrape_reviews.py
```

- Uses **google-play-scraper** to fetch ~500 reviews per bank app.
- Run it:

```bash
python scrape/scrape_reviews.py
```

### ✔ 3. Preprocessing Script (with Translation)
File:

```
scripts/preprocess.py
```

Cleans and normalizes the scraped data, translates non-English reviews to English.
Operations include:

- Drop duplicate reviews (bank + review_text)
- Drop rows with missing rating or text
- Normalize dates → YYYY-MM-DD
- Remove control characters and trim whitespace
- Translate non-English reviews to English using Google Translate
- Save cleaned dataset to:

```
data/reviews_clean_translated.csv
```

Run it:

```bash
python scripts/preprocess.py
```

### ✔ 4. Cleaned & Translated Dataset
Generated file:

```
data/reviews_clean_translated.csv
```

This dataset is ready for sentiment analysis (Task-2).

## Task-2 Deliverables

### ✔ 1. Sentiment Analysis & Labeling
File:

```
scripts/analyze_sentiment.py
```

- Uses VADER to compute sentiment scores and labels:
  - Positive, Negative, Neutral
- Processes translated reviews from Task-1

### 2. Thematic Extraction

- Assigns each review to a theme based on keywords:
  - Account Access / Login Issues → login, password, OTP
  - Transaction Performance → transfer, slow, failed
  - User Interface / UX → UI, design, layout
  - Customer Support → support, help, service
  - Feature Requests → fingerprint, notifications, new feature
- Reviews can be assigned multiple themes or “Other” if no keywords match

### ✔ 3. Sentiment & Theme Dataset
Generated file:

```
data/reviews_sentiment_themes.csv
```

Contains:

- review_text (English)
- rating
- review_date
- bank
- source
- sentiment_score
- sentiment_label
- theme

Run the script:

```bash
python scripts/analyze_sentiment.py
```

## Folder Structure

```
bank-reviews/
├── scrape/
│   └── scrape_reviews.py
├── scripts/
│   ├── preprocess.py
│   └── analyze_sentiment.py
├── data/
│   ├── reviews_raw.csv
│   ├── reviews_clean_translated.csv
│   └── reviews_sentiment_themes.csv
├── README.md
└── requirements.txt
```

## How to Set Up
Install dependencies:

```bash
pip install -r requirements.txt
```

Then run:

1. Scraper → generates raw dataset
2. Preprocessing with translation → generates reviews_clean_translated.csv
3. Sentiment & theme analysis → generates reviews_sentiment_themes.csv

## Apps Covered
- Bank App ID: CBE - com.combanketh.mobilebanking
- Bank of Abyssinia: com.boa.boaMobileBanking
- Dashen Bank: com.dashen.dashensuperapp