"""EX07- Unit Tests for dictionary.py!"""

__author__ = "730653507"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_use1() -> None:
    """Use Case 1 for invert({})."""
    test_dict: dict[str, str] = {"Peyton": "artist", "Brooke": "fashion designer", "Lucas": "writer", "Hailey": "teacher", "Nathan": "athlete"}
    assert invert(test_dict) == {"artist": "Peyton", "fashion designer": "Brooke", "writer": "Lucas", "teacher": "Hailey", "athlete": "Nathan"}


def test_invert_use2() -> None: 
    """Use Case 2 for invert({})."""
    test_dict: dict[str, str] = {"up": "down", "left": "right"}
    assert invert(test_dict) == {"down": "up", "right": "left"}


def test_invert_edge() -> None:
    """Edge Case for invert({}): empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_favorite_color_use1() -> None:
    """Use Case 1 for favorite_color({})."""
    test_dict: dict[str, str] = {"Hailey": "green", "Brooke": "purple", "Peyton": "purple"}
    assert favorite_color(test_dict) == "purple"


def test_favorite_color_use2() -> None:
    """Use Case 1 for favorite_color({})."""
    test_dict: dict[str, str] = {"Nathan": "red", "Lucas": "black", "Dan": "red", "Keith": "blue"}
    assert favorite_color(test_dict) == "red"


def test_favorite_color_edge() -> None:
    """Edge Case for favorite_color({}): tie between colors."""
    test_dict: [str, str] = {"Nathan": "red", "Brooke": "purple", "Peyton": "purple", "Dan": "red", "Lucas": "black"}
    assert favorite_color(test_dict) == "purple"


def test_count_use1() -> None:
    """Use Case 1 for count([])."""
    test_list: [str] = ["happy", "sad", "tired", "tired", "okay", "okay", "okay", "fine"]
    assert count(test_list) == {"happy": 1, "sad": 1, "tired": 2, "okay": 3, "fine": 1}


def test_count_use2() -> None:
    """Use Case 1 for count([])."""
    test_list: [str] = ["twix", "skittles", "reeses", "skittles", "kitkats", "reeses", "kitkats", "twix"]
    assert count(test_list) == {"twix": 2, "skittles": 2, "reeses": 2, "kitkats": 2}


def test_count_edge() -> None:
    """Edge Case for count([]): empty list."""
    test_list: [str] = []
    assert count(test_list) == {}


def test_alphabetizer_use1() -> None:
    """Use Case 1 for alphabetizer([])."""
    test_list: [str] = ["apples", "bananas", "cats"]
    assert alphabetizer(test_list) == {"a": ["apples"], "b": ["bananas"], "c": ["cats"]}


def test_alphabetizer_use2() -> None:
    """Use Case 2 for alphabetizer([])."""
    test_list: [str] = ["Car", "Ball", "Truck", "city", "Dirt", "Boston", "new"]
    assert alphabetizer(test_list) == {"c": ["Car", "city"], "b": ["Ball", "Boston"], "t": ["Truck"], "d": ["Dirt"], "n": ["new"]}


def test_alphabetizer_edge() -> None:
    """Edge Case for alphabetizer([]): empty list."""
    test_list: [str] = []
    assert alphabetizer(test_list) == {}


def test_update_attendance_use1() -> None:
    """Use Case 1 for update_attendance({}, "", "")."""
    test_dict: [str, list[str]] = {"Tuesday": ["Ron"]}
    test_day: str = "Wednesday"
    test_student: str = "Kate"
    assert update_attendance(test_dict, test_day, test_student) == {"Tuesday": ["Ron"], "Wednesday": ["Kate"]}


def test_update_attendance_use2() -> None:
    """Use Case 1 for update_attendance({}, "", "")."""
    test_dict: [str, list[str]] = {"Monday": ["Kiara", "June", "Alizeh"], "Tuesday": ["Raina", "Rosie"], "Saturday": ["Bob"]}
    test_day: str = "Saturday"
    test_student: str = "Bob"
    assert update_attendance(test_dict, test_day, test_student) == {"Monday": ["Kiara", "June", "Alizeh"], "Tuesday": ["Raina", "Rosie"], "Saturday": ["Bob"]}


def test_update_attendance_edge() -> None:
    """Edge Case for update_attendance({}, "", ""): empty second parameter."""
    test_dict: [str, list[str]] = {"Monday": ["Kiara", "Alizeh"], "Tuesday": ["Rosie"]}
    test_day: str = ""
    test_student: str = "Kate"
    assert update_attendance(test_dict, test_day, test_student) == {"Monday": ["Kiara", "Alizeh"], "Tuesday": ["Rosie"], "": ["Kate"]}