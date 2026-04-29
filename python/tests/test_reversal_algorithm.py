from algorithms.reversal_algorithm import reverse_right


def test_reverse_right():
    input_array = [1, 2, 3, 4, 5, 6, 7]
    assert [5, 6, 7, 1, 2, 3, 4] == reverse_right(input_array, 3)
