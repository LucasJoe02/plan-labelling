Plan Labelling Scripts by Lucas Redding (lre61) (SENG402 Building Plan AI Automation Project)

**Introduction**

The scripts in this project are meant to support the development of an AI model aimed at searching building plan images for doors and labelling the doors based on the category they fall into. The motivation for this is to save time and resources when attempting to provide quotes to building companies for doors when they request them from the client company 'Independent Doors' (ID). These scripts are used to take groups of building plans as PDFs and extract useful images from those plans that can then be used to train the AI model. There is the ability to decide on the DPI and format of the images as well as the page being extracted indivdually for each building plan pdf.

**Dependencies:**

    1. Python 3.8.10 (May work on other versions of Python 3)
    2. PyMuPDF (Installed with 'pip install PyMuPDF')
    3. Linux Mint OS (Other OSs may also work)

**How to run the application:**

    1. Ensure you have an input and output folder in your root directory
    2. Fill the input folder with building plan pdf documents
    3. Ensure that the output folder is empty
    4. Open the extract.py file to set the desired constants
    5. Set the values for PDF_DIR and PNG_DIR to the names of your input and output files respectively
    6. Set the desired DPI for the output image
    7. Adjust USER_INPUT: True to enter page numbers manually or False to enter page numbers via a file
    8. Ensure a file of page numbers seperated by newlines called 'page_nums.txt' is at root
    9. Leave 'page_nums.txt' empty if USER_INPUT is True otherwise make sure it is filled with page numbers
    10. Open the root folder in a terminal and run `python3 extract.py`
    11. If USER_INPUT is set to True then you will be prompted to input the page number to extract for each pdf
    12. After all pdfs have been looped through the output folder will have all the images extracted
  
Notes:
The 'page_nums.txt' file will fill with page numbers as you input them if USER_INPUT is True. This file can then be used to extract the same images in a different format or DPI without re-entering the desired page numbers. Running the 'clean.py' script will empty the set in its main function which can be adjusted to clean out the output folder.

mothership will win.
