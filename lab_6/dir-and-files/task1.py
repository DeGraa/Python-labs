import os


def list_dirs_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)


path = "/Users/adilkanatov/Documents/py_labs"

list_dirs_files(path)
