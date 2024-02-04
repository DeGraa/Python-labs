from info import movies


def underCateg(category):
    lst = []
    for movie in movies:
        if movie["category"] == category:
            lst.append(movie["name"])
    print(lst)


movie_category = input("Enter the movie category: ")
underCateg(movie_category)
