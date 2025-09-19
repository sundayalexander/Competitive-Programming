"""
Backtracking algorithm implementation in python using recursion.
"""

from statistics import median


def possible_comb(n: int, k: int) -> int:
    """
    Compute all possible combinations of k elements in n.
    This approach requires us to return the total number of possible ways we can pick k elements from n.
    This is a combination problem of C(n k)
    Args:
        n (int): total number of elements or population sample.
        k (int): number of k elements.
    Returns:
        int: number of possible combinations of n elements.
    """
    if (
        k == 0 or k == n
    ):  # If k is 0 or k is n, then there is only one possible way we can pick k elements from n.
        return 1
    # Return possible combination where n is n-1 with n-1 and k-1
    return possible_comb(n - 1, k) + possible_comb(n - 1, k - 1)


def palindrome(value: str) -> bool:
    """
    This checks whether a given string is a palindrome or not.
    A palindrome is a string that reads the same forwards and backwards. i.e. abba == abba
    Args:
        value (str): input string.
    Returns:
        bool: True if input string is a palindrome, False otherwise.
    """
    if len(value) <= 1:
        return True  # If the length of the input is less than one or a one, then is a palindrome.
    # Match the first character in the string value and the last character if they're of the same value.
    # And check the next n-2 string.
    return value[0] == value[-1] and palindrome(value[1:-1])


def move_single_disk(src: str, dst: str, disk: int) -> None:
    """
    Move disk from source to destination.
    This can be implemented using list as src and dst. Where the last element from src can be pop to dst.
    Args:
        src (str): source pole.
        dst (str): destination pole.
        disk (int): current disk to move.
    Returns:
        None
    """
    print(f"Moved disk #{disk} from pole {src} to pole {dst}")


def move_tower(n: int, src: str, dst: str, tmp: str) -> None:
    """
    This is a tower of Hanoi problem. See definition here: https://en.wikipedia.org/wiki/Tower_of_Hanoi
    This can be implemented using list as src, dst, and tmp. Where each element is pop into the other pole.
    To calculate the sum of steps required to move all disks from src to dst.
    We could adopt the sum of nth term of a GP: (a * (pow(r, n) -1)) / r -1.
    Where a = first term = 1 --> the first term is always 1.
          r  = common ratio = 2 --> common ration is always 2.
          n = number of disks
    i.e to find the number of steps required to move 7 disks from src to dst pole.
    sn = (1 * (pow(2, 7) -1)) / (2 -1) = 127
    Args:
        n (int): total number of disk in the tower.
        src (str): Source pole.
        dst (str): Destination pole.
        tmp (str): Temporary pole.
    Examples:
        >>>move_tower(3, "A", "B", "C")
        Moved disk #0 from pole A to pole B
        Moved disk #1 from pole A to pole C
        Moved disk #0 from pole B to pole C
        Moved disk #2 from pole A to pole B
        Moved disk #0 from pole C to pole A
        Moved disk #1 from pole C to pole B
        Moved disk #0 from pole A to pole B
    Returns:
        None
    """
    if n > 0:  # if number of available disks is greater than 0, then move disk.
        # Move disk from source pole to temporary pole.
        move_tower(n - 1, src, tmp, dst)
        # Swap a single disk position.
        move_single_disk(src, dst, n - 1)
        # Move disk from temporary pole back to destination pole.
        move_tower(n - 1, tmp, dst, src)


def quick_sort(items: list) -> list:
    """
    Quick sort algorithm implementation for educational purposes only.
    Args:
        items (list): list of items.

    Returns:
        list: sorted list of items.
    """
    if len(items) <= 1:
        return items
    length = len(items)
    pivot = median([items[0], items[-1], items[length // 2]])

    return (
        quick_sort([item for item in items if item < pivot])
        + [item for item in items if item == pivot]
        + quick_sort([item for item in items if item > pivot])
    )
