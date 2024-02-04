def reversedString(string):
    words = string.split()
    words.reverse()
    return " ".join(words)


sentence = str(input())

print(reversedString(sentence))
