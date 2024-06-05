import fitz
import os

PDF_DIR = "pdfs"
PNG_DIR = "pdfs"
DPI = 150

def pdftopng():
    """Convert all pdfs from a folder into pngs of each page"""
    for filename in os.listdir(PDF_DIR):
        name, file_extension = os.path.splitext(filename)
        f = os.path.join(PDF_DIR, filename)
        if file_extension.lower() == '.pdf':
            doc = fitz.open(f)
            for page in doc:
                pixmap = page.get_pixmap(dpi=DPI)
                pixmap.save(PNG_DIR + "/" + name + "-page-%i.png" % page.number)

def main():
    pdftopng()


if __name__ == "__main__":
    main()
