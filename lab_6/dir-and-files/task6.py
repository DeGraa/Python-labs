import string


for letter in string.ascii_uppercase:
    path = (
        "/Users/adilkanatov/Documents/py_labs/lab_6/dir-and-files/txt-documents/"
        + letter
        + ".txt"
    )
    with open(path, "w") as my_file:
        my_file.write("Hello".format(path))
