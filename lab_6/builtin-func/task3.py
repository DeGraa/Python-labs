def is_pal(s):
    s = "".join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]


word = input()

if is_pal(word):
    print(True)
else:
    print(False)
