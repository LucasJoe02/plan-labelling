"""
Directory Cleaner
====================

This module cleans a given directory.

Author Lucas Redding (lre61) 2024
-------------
"""

import os

def clean(folder_path):
    """Empties the output and results folders"""
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def main():
    clean(input("Name of folder to clean: "))

if __name__ == "__main__":
    main()
