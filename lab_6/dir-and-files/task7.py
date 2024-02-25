def copy_file(path1, path2):
    with open(path1, "r") as file1:
        with open(path2, "w") as file2:
            file2.write(file1.read())


file1 = input("The path of the source file: ")
file2 = input("The path of the destination file: ")
copy_file(file1, file2)
