import pandas as pd
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def run_trainer():
    print("\n--- [STEP 3/4] Training Sentiment Model (Logistic Regression) ---")
    df = pd.read_csv('data/cleaned_data.csv')
    
    train_df = df[df['split'] == 'train'].dropna(subset=['cleaned_review'])
    test_df = df[df['split'] == 'test'].dropna(subset=['cleaned_review'])
    
    vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
    X_train_tfidf = vectorizer.fit_transform(train_df['cleaned_review'])
    
    model = LogisticRegression(max_iter=1000, C=1.0)
    model.fit(X_train_tfidf, train_df['sentiment'])
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/sentiment_model.pkl')
    joblib.dump(vectorizer, 'models/vectorizer.pkl')
    print("✓ Logistic Regression Model & TF-IDF Vectorizer saved successfully.")

if __name__ == '__main__':
    run_trainer()