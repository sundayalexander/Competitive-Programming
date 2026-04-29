import pytest

from algorithms.prefix_and_postfix_sum import (
    prefix_sum,
    postfix_sum,
    find_pivot_index,
    find_pivot_index_optimized,
    product_of_array_except_self,
)


@pytest.mark.parametrize(
    "expected, nums",
    [
        ([5, 7, 6, 6, 9], [5, 2, -1, 0, 3]),
        ([1, 13, 8, 2, 52, 55], [1, 12, -5, -6, 50, 3]),
        ([1, 8, 11, 17, 22, 28], [1, 7, 3, 6, 5, 6]),
    ],
)
def test_prefix_sum(expected, nums):
    assert expected == prefix_sum(nums)


@pytest.mark.parametrize(
    "expected, nums",
    [
        ([9, 4, 2, 3, 3], [5, 2, -1, 0, 3]),
        ([55, 54, 42, 47, 53, 3], [1, 12, -5, -6, 50, 3]),
        ([28, 27, 20, 17, 11, 6], [1, 7, 3, 6, 5, 6]),
    ],
)
def test_postfix_sum(expected, nums):
    assert expected == postfix_sum(nums)


@pytest.mark.parametrize(
    "expected, nums",
    [(3, [1, 7, 3, 6, 5, 6]), (-1, [1, 2, 3]), (0, [2, 1, -1])],
)
def test_find_pivot_index(expected, nums):
    assert expected == find_pivot_index(nums)
    assert expected == find_pivot_index_optimized(nums)


@pytest.mark.parametrize(
    "expected, nums",
    [([24, 12, 8, 6], [1, 2, 3, 4]), ([0, 0, 9, 0, 0], [-1, 1, 0, -3, 3])],
)
def test_product_of_array_except_self(expected, nums):
    assert expected == product_of_array_except_self(nums)
