def is_palindrome(str):
    return str == str[::-1]


word = str(input())
print(is_palindrome(word))
