import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
CSV_FILE = "data/reviews_sentiment_themes.csv"

df = pd.read_csv(CSV_FILE)

# Strip whitespace from column names just in case
df.columns = df.columns.str.strip()

# Sentiment Analysis Counts
if 'sentiment_label' in df.columns:
    sentiment_counts = df['sentiment_label'].value_counts()
    sentiment_percent = df['sentiment_label'].value_counts(normalize=True) * 100

    print("Sentiment Counts:")
    print(sentiment_counts)
    print("\nSentiment Percentages:")
    print(sentiment_percent.round(2))
else:
    print("Error: 'sentiment_label' column not found!")

# Theme Analysis Counts
if 'theme' in df.columns:
    theme_counts = df['theme'].value_counts()
    theme_percent = df['theme'].value_counts(normalize=True) * 100

    print("\nTheme Counts:")
    print(theme_counts)
    print("\nTheme Percentages:")
    print(theme_percent.round(2))
else:
    print("Error: 'theme' column not found!")

# Bar Plot: Sentiment Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='sentiment_label', order=['positive','neutral','negative'])
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("outputs/sentiment_distribution.png")
plt.show()


# Bar Plot: Theme Distribution
plt.figure(figsize=(8,4))
sns.countplot(data=df, y='theme', order=theme_counts.index)
plt.title("Theme Distribution")
plt.xlabel("Number of Reviews")
plt.ylabel("Theme")
plt.tight_layout()
plt.savefig("outputs/theme_distribution.png")
plt.show()
