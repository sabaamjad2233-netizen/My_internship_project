from sentence_transformers import SentenceTransformer

# Load pre-trained Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(texts):
    """Converts a list of text strings into vector embeddings."""
    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings