import spacy
from collections import Counter

class KeywordExtractor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def get_keywords(self, text, top_n=3):
        doc = self.nlp(text)
        keywords = []
        
        for token in doc:
            if not token.is_stop and not token.is_punct and token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                keywords.append(token.lemma_.lower())
                
        freq = Counter(keywords)
        return [item[0] for item in freq.most_common(top_n)]