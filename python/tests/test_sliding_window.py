import pytest

from algorithms.sliding_window import max_window_sum, longest_substring


@pytest.mark.parametrize(
    "expected,nums,window_length",
    [(6, [5, 2, -1, 0, 3], 3), (51, [1, 12, -5, -6, 50, 3], 4)],
)
def test_max_window_sum(expected, nums, window_length):
    assert expected == max_window_sum(nums, window_length)


@pytest.mark.parametrize(
    "expected,input_str",
    [(3, "abcabcbb"), (1, "bbbbb"), (3, "pwwkew"), (1, " "), (3, "dvdf")],
)
def test_longest_substring(expected, input_str):
    assert expected == longest_substring(input_str)
