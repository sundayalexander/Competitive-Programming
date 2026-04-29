import pytest

from impy.algorithms.sort import cycle_sort, bubble_sort

_TEST_INPUTS = [
    ([2, 4, 5, 1, 3], [1, 2, 3, 4, 5]),
    ([9, 4, 6, 8, 14, 3], [3, 4, 6, 8, 9, 14]),
    ([4, 1, 5, 1, 2, 3], [1, 1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize(
    "nums,expected",
    _TEST_INPUTS,
)
def test_cycle_sort(nums, expected):
    assert cycle_sort(nums) == expected


@pytest.mark.parametrize(
    "nums,expected",
    _TEST_INPUTS,
)
def test_bubble_sort(nums, expected):
    assert bubble_sort(nums) == expected
