"""
Unit tests for binary search algorithms.
"""

from impy.algorithms.binary_search import binary_search_with_loop, search


def test_binary_search():
    test_cases = (
        # Format: (index, key, search space).
        (2, 3, [1, 2, 3, 4, 5]),
        (8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
        (-1, 4, [10, 20, 30, 40, 50]),
        (1, 20, [10, 20, 30, 40, 50]),
    )
    for test_case in test_cases:
        assert binary_search_with_loop(test_case[1], test_case[2]) == test_case[0]


def test_search():
    test_cases = (
        # Format: (index, key, search space).
        (2, 3, [1, 2, 3, 4, 5]),
        (8, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
        (-1, 4, [10, 20, 30, 40, 50]),
        (1, 20, [10, 20, 30, 40, 50]),
    )
    for test_case in test_cases:
        assert (
            search(test_case[1], test_case[2], 0, right=len(test_case[2]) - 1)
            == test_case[0]
        )
