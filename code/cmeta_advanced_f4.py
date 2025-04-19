# Versão F4 com embeddings reais
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import gzip
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def compressibility_score(text):
    compressed = gzip.compress(text.encode('utf-8'))
    return 1.0 - len(compressed) / len(text.encode('utf-8'))

def reflexivity_score(text):
    reflexive_terms = ['this dialogue', 'our conversation', 'we propose', 'AYA', 'spin']
    count = sum(text.count(term) for term in reflexive_terms)
    return min(1.0, count / 10)

def semantic_loop_score(blocks):
    embeddings = model.encode(blocks)
    similarities = cosine_similarity(embeddings)
    loops = np.sum(similarities > 0.7) - len(blocks)  # remove diagonal
    max_possible = len(blocks) * (len(blocks) - 1)
    return min(1.0, loops / max_possible) if max_possible > 0 else 0.0

def compute_cmeta_advanced_f4(text):
    blocks = text.split('.')  # simplistic segmentation
    blocks = [b.strip() for b in blocks if b.strip()]
    loop_sem = semantic_loop_score(blocks)
    compress_ratio = compressibility_score(text)
    reflexive_terms = reflexivity_score(text)
    return round((loop_sem * 0.4 + compress_ratio * 0.3 + reflexive_terms * 0.3), 4)
