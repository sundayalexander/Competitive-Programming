"""
Stack data structure implementation module.

This module provides implementation of a Stack data structure with basic operations:
- push: adds element to the top of the stack
- pop: removes and returns element from the top of the stack
- peek/top: returns the top element without removing it
- is_empty: checks if stack is empty

A stack follows Last-In-First-Out (LIFO) principle, where the last element added
is the first one to be removed. It is similar to a stack of plates where you can
only add or remove plates from the top.

Example usage:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    top = stack.peek()  # returns 2
    item = stack.pop()  # removes and returns 2
"""

from typing import Any


class Stack:
    """
    A class that represents an implementation of Stack data structure.

    A Stack is a collection of elements with two main principal operations:
    push, which adds an element to the collection, and pop, which removes and
    returns the most recently added element. This class provides methods for
    basic operations on the stack and can be used in scenarios requiring LIFO
    (Last In, First Out) data manipulation.
    """

    def __init__(self):
        self.__items__: list[Any] = []

    def push(self, item: Any) -> None:
        """
        Add a new item to the top of the Stack data.

        The method `push` is responsible for adding a new element to the
        top of Stack data maintaining a record of items.

        Args:
            item: The element to be added to the top of Stack.
        """
        self.__items__.append(item)

    def peek(self) -> Any:
        """
        Returns the top element of the Stack data.
        Returns:
            Any: The top element of the Stack data.
        """
        return self.__items__[-1]

    def pop(self) -> Any:
        """
        Removes and returns the top item from the Stack.

        This method is used to remove the last element from the Stack data
        and return it. It changes the state of the Stack by eliminating the
        top element.

        Returns:
            Any: The last item from the `items` list.

        Raises:
            IndexError: If the `items` list is empty.
        """
        return self.__items__.pop()

    def is_empty(self) -> bool:
        """
        Determines whether the stack is empty.

        The function checks the state of the Stack object and returns a boolean
        indicating if the object contains any elements. This method provides a
        straightforward way to evaluate the emptiness of the Stack.

        Returns:
            bool: True if the Stack contains elements, False otherwise.
        """
        return not bool(self.__items__)


class MinStack(Stack):
    """
    Problem Statement:
        Design a stack that supports:
        - push(x) -> None: pushes x on the stack.
            - Time complexity: O(1)
        - top() -> x: sees the top element and return it without deleting.
            - Time complexity: O(1)
        - getMin() -> x: returns the min value of the stack.
            - Time complexity: O(1)
        Conditions:
            - getMin() should return -1 on an empty stack.
            - pop() should do nothing on an empty stack.
            - top() should return -1 on an empty stack.
    Args:
        items (list[int]): list of items to be added to the stack.
    Returns:
        Stack: The stack containing the items.
    """

    def __init__(self):
        super().__init__()
        self.__min_bucket__ = Stack()

    def push(self, item: Any) -> None:
        """
        Add a new item to the top of the Stack data and push the current minimum item into the minimum item bucket
        Args:
            item (Any): item to be added to the top of the stack.
        """
        super().push(item)
        if self.__min_bucket__.is_empty():
            self.__min_bucket__.push(item)
        else:
            top = self.__min_bucket__.peek()
            if item <= top:
                self.__min_bucket__.push(item)
            else:
                self.__min_bucket__.push(top)

    def pop(self) -> Any:
        """
        Removes and returns the top item from the stack.
        Returns:
            Any: The last item from the `items` list.
        """
        item = None
        if not self.is_empty():
            item = super().pop()
        if not self.__min_bucket__.is_empty():
            self.__min_bucket__.pop()
        return item

    def get_min(self) -> Any:
        """
        Get the minimum item from the stack.
        Returns:
            Any: The minimum item from stack.
        """
        return self.__min_bucket__.peek() if not self.__min_bucket__.is_empty() else -1

    def top(self) -> Any:
        """
        Get the top item from the stack.
        Returns:
            Any: The top item from the stack or -1.
        """
        if not self.is_empty():
            return super().peek()
        return -1


def is_balanced_parentheses(parentheses: str) -> bool:
    """
    Determine if a given string value is a balanced parenthesis.
    Args:
        parentheses (str): A Given string value of parentheses.
    Returns:
        bool: True if the string value is a balanced parenthesis, False otherwise.
    """
    parenthesis_types = {"(": ")", "{": "}", "[": "]"}
    open_parentheses: Stack[str] = Stack()
    for char in parentheses:
        if char in parenthesis_types:
            open_parentheses.push(char)
        else:
            if open_parentheses.is_empty():
                return False
            parenthesis = open_parentheses.pop()
            if parenthesis_types.get(parenthesis) != char:
                return False

    return open_parentheses.is_empty()


