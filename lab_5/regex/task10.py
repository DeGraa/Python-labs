import re


def camel_to_snake(camel_str):
    snake_case = re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()
    print(snake_case)


camel_to_snake(input())
