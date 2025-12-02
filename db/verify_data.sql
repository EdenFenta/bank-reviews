-- Verify banks loaded correctly
SELECT * FROM banks LIMIT 10;

-- Count banks
SELECT COUNT(*) AS total_banks FROM banks;

-- Count reviews
SELECT COUNT(*) AS total_reviews FROM reviews;

-- Check mapping: every review has a bank
SELECT bank_id, COUNT(*) 
FROM reviews 
GROUP BY bank_id;

-- Check if any reviews missing sentiment
SELECT COUNT(*) AS missing_sentiment
FROM reviews
WHERE sentiment_label IS NULL;

-- Check if any dates invalid
SELECT COUNT(*) AS invalid_dates
FROM reviews
WHERE review_date IS NULL;

-- Sample reviews joined with bank names
SELECT b.bank_name, r.review_text, r.rating, r.sentiment_label
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id
LIMIT 20;