def canonical_path_formatter(path: str) -> str:
    """
    Simple path
    Given a path. The canonical path should have the following format:
    - Starts with '/'.
    - Any two directories are separated by a single slash '/'.
    - Does not end with a trailing '/'.
    - Only contains the directories on the path from the root directory to the target file or directory (ie., no period '.' or double period '..').

    Given a path, return the canonical path.
    Args:
        path (str): raw path string.

    Returns:
        str: The canonical representation of the raw path.
    """
    canonical_bucket: Stack[str] = Stack()
    path_segments = path.split("/")
    for segment in path_segments[1:]:
        if segment == "..":
            if not canonical_bucket.is_empty():
                canonical_bucket.pop()
        elif segment != "" and segment != " " and segment != ".":
            canonical_bucket.push(segment)

    return "/" + "/".join(canonical_bucket.__items__)


def is_redundant_parentheses(expression_str: str) -> int:
    """
    A string A contains operators, round braces and letters.
        - Return 1 if A has redundant braces, 0 otherwise.
        Constraints:
         - 1 <= N <= 1e5
         - Assumption:
            - It is assumed that all expressions is valid/balanced parentheses.
    Args:
        expression_str (str): expression to be evaluated.
    Returns:
        int: 1 if redundant parentheses, 0 otherwise.
    """
    parentheses_map: dict[str, str] = {"(": ")", "[": "]", "{": "}"}
    parentheses_bucket: Stack[int] = Stack()
    parentheses_count: dict[str, int] = {"(": 0, "[": 0, "{": 0}
    allowed_operators: set[str] = {"+", "-", "*", "/", "%", "^"}
    for data in expression_str:
        if data not in parentheses_map.values():
            parentheses_bucket.push(data)
            parentheses_count = {"(": 0, "[": 0, "{": 0}
        else:
            bucket_item = None
            found_operator = False
            while (
                bucket_item not in parentheses_map and not parentheses_bucket.is_empty()
            ):
                bucket_item = parentheses_bucket.pop()
                if bucket_item not in parentheses_map:
                    parentheses_count = {"(": 0, "[": 0, "{": 0}

                if bucket_item in allowed_operators:
                    found_operator = True

                if bucket_item in parentheses_map:
                    parentheses_count[bucket_item] += 1

            # Return 1 if no operator is found between parentheses
            if not found_operator:
                return 1

            # Return 1 if parenthesis is more than, that is a duplicate parentheses.
            if parentheses_count[bucket_item] > 1:
                return 1

    return 1 if max(parentheses_count.values()) > 1 else 0


def minimum_remove_to_valid_parentheses(invalid_str: str) -> str:
    """
    A minimum remove to make a valid parentheses.
    Problem Discussion
        - A string S contains "(", ")" and lowercase English letters.
        - Remove the min number of parentheses to make S valid.
        - Constraints:
          - 1 <= len(S) <= 1e5
    Args:
        invalid_str (str): The string to be validated.

    Returns:
        str: the valid parentheses string.
    """
    valid_parentheses = []
    parentheses_bucket = Stack()
    for index, char in enumerate(invalid_str):
        if char == "(":
            parentheses_bucket.push(index)
        elif char == ")":
            if not parentheses_bucket.is_empty():
                valid_parentheses.append(parentheses_bucket.pop())
                valid_parentheses.append(index)

    return "".join(
        [
            char
            for index, char in enumerate(invalid_str)
            if index in valid_parentheses or char not in "()"
        ]
    )


def longest_valid_parentheses(parentheses_str: str) -> int:
    """
    Return the count of the longest valid parentheses in a given string.
    Given a string of just "(" and ")".
    - Find the longest substring of valid parentheses.
    - Constraints:
       - 1 <= N <= 3e4
    Args:
        parentheses_str (str): parentheses string to be validated.
    Returns:
        int: the count of the longest valid parentheses.
    """
    parentheses_bucket = Stack()
    parentheses_status = [False] * len(parentheses_str)
    for index, char in enumerate(parentheses_str):
        if char == "(":
            parentheses_bucket.push(index)
        else:
            if not parentheses_bucket.is_empty():
                parentheses_status[parentheses_bucket.pop()] = True
                parentheses_status[index] = True

    valid_count = 0
    valid_parentheses_counts = []
    for is_valid in parentheses_status:
        if is_valid:
            valid_count += 1
        else:
            valid_parentheses_counts.append(valid_count)
            valid_count = 0

    return max(valid_parentheses_counts)
