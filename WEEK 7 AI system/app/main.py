from fastapi import FastAPI, HTTPException
from app.schemas import PredictRequest, PredictResponse
from app.model import model_service

app = FastAPI(
    title="Sentiment Analysis API",
    description="Week 7 - Microservice API for Post Sentiment",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"status": "Active", "message": "Sentiment API is running"}

@app.post("/predict", response_model=PredictResponse)
def predict_sentiment(payload: PredictRequest):
    try:
        sentiment = model_service.predict(payload.text)
        return PredictResponse(
            text=payload.text,
            sentiment=sentiment
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))