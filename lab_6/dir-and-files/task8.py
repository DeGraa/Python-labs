import os


def delete_file(path):
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"The file '{path}' has been successfully deleted")
        except Exception as e:
            print(e)
    else:
        print(f"The file '{path}' does not exist")


file_path = (
    "/Users/adilkanatov/Documents/py_labs/lab_6/dir-and-files/txt-documents/example.txt"
)
delete_file(file_path)
