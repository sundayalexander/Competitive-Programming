"""
TODO: Complete the exercise below.
Exercise link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/4_hash_table_exercise.md
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class Empty:
    """
    Empty class to represent an empty data structure.
    """

    def __str__(self):
        return ""


@dataclass
class Deleted:
    """
    Deleted class to represent a deleted data structure.
    """

    def __str__(self):
        return "deleted"


class HashTable(object):
    """
    HashTable implementation using pythong list as the underlying storage space. It uses linear probing technique to
    resolve collisions.
    This implementation is for educational purposes only.
    Optimized hashtable implementation is available as python dictionary(dict).
    """

    def __init__(self, capacity=10):
        self.__data__ = [Empty()] * capacity
        self.capacity = capacity
        self.__occupied__ = 0

    def __hash(self, key: str | int, position: int = 1) -> int:
        """
        Compute the hash function of a given key.
        Args:
            key (str): The key to hash.
            position (int, optional): The position of the hash function.
        Returns:
            int: the hash value of a given key
        """
        _index_size = 8
        _key_int_value = key
        if isinstance(key, str):
            _key_int_value = sum([ord(char) for char in key])

        _bin_values = bin(_key_int_value)[2:]

        if position - 1 >= len(_bin_values):
            _bin_values += bin(_key_int_value * position * 2)[2:]
            _index_size = _index_size * 2

        if len(_bin_values) > _index_size and position > 1:
            _bin_values = _bin_values[: -1 * (position - 1)][-1 * _index_size :]

        return int(_bin_values, 2) % self.capacity

    def add(self, key: str | int, value: Any) -> None:
        """
        Add a key value pair to the hash table.
        Args:
            key (int|str): The key to hash.
            value (Any): The value to hash.
        Returns:
            None
        """
        visit_address_count = 1
        while (_hash := self.__hash(key, visit_address_count)) and self.__data__[
            _hash
        ] not in (Empty(), Deleted()):
            visit_address_count += 1

        self.__data__[_hash] = (key, value)
        self.__occupied__ += 1
        self.resize()

    def probe(self, key: int | str) -> int:
        """
        Probe the hash table to see if the hash value exists.
        Args:
            key (int|str): The key to hash.
        Returns:
            int: The hash value if the hash value exists.
        """
        visit_address_count = 1
        _hash = self.__hash(key, visit_address_count)
        while (_hash_data := self.__data__[_hash]) and (
            _hash_data == Deleted()
            or (isinstance(_hash_data, tuple) and _hash_data[0] != key)
        ):
            visit_address_count += 1
            _hash = self.__hash(key, visit_address_count)
        return _hash

    def resize(self, shrink: bool = False) -> None:
        """
        Resize the hash table to optimize space.
        Args:
            shrink (bool, optional): Whether to shrink the hash table. Defaults to False.

        Returns:
            None
        """
        # if the number of element is equal to the hashtable threshold, then copy the element unto a new table.
        if self.__occupied__ == self.capacity // 2:
            temp = self.__data__
            self.capacity *= 2
            self.__data__ = [Empty()] * self.capacity
            [self.add(*data) for data in temp if isinstance(data, tuple)]
        elif self.__occupied__ < self.capacity // 4 and shrink:
            temp = self.__data__
            self.capacity = self.capacity // 2
            self.__data__ = [Empty()] * self.capacity
            [self.add(*data) for data in temp if isinstance(data, tuple)]

    def exists(self, key: str | int) -> bool:
        """
        Checks if the provided key exists in the hash table. Returns True if it exists False otherwise.
        Args:
            key (str|int): The key to check.
        Returns:
            bool: True if the key exists in the hash table, False otherwise.
        """
        value = self.__data__[self.probe(key)]
        return not isinstance(value, Empty)

    def remove(self, key: str | int) -> None:
        """
        Delete a given key item from the hash table.
        Args:
            key (str|int): The key to remove.
        Returns:
            None
        """
        self.__data__[self.probe(key)] = Deleted()
        self.__occupied__ -= 1
        self.resize(True)

    def get(self, key: str | int) -> Any:
        """
        Retrieve the value for the given key from the hash table.
        Args:
            key (str|int): The key to retrieve.
        Returns:
            Any: The value for the given key from the hash table.
        """
        value = self.__data__[self.probe(key)]
        if isinstance(value, Empty):
            return None
        return value[1]
