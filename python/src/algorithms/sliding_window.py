"""
Sliding window algorithm
The sliding window algorithm is a powerful technique for efficiently solving problems that involve contiguous sequences (subarrays or substrings) in data structures like arrays and strings. It optimizes time complexity from a typical O(n²) or O(n³) in a brute-force approach to a linear O(n) by avoiding redundant computations.
Learn more here:https://www.geeksforgeeks.org/dsa/window-sliding-technique/
"""


def max_window_sum(nums: list[int], window_length: int) -> int:
    """
    Calculate the maximum sum over a given window length.
    Args:
        nums (list[int]): a list of integers.
        window_length (int): the window length.

    Returns:

    """
    current_sum = sum(nums[:window_length])
    max_sum_so_far = current_sum
    nums_length = len(nums)
    for index in range(nums_length - window_length):
        current_sum += nums[index + window_length] - nums[index]
        max_sum_so_far = max(max_sum_so_far, current_sum)

    return max_sum_so_far


# Dynamic window size implementation.
def longest_substring(input_str: str) -> int:
    """
    Find the length of the Longest Substring Without Repeating Characters

    Args:
        input_str (str): the input string.

    Returns:
        int: the length of the longest substring
    """

    right_index = 0
    left_index = right_index
    current_length = 0
    maximum_length = current_length
    input_length = len(input_str)
    seen_characters = set()

    while right_index < input_length:
        if input_str[right_index] not in seen_characters:
            current_length += 1
            seen_characters.add(input_str[right_index])
            right_index += 1

        else:
            current_length -= 1
            seen_characters.remove(input_str[left_index])
            left_index += 1

        maximum_length = max(maximum_length, current_length)

    return maximum_length
