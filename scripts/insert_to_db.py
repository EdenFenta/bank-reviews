import psycopg2
import pandas as pd

DB_NAME = "bank_reviews"
DB_USER = "edenfenta"
DB_PASSWORD = ""  
DB_HOST = "localhost"

df = pd.read_csv("data/reviews_sentiment_themes.csv")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST
)

cur = conn.cursor()

# Get bank_name → bank_id mapping
cur.execute("SELECT bank_id, bank_name FROM banks;")
bank_map = {name: bid for bid, name in cur.fetchall()}

insert_query = """
INSERT INTO reviews 
(bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, theme)
VALUES (%s, %s, %s, %s, %s, %s, %s);
"""

count = 0

for _, row in df.iterrows():
    cur.execute(insert_query, (
        bank_map[row["bank"]],
        row["review_text"],
        int(row["rating"]),
        row["review_date"],
        row["sentiment_label"],
        float(row["sentiment_score"]),
        row["theme"]
    ))
    count += 1

conn.commit()
cur.close()
conn.close()

print(f"Inserted {count} reviews successfully!")