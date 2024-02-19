import re

pattern = "[a-z]+_[a-z]+"

x = re.findall(pattern, input())

print(x)
