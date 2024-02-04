from info import movies


def sublist():
    lst = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            lst.append(movie["name"])
    print(lst)


sublist()
