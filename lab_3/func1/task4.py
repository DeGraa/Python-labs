from math import sqrt


def isPrime(num):
    if num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
                break
        else:
            return True
    else:
        return False


def filter_prime(*list):
    updatedList = []
    for i in range(0, len(list) - 1):
        if isPrime(list[i]):
            updatedList.append(list[i])
    return updatedList


# def filter_prime(*list):
#     updatedList = []
#     for item in list:
#         if isPrime(item):
#             updatedList.append(item)
#     return updatedList


print(filter_prime(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15))
