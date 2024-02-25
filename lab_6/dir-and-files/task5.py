path = (
    "/Users/adilkanatov/Documents/py_labs/lab_6/dir-and-files/txt-documents/example.txt"
)


lst = [1, 2, 3, 4, 5]

with open(path, "w") as my_file:
    for item in lst:
        my_file.write(str(item) + "\n")
