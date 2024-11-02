# PDF Plan Extraction Toolkit

This toolkit provides functionality for cleaning converting PDF pages to PNG images, and extracting specific pages as images from multiple PDFs. The modules are designed to work with PDF files in specified input directories, producing images in PNG format at a chosen DPI resolution.

## Overview
This project consists of three main Python scripts:

* convert.py: Converts a single page of a PDF to a PNG image.
* extract.py: Extracts images of selected pages from multiple PDFs.
* clean.py: Cleans a specified directory by removing all files in it.

## Requirements
* Python 3.x
* PyMuPDF (fitz) library for PDF processing:
    ```
    pip install pymupdf
    ```
## Usage

1. PDF Image Converter: Use `python convert.py` to convert a single PDF page to PNG. The script will prompt for details about input and output folders, DPI, PDF filename, and the desired page number.

2. PDF Image Extractor: Run `python extract.py` to batch extract pages from PDFs in a folder. You can choose to manually enter page numbers or use a text file listing page numbers for each PDF.

3. Directory Cleaner: Run `python clean.py` to clear a specified directory. You'll be prompted for the directory path.