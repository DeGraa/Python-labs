class StringOperations:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        print(self.string.upper())


word = str(input())
ex1 = StringOperations(word)

print(ex1.getString())
ex1.printString()
