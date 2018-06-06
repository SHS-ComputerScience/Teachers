def convert(n, base=64):
	""" Return string of n in base."""
	n = ord(n)
	# Base64: A-Z (65-90), a-z (97-122), 0-9 (48-57), + (43), / (47)
	digits = "".join(chr(x) for x in range(65, 91)) +  \
				"".join(chr(x) for x in range(97, 123)) + \
				"".join(chr(x) for x in range(48, 58)) +  \
				chr(43) +                                 \
				chr(47)
	if n < base:
		return digits[n]
	else:
		return convert(n // base, base) + digits[n % base]

print(convert("255"))