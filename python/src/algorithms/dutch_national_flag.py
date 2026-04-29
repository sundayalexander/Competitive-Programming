"""
The Dutch National Flag Algorithm Implementation

Given an array arr[] consisting of only 0s, 1s, and 2s. The objective is to sort the array, i.e., put all 0s first,
then all 1s and all 2s in last.

This problem is the same as the famous "Dutch National Flag problem". The problem was proposed by Edsger Dijkstra.
The problem is as follows:

Given n balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls
such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours
being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue
coloured balls).
"""


def sort_array(inputs: list[int]) -> list[int]:
    """
    Sort a given array of integers with the values of 0,1,2 using the DNF algorithm.
    Args:
        inputs (list[int]): an array of integers

    Returns:
        list[int]: the sorted array
    """
    # Defince the indices.
    low, middle, high = 0, 0, len(inputs) - 1
    while middle <= high:
        if inputs[middle] == 0:
            inputs[low], inputs[middle] = inputs[middle], inputs[low]
            low += 1
            middle += 1
        elif inputs[middle] == 2:
            inputs[high], inputs[middle] = inputs[middle], inputs[high]
            high -= 1
        else:
            middle += 1

    return inputs
