from random import randint


def game():
    print("Hello! What is your name?")
    name = str(input())
    print(f"Well, {name}, I am thinking of a number between 1 and 20. \nTake a guess.")

    target_number = randint(1, 20)

    count = 0

    while True:
        num = int(input())
        count += 1

        if num > target_number:
            print("Your guess is too high. \nTake a guess.")
        elif num < target_number:
            print("Your guess is too low. \nTake a guess.")
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break


game()
