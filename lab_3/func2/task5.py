from info import movies


def average(category):
    lst = []

    for movie in movies:
        if movie["category"] == category:
            lst.append(movie["imdb"])

    avg = sum(lst) / len(lst)
    print(avg)


movie_category = input()
average(movie_category)
