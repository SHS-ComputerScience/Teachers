# -------------------------
#  Palindrome Checker v1.0
# -------------------------

def is_palindrome(sequence):
	""" Function to return true is sequence is a valid palindrome or
		false if it is not. Assumes that sequence is a string which
		could be either a word or a phrase.
		"""
	max = len(sequence) - 1 # gets the index of the last character in sequence
	reversed_sequence = ""  # creates 'placeholder' for our reversed sequence

	# loop to reverse the order of characters in sequence
	for i in range(max, -1, -1): # i starts as the index of last character (max) and
								 # then decreases (or decrements) by 1 until it gets to 0
		# adds (or concatenates) the character in sequence at index i to reversed_sequence
		reversed_sequence = reversed_sequence + sequence[i]

	if sequence == reversed_sequence:
		return True # if sequence and reversed_sequence match, then sequence is a palindrome
	else:
		return False # if they don't match, then sequence is not a palindrome

# ------
# Tests
# ------
print(is_palindrome("racecar")) # Should be true
print(is_palindrome("A Toyota's a Toyota")) # Should be true **
print(is_palindrome("computer")) # Should be false
print(is_palindrome("This is false")) # Should be false

# ** Why does this return false? How could we alter our algorithhm to make it return true?