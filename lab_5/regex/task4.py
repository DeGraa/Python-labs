import re

pattern = "[A-Z][a-z]+"

x = re.findall(pattern, input())

print(x)
