import fitz
import os

USER_INPUT = True

PDF_DIR = "plans"
PNG_DIR = "pngs"
DPI = 150
PAGE_NUMS = "page_nums.txt"

def get_page_numbers():
    """Return a list of page nums from a file"""
    numbers = []
    with open(PAGE_NUMS, "r") as file:
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
        page_numbers = get_page_numbers()
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
