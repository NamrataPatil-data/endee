from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Simulating Endee vector storage
vector_store = {}

def store_skills(skills):
    for skill in skills:
        vector_store[skill] = model.encode(skill)

def search_skill(query, top_k=10):
    query_vec = model.encode(query)

    scores = {}
    for skill, vec in vector_store.items():
        similarity = np.dot(query_vec, vec) / (
            np.linalg.norm(query_vec) * np.linalg.norm(vec)
        )
        scores[skill] = similarity

    sorted_skills = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    return [skill for skill, _ in sorted_skills[:top_k]]