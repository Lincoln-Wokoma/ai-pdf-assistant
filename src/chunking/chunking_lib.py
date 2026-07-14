from langchain_text_splitters import RecursiveCharacterTextSplitter

def RecursiveChunking(document, chunk_size=100, chunk_overlap=10):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(document)