path = "/Users/adilkanatov/Documents/py_labs/lab_6/dir-and-files/txt-documents/text.txt"

try:
    with open(path) as my_file:
        line_count = sum(1 for line in my_file)
    print(line_count)
except FileNotFoundError:
    print("File not found")
