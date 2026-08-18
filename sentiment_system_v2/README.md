# Intelligent Sentiment System v2.0

An end-to-end sentiment analysis pipeline with confidence filtering, automated data ingestion, keyword extraction, and analytics endpoints.

## Architecture Pipeline
- **Crawler:** Collects raw unstructured posts and saves to SQLite DB.
- **Cleaner:** Normalizes text, strips URLs, stopwords, and punctuation.
- **Model & Confidence Filter:** Predicts sentiment probabilities with an uncertainty threshold (< 0.60).
- **Keyword Extraction:** Extracts top TF-IDF n-grams per post.
- **Analytics Engine:** Computes real-time keyword frequency trends and sentiment class distributions.
- **API Service:** FastAPI interface exposing ingestion, prediction, and analytics endpoints.

## Setup & Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt