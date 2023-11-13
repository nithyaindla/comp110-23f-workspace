"""Combining two lists into a dictionary."""

__author__ = "730653507"


def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]:
    """Converts two lists into a single dictionary."""
    dictionary: dict[str, int] = {}
    
    if len(key_list) != len(value_list) or len(key_list) == 0 or len(value_list) == 0:
        """Returns an empty list if either list is empty or lists don't have equal lengths."""
        return dictionary
    else:
        for i in range(0, len(key_list)):
            dictionary[key_list[i]] = value_list[i]
        return dictionary

    
#print(zip(["head", "shoulders", "knees", "toes"], [1, 2, 3, 4]))