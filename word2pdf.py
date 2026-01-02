#!/usr/bin/env python3
"""
Simple Word to PDF converter
Converts all Word documents in a folder to PDF format
"""

import os
import sys
from pathlib import Path
from docx2pdf import convert


def convert_folder(input_folder):
    """
    Convert all Word documents in the specified folder to PDF

    Args:
        input_folder: Path to folder containing Word documents
    """
    input_path = Path(input_folder)

    if not input_path.exists():
        print(f"Error: Folder '{input_folder}' does not exist")
        sys.exit(1)

    if not input_path.is_dir():
        print(f"Error: '{input_folder}' is not a directory")
        sys.exit(1)

    # Find all Word documents
    word_files = list(input_path.glob("*.docx")) + list(input_path.glob("*.doc"))

    if not word_files:
        print(f"No Word documents found in '{input_folder}'")
        return

    print(f"Found {len(word_files)} Word document(s) to convert")

    # Convert each file
    for word_file in word_files:
        pdf_file = word_file.with_suffix('.pdf')

        try:
            print(f"Converting: {word_file.name} -> {pdf_file.name}")
            convert(str(word_file), str(pdf_file))
            print(f"  ✓ Success")
        except Exception as e:
            print(f"  ✗ Failed: {e}")

    print("\nConversion complete!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word2pdf.py <folder_path>")
        print("Example: python word2pdf.py ./my_documents")
        sys.exit(1)

    folder = sys.argv[1]
    convert_folder(folder)
