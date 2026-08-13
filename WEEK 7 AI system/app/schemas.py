from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text: str = Field(..., example="This product is really amazing!")

class PredictResponse(BaseModel):
    text: str
    sentiment: str