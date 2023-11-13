"""Practice Writing Functions."""


def mimic(my_words: str) -> str:
    """Given the string my my_words, outputs the same string."""
    return my_words


def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at the index letter_idx."""
    if letter_idx >= len(my_words):
        return ("Index too high!")
    # If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]


mimic("hello!")
print(mimic("hello!"))  # this displays the return
print(mimic_letter("hello", 4))