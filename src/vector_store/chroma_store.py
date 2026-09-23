import chromadb
from src.extraction.pdf_reader import extract_text_from_pdf
from src.chunking.chunking_lib import RecursiveChunking
from src.embeddings.embedding import generate_embeddings


client = chromadb.PersistentClient(path = "./chromadb")

collection = client.get_or_create_collection(name = "pdf_docments")

path = "/home/gamp/ai-pdf-assistant/data/The-Psychology-of-Money.pdf"

document = extract_text_from_pdf(path)
chunks = RecursiveChunking(document)
embedding = generate_embeddings(chunks)

for i in range(1, len(chunks)):

    collection.add(

        ids = [f"chunk_{i}"],
        documents = [chunks[i]],
        embeddings = [embedding[i].tolist()],
        metadatas = [
            {
                "source": "The-Psychology-of-Money.pdf",
                "chunk_index": i
            }
        ]
    )

question = "Why is saving money important?"
question_embedding = generate_embeddings([question])

result = collection.query(
    query_embeddings = [question_embedding[0].tolist()],
    n_results = 4
)
print(result)
print("Number of records:", collection.count())
print(collection.name)