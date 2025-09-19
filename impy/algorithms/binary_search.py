"""
Implementation of Binary Search Algorithm using different approaches.
"""


def binary_search_with_loop(key: int, search_space: list[int]) -> int:
    """
    Find a key in a sorted list of items in the specified search space.
    An implementation of Binary Search Algorithm using a loop.
    Args:
        key (str|int): The key to search for in the search space.
        search_space (list): The search space to search in.

    Returns:
        int: The index of the key if found, else -1
    """
    left = 0
    right = len(search_space) - 1
    while left < right:
        mid = left + (right - left) // 2

        if key == search_space[mid]:
            return mid

        if search_space[mid] < key:
            left = mid + 1
        else:
            right = mid

    return -1


def search(key: int, search_space: list[int], left: int = 0, right: int = 0) -> int:
    """
    Find a key in a sorted list of items in the specified search space.
    An implementation of Binary Search Algorithm using a backtracking approach.
    Args:
        key (int): The key to search for in the search space.
        search_space (list): The search space to search in.
        left (int, optional): The index of the key to search for in the search space.
        right (int, optional): The index of the key to search for in the search space.

    Returns:
        int: The index of the key if found, else -1
    """

    if not search_space or left >= right:
        return -1

    mid = left + (right - left) // 2

    if key == search_space[mid]:
        return mid

    if search_space[mid] < key:
        return search(key, search_space, mid + 1, right)
    else:
        return search(key, search_space, left, mid)
