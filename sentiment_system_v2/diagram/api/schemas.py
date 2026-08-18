from pydantic import BaseModel
from typing import List, Dict, Any

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    raw_text: str
    cleaned_text: str
    sentiment: str
    confidence: float
    low_confidence: bool
    keywords: List[str]

class AnalyticsResponse(BaseModel):
    sentiment_distribution: Dict[str, Any]
    trending_keywords: List[Dict[str, Any]]