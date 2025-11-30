from googletrans import Translator
translator = Translator()

import pandas as pd
import os
import re

INPUT_FILE = "data/reviews_raw.csv"
OUTPUT_FILE = "data/reviews_clean_translated.csv"

def clean_text(text):
    if pd.isna(text):
        return ""
    # Remove control characters and excessive whitespace
    text = re.sub(r"[\r\n\t]+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def translate_if_non_english(text):
    try:
        if not text.isascii():  # detect non-English text
            translated = translator.translate(text, src='auto', dest='en')
            return translated.text
        return text
    except:
        return text  # fallback if translation fails

def main():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"{INPUT_FILE} not found. Make sure reviews_raw.csv exists.")

    print("Loading raw reviews...")
    df = pd.read_csv(INPUT_FILE)

    # --- Drop missing values ---
    df = df.dropna(subset=["rating", "review_text"])

    # --- Clean date format ---
    print("Normalizing dates...")
    df["review_date"] = pd.to_datetime(df["review_date"], errors="coerce").dt.date
    df = df.dropna(subset=["review_date"])  # Drop rows with invalid dates

    # --- Clean text ---
    print("Cleaning text fields...")
    df["review_text"] = df["review_text"].apply(clean_text)

    # --- Translate non-English reviews ---
    print("Translating non-English reviews to English...")
    df["review_text"] = df["review_text"].apply(translate_if_non_english)

    # --- Drop duplicates ---
    print("Dropping duplicates...")
    df = df.drop_duplicates(subset=["bank", "review_text"], keep="first")

    # --- Save ---
    print(f"Saving clean file to {OUTPUT_FILE} ...")
    df.to_csv(OUTPUT_FILE, index=False)

    print("Done! Cleaned dataset saved.")

if __name__ == "__main__":
    main()
