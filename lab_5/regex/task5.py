import re

pattern = "a.*b$"

if re.search(pattern, input()):
    print(True)
else:
    print(False)
