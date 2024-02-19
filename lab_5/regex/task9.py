import re


def insert_spaces(string):
    x = re.sub("(.)([A-Z])", r"\1 \2", string)
    print(x)


insert_spaces(input())

################# Alternative
# x = re.sub(r"(?<!^)(?=[A-Z])", " ", string)
