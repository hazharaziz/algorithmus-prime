import unittest
from unittest import result
from insertion_sort import *

class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        numbers = []
        insertion_sort(numbers)
        self.assertIsNotNone(numbers)
        self.assertEqual(0, len(numbers))

    def test_single_element_list(self):
        numbers = [1]
        insertion_sort(numbers)
        self.assertIsNotNone(numbers)
        self.assertEqual(1, len(numbers))
        self.assertEqual(1, numbers[0])

    def test_list_of_numbers(self):
        numbers_1 = [4, 2, 5, 1]
        numbers_2 = [31, 41, 59, 26, 41, 58]
        
        insertion_sort(numbers_1, False)
        self.assertIsNotNone(numbers_1)
        self.assertEqual(4, len(numbers_1))
        self.assertListEqual([5, 4, 2, 1], numbers_1)

        insertion_sort(numbers_2)
        self.assertIsNotNone(numbers_2)
        self.assertEqual(6, len(numbers_2))
        self.assertListEqual([26, 31, 41, 41, 58, 59], numbers_2)


if __name__ == '__main__':
    unittest.main()