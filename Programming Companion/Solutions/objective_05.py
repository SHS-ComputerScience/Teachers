""" Name: <Enter your name>
    Date: <Enter today's date>

    ================================================
     PROGRAMMING COMPANION OBJECTIVE 05 (SOLUTIONS)
    ================================================

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
""" Write a program that asks the user how many sides a dice has and outputs
    a random number for that dice."""


# import random

# sides = int(input('Enter number of sides: '))
# number = random.randint(1, sides)

# print('You rolled', number)


# -----------------------------------------------
#  Divisible Challenge
# -----------------------------------------------
""" Write a program that asks the user for two numbers. The program should
    output whether the two numbers are exactly divisible by each other. If not,
    it should return the remainder. If the user enters a 0 the program should
    give an error message (see the Programming Companion PDF for test data)."""


# input_1 = int(input('Enter number 1: '))
# input_2 = int(input('Enter number 2: '))

# if input_1 == 0:
#     print('Error: you cannot divide by zero')
# elif input_2 % input_1 == 0:
#     print(input_2, 'is exactly divisible by', input_1)
# else:
#     print(input_2, 'is not exactly divisible by', input_1)
#     print('There is a remainder of', input_2 % input_1)


# -----------------------------------------------
#  Month Challenge
# -----------------------------------------------
""" Write a program that lets the user enter a number between 1 and 12 and
    displays the month name for that month number and the number of days in the
    month. The input 3 would therefore display March has 31 days.

    Remember February has 28 or 29 days depending on whether it is a leap year.
    It is a leap year if the year is exactly divisible by 4."""


# month = int(input('Enter the month (1-12): '))

# # get name of month from number
# if month == 1:
#     month_name = 'January'
# elif month == 2:
#     month_name = 'February'
# elif month == 3:
#     month_name = 'March'
# elif month == 4:
#     month_name = 'April'
# elif month == 5:
#     month_name = 'May'
# elif month == 6:
#     month_name = 'June'
# elif month == 7:
#     month_name = 'July'
# elif month == 8:
#     month_name = 'August'
# elif month == 9:
#     month_name = 'September'
# elif month == 10:
#     month_name = 'October'
# elif month == 11:
#     month_name = 'November'
# elif month == 12:
#     month_name = 'December'

# # get number of days in month
# if month == 2:
#     year = int(input('Enter the year: '))
#     # february has 29 days in a leap year and 28 days otherwise
#     if year % 4 == 0:
#         days == 29
#     else:
#         days == 28
# # odd months before august have 31 days, even months after july have 30
# elif month < 8 and month % 2 == 1 or month > 7 and month % 2 == 0:
#     days = 31
# else:
#     days = 30

# print(month_name, 'has', days, 'days')


# -----------------------------------------------
#  Dice Game Challenge
# -----------------------------------------------
""" Write a program to calculate the score in a simple dice game (see the
    Programming Companion PDF for game rules flowchart)."""


# import random

# dice_1 = random.randint(1, 6)
# dice_2 = random.randint(1, 6)
# dice_3 = random.randint(1, 6)

# if dice_1 == dice_2 == dice_3:
#     score = dice_1 + dice_2 + dice_3
# elif dice_1 == dice_2:
#     score = (dice_1 + dice_2) - dice_3
# elif dice_2 == dice_3:
#     score = (dice_2 + dice_3) - dice_1
# elif dice_3 == dice_1:
#     score = (dice_3 + dice_1) - dice_2
# else:
#     score = 0

# print('You rolled a {}, {} and {}'.format(dice_1, dice_2, dice_3))
# print('You score is', score)
