from src.vector_store.chroma_store import collection
from src.embeddings.embedding import generate_embeddings



def retrieve_relevant_chunks(question):
    question_embedding = generate_embeddings([question])
    result = collection.query(
        query_embeddings = [question_embedding[0].tolist()],
        n_results = 4
    )

    return result["documents"][0]
