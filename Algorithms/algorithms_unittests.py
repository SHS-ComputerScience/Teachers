import unittest
from LinearSearch.linear_search import linear_search
from BinarySearch.binary_search import binary_search


class SearchTests(unittest.TestCase):

    def test_linear_search_value_in_array(self):
        self.assertTrue(linear_search('abcdefghijklmnopqrstuvw.yz', 'r'))
    
    def test_linear_search_value_not_in_array(self):
        self.assertFalse(linear_search('abcdefghijklmnopqrstuvw.yz', 'x'))

    def test_binary_search_value_in_array(self):
        self.assertTrue(binary_search('abcdefghijklmnopqrstuvw.yz', 'r'))
    
    def test_binary_search_value_not_in_array(self):
        self.assertFalse(binary_search('abcdefghijklmnopqrstuvw.yz', 'x'))


if __name__ == '__main__':
    unittest.main()