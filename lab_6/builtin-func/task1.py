from functools import reduce


numbers = input().split()
print(reduce(lambda a, b: int(a) * int(b), numbers))


########################## Alternative
# from math import prod

# numbers2 = [1, 2, 3, 4, 5]
# print(prod(numbers2))
