from algorithms.bitwise_operations import number_of_different_bits, divide_two_integers


def test_number_of_different_bits() -> None:
    test_scenarios = {(2, 1): 2, (22, 15): 3, (3, 1): 1}
    for expression, expected_value in test_scenarios.items():
        assert number_of_different_bits(*expression) == expected_value


def test_divide_two_integers() -> None:
    test_scenarios = {
        (10, 2): 5,
        (7, 2): 3,
        (7, 3): 2,
        (7, -3): -2,
        (10, 3): 3,
        (100, 30): 3,
    }
    for expression, expected_value in test_scenarios.items():
        assert divide_two_integers(*expression) == expected_value
