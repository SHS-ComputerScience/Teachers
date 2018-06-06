# -------------------------------------------------------------
# Code Challenge 3: Email Validator (Exemplar: Basic challenge)
# -------------------------------------------------------------

""" Make a program to check whether an email address is valid or not.
	For instance, you could make sure that there are no spaces, that
	there is an @ symbol and a dot somewhere after it. Also check the
	length of the parts at the start, and that the end parts of the
	address are not blank.
	"""

valid_address = False
email_address = input("Enter email address: ")

# find mandatory and invalid characters
at_index = email_address.find("@")
dot_index = email_address[at_index:].find(".")
space_index = email_address.find(" ")

# get mailbox and domain name lengths
mailbox_length = len(email_address[:at_index])
domain_length = len(email_address[dot_index:])

if space_index < 0: # if no spaces present
	if not at_index < 0 and not dot_index < 0: # if '@' and '.' present
		if mailbox_length > 0 and domain_length > 0: # if mailbox and domain present
			valid_address = True # then address is valid

if valid_address:
	print("Valid email address")
else:
	print("Invalid email address")