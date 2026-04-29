import pytest

from impy.algorithms.majority_voting import majority_votes


@pytest.mark.parametrize(
    "expected, candidates",
    [
        (1, [1, 1, 1, 1, 2, 3, 5]),
        ("A", ["A", "A", "A", "A", "B", "C", "E"]),
        (1, [1, 3, 1, 1, 4, 1, 1, 5, 1, 1, 6, 2, 2]),
    ],
)
def test_majority_votes(candidates, expected):
    assert expected == majority_votes(candidates)
