# scripts/insights_and_viz.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import json

# Configuration
CSV_FILE = "data/reviews_sentiment_themes.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data():
    """Load cleaned + sentiment + theme CSV."""
    df = pd.read_csv(CSV_FILE)
    df.columns = df.columns.str.strip()
    
    # Ensure consistent column naming
    if "bank_name" in df.columns:
        df.rename(columns={"bank_name": "bank"}, inplace=True)
    
    return df

def aggregate_kpis(df):
    total = len(df)
    by_bank = df.groupby('bank').agg(
        reviews=('review_text','count'),
        avg_rating=('rating', 'mean'),
        positive_pct=('sentiment_label', lambda x: (x=='positive').mean()*100),
        negative_pct=('sentiment_label', lambda x: (x=='negative').mean()*100)
    ).reset_index()
    return total, by_bank

def top_themes(df, top_n=10):
    c = Counter(df['theme'].fillna("Other").tolist())
    return c.most_common(top_n)

def plot_sentiment_per_bank(df):
    plt.figure(figsize=(8,5))
    sns.countplot(
        data=df, x='bank', hue='sentiment_label',
        order=sorted(df['bank'].unique()),
        hue_order=['positive','neutral','negative']
    )
    plt.title("Sentiment by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Reviews")
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "sentiment_by_bank.png")
    plt.savefig(p); plt.close()
    print("Saved:", p)

def plot_rating_dist(df):
    plt.figure(figsize=(8,5))
    sns.countplot(
        data=df, 
        x='bank', 
        hue='rating',
        order=sorted(df['bank'].unique())
    )
    plt.title("Rating Distribution by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Count")
    plt.tight_layout()
    p = os.path.join(OUTPUT_DIR, "rating_by_bank.png")
    plt.savefig(p); plt.close()
    print("Saved:", p)

def plot_theme_counts(df, top_n=10):
    c = Counter(df['theme'].fillna('Other').tolist())
    items = c.most_common(top_n)
    labels, counts = zip(*items)

    plt.figure(figsize=(8,5))
    sns.barplot(x=list(counts), y=list(labels))
    plt.title("Top Themes")
    plt.xlabel("Count")
    plt.tight_layout()

    p = os.path.join(OUTPUT_DIR, "top_themes.png")
    plt.savefig(p); plt.close()
    print("Saved:", p)

def sentiment_by_theme(df):
    pt = pd.crosstab(df['theme'].fillna('Other'), df['sentiment_label'])

    # Reorder columns if they exist
    cols = [c for c in ['positive', 'neutral', 'negative'] if c in pt.columns]
    pt = pt[cols]

    pt_norm = pt.div(pt.sum(axis=1), axis=0).fillna(0)
    pt_norm.plot(kind='bar', stacked=True, figsize=(10,6))

    plt.title("Sentiment Distribution per Theme (fraction)")
    plt.xlabel("Theme")
    plt.ylabel("Proportion")
    plt.tight_layout()

    p = os.path.join(OUTPUT_DIR, "sentiment_by_theme.png")
    plt.savefig(p); plt.close()
    print("Saved:", p)

def save_kpi_table(total, by_bank):
    p = os.path.join(OUTPUT_DIR, "kpi_summary.csv")
    by_bank.to_csv(p, index=False)
    print("Saved:", p)

def main():
    df = load_data()

    total, by_bank = aggregate_kpis(df)
    print(f"Total reviews: {total}")
    print(by_bank)

    save_kpi_table(total, by_bank)

    plot_sentiment_per_bank(df)
    plot_rating_dist(df)
    plot_theme_counts(df)
    sentiment_by_theme(df)

    # Identify drivers/pain points per bank:
    issues = []
    for bank in df['bank'].unique():
        sub = df[df['bank'] == bank]

        negative = sub[sub['sentiment_label'] == 'negative']
        negative_theme_counts = Counter(negative['theme'].fillna('Other').tolist())

        top_negative_themes = negative_theme_counts.most_common(3)

        samples = negative[['review_text', 'rating']].head(5).to_dict(orient='records')

        issues.append({
            "bank": bank,
            "total_reviews": len(sub),
            "negative_reviews": len(negative),
            "top_negative_themes": top_negative_themes,
            "sample_negative_reviews": samples
        })

    # Save results
    with open(os.path.join(OUTPUT_DIR, "bank_issues.json"), "w", encoding="utf-8") as f:
        json.dump(issues, f, ensure_ascii=False, indent=2)

    print("Saved: outputs/bank_issues.json")

if __name__ == "__main__":
    main()
