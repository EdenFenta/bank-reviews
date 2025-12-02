import pandas as pd
import json
import os
from collections import Counter

INPUT_FILE = "data/reviews_sentiment_themes.csv"
KEYWORD_FILE = "analysis/keywords_per_bank.json"
OUTPUT_FILE = "analysis/bank_insights.md"
os.makedirs("analysis", exist_ok=True)

def top_themes(sub, label, n=1):
    temp = sub[sub["sentiment_label"] == label]
    c = Counter(temp["theme"].fillna("Other"))
    return [t for t, _ in c.most_common(n)]

def main():
    df = pd.read_csv(INPUT_FILE)
    df.columns = df.columns.str.strip()

    try:
        with open(KEYWORD_FILE, "r") as f:
            keywords = json.load(f)
    except:
        keywords = {}

    md = []
    md.append("# Bank Insights: Drivers & Pain Points\n")

    for bank in df["bank"].unique():
        sub = df[df["bank"] == bank]

        # 1 driver (positive theme)
        driver = top_themes(sub, "positive")[0] if len(sub) else "N/A"

        # 1 pain point (negative theme)
        pain = top_themes(sub, "negative")[0] if len(sub) else "N/A"

        # top keywords
        top_kw = keywords.get(bank, [])[:10]
        kw_list = ", ".join([k for k, _ in top_kw]) if top_kw else "N/A"

        md.append(f"## {bank}\n")
        md.append(f"**Top Driver:** {driver}\n")
        md.append(f"**Top Pain Point:** {pain}\n")
        md.append(f"**Top Keywords:** {kw_list}\n")

        # Add example negative reviews (3 samples)
        neg_samples = sub[sub["sentiment_label"] == "negative"]["review_text"].head(3).tolist()
        if neg_samples:
            md.append("**Example Negative Reviews:**")
            for r in neg_samples:
                md.append(f"- {r}")
        md.append("\n---\n")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"Saved insights to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
