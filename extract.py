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

def get_page_numbers(nums):
    """Return a list of page nums from a file"""
    numbers = []
    with open(nums, "r") as file:
        for line in file:
            linelist = line.split()
            number = int(linelist[0].strip())
            numbers.append(number)
    return numbers

def get_page_num(i, page_numbers, name, user_input, page_nums):
    """Either get a page number from user input or the page_numbers list"""
    if user_input:
        page_num = int(input("Enter page num of lighting page: "))
        with open(page_nums, "a") as file:
            file.write(str(page_num)+" "+name+"\n")
    else:
        page_num = page_numbers[i]
    return page_num

def extract_pages(pdf_dir, png_dir, dpi, user_input, page_nums):
    """Convert a given page of a pdf to a png and save to png folder"""
    page_numbers = []
    if not user_input:
        page_numbers = get_page_numbers(page_nums)
    for i, filename in enumerate(sorted(os.listdir(pdf_dir))):
        name, file_extension = os.path.splitext(filename)
        f = os.path.join(pdf_dir, filename)
        if file_extension.lower() == '.pdf':
            print(name)
            page_num = get_page_num(i, page_numbers, name, user_input, page_nums)
            doc = fitz.open(f)
            if page_num <= doc.page_count and page_num > 0:
                page = doc[page_num-1]
                pixmap = page.get_pixmap(dpi=dpi)
                pixmap.save(png_dir + "/" + name + "-page-%i.png" % page_num)


def main():
    print("Welcome to png building plan extraction.\nEnter the name of the input folder containing the pdf files: ")
    pdf_dir = input()
    print("Enter the name of the output folder to place the extracted png files: ")
    png_dir = input()
    print("Enter the desired output dpi for the extracted images: ")
    dpi = int(input())
    print("Do you want to get plan page numbers to extract from a file? (y/n): ")
    file_input = input().lower()
    page_nums = "page_nums.txt"
    while file_input not in ["y", "yes", "n", "no"]:
        print("Enter only 'y' or 'n'")
        print("Do you want to get plan page numbers to extract from a file? (y/n): ")
        file_input = input().lower()
    if file_input in ["y", "yes"]:
        user_input = False
        print("Enter the name of the .txt file containing the pdf names and page numbers (e.g. page_nums.txt): ")
        page_nums = input()
    else:
        user_input = True

    extract_pages(pdf_dir, png_dir, dpi, user_input, page_nums)


if __name__ == "__main__":
    main()
