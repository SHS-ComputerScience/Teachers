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
		self.assertEqual(reverse_str_recursive(
			[1,2,3]), ']3 ,2 ,1[')
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
		self.assertEqual(list_sum([0.5, 1.235, 2.765]), 4.5)
	def test_negative_integers(self):
		self.assertEqual(list_sum([-5, -3, -2]), -10)
	def test_negative_floats(self):
		self.assertEqual(list_sum([-6.3, -3.275, -0.425]), -10)
	def test_zero(self):
		self.assertEqual(list_sum([0]), 0)

# ------------------------------------------------------------
#  Recursion Exercise 2:
#    Write a test case for your factorial() function.
# ------------------------------------------------------------

class Factorial(unittest.TestCase):
	def test_5_120(self):
		self.assertEqual(factorial(5), 120)
	def test_0_1(self):
		self.assertEqual(factorial(0), 1)
	def test_1_1(self):
		self.assertEqual(factorial(0), 1)
	def test_9_362880(self):
		self.assertEqual(factorial(10), 3628800)

# ------------------------------------------------------------
#  Recursion Exercise 3:
#    Write a test case for your fibonacci() function.
# ------------------------------------------------------------

class Fibonacci(unittest.TestCase):
	def test_1_1(self):
		self.assertEqual(fibonacci(1), 1)
	def test_2_1(self):
		self.assertEqual(fibonacci(2), 1)
	def test_3_2(self):
		self.assertEqual(fibonacci(3), 2)
	def test_4_3(self):
		self.assertEqual(fibonacci(4), 3)
	def test_5_5(self):
		self.assertEqual(fibonacci(5), 5)
	def test_6_8(self):
		self.assertEqual(fibonacci(6), 8)
	def test_7_13(self):
		self.assertEqual(fibonacci(7), 13)
	def test_8_21(self):
		self.assertEqual(fibonacci(8), 21)
	def test_25_75025(self):
		self.assertEqual(fibonacci(25), 75025)

# ------------------------------------------------------------
#  Recursion Exercise 4:
#    Write a test case for your n_dimensional_list_sum()
#    function.
# ------------------------------------------------------------

class nDimensionalListSum(unittest.TestCase):
	def test_1d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, 2, 3, 4, 5, 6]), 21)
	def test_2d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, 2, [3, 4, 5, 6]]), 21)
	def test_3d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, 2, [3, 4, [5, 6]]]), 21)
	def test_4d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, 2, [3, 4, [5, [6]]]]), 21)
	def test_5d_list(self):
		self.assertEqual(n_dimensional_list_sum(
			[1, [2, [3, [4, 5, [6]]]]]), 21)

# ------------------------------------------------------------
#  Recursion Exercise 5:
#    Write a test case for your int_to_string() function.
# ------------------------------------------------------------

class nBaseStringCoversion(unittest.TestCase):

	def test_10_2_1010(self):
		self.assertEqual(int_to_string(10, 2), '1010')
	def test_10_4_22(self):
		self.assertEqual(int_to_string(10, 4), '22')
	def test_10_6_14(self):
		self.assertEqual(int_to_string(10, 6), '14')
	def test_10_8_22(self):
		self.assertEqual(int_to_string(10, 8), '12')
	def test_10_10_22(self):
		self.assertEqual(int_to_string(10, 10), '10')
	def test_10_16_a(self):
		self.assertEqual(int_to_string(10, 16), 'A')
	def test_3501_16_dad(self):
		self.assertEqual(int_to_string(3501, 16), 'DAD')

# ------------------------------------------------------------

if __name__ == '__main__':
	unittest.main()