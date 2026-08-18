from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(text: str, top_n: int = 3) -> list:
    if not text or len(text.split()) < 2:
        return text.split()
    
    try:
        tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=top_n)
        tfidf.fit([text])
        return list(tfidf.vocabulary_.keys())
    except ValueError:
        return text.split()[:top_n]