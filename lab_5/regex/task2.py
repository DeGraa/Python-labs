import re

pattern = "ab{2,3}"

if re.search(pattern, input()):
    print(True)
else:
    print(False)
