def checker(tup):
    return all(tup)


tuple1 = (True, True, True)
tuple2 = (True, False, True)

print(checker(tuple1))
print(checker(tuple2))
