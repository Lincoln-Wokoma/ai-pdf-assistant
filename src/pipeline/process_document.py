from src.extraction.pdf_reader import extract_text_from_pdf
from src.chunking.chunking_lib import RecursiveChunking
from src.embeddings.embedding import generate_embeddings
from sentence_transformers import util


pdf_path = "/home/gamp/ai-pdf-assistant/data/The-Psychology-of-Money.pdf"

document = extract_text_from_pdf(pdf_path)

chunks = RecursiveChunking(document)
embeddings = generate_embeddings(chunks)

questions = [input("Input your question: ")]

question_embed = generate_embeddings(questions)
largest = 0
count = 0
for count, embedding in enumerate(embeddings):
    score = util.cos_sim(question_embed, embedding).item()

    if score > largest:
        largest = score
        required_chunk = chunks[count]
        similar_embedding = embedding


print("Highest similarity score", largest)
print("Chunk with highest simiarity", required_chunk)
print("Embedding", similar_embedding)