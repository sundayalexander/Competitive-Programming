"""
An implementation of a Linkedlist data structure.
Implementation approach can be found here: https://github.com/sundayalexander/coding-interview-university#data-structures
This data structure is for learning purpose only, an optimized implementation is available for production use in the python community.
It is advisable to avoid linked list when possible. Check this resource for more:https://www.youtube.com/watch?v=bXsKnUGndEU
"""

from typing import Any, Callable

_INDEX_OUT_OF_RANGE_MESSAGE = "Index out of range"


class Node:
    """
    Linkedlist element node  to hold the data,  next pointer, and previous node pointer.
    Attributes:
        data (Any): the actual  data to store.
        next (Node): the next Node object.
        previous (Node): the previous Node object.
    """

    def __init__(self, data: Any = None, next: "Node" = None, prev: "Node" = None):
        self.data = data
        self.next = next
        self.previous = prev

    def __str__(self):
        return str(self.data)

    def __eq__(self, other: "Node") -> bool:
        """
        Override equality operation to assert the required attributes matches.
        Args:
            other (Node): the other Node object.
        Returns:
        """
        return (
            self.data == other.data
            and self.next == other.next
            and self.previous == other.previous
        )


class LinkedList:
    """
    Linkedlist class to handle linkedlist data structure operations on  linked nodes.
    Attributes:
        head (Node): the head of the linked list.
        tail (Node): the tail of the linked list.
        size (int): the size of the linked list.
    """

    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def empty(self) -> bool:
        """
        Check if the linkedlist is empty to return True, otherwise return False.
        Returns:
            bool: returns True if the linkedlist is empty, otherwise return False.
        """
        return self.size == 0

    def get_node_at(self, stop_count: int = -1) -> Node:
        """
        Get the node at a given stop count from the linked list or return the last node in the list.
        Args:
            stop_count (int): the stop count of the linked list.
        Returns:
            Node: the node at a given stop count from the linked list.
        """
        node = self.head
        counter = 1
        while node and (stop_count == -1 or counter < stop_count):
            node = node.next
            counter += 1
        return node

    def value_at(self, index: int) -> Any:
        """
        Return the data of the node at the given index in the linked list.
        Args:
            index (int): the index of the node data to return.
        Returns:
            Any: the data at the given index in the linked list.
        """
        if index < 0 or index > self.size:
            return None

        return self.get_node_at(index).data

    def push_front(self, data: Any) -> None:
        """
        Adds an item to the front of the Linkedlist.
        Args:
            data (Any): the data to add.

        Returns:
            None
        """
        self.head = Node(data, next=self.head)
        if self.empty():
            self.tail = self.head
        self.size += 1

    def pop_front(self) -> Any:
        """
        Remove the front item and return its value.
        Returns:
            Any: the data at the front of the linked list.
        """
        if self.empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def push_back(self, data: Any) -> None:
        """
        Adds an item to the back of the Linkedlist.
        Args:
            data (Any): the data to add.
        Returns:
        """
        if self.empty():
            self.push_front(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.size += 1

    def pop_back(self):
        """
        Remove tem from the back of the list and return its value.
        Returns:
            Any: the data at the back of the linked list.
        """
        if self.empty():
            return None

        data = self.tail.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.get_node_at(self.size - 1).next = None
        self.size -= 1
        return data

    def __len__(self) -> int:
        return self.size

    def front(self) -> Any:
        """
        Return the value of the front item of the linked list.
        Returns:
            Any: the data at the front of the linked list.
        """
        if self.empty():
            return None
        return self.head.data

    def back(self) -> Any:
        """
        Return the value of the back item of the linked list.
        Returns:
            Any: the data at the back of the linked list.
        """
        if self.empty():
            return None
        return self.tail.data

    def insert(self, data: Any, index: int) -> None:
        """
        Insert value at index, so the current item at that index is pointed to by the new item at the index.
        Args:
            data (Any): the data to insert.
            index (int): index where to insert the new data.

        Returns:
            None
        """
        if index > self.size:
            raise IndexError()
        if index == 1:
            self.push_front(data)
        else:
            before_node = self.get_node_at(index - 1)
            before_node.next = Node(data, next=before_node.next)
            self.size += 1

    def erase(self, index: int) -> None:
        """
        Removes item at a specified index from the linked list.

        Args:
            index (int): index of the item to erase.

        Returns:
            None
        """
        if index > self.size:
            raise IndexError(_INDEX_OUT_OF_RANGE_MESSAGE)
        if index == 1:
            self.pop_front()

        elif index == self.size:
            self.pop_back()
        else:
            before_node = self.get_node_at(index - 1)
            before_node.next = None
            self.size -= 1

    def value_n_from_end(self, n: int) -> Any:
        """
        Returns the value of the node at the nth position from the end of the list
        Returns:
            Any: the data at the nth position of the linked list.
        """
        if self.empty():
            return None
        return self.get_node_at((self.size - n) + 1).data

    def reverse(self) -> None:
        """
        Reverse the elements of the linked list.
        Returns:
            None
        """
        self.tail = self.head
        self.head = None
        node = self.tail
        while node:
            temp_node = node
            node = node.next
            temp_node.next = self.head
            self.head = temp_node

    def remove_value(self, data: Any) -> None:
        """
        Removes the first item that match the given data in the list.
        Args:
            data (Any): the data to match and remove.
        Returns:
            None
        """
        if self.empty():
            return None

        if self.head.data == data:
            self.pop_front()
            return None
        elif self.tail.data == data:
            self.pop_back()
            return None

        node = self.head

        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                self.size -= 1
                return None
            node = node.next

    def traverse(self, func: Callable) -> None:
        """
        Traverse though the nodes in the linked list.
        Args:
            func (Callable): callable function with index, and node args.
        Returns:
            None
        """
        node = self.head
        index = 1
        while node:
            func(index, node)
            node = node.next
            index += 1


class DoublyLinkedList(LinkedList):

    def push_front(self, data: Any) -> None:
        """
        Adds an item to the front of the Linkedlist with both next and previous connections.
        Args:
            data (Any): the data to add.

        Returns:
            None
        """
        super().push_front(data)
        if self.head.next:
            self.head.next.previous = self.head

    def push_back(self, data: Any) -> None:
        """
        Adds an item to the back of the Linkedlist with connection to the previous item.
        Args:
            data (Any): the data to add.
        Returns:
        """
        if self.empty():
            self.push_front(data)
        else:
            self.tail.next = Node(data, prev=self.tail)
            self.tail = self.tail.next
            self.size += 1

    def insert(self, data: Any, index: int) -> None:
        """
        Insert value at index, so the current item at that index is pointed to by the new item at
        the index and the current item previous is set to the new item.
        Args:
            data (Any): the data to insert.
            index (int): index where to insert the new data.
        Returns:
            None
        """
        if index > self.size:
            raise IndexError(_INDEX_OUT_OF_RANGE_MESSAGE)
        if index == 1:
            self.push_front(data)
        else:
            current_node = self.get_node_at(index)
            temp_node = Node(data, next=current_node, prev=current_node.previous)
            temp_node.previous.next = temp_node
            current_node.previous = temp_node
            self.size += 1

    def erase(self, index: int) -> None:
        """
        Removes item at a specified index from the linked list.
        Args:
            index (int): index of the item to erase.
        Returns:
            None
        """
        if index > self.size:
            raise IndexError(_INDEX_OUT_OF_RANGE_MESSAGE)
        if index == 1:
            self.pop_front()

        elif index == self.size:
            self.pop_back()
        else:
            current_node = self.get_node_at(index)
            current_node.next.previous = current_node.previous
            current_node.previous.next = current_node.next
            current_node = None
            self.size -= 1

    def pop_front(self) -> Any:
        """
        Remove the front item, disassociate the new front item previous connection to old front item and
        return its value.
        Returns:
            Any: the data at the front of the linked list.
        """
        if self.empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.head.previous = None
        self.size -= 1
        return data

    def pop_back(self):
        """
        Remove item from the back of the list, disassociate the connection with the previous tail item
        and return its value.
        Returns:
            Any: the data at the back of the linked list.
        """
        if self.empty():
            return None

        data = self.tail.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        self.size -= 1
        return data

    def reverse(self) -> None:
        """
        Reverse the elements of the linked list and update the connections.
        Returns:
            None
        """
        self.tail = self.head
        self.head = None
        node = self.tail
        while node:
            temp_node = node
            node = node.next
            temp_node.next = self.head
            temp_node.next.previous = temp_node
            self.head = temp_node
            self.head.previous = None

    def remove_value(self, data: Any) -> None:
        """
        Removes the first item that match the given data in the list.
        Args:
            data (Any): the data to match and remove.
        Returns:
            None
        """
        if self.empty():
            return None

        if self.head.data == data:
            self.pop_front()
            return None
        elif self.tail.data == data:
            self.pop_back()
            return None

        node = self.head

        while node.next:
            if node.next.data == data:
                node.next.next.previous = node
                node.next = node.next.next
                self.size -= 1
                return None
            node = node.next
