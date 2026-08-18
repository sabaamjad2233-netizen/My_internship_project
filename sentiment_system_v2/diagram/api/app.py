from fastapi import FastAPI
from src.database import init_db, get_connection
from src.crawler import run_crawler
from src.cleaner import clean_text
from src.model import predict_sentiment
from src.keywords import extract_keywords
from src.analytics import get_sentiment_distribution, get_keyword_trends
from api.schemas import PredictRequest, PredictResponse, AnalyticsResponse

app = FastAPI(title="Intelligent Sentiment System API", version="2.0")

@app.on_event("startup")
def startup_event():
    init_db()

@app.post("/crawl-and-process")
def trigger_crawl_and_process():
    run_crawler()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, raw_text FROM posts WHERE processed_flag = 0")
    unprocessed = cursor.fetchall()
    
    for post_id, raw_text in unprocessed:
        cleaned = clean_text(raw_text)
        sentiment, conf, low_conf = predict_sentiment(cleaned)
        kw = extract_keywords(cleaned)
        kw_str = ", ".join(kw)
        
        cursor.execute("""
            UPDATE posts 
            SET cleaned_text = ?, sentiment = ?, confidence = ?, keywords = ?, processed_flag = 1
            WHERE id = ?
        """, (cleaned, sentiment, conf, kw_str, post_id))
        
    conn.commit()
    conn.close()
    return {"message": f"Processed {len(unprocessed)} new records."}

@app.post("/predict", response_model=PredictResponse)
def single_predict(request: PredictRequest):
    cleaned = clean_text(request.text)
    sentiment, conf, low_conf = predict_sentiment(cleaned)
    kw = extract_keywords(cleaned)
    
    return {
        "raw_text": request.text,
        "cleaned_text": cleaned,
        "sentiment": sentiment,
        "confidence": conf,
        "low_confidence": low_conf,
        "keywords": kw
    }

@app.get("/analytics", response_model=AnalyticsResponse)
def fetch_analytics():
    dist = get_sentiment_distribution()
    trends = get_keyword_trends()
    formatted_trends = [{"keyword": k, "frequency": v} for k, v in trends]
    
    return {
        "sentiment_distribution": dist,
        "trending_keywords": formatted_trends
    }