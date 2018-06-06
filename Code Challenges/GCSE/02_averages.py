# ---------------------------------------------------------
# Code Challenge 2: Averages (Exemplar: Basic challenge)
# ---------------------------------------------------------

def average(number_list):
	""" Function to return the average value of a list of numbers
		"""
	total = 0
	count = len(number_list)

	# Calculate sum of all numbers in list
	for number in number_list:
		total += number

	# Alternatively, you could use:
	# for i in range(count):
	#     total += number_list[i]

	return total / count # calculate average

# Main program --------------------------------------------

user_numbers = []
getting_numbers = True

# loop until user quits
while getting_numbers:
	valid_input = False
	# loop until user enters valid input
	while not valid_input:
		user_input = input("Enter number or 'q' to quit: ")
		if user_input.lower() == "q":
			getting_numbers = False
			valid_input = True
		else:
			try:
				# check for decimal point
				if "." in user_input:
					number = float(user_input)
				else:
					number = int(user_input)
				user_numbers.append(number)
				valid_input = True
			except: # error-handling if casting fails
				print("ERROR: Invalid number")

if len(user_numbers) > 0:
	average = average(user_numbers)
	print("The average value of", user_numbers, "is", average)