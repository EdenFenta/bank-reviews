import pandas as pd
import os
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon if not already
nltk.download('vader_lexicon')

INPUT_FILE = "data/reviews_clean_translated.csv"
OUTPUT_FILE = "data/reviews_sentiment_themes.csv"

# --- Define themes ---
def assign_theme(text):
    text = text.lower()
    if any(k in text for k in ["login", "password", "otp"]):
        return "Account Access"
    elif any(k in text for k in ["transfer", "slow", "failed"]):
        return "Transaction Performance"
    elif any(k in text for k in ["ui", "design", "layout"]):
        return "User Interface"
    elif any(k in text for k in ["support", "help", "service"]):
        return "Customer Support"
    elif any(k in text for k in ["fingerprint", "notification", "feature"]):
        return "Feature Requests"
    else:
        return "Other"

def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"{INPUT_FILE} not found. Make sure reviews_clean_translated.csv exists.")

    print("Loading cleaned and translated reviews...")
    df = pd.read_csv(INPUT_FILE)

    # --- Sentiment analysis using VADER ---
    print("Running VADER sentiment analysis...")
    sid = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['review_text'].apply(lambda x: sid.polarity_scores(x)['compound'])
    df['sentiment_label'] = df['sentiment_score'].apply(
        lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
    )

    # --- Assign themes ---
    print("Assigning themes...")
    df['theme'] = df['review_text'].apply(assign_theme)

    # --- Save final CSV ---
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved sentiment & theme data to {OUTPUT_FILE}")

    # --- Optional: show first 10 rows ---
    print(df[['review_text','sentiment_score','sentiment_label','theme']].head(10))

if __name__ == "__main__":
    main()
