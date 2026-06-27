from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent

file_dir = parent_dir / "data" / "The-Psychology-of-Money.pdf"
print(f"Parent directory: {parent_dir}")
print(f"File directory: {file_dir}")    