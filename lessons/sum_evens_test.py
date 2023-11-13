"""Testing my sum of evens function."""
# all test files should be named so that it ends with _test

from lessons.sum_evens import sum_evens_of_list


# all test functions must start with test_.
def test_empty_list() -> None:
    # edge case: odd cases like empty list or some other weird something.
    """Tests sum_evens_of_list([]); should return 0."""
    assert sum_evens_of_list([]) == 0


def test_sum_one_element() -> None:
    # use cases: typical expected cases.
    """Tests sum_evens_of_list([2]); should return 2."""
    test_list: list[int] = [2]
    assert sum_evens_of_list(test_list) == 2


def test_sum_positives() -> None:
    """Tests sum_events_of_list([1, 2, 3, 4]); should return 6."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_of_list(test_list) == 6


def test_sum_neg_and_pos() -> None:
    """Tests sum_events_of_list([-1, -2, 3, 4]); should return 2."""
    test_list: list[int] = [-1, -2, 3, 4]
    assert sum_evens_of_list(test_list) == 2


# to run the test, type this into terminal: python -m pytest lessons/sum_evens_test.py.