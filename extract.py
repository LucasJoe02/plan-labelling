"""
PDF Image Extractor
====================

This module provides functionality to extract images from PDF files. 
It leverages libraries such as PyMuPDF (fitz) to read and process PDF documents, 
identifying and saving images of selected pages to a specified directory.
Directions of use can be found in the README.

Author Lucas Redding (lre61) 2024
-------------
"""

import fitz
import os

USER_INPUT = True           # True to manually input page numbers for pdf extraction or False to read page numbers from file

PDF_DIR = "plans"           # Directory containing pdfs
PNG_DIR = "pngs"            # Directory containing pngs
DPI = 150                   # DPI to extract images at
PAGE_NUMS = "page_nums.txt" # File to save or read page numbers from

def get_page_numbers(nums):
    """Return a list of page nums from a file"""
    numbers = []
    with open(nums, "r") as file:
        for line in file:
            linelist = line.split()
            number = int(linelist[0].strip())
            numbers.append(number)
    return numbers

def get_page_num(i, page_numbers, name):
    """Either get a page number from user input or the page_numbers list"""
    if USER_INPUT:
        page_num = int(input("Enter page num of lighting page: "))
        with open(PAGE_NUMS, "a") as file:
            file.write(str(page_num)+" "+name+"\n")
    else:
        page_num = page_numbers[i]
    return page_num

def extract_pages():
    """Convert a given page of a pdf to a png and save to png folder"""
    page_numbers = []
    if not USER_INPUT:
        page_numbers = get_page_numbers(PAGE_NUMS)
    for i, filename in enumerate(sorted(os.listdir(PDF_DIR))):
        name, file_extension = os.path.splitext(filename)
        f = os.path.join(PDF_DIR, filename)
        if file_extension.lower() == '.pdf':
            print(name)
            page_num = get_page_num(i, page_numbers, name)
            doc = fitz.open(f)
            if page_num <= doc.page_count and page_num > 0:
                page = doc[page_num-1]
                pixmap = page.get_pixmap(dpi=DPI)
                pixmap.save(PNG_DIR + "/" + name + "-page-%i.png" % page_num)


def main():
    extract_pages()


if __name__ == "__main__":
    main()
