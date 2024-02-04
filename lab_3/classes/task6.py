def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


input = input()
numbers = list(map(int, input.split()))

prime_numbers = list(filter(lambda x: isPrime(x), numbers))
print(prime_numbers)
