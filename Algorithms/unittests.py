import unittest
from QuickSort.quick_sort import quick_sort


class QuickSort(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(quick_sort([19, 6, 0.5, 2, 155, 43, -7]),[-7, 0.5, 2, 6, 19, 43, 155])

    def test_characters(self):
		self.assertEqual(quick_sort(['b', 'A', 'a', 'C', 'B', 'c']), ['A', 'B', 'C', 'a', 'b', 'c'])

    def test_strings(self):
		self.assertEqual(quick_sort(['fish', 'dog', 'cat', 'ant']), ['ant', 'cat', 'dog', 'fish'])


if __name__ == "__main__":
	unittest.main()