import re


def toCamel(snakeText):
    regex = "^(\w+)\_(\w+)"
    match = re.search(regex, snakeText)
    if match:
        first = match.group(1)
        second = match.group(2)

        second = second[0].upper() + second[1:]
        camelText = first + second
        print(camelText)


toCamel(input())

#################################### Alternative

# def snake_to_camel(snake_str):
#     components = snake_str.split("_")
#     camel_case = components[0] + "".join(x.title() for x in components[1:])
#     return camel_case


# camel_case_str = snake_to_camel(input())
# print(camel_case_str)
