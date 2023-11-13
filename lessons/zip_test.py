"""Test my zip function."""

__author__ = "730653507"

from lessons.zip import zip


def test_two_empty_lists() -> None:
    """Edge case: Tests zip([], []); should return {}"""
    test_list1: list[str] = []
    test_list2: list[int] = []
    assert zip(test_list1, test_list2) == {}


def test_negative_nums() -> None:
    """Use case 1: Tests zip(["head", "shoulders", "knees", "toes"], [-1, -2, -3, -4]); should return {'head': 1, 'shoulders': 2, 'knees': 3, 'toes': 4}"""
    test_list1: list[str] = ["head", "shoulders", "knees", "toes"]
    test_list2: list[int] = [1, 2, 3, 4]
    assert zip(test_list1, test_list2) == {'head': 1, 'shoulders': 2, 'knees': 3, 'toes': 4}


def test_unique_lists() -> None:
    """Use Case 2: Tests zip(["a", "b", "c"], [1, 2, 3]); should return {'a': 1, 'b': 2, 'c': 3}"""
    test_list1: list[str] = ["a", "b", "c"]
    test_list2: list[int] = [1, 2, 3]
    assert zip(test_list1, test_list2) == {'a': 1, 'b': 2, 'c': 3}