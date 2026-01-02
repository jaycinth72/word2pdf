# Word to PDF Converter

Simple Python script to batch convert Word documents to PDF format.

## Prerequisites

**Linux users**: You need LibreOffice installed:
```bash
sudo apt-get install libreoffice
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python word2pdf.py <folder_path>
```

### Example

```bash
python word2pdf.py ./my_documents
```

This will convert all `.doc` and `.docx` files in the specified folder to PDF format with the same base filename.

## Features

- Converts both `.doc` and `.docx` files
- Preserves original filenames (changes extension to `.pdf`)
- Shows progress for each file
- Error handling for individual files (continues on failure)

## Output

PDFs are saved in the same folder as the source Word documents.
