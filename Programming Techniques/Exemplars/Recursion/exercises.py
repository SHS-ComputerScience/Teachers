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
	if len(n_list) == 1:
		return n_list[0]
	else:
		return n_list[0] + list_sum(n_list[1:])

# ------------------------------------------------------------
# Recursion Exercise 2:
#   Write a function to get the factorial of a non-negative
#   integer.
# ------------------------------------------------------------

def factorial(n):
	""" Returns the factorial of a non-negative integer."""
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)

# ------------------------------------------------------------
# Recursion Exercise 3:
#   Write a function to solve the Fibonacci sequence.
# ------------------------------------------------------------

def fibonacci(n):
	""" Return solved Fibonacci sequence."""
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

# ------------------------------------------------------------
# Recursion Exercise 4:
#   Write a function to calculate the sum of an n-dimensional
#   list of numbers.
# ------------------------------------------------------------

def n_dimensional_list_sum(n_list):
	""" Return the sum of an n-dimensional list of numbers."""
	total = 0
	for i in range(len(n_list)):
		if isinstance(n_list[i], list):
			total += n_dimensional_list_sum(n_list[i])
		else:
			total += n_list[i]
	return total

# ------------------------------------------------------------
# Recursion Exercise 5:
#   Write a function to converting an Integer to a string in
#   any base.
# ------------------------------------------------------------

def int_to_string(n, base):
	""" Returns string of integer in given base."""
	digits = '0123456789ABCDEF'
	if n < base:
		return digits[n]
	else:
		return int_to_string(n // base, base) + digits[n % base]

print(int_to_string(10, 12))