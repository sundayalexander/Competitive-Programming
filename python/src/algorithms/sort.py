"""
This module contains major algorithms related to sorting techniques.
Resources for sorting algorithms: https://algodaily.com/lessons/fundamental-sorting-algorithms-bubble-and-insertion
"""


def bubble_sort(nums: list[int]) -> list[int]:
    """
    BUBBLE sort algorithm implementation to sort a list of integers.
    Args:
        nums:

    Returns:
        list: sorted list
    """
    nums_len = len(nums)
    for outer_index in range(nums_len):
        for inner_index in range(outer_index, nums_len - 1):
            if nums[inner_index] > nums[inner_index + 1]:
                nums[inner_index], nums[inner_index + 1] = (
                    nums[inner_index + 1],
                    nums[inner_index],
                )

    return nums


def cycle_sort(nums: list[int]) -> list[int]:
    """
    This is a implementation of cycle/cyclic sort algorithm using two pointers.
    Args:
        nums (list[int]): a list of integers.

    Returns:
        list: sorted list
    """
    left = 0
    nums_len = len(nums)
    right = nums_len - 1
    while left <= right:
        count = 0
        for index in range(nums_len):
            if nums[index] < nums[left]:
                count += 1

        if count > left:
            nums[left], nums[count] = nums[count], nums[left]
            right -= 1

        else:
            left += 1

    return nums
