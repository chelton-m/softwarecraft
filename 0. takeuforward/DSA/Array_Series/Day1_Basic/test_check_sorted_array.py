import pytest
from check_sorted_array import is_sorted

@pytest.mark.parametrize("arr, expected", [
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 6, 7, 8], False),
    ([1, 2, 2, 3, 4], True),
    ([10, 20, 30, 40, 50], True),
    ([0, 0, 0, 0], True),
    ([-1, -2, -3, -4], False),
    ([1000, 2000, 3000, 4000, 5000], True),
    ([1], True),
    ([5, 5, 5, 5], True),
    ([1, 2, 3, 2, 5], False),
])
def test_is_sorted(arr, expected):
    assert is_sorted(arr) == expected


def test_is_sorted_single_element():
    assert is_sorted([42]) == True


def test_is_sorted_empty():
    assert is_sorted([]) == True


def test_is_sorted_negative_numbers():
    assert is_sorted([-5, -3, -1, 0, 2]) == True
    assert is_sorted([-5, -3, -1, 0, -2]) == False
