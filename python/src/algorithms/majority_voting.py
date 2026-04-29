"""
Boyer-Moore Majority Voting Algorithm.
The Boyer–Moore Voting Algorithm efficiently finds the majority element in an array—an element that appears more
than N/2 times—using two passes. In the first pass, it selects a potential candidate by increasing a counter
when the same element is encountered and decreasing it when a different element appears, effectively canceling out
non-majority elements. In the second pass, the algorithm verifies whether this candidate actually occurs more
than N/2 times. This method runs in O(N) time and requires only O(1) extra space, making it both fast and
memory-efficient.
"""


def majority_votes(candidates: list[str | int] | tuple[str | int]) -> int | str | None:
    """
    A basic implementation of the Boyer-Moore majority voting algorithm.
    Args:
        candidates (list): A list of candidate values.
    Returns:
        int|str|None: The majority candidate of the array.
    """
    candidate = candidates[0]
    votes = 0

    # Find a majority candidate.
    for current_candidate in candidates:
        if candidate == current_candidate:
            votes += 1
        elif votes > 0:
            votes -= 1

        if votes == 0:
            candidate = current_candidate
            votes = 1

    # Count the number of majority candidate votes.
    count = 0
    for current_candidate in candidates:
        if candidate == current_candidate:
            count += 1

    if count > len(candidates) // 2:
        return candidate
    return None
