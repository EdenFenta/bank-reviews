-- Banks table: list of banks / apps
CREATE TABLE IF NOT EXISTS banks (
  bank_id SERIAL PRIMARY KEY,
  bank_name TEXT NOT NULL UNIQUE,
  app_id TEXT
);

-- Reviews table: cleaned reviews and analysis results
CREATE TABLE IF NOT EXISTS reviews (
  review_id TEXT PRIMARY KEY,       
  bank_id INTEGER NOT NULL REFERENCES banks(bank_id) ON DELETE CASCADE,
  review_text TEXT,
  rating SMALLINT,
  review_date DATE,
  sentiment_label TEXT,
  sentiment_score REAL,
  theme TEXT,
  source TEXT,
  thumbs_up INTEGER,
  app_version TEXT
);

-- indices to speed queries
CREATE INDEX IF NOT EXISTS idx_reviews_bank ON reviews(bank_id);
CREATE INDEX IF NOT EXISTS idx_reviews_date ON reviews(review_date);
CREATE INDEX IF NOT EXISTS idx_reviews_sentiment ON reviews(sentiment_label);