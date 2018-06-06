import unittest
from exercises import *

# ------------------------------------------------------------
# Test Case Example:
# ------------------------------------------------------------

class TestReverseStringRecursive(unittest.TestCase):
	def test_string_type(self):
		self.assertEqual(reverse_str_recursive('Thomas'), 'samohT')
	def test_empty_string(self):
		self.assertEqual(reverse_str_recursive(''), '')
	def test_None_type(self):
		self.assertEqual(reverse_str_recursive(None), 'enoN')
	def test_integer_type(self):
		self.assertEqual(reverse_str_recursive(123), '321')
	def test_list_type(self):
		self.assertEqual(reverse_str_recursive([1,2,3]), ']3 ,2 ,1[')
	def test_dict_type(self):
		self.assertEqual(reverse_str_recursive(
			{1:'a', 2:'b', 3:'C'}), "}'C' :3 ,'b' :2 ,'a' :1{")

# ------------------------------------------------------------
# Recursion Exercise 1:
#   Write a test case for your list_sum() function.
# ------------------------------------------------------------

class ListSum(unittest.TestCase):
	def test_integers(self):
		self.assertEqual(list_sum([1, 2, 3]), 6)
	def test_floats(self):
		pass # replace pass with your code
	def test_negative_integers(self):
		pass # replace pass with your code
	def test_negative_floats(self):
		pass # replace pass with your code
	def test_zero(self):
		pass # replace pass with your code
	# additional tests?

# ------------------------------------------------------------
#  Recursion Exercise 2:
#    Write a test case for your factorial() function.
# ------------------------------------------------------------

class Factorial(unittest.TestCase):
	def test_5_120(self):
		self.assertEqual(factorial(5), 120)
	# add your own tests here

# ------------------------------------------------------------
#  Recursion Exercise 3:
#    Write a test case for your fibonacci() function.
# ------------------------------------------------------------

class Fibonacci(unittest.TestCase):
	def test_7_13(self):
		self.assertEqual(fibonacci(7), 13)
	# add your own tests here

# ------------------------------------------------------------
#  Recursion Exercise 4:
#    Write a test case for your n_dimensional_list_sum()
#    function.
# ------------------------------------------------------------

class nDimensionalListSum(unittest.TestCase):
	def test_2d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, 2, [3, 4, 5, 6]]), 21)
	# add your own tests here

# ------------------------------------------------------------
#  Recursion Exercise 5:
#    Write a test case for your int_to_string() function.
# ------------------------------------------------------------

class nBaseStringCoversion(unittest.TestCase):
	def test_10_16_a(self):
		self.assertEqual(int_to_string(10, 16), 'A')
	# add your own tests here

# ------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()