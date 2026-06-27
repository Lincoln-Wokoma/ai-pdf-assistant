import pymupdf
from pathlib import Path
from typing import Union

def extract_text_from_pdf(pdf_path: Union[str, Path]) -> str:
    """
    Extracts text from a PDF file.

    Args:
        pdf_path (Union[str, Path]): The path to the PDF file.
    """
    doc = pymupdf.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text("text")

    doc.close()
    return text

if __name__ == "__main__":
    doc_path = input("Enter the path to the PDF file: ")
    print(extract_text_from_pdf(Path(doc_path)))