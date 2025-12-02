import pandas as pd
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer


# Load CSV
df = pd.read_csv("data/reviews_clean_translated.csv")

# Detect which text column exists
TEXT_COL = None
for col in ["translated_text", "cleaned_review", "review_text", "review"]:
    if col in df.columns:
        TEXT_COL = col
        break

if TEXT_COL is None:
    raise Exception("No valid text column found. Expected translated_text or cleaned_review or review_text.")

print(f"Using text column: {TEXT_COL}")

df = df.dropna(subset=[TEXT_COL])


# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=2500,
    ngram_range=(1, 2)
)


# Helper: Extract keywords
def get_tfidf_keywords(texts, top_k=15):
    tfidf = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf.mean(axis=0).A1

    ranked = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)

    return [
        {"keyword": word, "score": float(score)}
        for word, score in ranked[:top_k]
    ]


# Keywords per bank
bank_keywords = {}
for bank in df["bank"].unique():
    subset = df[df["bank"] == bank][TEXT_COL]
    if len(subset):
        bank_keywords[bank] = get_tfidf_keywords(subset)


# Keywords per sentiment (if available)
sentiment_keywords = {}
if "sentiment_label" in df.columns:
    for s in df["sentiment_label"].unique():
        subset = df[df["sentiment_label"] == s][TEXT_COL]
        if len(subset):
            sentiment_keywords[s] = get_tfidf_keywords(subset)


# Output JSON
os.makedirs("outputs", exist_ok=True)
output = {
    "keywords_by_bank": bank_keywords,
    "keywords_by_sentiment": sentiment_keywords
}

with open("outputs/keywords.json", "w") as f:
    json.dump(output, f, indent=4)

print("TF-IDF keywords saved to outputs/keywords.json")
