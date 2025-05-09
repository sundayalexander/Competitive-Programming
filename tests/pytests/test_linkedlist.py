"""
Linkedlist test case module.
"""

from unittest import TestCase

from impy.datastructures.linkedlist import LinkedList, DoublyLinkedList, Node


class LinkedListTestCase(TestCase):
    def setUp(self):
        self.list = LinkedList()
        self.list.push_back(2)

    def tearDown(self):
        self.list = None

    def test_push(self):
        self.assertEqual(self.list.size, 1)

        self.list.push_back(3)
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.back(), 3)
        self.assertEqual(self.list.front(), 2)
        self.list.push_front(4)
        self.assertEqual(self.list.front(), 4)
        self.assertEqual(self.list.size, 3)
        self.list.pop_front()
        self.list.pop_back()

    def test_list_traversal(self):
        for i in range(10):
            self.list.push_back(i)
        node = self.list.head.next
        counter = 0
        while node:
            self.assertEqual(node.data, counter)
            node = node.next
            counter += 1

        self.list = LinkedList()
        self.list.push_front(2)

    def test_reversal(self):
        linkedlist = LinkedList()
        for i in range(10):
            linkedlist.push_back(i)
        self.assertEqual(linkedlist.front(), 0)
        self.assertEqual(linkedlist.back(), 9)
        linkedlist.reverse()

        node = linkedlist.head
        counter = 9
        while node:
            self.assertEqual(node.data, counter)
            node = node.next
            counter -= 1
        self.assertEqual(linkedlist.front(), 9)
        self.assertEqual(linkedlist.back(), 0)

    def test_get_nth_element_from_back(self):
        for i in range(10):
            self.list.push_back(i)
        self.assertEqual(self.list.size, 11)
        self.assertEqual(len(self.list), 11)
        self.assertEqual(self.list.value_n_from_end(3), 7)
        self.list = LinkedList()
        self.list.push_front(2)

    def test_remove_value(self):
        self.list.insert(10, 1)
        self.assertEqual(self.list.front(), 10)
        self.assertEqual(self.list.back(), 2)
        self.list.push_front(3)
        self.list.traverse(print)
        self.assertEqual(self.list.size, 3)
        self.assertEqual(self.list.front(), 3)
        self.list.remove_value(10)
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.value_at(2), 2)
        self.assertEqual(self.list.head.data, 3)
        self.list.remove_value(3)

    def test_erase_at_index(self):
        self.list.insert(10, 1)
        self.assertEqual(self.list.front(), 10)
        self.list.traverse(print)
        self.list.erase(1)
        self.assertEqual(self.list.front(), 2)
        self.assertEqual(self.list.size, 1)


class DoublyLinkedListTestCase(TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()
        self.list.push_back(2)

    def tearDown(self):
        self.list = None

    def assert_list_item(self, index: int, node: Node):
        values = [50, 4, 99, 3, 11, 2, 10]
        self.assertEqual(values[index - 1], node.data)

    def test_push(self):
        self.assertEqual(self.list.size, 1)
        self.list.push_front(3)
        self.list.push_front(4)
        self.list.push_back(10)
        self.list.insert(50, 1)
        self.list.insert(99, 3)
        self.list.insert(11, 5)
        self.list.traverse(self.assert_list_item)
        self.assertEqual(self.list.size, 7)
        self.list = DoublyLinkedList()
        self.list.push_front(2)

    def test_item_remove(self):
        for i in range(3, 20):
            self.list.push_back(i)

        self.assertEqual(self.list.value_at(14), 15)
        self.list.remove_value(15)
        self.assertEqual(self.list.value_at(14), 16)
        self.list.erase(14)
        self.assertEqual(self.list.value_at(14), 17)
        self.list.pop_front()
        self.assertNotEqual(self.list.front(), 2)
        self.list.pop_back()
        self.assertNotEqual(self.list.back(), 19)
        self.list = DoublyLinkedList()
        self.list.push_front(2)
