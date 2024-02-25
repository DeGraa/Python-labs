import os


def check_path(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print(f"Path '{path}' does not exist")


check_path(input("Enter path to check: "))
