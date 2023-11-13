"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730653507"

count = 0
word = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char = input("Enter a single character: ")
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

else:
    print("Searching for " + char + " in " + word)
    if word[0] == char:
        count = count + 1
        print(char + " found at index 0")
   
    if word[1] == char:
        count = count + 1
        print(char + " found at index 1")

    if word[2] == char:
        count = count + 1
        print(char + " found at index 2")

    if word[3] == char:
        count = count + 1
        print(char + " found at index 3")

    if word[4] == char:
        count = count + 1
        print(char + " found at index 4")

    if count == 1:
        print(str(count) + " instance of " + char + " found in " + word)

if count > 1:
    print(str(count) + " instances of " + char + " found in " + word)

if count == 0:
    print("No instances of " + char + " found in " + word)