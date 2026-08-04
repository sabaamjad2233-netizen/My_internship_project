import pandas as pd
import re
import os
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text)
    text = re.sub(r'<.*?>', '', text)                  # Remove HTML tags
    text = re.sub(r'http\S+|www\.\S+', '', text)       # Remove URLs
    text = text.lower()                               # Lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)          # Remove non-alpha
    words = text.split()
    words = [w for w in words if w not in stop_words] # Remove stopwords
    return " ".join(words)

def run_cleaner():
    print("\n--- [STEP 2/4] Starting Text Cleaner ---")
    raw_path = 'data/raw_data.csv'
    df = pd.read_csv(raw_path)
    
    df['cleaned_review'] = df['review_text'].apply(clean_text)
    
    clean_path = 'data/cleaned_data.csv'
    df.to_csv(clean_path, index=False)
    print(f"✓ Cleaned dataset saved to '{clean_path}' ({len(df)} rows).")

if __name__ == '__main__':
    run_cleaner()