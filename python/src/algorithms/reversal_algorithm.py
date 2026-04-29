"""
The
reversal algorithm is an efficient, in-place method primarily used for rotating an array by a given number of elements. It works by performing a series of three array reversals to achieve the desired rotation with optimal time and space complexity.
Reversal Algorithm for Array Rotation
The general idea is to divide the array into two parts, A and B, around the rotation point, reverse each part individually, and then reverse the entire array.

Steps for Left Rotation
To rotate an array arr of size n to the left by d positions:

    Reverse the first part (A): Reverse the elements from index 0 to d-1.
    Reverse the second part (B): Reverse the elements from index d to n-1.
    Reverse the entire array: Reverse all elements from index 0 to n-1


Steps for Right Rotation
To rotate an array arr of size n to the right by d positions:

    Reverse the entire array: Reverse all elements from index 0 to n-1.
    Reverse the first part: Reverse the elements from index 0 to d-1.
    Reverse the second part: Reverse the elements from index d to n-1.

Learn more here: https://www.geeksforgeeks.org/dsa/program-for-array-rotation-continued-reversal-algorithm/
"""


def reverse_right(input_array: list[int], d: int) -> list[int]:
    """
    Reverse the given array to the right by d positions.
    Args:
        input_array (list[int]): Input array.
        d (int): Desired position of elements to reverse the array.

    Returns:
        list[int]: the reversed array.

    """
    input_length = len(input_array)
    limit = d % input_length if d > input_length else d
    input_array.reverse()

    # reverse 0 to d-1 array indices
    start = 0
    stop = limit - 1
    for _ in range(limit // 2):
        input_array[start], input_array[stop] = input_array[stop], input_array[start]
        start += 1
        stop -= 1

    # reverse 0 to d-1 array indices
    start = limit
    stop = input_length - 1
    for _ in range((input_length - limit) // 2):
        input_array[start], input_array[stop] = input_array[stop], input_array[start]
        start += 1
        stop -= 1

    return input_array
