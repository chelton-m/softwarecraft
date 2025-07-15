import pytest
from largest_element import largest_element


@pytest.mark.parametrize("arr, expected", [
    ([10, 2], 10),
    ([3, 30, 34, 5, 9], 34),
    ([1, 2, 3, 4, 5], 5),
    ([100, 20, 30, 40, 50], 100),
    ([0, 0, 0, 0], 0),
    ([-1, -2, -3, -4], -1),
    ([1000, 2000, 3000, 4000, 5000], 5000),
    ([1], 1),
    ([5, 5, 5, 5], 5),
])
def test_largest_element(arr, expected):
    assert largest_element(arr) == expected


def test_largest_element_single_negative():
    assert largest_element([-10]) == -10


def test_largest_element_mixed():
    assert largest_element([-10, 0, 10]) == 10


def test_largest_element_all_same():
    assert largest_element([7, 7, 7, 7]) == 7


def test_largest_element_large_numbers():
    assert largest_element([999999999, 123456789, 987654321]) == 999999999
