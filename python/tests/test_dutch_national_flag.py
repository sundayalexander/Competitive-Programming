from impy.algorithms.dutch_national_flag import sort_array


def test_majority_votes():
    sample_input = [0, 1, 2, 0, 1, 2]
    assert [0, 0, 1, 1, 2, 2] == sort_array(sample_input)
