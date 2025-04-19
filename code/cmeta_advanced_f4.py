from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import gzip
import numpy as np
import re

def get_blocks(text, block_size=5):
    sentences = re.split(r'[.!?]\s+', text)
    return [" ".join(sentences[i:i+block_size]) for i in range(0, len(sentences), block_size)]

def semantic_loops(blocks, threshold=0.7):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(blocks)
    sim_matrix = cosine_similarity(embeddings)
    np.fill_diagonal(sim_matrix, 0)
    loop_score = np.sum(sim_matrix > threshold) / (len(blocks)**2 - len(blocks))
    return min(loop_score, 1.0)

def compressibility_score(text):
    original = len(text.encode('utf-8'))
    compressed = len(gzip.compress(text.encode('utf-8')))
    if original == 0:
        return 0
    return 1 - (compressed / original)

def reflexive_terms_score(text, terms=["this", "we", "I", "our", "my", "AYA", "conversation", "dialogue"]):
    words = re.findall(r'\b\w+\b', text.lower())
    count = sum(1 for word in words if word in terms)
    return min(count / len(words), 1.0) if words else 0.0

def compute_cmeta_advanced(text, w_loops=0.4, w_comp=0.3, w_refl=0.3):
    blocks = get_blocks(text)
    loop_score = semantic_loops(blocks)
    comp_score = compressibility_score(text)
    refl_score = reflexive_terms_score(text)
    return {
        "C_meta_loops": loop_score,
        "C_meta_compress": comp_score,
        "C_meta_refl": refl_score,
        "C_meta_advanced": round(loop_score * w_loops + comp_score * w_comp + refl_score * w_refl, 4)
    }

# Example usage:
if __name__ == "__main__":
    with open("sample.txt", "r", encoding="utf-8") as f:
        text = f.read()
    scores = compute_cmeta_advanced(text)
    for k, v in scores.items():
        print(f"{k}: {v}")
