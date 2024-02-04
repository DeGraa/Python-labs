heads, legs = map(int, input().split())


def solve(heads, legs):
    rabbits = (legs - 2 * heads) / 2
    chickens = heads - rabbits
    print(int(rabbits), int(chickens))


solve(heads, legs)
