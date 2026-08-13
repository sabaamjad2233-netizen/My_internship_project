import torch
from sentence_transformers import util

def search_similar_posts(query_embedding, post_embeddings, posts, top_k=2):
    """Calculates cosine similarity and returns top relevant posts."""
    # Compute similarity scores
    cosine_scores = util.cos_sim(query_embedding, post_embeddings)[0]
    
    # Sort results by highest score
    top_results = torch.topk(cosine_scores, k=top_k)
    
    results = []
    for score, idx in zip(top_results.values, top_results.indices):
        results.append({
            "post": posts[idx],
            "score": float(score)
        })
    return results