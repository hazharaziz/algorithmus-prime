import unittest
from unittest import result
from insertion_sort import *

class TestInsertionSort(unittest.TestCase):

    def test_single_element_list(self):
        numbers = [1]
        insertion_sort(numbers)
        self.assertIsNotNone(numbers)
        self.assertEqual(1, len(numbers))
        self.assertEqual(1, numbers[0])

    def test_list_of_numbers(self):
        numbers = [4, 2, 5, 1]
        insertion_sort(numbers)
        self.assertIsNotNone(numbers)
        self.assertEqual(4, len(numbers))
        self.assertListEqual([1, 2, 4, 5], numbers)


if __name__ == '__main__':
    unittest.main()