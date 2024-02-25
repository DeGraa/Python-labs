string = input()

upper = sum(1 for char in string if char.isupper())
lower = sum(1 for char in string if char.islower())

print("the number of upper case letters: ", upper)
print("the number of lower case letters: ", lower)
