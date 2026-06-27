import pymupdf
from pathlib import Path
from typing import Union

def extract_text_from_pdf(pdf_path: Union[str, Path], output_path: Union[str, Path]) -> None:
    """
    Extracts text from a PDF file and saves it to a text file.

    Args:
        pdf_path (Union[str, Path]): The path to the PDF file.
        output_path (Union[str, Path]): The path to the output text file.
    """
    doc = pymupdf.open(pdf_path)

    with open(output_path, "wb") as out:
        for page in doc:
            text = page.get_text("text")
            out.write(text.encode("utf-8"))
            #out.write(bytes((12,)))  # Form feed character to separate pages

    doc.close()

if __name__ == "__main__":
    print(extract_text_from_pdf(Path("C:/Users/Lincoln/Documents/Projects/AI_Automation & Engineering/ai-pdf-assistant/data/The-Psychology-of-Money.pdf"), Path("C:/Users/Lincoln/Documents/Projects/AI_Automation & Engineering/ai-pdf-assistant/data/processed_data/The-Psychology-of-Money.txt")))