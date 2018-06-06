"""
===============================================
 PROGRAMMING COMPANION OBJECTIVE 03 (EXEMPLAR)
===============================================

KEY LEARNING POINTS:
 - String manipulation

KEY WORDS:
 - .upper()
 - .lower()
 - len()
 - [:?], [-?:] and [?:?] (string slicing)
 - .find()

"""

# -----------------------------------------------
#  Initials & Surname Challenge
# -----------------------------------------------

forename = input("Enter forename: ")
surname = input("Enter surname: ")

initial = forename[0]
upper_initial = initial.upper()
upper_surname = surname.upper()

print(upper_initial, upper_surname)

# # -----------------------------------------------
# #  Airline Ticket Challenge
# # -----------------------------------------------

city_1 = input("Enter first city name: ")
city_2 = input("Enter second city name: ")

abbr_1 = city_1[:4].upper()
abbr_2 = city_2[:4].upper()

print("%s-%s" % (abbr_1, abbr_2))

# # -----------------------------------------------
# #  Name Separator Challenge
# # -----------------------------------------------

fullname = input("Enter full name: ")

space_index = fullname.find(" ")
forename = fullname[:space_index]
surname = fullname[space_index + 1:]

print("Forename:", forename)
print("Surname:", surname)

# -----------------------------------------------
#  Word Extractor Challenge
# -----------------------------------------------

sentence = "Quick brown fox jumps over the lazy dog."
print(sentence)

word = input("Enter word to remove from sentence: ")

first_index = sentence.find(word) - 1
last_index = first_index + len(word) + 1

print(sentence[:first_index] + sentence[last_index:])
