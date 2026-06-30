

def Chunker(text):
    """
    Splits the input text into chunks based on double newlines.

    Args:
        text (str): The input text to be chunked.

    Returns:
        list: A list of text chunks.
    """
    chunks = text.split("\n \n")
    return chunks