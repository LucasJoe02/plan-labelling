import os

"""Empties the output and results folders"""
def clean(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def main():
    clean('pngs')

if __name__ == "__main__":
    main()
