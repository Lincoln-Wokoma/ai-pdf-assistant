from src.vector_store.retriever import retrieve_relevant_chunks
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

question = "Why do we save"

result = retrieve_relevant_chunks(question)

context = "\n\n".join(result)

prompt = f"""
You are an assistant answering questions about the provided PDF.

Context:
{context}

Question:
{question}

Answer the question using the context provided.
"""

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=prompt
)

print(interaction.output_text)