"""
PDF Image Converter
====================

This module converts a page from a single pdf file into a png image.
Directions of use can be found in the README.

Author Lucas Redding (lre61) 2024
-------------
"""

import fitz
import os

def pdftopng(pdf_dir, png_dir, dpi, plan, page_num):
    """Convert a page of pdf from a folder into a png"""
    name, file_extension = os.path.splitext(plan)
    f = os.path.join(pdf_dir, plan)
    if file_extension.lower() == '.pdf':
        doc = fitz.open(f)
        if page_num <= doc.page_count and page_num > 0:
                page = doc[page_num-1]
                pixmap = page.get_pixmap(dpi=dpi)
                pixmap.save(png_dir + "/" + name + "-page-%i.png" % page_num)

def main():
    print("This program converts a page from a single pdf file into a png.\nEnter the name of the input folder containing the pdf file: ")
    pdf_dir = input()
    print("Enter the name of the output folder to place the extracted png file: ")
    png_dir = input()
    print("Enter the desired output dpi for the extracted image: ")
    dpi = int(input())
    print("Enter filename of plan pdf (e.g. 'building_plan.pdf'): ")
    plan = input()
    page_num = int(input("Enter page num of lighting page: "))
    pdftopng(pdf_dir, png_dir, dpi, plan, page_num)


if __name__ == "__main__":
    main()
