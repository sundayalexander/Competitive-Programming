"""
Test module for Stack data structure implementation.
This is for educational purpose only.
"""

from impy.datastructures.stack import (
    is_balanced_parentheses,
    canonical_path_formatter,
    MinStack,
    is_redundant_parentheses,
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
        print(expression, expected_result)
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
