import math


def volume(rad):
    return 4 / 3 * rad**3 * math.pi


radius = int(input())
print(volume(radius))
