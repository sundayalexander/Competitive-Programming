"""
PREFIX SUM
Imagine you’re working on a problem that requires frequent range sum queries, like calculating the sum of elements
between two indices in an array. A naive approach would be to recalculate the sum each time, leading to inefficiencies.

What if we could precompute values to speed up these queries? That’s where the Prefix Sum Design Pattern comes in!
It’s a powerful technique that optimizes range-based calculations, making them much faster.

POSTFIX SUM
The term "postfix sum algorithm" generally refers to one of two distinct concepts, depending on the context:
the evaluation of an expression written in postfix notation (Reverse Polish Notation) or the computation of a suffix
sum array (also known as reverse cumulative sum).
1. Evaluation of a Postfix Expression
A postfix expression is one where operators follow their operands (e.g., 5 2 + instead of 5 + 2). The algorithm for
evaluating such an expression uses a stack.
Algorithm Steps:

    Initialize an empty stack.
    Iterate through the expression from left to right.
    If the current element is an operand (a number), push it onto the stack.
    If the current element is an operator (+, -, *, /), pop the top two operands from the stack (let's call them
    operand2 and operand1, in that order), apply the operation (operand1 operator operand2), and push the result
     back onto the stack.
    After processing the entire expression, the single remaining value in the stack is the result.

2. Suffix Sum Array
A suffix sum array (sometimes referred to as a "postfix sum" in a different context) is a precomputed array where each
element at index i stores the sum of all elements from index i to the end of the original array.
Algorithm Steps:

    Create a new array, suffixSum, of the same size as the original array.
    Initialize the last element of suffixSum with the last element of the original array: suffixSum[n-1] = arr[n-1],
    where n is the array length.
    Iterate through the original array from the second-to-last element down to the first element (from n-2 to 0).
    For each index i, calculate the suffixSum[i] by adding the current element arr[i] to the previously computed
    suffixSum of the next index: suffixSum[i] = arr[i] + suffixSum[i + 1].
    The resulting suffixSum array allows for quick calculation of sums for any right-side subarray in O(1) time after
    the initial O(n) preprocessing.
"""


def prefix_sum(input_array: list[int]) -> list:
    """
    Compute the prefix sum of an array of integers.
    Args:
        input_array (list[int]): An array of integers.

    Returns:
        list[int]: The prefix sum of an array of integers.
    """
    array_length = len(input_array)
    prefix_sum_array: list[int] = [0] * len(input_array)
    prefix_sum_array[0] = input_array[0]
    for index in range(1, array_length):
        prefix_sum_array[index] = prefix_sum_array[index - 1] + input_array[index]

    return prefix_sum_array


def postfix_sum(input_array: list[int]) -> list:
    """
    Compute the postfix sum of an array of integers.
    Args:
        input_array (list[int]): An array of integers.

    Returns:
        list[int]: The prefix sum of an array of integers.
    """
    array_length = len(input_array)
    postfix_sum_array: list[int] = [0] * len(input_array)
    postfix_sum_array[array_length - 1] = input_array[array_length - 1]
    for index in range(array_length - 2, -1, -1):
        postfix_sum_array[index] = postfix_sum_array[index + 1] + input_array[index]

    return postfix_sum_array


def find_pivot_index(nums: list[int]) -> int:
    """
    Using prefix and postfix sum array to find the pivot index.

    Question Statement
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the
    sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Returns:
        int: The pivot index.
    """
    array_length = len(nums)
    prefix_sum_array = [0] * array_length
    postfix_sum = [0] * array_length
    prefix_sum_array[0] = nums[0]
    postfix_sum[array_length - 1] = nums[array_length - 1]
    for index in range(1, array_length):
        prefix_sum_array[index] = nums[index] + prefix_sum_array[index - 1]
        postfix_sum[array_length - (1 + index)] = (
            postfix_sum[array_length - index] + nums[array_length - (1 + index)]
        )

    for index in range(array_length):
        if prefix_sum_array[index] == postfix_sum[index]:
            return index

    return -1


def find_pivot_index_optimized(nums: list[int]) -> int:
    """
    Using prefix and postfix sum array to find the pivot index.

    Question Statement
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the
    sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

    Returns:
        int: The pivot index.
    """
    array_length = len(nums)
    prefix_sum_array = [0] * array_length
    prefix_sum_array[0] = nums[0]
    total_sum = sum(nums)
    for index in range(array_length):
        if index != 0:
            prefix_sum_array[index] = nums[index] + prefix_sum_array[index - 1]

        if prefix_sum_array[index] == total_sum:
            return index

        total_sum -= nums[index]

    return -1


def product_of_array_except_self(nums: list[int]) -> list[int]:
    """
    Compute the product of an array of integers except the current index element using prefix and postfix array.

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
    elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.
    Args:
        nums (list[int]): An array of integers.

    Returns:
        list[int]: The product of an array of integers.
    """
    array_length = len(nums)
    prefix_array: list[int] = [0] * array_length
    postfix_array: list[int] = [0] * array_length
    prefix_array[0] = 1
    postfix_array[array_length - 1] = 1
    result_array: list[int] = [0] * array_length
    for index in range(array_length - 1):
        prefix_array[index + 1] = prefix_array[index] * nums[index]
        postfix_array[array_length - (2 + index)] = (
            postfix_array[array_length - (1 + index)] * nums[array_length - (1 + index)]
        )

    for index in range(array_length):
        result_array[index] = prefix_array[index] * postfix_array[index]

    return result_array