import re

pattern = "ab*"

if re.search(pattern, input()):
    print(True)
else:
    print(False)
