import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "sentiment_model.pkl")
VEC_PATH = os.path.join(MODEL_DIR, "vectorizer.pkl")

CONFIDENCE_THRESHOLD = 0.60

def train_default_model():
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    sample_train_texts = [
        "love this product amazing", "great service highly recommended",
        "excellent performance loved it", "bad experience worst ever",
        "terrible service horrible quality", "awful waste of money completely"
    ]
    labels = ["positive", "positive", "positive", "negative", "negative", "negative"]
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sample_train_texts)
    
    model = LogisticRegression()
    model.fit(X, labels)
    
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(VEC_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

def get_model_and_vec():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VEC_PATH):
        train_default_model()
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VEC_PATH, "rb") as f:
        vec = pickle.load(f)
    return model, vec

def predict_sentiment(cleaned_text: str):
    if not cleaned_text:
        return "neutral", 0.0, False

    model, vec = get_model_and_vec()
    vec_text = vec.transform([cleaned_text])
    
    probabilities = model.predict_proba(vec_text)[0]
    classes = model.classes_
    max_idx = probabilities.argmax()
    
    confidence = float(probabilities[max_idx])
    label = classes[max_idx]
    
    # Confidence Filtering logic
    is_low_confidence = confidence < CONFIDENCE_THRESHOLD
    if is_low_confidence:
        final_label = "uncertain"
    else:
        final_label = label

    return final_label, round(confidence, 4), is_low_confidence