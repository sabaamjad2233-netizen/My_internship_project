import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
STOP_WORDS = set(stopwords.words('english'))

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    
    # Lowercase & remove URLs
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    
    # Remove special characters, punctuations & digits
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    
    # Remove stopwords and extra whitespaces
    tokens = text.split()
    cleaned_tokens = [w for w in tokens if w not in STOP_WORDS and len(w) > 2]
    
    return " ".join(cleaned_tokens)