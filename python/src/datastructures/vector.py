"""
An implementation of a Vector mutable array with automatic resizing data structure.
Implementation approach can be found here: https://github.com/sundayalexander/coding-interview-university#data-structures
This data structure is for learning purpose only, an optimized implementation is available for production use in the python community.
"""

from typing import Any

_INDEX_ERROR_MESSAGE = "Index out of range."


class Vector:
    """
    Vector mutable array with automatic resizing data structure.
    Attributes:
        __data: python list data structure.
        capacity: This represents the maximum allowed elements in the vector.
        size: This represents the total element currently in the vector.
    """

    def __init__(self, capacity: int) -> None:
        self.__data: list = []
        self.capacity: int = capacity
        self.size: int = 0

    def is_empty(self) -> bool:
        """
        Check if the vector if there are no elements inside it, return False otherwise False.
        Returns:
            bool: True if the vector is empty, False otherwise.
        """
        return self.size == 0

    def at(self, index: int) -> Any:
        """
        Return the element at the specified index from the vector.
        Args:
            index (int): The index of the element to return.
        Raises:
            IndexError: If the index is out of range.
        Returns:
            Any: The element at the specified index.
        """
        if index < 0 or index >= self.size:
            raise IndexError(_INDEX_ERROR_MESSAGE)
        return self.__data[index]

    def push(self, item: Any) -> None:
        """
        Add an element to the tail of the vector data if the vector has not reached capacity,
        otherwise raise an exception.
        Args:
            item (Any): The element to add to the vector.
        Raises:
            MemoryError: If the vector has reached allowed capacity.
        Returns:
            None
        """
        if self.size >= self.capacity:
            raise MemoryError("Vector capacity reached.")
        self.__data.append(item)
        self.size += 1

    def insert(self, index: int, item: Any) -> None:
        """
        Insert an element in the specified index if the vector has not reached capacity, otherwise raise an exception.
        Args:
            index (int): The index of where to insert the element.
            item (Any): The element to insert.
        Raises:
            IndexError: If the index is out of range.
        Returns:
            None
        """
        if index >= self.size:
            raise IndexError(_INDEX_ERROR_MESSAGE)

        self.__data.insert(index, item)

    def prepend(self, item: Any) -> None:
        """
        Add an element to the beginning of the vector data if the vector has not reached capacity,
        otherwise raise an exception.
        Args:
            item (Any): The element to add to the beginning of the vector.
        Returns:
            None
        """
        if self.size >= self.capacity:
            raise MemoryError("Vector capacity reached.")
        self.__data.insert(0, item)
        self.size += 1

    def pop(self) -> Any:
        """
        Remove and return the element from the tail of the vector.
        Raises:
            IndexError: If the vector is empty.
        Returns:
            Any: The element from the tail of the vector.
        """
        if self.size == 0:
            raise IndexError("Vector is empty.")
        self.size -= 1
        return self.__data.pop()

    def delete(self, index: int) -> None:
        """
        Delete the element at the specified index from the vector.
        Args:
            index (int): The index of the element to delete.
        Raises:
            IndexError: If the index is out of range.
        Returns:
            None
        """
        if index < 0 or index >= self.size:
            raise IndexError(_INDEX_ERROR_MESSAGE)
        self.__data.pop(index)
        self.size -= 1

    def remove(self, item: Any) -> None:
        """
        Looks for the specified item and removes index holding it (even if in multiple places).
        Args:
            item (Any): The element to remove.
        Returns:
            None
        """
        _temp_list = self.__data.copy()
        pop_counter = 0
        for index, _item in enumerate(_temp_list):
            if item == _item:
                self.__data.pop(index - pop_counter)
                self.size -= 1
                pop_counter += 1

    def find(self, item: Any) -> int:
        """
        Looks for item and returns first index with that value, -1 if not found
        Args:
            item (Any): The element to find.
        Returns:
            int: The index of the item if found, -1 otherwise.
        """
        try:
            return self.__data.index(item)
        except ValueError:
            return -1

    def resize(self, new_capacity: int) -> None:
        """
        Resize the vector to the specified new capacity.
        Shrink the vector if the new capacity is smaller than the current capacity.
        Args:
            new_capacity (int): new capacity of the vector.
        Returns:
            None
        """
        self.__data = self.__data[:new_capacity]
        self.capacity = new_capacity
        if self.size > new_capacity:
            self.size = new_capacity
