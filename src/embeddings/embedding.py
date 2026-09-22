from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    return model.encode(chunks)

