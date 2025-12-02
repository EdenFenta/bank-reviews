# Bank App Reviews

This repository collects, preprocesses, analyzes, and visualizes Google Play Store reviews for Ethiopian banking mobile applications.  
It includes review scraping, cleaning, translation, sentiment labeling, thematic extraction, KPI generation, visualization, and insights reporting.

## Task Overview

- **Task-1:** Scraping, cleaning, translating reviews
- **Task-2:** Sentiment analysis & thematic extraction
- **Task-3:** KPI aggregation, data visualization, and per-bank issue detection
- **Task-4:** Insights generation, findings documentation, and reporting

## Task-1 Deliverables (✔ Completed)

1. **Raw Scraped Reviews**  
   Generated file:  
   ```
   data/reviews_raw.csv
   ```  
   Contains:  
   - bank  
   - review_text  
   - rating  
   - review_date  
   - thumbs_up  
   - app_version  

2. **Scraper Script**  
   ```
   scrape/scrape_reviews.py
   ```  
   Run:  
   ```bash
   python scrape/scrape_reviews.py
   ```

3. **Preprocessing + Translation**  
   ```
   scripts/preprocess.py
   ```  
   Operations:  
   - Drop duplicates  
   - Remove missing values  
   - Normalize dates  
   - Clean text  
   - Translate non-English reviews → English  
   - Output:  
     ```
     data/reviews_clean_translated.csv
     ```  
   Run:  
   ```bash
   python scripts/preprocess.py
   ```

4. **Output (Clean + Translated Dataset)**  
   ```
   data/reviews_clean_translated.csv
   ```  
   This is the input for Task-2.

## Task-2 Deliverables (✔ Completed)

1. **Sentiment Analysis**  
   Script:  
   ```
   scripts/analyze_sentiment.py
   ```  
   - Computes VADER sentiment score  
   - Labels each review as positive, neutral, or negative  

2. **Thematic Classification**  
   Themes include:  
   - Transaction Performance  
   - Customer Support  
   - Account Access  
   - User Interface / UX  
   - Feature Requests  
   - Other  

3. **Output Dataset**  
   ```
   data/reviews_sentiment_themes.csv
   ```  
   Contains:  
   - review_text  
   - bank  
   - rating  
   - sentiment_label  
   - sentiment_score  
   - theme  
   Run:  
   ```bash
   python scripts/analyze_sentiment.py
   ```

## Task-3 Deliverables: KPIs & Visualizations (✔ Completed)

1. **KPI Aggregation**  
   Script:  
   ```
   scripts/insights_and_viz.py
   ```  
   Generates KPIs such as:  
   - Total reviews per bank  
   - Average rating per bank  
   - Positive / negative sentiment percentages  
   - Theme distribution  
   - Top recurring issues  
   Saved to:  
   ```
   outputs/kpi_summary.csv
   ```

2. **Visualizations**  
   Automatically generated:  

   | Visualization             | Output File                  |
   |---------------------------|------------------------------|
   | Sentiment by Bank         | outputs/sentiment_by_bank.png |
   | Rating Distribution       | outputs/rating_by_bank.png   |
   | Top Themes                | outputs/top_themes.png       |
   | Sentiment by Theme (stacked bar) | outputs/sentiment_by_theme.png |

3. **Per-Bank Issue Detection**  
   The script also analyzes:  
   - Most common negative themes per bank  
   - First samples of negative reviews  
   - Pain points grouped by category  
   Saved to:  
   ```
   outputs/bank_issues.json
   ```  
   Run Task-3:  
   ```bash
   python scripts/insights_and_viz.py
   ```

## Task-4 Deliverables: Insights & Reporting (✔ Completed)

Task-4 focuses on turning the data into actionable insights and preparing a business-ready report.

1. **Insights for Each Bank**  
   Includes:  
   - What users complain about most  
   - What drives negative sentiment  
   - Which features users request  
   - Operational issues (e.g., login failures, transfer errors)  
   - UX issues (e.g., slow performance, poor navigation)  
   - Support-related frustrations  
   - Version-specific issues  

2. **Comparative Analysis Across Banks**  
   Findings include:  
   - Which bank has higher positive sentiment  
   - Which bank has more consistent user ratings  
   - Banks with recurring payment/transfer failures  
   - Banks with OTP/login concerns  
   - Banks with UI/UX complaints  

3. **Business Recommendations**  
   Outputs include insights such as:  
   - Improve OTP reliability  
   - Optimize transaction speed  
   - Redesign UI elements  
   - Better error messaging  
   - Strengthen customer support turnaround  
   - Add biometric login or dark mode  
   - Improve onboarding flow  

4. **Full Report (Optional Additional Export)**  
   A structured PDF or Markdown report can be generated including:  
   - Executive summary  
   - KPI tables  
   - Trend charts  
   - Per-bank insights  
   - Recommendations  
   - Appendices (methodology & code)  
   If needed, run:  
   ```bash
   python generate_report.py
   ```  
   (Optional script — only if added.)

## Folder Structure

```
bank-reviews/
├── scrape/
│   └── scrape_reviews.py
├── scripts/
│   ├── preprocess.py
│   ├── analyze_sentiment.py
│   └── insights_and_viz.py
├── data/
│   ├── reviews_raw.csv
│   ├── reviews_clean_translated.csv
│   └── reviews_sentiment_themes.csv
├── outputs/
│   ├── *.png
│   ├── kpi_summary.csv
│   └── bank_issues.json
├── README.md
└── requirements.txt
```

## Apps Covered

- **CBE:** com.combanketh.mobilebanking
- **Bank of Abyssinia:** com.boa.boaMobileBanking
- **Dashen Bank:** com.dashen.dashensuperapp

## Setup Instructions

Install dependencies:  
```bash
pip install -r requirements.txt
```

Run steps in order:  
```bash
python scrape/scrape_reviews.py
python scripts/preprocess.py
python scripts/analyze_sentiment.py
python scripts/insights_and_viz.py
```
