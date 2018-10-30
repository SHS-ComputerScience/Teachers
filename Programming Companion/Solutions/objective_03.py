""" Name: <Enter your name>
    Date: <Enter today's date>

    ================================================
     PROGRAMMING COMPANION OBJECTIVE 03 (SOLUTIONS)
    ================================================

    KEY LEARNING POINTS:
    - String manipulation

    KEY WORDS:
    - string.upper()
    - string.lower()
    - len()
    - [:?], [-?:] and [?:?] (string slicing)
    - string.find()
"""

# -----------------------------------------------
#  Initials & Surname Challenge
# -----------------------------------------------
""" Write the program to ask for a person’s forename and surname, outputting
    their first initial and the rest of their name in capitals."""


# forename = input("Enter forename: ")
# surname = input("Enter surname: ")

# initial = forename[0]
# upper_initial = initial.upper()
# upper_surname = surname.upper()

# print(upper_initial, upper_surname)


# -----------------------------------------------
#  Airline Ticket Challenge
# -----------------------------------------------
""" Write a program that allows the user to input the name of two cities.
    The program should then output the first 4 characters of each city in
    capital letters, separated by a dash."""


# city_1 = input("Enter first city name: ")
# city_2 = input("Enter second city name: ")

# abbreviation_1 = city_1[:4].upper()
# abbreviation_2 = city_2[:4].upper()

# print("%s-%s" % (abbreviation_1, abbreviation_2))


# -----------------------------------------------
#  Name Separator Challenge
# -----------------------------------------------
""" Write a program that allows the user to enter their full name on one line.
    The program should then output for example:
    
    Forename: Simon
    Surname: Hall

    The program needs to find the space and then extract the characters to the
    left and right of the space into two different variables."""


# fullname = input("Enter full name: ")

# space_index = fullname.find(" ")
# forename = fullname[:space_index]
# surname = fullname[space_index + 1:]

# print("Forename:", forename)
# print("Surname:", surname)


# -----------------------------------------------
#  Word Extractor Challenge
# -----------------------------------------------
""" Write a program that outputs the sentence:
    Quick brown fox jumps over the lazy dog. 
    
    The user can then enter the word to be cut from the sentence.
    The sentence is then output with the word removed."""


# sentence = "Quick brown fox jumps over the lazy dog."
# print(sentence)

# word = input("Enter word to remove from sentence: ")

# first_index = sentence.find(word) - 1
# last_index = first_index + len(word) + 1

# print(sentence[:first_index] + sentence[last_index:])
