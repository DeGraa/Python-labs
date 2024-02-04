def uniqueList(lst):
    unique_list = []
    for elem in lst:
        if elem not in unique_list:
            unique_list.append(elem)
    return unique_list


print(uniqueList([1, 1, 2, 3, 4, 5]))
