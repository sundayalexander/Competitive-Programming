"""
Test module for python implementation of vector data structure.
"""

from unittest import TestCase

from impy.datastructures.vector import Vector


class VectorTestCase(TestCase):
    def setUp(self):
        self.vector = Vector(5)
        self.vector.push(2)

    def test_is_empty(self):
        self.assertEqual(self.vector.size, 1)
        self.assertEqual(self.vector.capacity, 5)
        self.vector.pop()
        self.assertEqual(self.vector.size, 0)
        self.assertTrue(self.vector.is_empty())
        self.vector.push(2)
        self.assertFalse(self.vector.is_empty())

    def test_at_element_access(self):
        self.assertEqual(self.vector.at(0), 2)
        with self.assertRaises(IndexError) as exc:
            self.vector.at(10)
        self.assertEqual(str(exc.exception), "Index out of range.")

    def test_insert_element(self):
        self.vector.insert(0, 10)
        self.assertEqual(self.vector.at(0), 10)
        self.vector.insert(0, 2)
        with self.assertRaises(IndexError) as exc:
            self.vector.insert(10, 7)

        self.assertEqual(str(exc.exception), "Index out of range.")

    def test_prepend_element(self):
        self.vector.prepend(50)
        self.assertEqual(self.vector.at(0), 50)
        self.assertEqual(self.vector.size, 2)
        self.vector.delete(0)
        self.assertEqual(self.vector.size, 1)
        self.assertEqual(self.vector.at(0), 2)

    def test_remove_element(self):
        self.assertEqual(self.vector.size, 1)
        self.vector.push(10)
        self.vector.push(10)
        self.assertEqual(self.vector.size, 3)
        self.assertEqual(self.vector.at(1), 10)
        self.vector.remove(10)
        self.assertEqual(self.vector.size, 1)

    def test_find_element(self):
        self.assertEqual(self.vector.find(2), 0)
        self.assertEqual(self.vector.find(10), -1)

    def test_resize_vector(self):
        self.vector.resize(10)
        self.assertEqual(self.vector.capacity, 10)

        for i in range(9):
            self.vector.push(i)
        self.assertEqual(self.vector.size, 10)

        with self.assertRaises(MemoryError) as exc:
            self.vector.push(10)

        self.assertEqual(str(exc.exception), "Vector capacity reached.")

        self.vector.resize(1)
        self.assertEqual(self.vector.capacity, 1)
        self.vector.resize(5)
        self.assertEqual(self.vector.capacity, 5)
        self.assertEqual(self.vector.size, 1)
