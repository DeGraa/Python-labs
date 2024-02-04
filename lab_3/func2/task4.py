from info import movies


def average(lst):

    total = 0
    num = len(lst)

    for name in lst:
        for movie in movies:
            if movie["name"] == name:
                total += movie["imdb"]

    avg = total / num
    return avg


print(
    average(
        [
            "Usual Suspects",
            "Hitman",
        ]
    )
)
