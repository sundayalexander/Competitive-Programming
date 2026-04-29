"""
Suffix Array Data Structure Implementation.
A suffix array is a sorted array of all suffixes of a given string. More formally if you are given a string 'S' then
the suffix array for this string contains the indices 0 to n, such that the suffixes starting from these indices are
sorted lexicographically.
Read more here:
https://en.wikipedia.org/wiki/Suffix_array
https://www.geeksforgeeks.org/competitive-programming/suffix-arrays-for-competitive-programming/
https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-nlognlogn-algorithm/
"""


def naive_suffix_array(value: str) -> list[int]:
    """
    Implementation of a naive suffix array for competitive programming.
    Args:
        value (str): Input array to competitive programming.

    Returns:
        list[int]: Suffix array for competitive programming.
    """
    value_length = len(value)
    temp_ = [(value[index:], index) for index in range(value_length)]
    temp_.sort(key=lambda suffix_: suffix_[0])
    suffix_array = [suffix_[1] for suffix_ in temp_]
    del temp_
    return suffix_array


def common_prefix_count(value_1: str, value_2: str) -> int:
    """
    Count the length of the common prefix of two strings.
    Args:
        value_1 (str): input string one.
        value_2 (str): input string two.

    Returns:
        int: Length of the common prefix array.
    """
    value_length = min(len(value_1), len(value_2))
    prefix_length = 0
    for index in range(value_length):
        if value_1[index] == value_2[index]:
            prefix_length += 1
        else:
            break
    return prefix_length


def common_prefix_array(value: str, suffix_array_builder: callable) -> list[int]:
    """
    Compute the common prefix array for the given values.
    Args:
        suffix_array_builder (callable): Function that takes a string and returns a list of integers.
        value (str): Input array to competitive programming.

    Returns:
        list[int]: Suffix array for competitive programming.
    """
    value_length = len(value)
    suffix_array = suffix_array_builder(value)

    lcp_array = [0] * value_length
    for index in range(1, value_length):
        lcp_array[index] = common_prefix_count(
            value[suffix_array[index - 1] :], value[suffix_array[index] :]
        )

    return lcp_array
