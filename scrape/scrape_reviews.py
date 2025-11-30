import pandas as pd
from google_play_scraper import reviews, Sort

# Bank Android app IDs
APPS = {
    "CBE": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

OUTPUT_FILE = "data/reviews_raw.csv"

def fetch_reviews(app_id, bank_name, count=500):
    print(f"Fetching reviews for {bank_name}...")

    all_reviews = []

    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=count
    )

    for r in result:
        all_reviews.append({
            "bank": bank_name,
            "review_text": r.get("content", ""),
            "rating": r.get("score", None),
            "review_date": r.get("at", None),
            "thumbs_up": r.get("thumbsUpCount", 0),
            "app_version": r.get("reviewCreatedVersion", None)
        })

    return all_reviews

def main():
    all_data = []

    for bank, app_id in APPS.items():
        reviews_list = fetch_reviews(app_id, bank, count=500)
        all_data.extend(reviews_list)

    df = pd.DataFrame(all_data)

    print(f"Saving scraped data to {OUTPUT_FILE}...")
    df.to_csv(OUTPUT_FILE, index=False)
    print("Done!")

if __name__ == "__main__":
    main()
