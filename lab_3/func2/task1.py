from info import movies


def rating(value):
    for movie in movies:
        if movie["name"] == value:
            return movie["imdb"] > 5.5
    return False


movie_name = input("Enter the movie name: ")
print(rating(movie_name))
