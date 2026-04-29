"""
Unit test for Two pointers implementation based on case studies.
"""

import pytest

from impy.algorithms.two_pointers import (
    trapping_rain_water,
    move_zeroes,
    move_zeros_using_for_loop,
    is_subsequence,
    max_num_k_sum_pairs,
    move_zeros_using_unstable_partition,
)


@pytest.mark.parametrize(
    "value,expected",
    [([3, 0, 1, 0, 4, 0, 2], 10), ([3, 0, 2, 0, 4], 7), ([2, 1, 5, 3, 1, 0, 4], 9)],
)
def test_trapping_rain_water(value, expected):
    assert expected == trapping_rain_water(value)


@pytest.mark.parametrize(
    "value,expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([3, 0, 1, 0, 4, 0, 2], [3, 1, 4, 2, 0, 0, 0]),
    ],
)
def test_move_zeroes(value, expected):
    move_zeroes(value)
    assert value == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([3, 0, 1, 0, 4, 0, 2], [3, 1, 4, 2, 0, 0, 0]),
    ],
)
def test_move_zeroes_using_slow_and_fast_pointer(value, expected):
    move_zeros_using_for_loop(value)
    assert value == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ([0, 1, 0, 3, 12], [12, 1, 3, 0, 0]),
        ([3, 0, 1, 0, 4, 0, 2], [3, 2, 1, 4, 0, 0, 0]),
    ],
)
def test_move_zeroes_using_unstable_partition(value, expected):
    move_zeros_using_unstable_partition(value)
    assert value == expected


@pytest.mark.parametrize(
    "value,expected",
    [(["abc", "ahbgdc"], True), (["axc", "ahbgdc"], False), (["", "ahbgdc"], True)],
)
def test_is_subsequence(value, expected):
    assert is_subsequence(*value) == expected


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 3, 4], 5, 2),
        ([1, 3, 3, 3, 4], 6, 1),
        ([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2, 2),
        ([1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5], 7, 5),
        ([1, 1, 1, 2, 2, 2, 3, 4], 4, 2),
    ],
)
def test_max_num_k_sum_pairs(nums, k, expected):
    assert max_num_k_sum_pairs(nums, k) == expected
