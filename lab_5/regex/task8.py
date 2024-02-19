import re


def split_string(string):
    x = re.findall("[A-Z][^A-Z]*", string)
    print(x)


split_string(input())
