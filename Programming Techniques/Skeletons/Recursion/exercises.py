# ------------------------------------------------------------
# Recursive Function Example:
# ------------------------------------------------------------

def reverse_str_recursive(string):
	""" Returns a reversed string of string."""
	string = str(string)
	if string == '':
		return string
	else:
		return reverse_str_recursive(string[1:]) + string[0]

# ------------------------------------------------------------
# Recursion Exercise 1:
#   Write a function to calculate the sum of a list of
#   numbers.
# ------------------------------------------------------------

def list_sum(n_list):
	""" Returns the sum of a list of numbers."""
	pass # replace pass with your code

# ------------------------------------------------------------
# Recursion Exercise 2:
#   Write a function to get the factorial of a non-negative
#   integer.
# ------------------------------------------------------------

def factorial(n):
	""" Returns the factorial of a non-negative integer."""
	pass # replace pass with your code

# ------------------------------------------------------------
# Recursion Exercise 3:
#   Write a function to solve the Fibonacci sequence.
# ------------------------------------------------------------

def fibonacci(n):
	""" Return solved Fibonacci sequence."""
	pass # replace pass with your code

# ------------------------------------------------------------
# Recursion Exercise 4:
#   Write a function to calculate the sum of an n-dimensional
#   list of numbers.
# ------------------------------------------------------------

def n_dimensional_list_sum(n_list):
	""" Return the sum of an n-dimensional list of numbers."""
	pass # replace pass with your code

# ------------------------------------------------------------
# Recursion Exercise 5:
#   Write a function to converting an Integer to a string in
#   any base.
# ------------------------------------------------------------

def int_to_string(n, base):
	""" Returns string of integer in given base."""
	pass # replace pass with your code
