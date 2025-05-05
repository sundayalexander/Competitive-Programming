"""
Test module for Stack data structure implementation.
This is for educational purpose only.
"""

from impy.datastructures.stack import (
    is_balanced_parentheses,
    canonical_path_formatter,
    MinStack,
    is_redundant_parentheses,
    minimum_remove_to_valid_parentheses,
    longest_valid_parentheses,
    infix_to_postfix,
    evaluate_postfix_expression,
)


def test_stack_with_balanced_parentheses():
    parentheses_list = (
        "((([[[{{{}}}]]])))",
        ")()()()()(",
        "(){}()[]{}((((((({})))))))",
    )
    expected_results = (True, False, True)
    for parentheses, expected_result in zip(parentheses_list, expected_results):
        assert is_balanced_parentheses(parentheses) == expected_result


def test_stack_with_canonical_path():
    paths = ("/home/", "/../", "/home//1337/./", "home/../../tmp//./")
    expected_results = ("/home", "/", "/home/1337", "/tmp")
    for path, expected_result in zip(paths, expected_results):
        assert canonical_path_formatter(path) == expected_result


def test_stack_with_is_redundant_parentheses():
    expressions = (
        "(a+b)",
        "(a+((2-)*b/(7))",
        "((8))",
        "(r*(8+9)*(9-8))",
        "a(9((0)))",
        "(a)",
    )
    expected_results = (0, 1, 1, 0, 1, 1)
    for expression, expected_result in zip(expressions, expected_results):
        assert is_redundant_parentheses(expression) == expected_result


def test_stack_with_min_stack():
    """
    Problem Statement:
        Design a stack that supports:
        - push(x) -> None: pushes x on the stack.
        - top() -> x: sees the top element and return it without deleting.
        - getMin() -> x: returns the min value of the stack.
    """
    item_bucket: MinStack[int] = MinStack()
    item_bucket.push(5)
    assert item_bucket.get_min() == 5
    item_bucket.push(10)
    assert item_bucket.get_min() == 5
    item_bucket.push(1)
    assert item_bucket.get_min() == 1
    item_bucket.pop()
    assert item_bucket.get_min() == 5
    item_bucket.pop()
    assert item_bucket.get_min() == 5
    item_bucket.pop()
    assert item_bucket.get_min() == -1
    assert item_bucket.top() == -1
    assert item_bucket.pop() == None


def test_stack_with_min_remove_to_valid_parentheses():
    invalid_parentheses = (
        ")a(b.d)",
        "tan(isq)",
        "(1337)",
        "a)(b)d(c(e)",
    )
    expected_results = ("a(b.d)", "tan(isq)", "(1337)", "a(b)dc(e)")
    for invalid, expected_result in zip(invalid_parentheses, expected_results):
        assert minimum_remove_to_valid_parentheses(invalid) == expected_result


def test_stack_with_longest_valid_parentheses():
    invalid_parentheses = (
        "()(((",
        "()((()",
        "()()()((((((()))))))(",
    )
    expected_results = (2, 2, 20)
    for invalid, expected_result in zip(invalid_parentheses, expected_results):
        assert longest_valid_parentheses(invalid) == expected_result


def test_stack_with_infix_to_postfix():
    assert infix_to_postfix("0-1+(3*3)/7") == "01-33*7/+"
    assert infix_to_postfix("1+3/4*5-7") == "134/5*+7-"
    assert infix_to_postfix("1+3/(4*5)-7") == "1345*/+7-"
    assert infix_to_postfix("1+3*(4*(1*5))-7") == "13415***+7-"


def test_stack_with_evaluate_postfix_expression():
    assert evaluate_postfix_expression([1, "+", 1, 2, "*"]) == 2
    assert (
        evaluate_postfix_expression(["0", "1", "-", "3", "3", "*", "7", "/", "+"])
        == 0.2857142857142858
    )
    assert (
        evaluate_postfix_expression(
            ["1", "3", "4", "1", "5", "*", "*", "*", "+", "7", "-"]
        )
        == 54
    )
