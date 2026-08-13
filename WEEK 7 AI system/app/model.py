import joblib
import os

# Model File Path Setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "sentiment_model.pkl")

class SentimentModel:
    def __init__(self):
        # Pickle file load ho rahi hai
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            self.model = None

    def predict(self, text: str) -> str:
        if not self.model:
            # Agar model file nahi milti toh fallback/dummy prediction
            return "positive" if "good" in text.lower() or "amazing" in text.lower() else "negative"
        
        # Scikit-learn model inference
        prediction = self.model.predict([text])[0]
        return str(prediction)

model_service = SentimentModel()