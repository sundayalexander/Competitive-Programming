"""
Bit manipulation resource: https://graphics.stanford.edu/~seander/bithacks.html#OperationCounting
https://bits.stephan-brumme.com/
"""

import sys


def is_bit_set(value: int, position: int) -> bool:
    """
    Check if a bit value is set (1) in a particular position.
    Args:
        value (int): Value to check.
        position (int): Position to look at.

    Returns:
        bool: True if the bit value is set, False otherwise.
    """
    shifted = value >> position
    bit_set_in_position = shifted & 1
    return bool(bit_set_in_position)


def is_bit_even(value: int) -> bool:
    """
    Check if a bit value is even or odd.
    Args:
        value (int): Value to check.:

    Returns:
        bool: True if the bit value is even, False otherwise.
    """
    return (value & 1) == 0


def compute_value_sign(value: int):
    """
    Compute the sign of an integer value.
    Args:
        value (int): Value to compute the sign of.

    Returns:
        int: Sign of an integer value.
    """
    return value >> value.bit_count()


def int_absolute_value(value: int) -> int:
    """
    Compute the absolute value of an integer.
    Args:
        value ():

    Returns:

    """
    mask = value >> sys.maxsize.bit_count()
    return (value ^ mask) - mask


def is_different_sign(value_1: int, value_2: int) -> bool:
    """
    Determine if two values are of different signs.
    Args:
        value_1 (int): Value to check.
        value_2 (int): Value to check.

    Returns:
        bool: True if the two values are of different signs, False otherwise.
    """
    return (value_1 ^ value_2) < 0


def is_bit_power_of_two(value: int) -> bool:
    """
    Check if a bit value is a power of two.
    Args:
        value (int): Value to check.

    Returns:
        bool: True if the bit value is even, False otherwise.
    """
    return (value & value - 1) == 0


def number_of_different_bits(first_value: int, second_value: int) -> int:
    """
    Count the number of bits that are different between two values.
    Args:
        first_value (int): First value.
        second_value (int): Second value.

    Returns:
        int: Number of bits that are different between two values.
    """
    xor_bits = first_value ^ second_value
    return xor_bits.bit_count()


def divide_two_integers(dividend: int, divisor: int) -> int:
    """
    29. Divide Two Integers
    Medium
    Topics
    premium lock iconCompanies

    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

    Return the quotient after dividing dividend by divisor.

    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



    Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = 3.33333.. which is truncated to 3.

    Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = -2.33333.. which is truncated to -2.

    Constraints:

        -231 <= dividend, divisor <= 231 - 1
        divisor != 0


    Returns:
        int: Number of bits that are different between two integers.
    """
    if dividend > pow(2, 31) or (divisor > pow(2, 31) - 1):
        return 0

    if dividend == divisor:
        return 1

    is_negative = (dividend ^ divisor) < 0
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)

    bit_multipler = 1
    quotient = 0
    while (1 << bit_multipler) <= abs_divisor:
        quotient = abs_dividend >> bit_multipler
        print(quotient, bit_multipler, divisor)
        bit_multipler += 1

    # handle odd number divisor
    if (1 << bit_multipler) - abs_divisor == 1:
        quotient = abs_dividend >> bit_multipler
        quotient = abs(~quotient)

    # Account for negative
    if is_negative:
        quotient = -quotient

    return quotient
