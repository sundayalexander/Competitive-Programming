"""
Two Pointers algorithm implementation using different case studies.
"""


def trapping_rain_water(heights: list[int]) -> int:
    """
     Given an array arr[] of size n consisting of non-negative integers, where each element represents the height of a
     bar in an elevation map and the width of each bar is 1, determine the total amount of water that can be trapped
     between the bars after it rains.
    Args:
        heights (list[int]): An array containing only positive integers.

    Returns:
        int: The total amount of water that can be trapped between the bars after it rains.
    """
    max_water = 0
    left, right = 0, len(heights) - 1
    left_max_height, right_max_height = heights[left], heights[right]
    left += 1
    right -= 1
    while left <= right:
        # Navigate through the container's heights.
        if left_max_height <= right_max_height:
            max_water += max(left_max_height - heights[left], 0)
            left_max_height = max(left_max_height, heights[left])
            left += 1
        else:
            max_water += max(right_max_height - heights[right], 0)
            right_max_height = max(right_max_height, heights[right])
            right -= 1

    return max_water


def move_zeroes(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
    elements.
    Note that you must do this in-place without making a copy of the array.

    Returns:
        None
    """
    left, right = 0, 1
    nums_length = len(nums)
    while right < nums_length:
        # Determine if the element on left pointer is zero and the element on right pointer is not zero.
        if nums[left] != nums[right] and nums[left] == 0:
            # Swap the elements.
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        elif left == right:
            right += 1
        elif nums[left] != 0:
            left += 1
        else:
            right += 1


def move_zeros_using_for_loop(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
    elements.
    Note that you must do this in-place without making a copy of the array.

    This is implemented using slow and fast pointerrs.

    Args:
        nums (list[int]): An array containing only positive integers.

    Returns:
        None
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


def move_zeros_using_unstable_partition(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
    elements.
    Note that you must do this in-place without making a copy of the array.

    This is implemented using unstable partitions.

    Args:
        nums (list[int]): An array containing only positive integers.

    Returns:
        None
    """
    right = len(nums) - 1
    left = 0
    while left <= right:
        if nums[right] == 0:
            right -= 1
        elif nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
        else:
            left += 1


def is_subsequence(s: str, t: str) -> bool:
    """
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
    of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not).

    Example 1:

    Input: s = "abc", t = "ahbgdc"
    Output: true

    Args:
        s (str): the expected subsequence value.
        t (str): the actual string containing the subsequence or not.

    Returns:
        bool: return true if s is a subsequence of t, or false otherwise.
    """
    subsequence_pointer = 0
    t_length = len(t)
    s_length = len(s)
    matched_index = -1
    # Walk through t string and compare the index value with sequence pointer value;
    for index in range(t_length):
        if subsequence_pointer == s_length:
            break
        if s[subsequence_pointer] == t[index]:
            matched_index = subsequence_pointer
            subsequence_pointer += 1
    # Determine if all index has been matched.
    return matched_index == s_length - 1


def max_num_k_sum_pairs(nums: list[int], k: int) -> int:
    """
    You are given an integer array nums and an integer k.
    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
    Return the maximum number of operations you can perform on the array.
    Args:
        nums (list[int]): an integer array
        k (int): an integer sum value.

    Returns:
        int: number of operations.
    """
    operation_count = 0
    left, right = 0, len(nums) - 1
    nums.sort()
    while left < right:
        print(nums[left], nums[right])
        if nums[left] + nums[right] == k:
            operation_count += 1
            left += 1
        elif nums[left] + nums[right] < k:
            left += 1
        elif nums[left] > k:
            left += 1

        right -= 1

    return operation_count
