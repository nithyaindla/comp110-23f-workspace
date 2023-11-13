"""Dictionary related utility functions."""

__author__ = "730653507"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the inputted dictionary."""
    key_list = []
    value_list = []
    for i in dictionary:
        if dictionary[i] in value_list:
            raise KeyError("Duplicate keys are not allowed.")
        else: 
            key_list.append(i)
            value_list.append(dictionary[i])
    new_dict: dict[str, str] = {}
    for i in range(0, len(value_list)):
        if value_list[i] in new_dict:
            raise KeyError("error message of your choice here!")
        else:
            new_dict[value_list[i]] = key_list[i]
    return new_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color that appears/is voted for most frequently."""
    color_counter: dict[str, int] = {}
    popcolor: str = ""
    i: int = 0
    for name in dictionary:
        if dictionary[name] in color_counter:
            color_counter[dictionary[name]] += 1
        else: 
            color_counter[dictionary[name]] = 1
        if i < color_counter[dictionary[name]]:
            popcolor = dictionary[name]
            i = color_counter[dictionary[name]]
    return popcolor


def count(input: list[str]) -> dict[str, int]:
    """Counts the number of times each value in the list appeared in the input list and outputs a dictionary.""" 
    result: dict[str, int] = {}
    for i in input:
        if i in result:
            result[i] = result[i] + 1
        else: 
            result[i] = 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of lists that organize words by their starting letter."""
    result: dict[str, list[str]] = {}
    for word in input:
        start: str = word[0].lower()
        if start not in result:
            result[start] = [word]
        else:
            result[start].append(word)
    print(result)
    return result          


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates and returns a dictionary of days of the week and present students."""
    i: list[str] = []
    if day in attendance_log:
        i = attendance_log[day]
        if student not in attendance_log:
            i.append(student)
        attendance_log[day] = i
    else:
        i.append(student)
        attendance_log[day] = [student]
    return attendance_log