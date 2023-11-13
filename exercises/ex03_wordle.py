"""EX03 - Wordle - THE OG WORDLE."""

__author__ = "730653507"


def contains_char(word: str, char: str) -> bool:
    """This function checks for the existence of a specific character(parameter 2) in a word(parameter 1)."""
    assert len(char) == 1
    i = 0
    bool_contains_char = False
    """Checks every index of the word(parameter 2) for the character(parameter 1)."""
    while i < len(word):
        if word[i] == char:
            bool_contains_char = True
        i = i + 1
    return bool_contains_char

    
def emojified(user_guess: str, secret_word: str) -> str:
    """This function codes the guess(parameter 2) into emojis that correlate with the correctness of the guess in respect to the secret word(parameter 1)."""
    WHITE_BOX: str = "\U00002B1C"  # this char doesn't exist in word at all
    GREEN_BOX: str = "\U0001F7E9"  # this char exists and is in the right place
    YELLOW_BOX: str = "\U0001F7E8"  # this char exists but is in the wrong place
    assert len(user_guess) == len(secret_word)
    output: str = ""
    x = 0
    """checks every character of guess"""
    while x < len(user_guess):
        """if the characters match"""
        if secret_word[x] == user_guess[x]:
            output = output + GREEN_BOX
        elif contains_char(secret_word, user_guess[x]):
            output = output + YELLOW_BOX
        else: 
            output = output + WHITE_BOX
        x = x + 1
    return output


def input_guess(expected_length: int) -> str:
    """This function collects the user guesses of a specified length(parameter 1) and makes sure that they are of the correct length."""
    user_input = input("Enter a " + str(expected_length) + " character word: ")
    while len(user_input) != expected_length:
        user_input = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return (user_input)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_Number = 1
    secret = "codes"
    win: bool = False
    while (turn_Number <= 6) and win is False:
        print("=== Turn " + str(turn_Number) + "/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print("You won in " + str(turn_Number) + "/6 turns!")
            win = True
        else:
            turn_Number = turn_Number + 1
    if win is False: 
        print("X/6 - Sorry, try again tomorrow!")
        

if __name__ == "__main__":
    main()