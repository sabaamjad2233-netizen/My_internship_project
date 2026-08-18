from collections import Counter
from src.database import get_connection

def get_sentiment_distribution():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sentiment, COUNT(*) FROM posts WHERE processed_flag = 1 GROUP BY sentiment")
    rows = cursor.fetchall()
    conn.close()
    
    total = sum(count for _, count in rows)
    distribution = {sentiment: count for sentiment, count in rows}
    
    return {
        "total_processed": total,
        "counts": distribution,
        "percentages": {k: round((v / total) * 100, 2) for k, v in distribution.items()} if total > 0 else {}
    }

def get_keyword_trends(top_k: int = 5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT keywords FROM posts WHERE processed_flag = 1 AND keywords IS NOT NULL")
    rows = cursor.fetchall()
    conn.close()
    
    all_keywords = []
    for (kw_str,) in rows:
        if kw_str:
            all_keywords.extend([k.strip() for k in kw_str.split(",") if k.strip()])
            
    counter = Counter(all_keywords)
    return counter.most_common(top_k)