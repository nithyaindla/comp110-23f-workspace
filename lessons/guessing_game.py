"""Program that loops until correct number is guessed."""

from random import randint

secret: int = randint(1, 10)
guess: int = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    print("Wrong!")
    # hints!
    if guess > secret:
        print("hint: too high!")
    else:
        print("hint: too low!")
    # Ask for a different guess
    guess = int(input("Try again: "))

# If I've reached this point, guess must = secret
print("You guessed right!")
