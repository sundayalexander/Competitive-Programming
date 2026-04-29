"""
Test module for the suffix array implementation.
"""

import pytest

from datastructures.suffix_array import naive_suffix_array, common_prefix_array


@pytest.mark.parametrize(
    "value,expected",
    [
        ("banana", [5, 3, 1, 0, 4, 2]),
        ("geeksforgeeks", [9, 1, 10, 2, 5, 8, 0, 11, 3, 6, 7, 12, 4]),
    ],
)
def test_suffix_array_naive(value, expected):
    assert expected == naive_suffix_array(value)


@pytest.mark.parametrize(
    "value,expected",
    [
        ("banana", [0, 1, 3, 0, 0, 2]),
        ("geeksforgeeks", [0, 4, 1, 3, 0, 0, 5, 0, 2, 0, 0, 0, 1]),
    ],
)
def test_common_prefix_array(value, expected):
    assert expected == common_prefix_array(value, naive_suffix_array)
