import pandas as pd
import os
import nltk
from nltk.corpus import movie_reviews

def run_scraper():
    print("--- [STEP 1/4] Scraping NLTK Movie Reviews Dataset ---")
    
    # Download NLTK movie_reviews corpus
    nltk.download('movie_reviews', quiet=True)
    
    reviews = []
    labels = []
    
    for fileid in movie_reviews.fileids():
        labels.append('positive' if fileid.startswith('pos/') else 'negative')
        reviews.append(movie_reviews.raw(fileid))
        
    df = pd.DataFrame({'review_text': reviews, 'sentiment': labels})
    
    # Split 80-20 into train and test
    train_size = int(len(df) * 0.8)
    df['split'] = ['train'] * train_size + ['test'] * (len(df) - train_size)
    
    os.makedirs('data', exist_ok=True)
    out_path = 'data/raw_data.csv'
    df.to_csv(out_path, index=False)
    
    print(f"[Scraper] Total rows loaded: {len(df)}")
    print(f"✓ Scraped raw dataset saved to '{out_path}'")

if __name__ == '__main__':
    run_scraper()