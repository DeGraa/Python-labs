orderedList = [0, 0, 7]


def spy_game(lst):
    updatedlst = []
    for i in range(len(lst)):
        if lst[i] == 0 or lst[i] == 7:
            updatedlst.append(lst[i])

    if updatedlst == orderedList:
        return True
    else:
        return False


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
