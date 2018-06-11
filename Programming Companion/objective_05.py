"""
===============================================
 PROGRAMMING COMPANION OBJECTIVE 05 (EXEMPLAR)
===============================================

KEY LEARNING POINTS:
 - Arithmetic operations and random numbers

ARITHMETIC OPERATORS:
 + addition         ** power of
 - subtraction      // integer division (floor)
 * multiplication   %  modulus (remainder)
 / division         

KEY WORDS:
 - import
 - random.randint()

"""

# -----------------------------------------------
#  RPG Dice Challenge
# -----------------------------------------------

# import random

# sides = int(input('Enter number of sides: '))
# number = random.randint(1, sides)

# print('You rolled', number)

# -----------------------------------------------
#  Divisible Challenge
# -----------------------------------------------

input_1 = int(input('Enter number 1: '))
input_2 = int(input('Enter number 2: '))

if input_1 == 0:
    print('Error: you cannot divide by zero')
elif input_2 % input_1 == 0:
    print(input_2, 'is exactly divisible by', input_1)
else:
    print(input_2, 'is not exactly divisible by', input_1)
    print('There is a remainder of', input_2 % input_1)

# -----------------------------------------------
#  Month Challenge
# -----------------------------------------------



# -----------------------------------------------
#  Dice Game Challenge
# -----------------------------------------------

