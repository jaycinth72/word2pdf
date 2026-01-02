#!/usr/bin/env python3
"""
Simple Word to PDF converter
Converts all Word documents in a folder to PDF format
"""

import os
import sys
from pathlib import Path
from docx2pdf import convert
import fitz  # PyMuPDF


def create_thumbnail(pdf_path, jpg_path):
    """
    Create a JPG image of the first page of a PDF

    Args:
        pdf_path: Path to the PDF file
        jpg_path: Path where the JPG should be saved
    """
    pdf_document = fitz.open(pdf_path)
    first_page = pdf_document[0]

    # Render page to an image (matrix for resolution, 2.0 = 2x resolution)
    pix = first_page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
    pix.save(jpg_path)

    pdf_document.close()


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
        jpg_file = word_file.with_suffix('.jpg')

        try:
            print(f"Converting: {word_file.name} -> {pdf_file.name}")
            convert(str(word_file), str(pdf_file))
            print(f"  [OK] PDF created")

            # Create thumbnail
            print(f"Creating thumbnail: {jpg_file.name}")
            create_thumbnail(str(pdf_file), str(jpg_file))
            print(f"  [OK] Thumbnail created")

        except Exception as e:
            print(f"  [FAIL] Error: {e}")

    print("\nConversion complete!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python word2pdf.py <folder_path>")
        print("Example: python word2pdf.py ./my_documents")
        sys.exit(1)

    folder = sys.argv[1]
    convert_folder(folder)
