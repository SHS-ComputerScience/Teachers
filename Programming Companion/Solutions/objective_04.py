""" Name: <Enter your name>
    Date: <Enter today's date>

    ================================================
     PROGRAMMING COMPANION OBJECTIVE 04 (SOLUTIONS)
    ================================================

    KEY LEARNING POINTS:
    - Selection statements

    KEY WORDS:
    - if
    - elif
    - else
"""

# -----------------------------------------------
#  Under Age Challenge
# -----------------------------------------------
""" Write a program that asks for your age. If you are over 18 it outputs the
    message, 'Over 18', otherwise it outputs, 'Under 18'."""


# age = int(input('Enter age: '))

# if age >= 18:
#     print('Over 18')
# else:
#     print('Under 18')


# -----------------------------------------------
#  Water Temperature Challenge
# -----------------------------------------------
""" Write a program that reads in the temperature of water in a container in
    Centigrade and displays a message stating whether the water is frozen (zero
    or below), boiling (100 or greater) or neither."""


# temperature = float(input('Enter water temperature in Centigrade: '))

# if temperature <= 0:
#     print('The water is frozen')
# elif temperature >= 100:
#     print('The water is boiling')
# else:
#     print('The water is neither frozen nor boiling')


# -----------------------------------------------
#  Vocational Grade Challenge
# -----------------------------------------------
""" Write a program that allows you to enter a test mark out of 100.
    The program outputs 'FAIL' for a score less than 40, 'PASS' for a score
    of 40 or more, 'MERIT' for a score of 60 or more and 'DISTINCTION' for a
    score of 80 or more."""


# test_mark = int(input('Enter test mark out of 100: '))

# if test_mark < 40:
#     print('FAIL')
# elif test_mark < 60:
#     print('PASS')
# elif test_mark < 80:
#     print('MERIT')
# else:
#     print('DISTINCTION')


# -----------------------------------------------
#  Extended Visual Dice Challenge
# -----------------------------------------------
""" Write a program that asks for a number and outputs that number as a
    graphical dice."""


# number = int(input('Enter number (1-6): '))

# print('ooooooooooooo')
# print('o           o')

# if number == 1:
#     print('o           o')
#     print('o     #     o')
#     print('o           o')
# elif number == 2:
#     print('o  #        o')
#     print('o           o')
#     print('o        #  o')
# elif number == 3:
#     print('o  #        o')
#     print('o     #     o')
#     print('o        #  o')
# elif number == 4:
#     print('o  #     #  o')
#     print('o           o')
#     print('o  #     #  o')
# elif number == 5:
#     print('o  #     #  o')
#     print('o     #     o')
#     print('o  #     #  o')
# else:
#     print('o  #     #  o')
#     print('o  #     #  o')
#     print('o  #     #  o')

# print('o           o')
# print('ooooooooooooo')


# -----------------------------------------------
#  Greatest Number Challenge
# -----------------------------------------------
""" Write a program to display the larger of two numbers entered."""


# number_1 = int(input('Enter first number: '))
# number_2 = int(input('Enter second number: '))

# if number_1 > number_2:
#     print('The largest number is', number_1)
# else:
#     print('The largest number is', number_2)


# -----------------------------------------------
#  Nitrate Challenge
# -----------------------------------------------
""" Write a program to determine the dose of nitrates administered to a carbon
    source (see flowchart on Programming Companion PDF for details)."""


# nitrate_level = float(input('Enter nitrate level (1-50): '))

# if nitrate_level > 10:
#     print('Dose 3ml')
# elif nitrate_level > 2.5:
#     print('Dose 2ml')
# elif nitrate_level > 1:
#     print('Dose 1ml')
# else:
#     print('Dose 0.5ml')


# -----------------------------------------------
#  Portfolio Grade Challenge
# -----------------------------------------------
""" Write a program that inputs a mark from the keyboard for sections of a
    project: 'analysis', 'design', 'implementation' and 'evaluation'. The
    program should output the total mark, the grade, and how many more marks
    were needed to get into the next mark band.

    Grades are:
    0   U
    4   G
    13  F
    22  E
    31  D
    41  C
    54  B
    67  A
    80  A*"""


# mark_1 = int(input('Enter analysis mark (max 25): '))
# mark_2 = int(input('Enter design mark (max 25): '))
# mark_3 = int(input('Enter implementation mark (max 25): '))
# mark_4 = int(input('Enter evaluation mark (max 25): '))

# total_mark = mark_1 + mark_2 + mark_3 + mark_4
# print(total_mark)

# if total_mark < 4:
#     print('U')
#     print(4 - total_mark, 'needed to reach next band')
# elif total_mark < 13:
#     print('G')
#     print(13 - total_mark, 'needed to reach next band')
# elif total_mark < 22:
#     print('F')
#     print(22 - total_mark, 'needed to reach next band')
# elif total_mark < 31:
#     print('E')
#     print(31 - total_mark, 'needed to reach next band')
# elif total_mark < 41:
#     print('D')
#     print(41 - total_mark, 'needed to reach next band')
# elif total_mark < 54:
#     print('C')
#     print(54 - total_mark, 'needed to reach next band')
# elif total_mark < 67:
#     print('B')
#     print(67 - total_mark, 'needed to reach next band')
# elif total_mark < 80:
#     print('A')
#     print(80 - total_mark, 'needed to reach next band')
# else:
#     print('A*')


# -----------------------------------------------
#  Cash Machine Challenge
# -----------------------------------------------
""" A cash machine dispenses £10 and £20 notes to a maximum of £250.
    Write a program that shows the user their balance, asks them how much to
    withdraw, ensures this is a valid amount without going overdrawn and with
    the notes available and outputs the new balance."""


# balance = 500
# withdrawal_limit = 250

# print('Balance: £', balance)
# withdrawal_amount = int(input('Enter withdrawal amount: '))

# if withdrawal_amount % 10 == 0:
#     if withdrawal_amount <= balance:
#         if withdrawal_amount <= withdrawal_limit:
#             balance -= withdrawal_amount
#             print('£', withdrawal_amount, 'withdrawn')
#             print('Remaining balance: £', balance)
#         else:
#             print('Amount exceeds withdrawal limit of £', withdrawal_limit)
#     else:
#         print('Not enough funds available')
# else:
#     print('This machine only dispenses £10 and £20 notes')


# -----------------------------------------------
#  Periodic Table Challenge
# -----------------------------------------------
""" Write a program that asks the user to enter the symbol or name of an
    element, or group it belongs to. The program should output the name of the
    element and its atomic weight.
    
    E.g. The user enters Li. The program outputs:
    
    Element: Lithium
    Atomic Weight: 6.94
    Group: Alkali metals
    
    If the user enters Alkali metals, the program outputs the data for all the
    elements in the alkali metals group. You only need to get this working for
    6 elements from two different groups."""


# query = input('Enter symbol, name or group of element: ').lower()
# print()

# if query == 'li' or query == 'lithium' or query == 'alkali metals':
#     print('Element: Lithium')
#     print('Atomic Weight: 6.94')
#     print('Group: Alkali Metals')
#     print()
# if query == 'na' or query == 'sodium' or query == 'alkali metals':
#     print('Element: Sodium')
#     print('Atomic Weight: 22.990')
#     print('Group: Alkali Metals')
#     print()
# if query == 'k' or query == 'potassium' or query == 'alkali metals':
#     print('Element: Potassium')
#     print('Atomic Weight: 39.098')
#     print('Group: Alkali Metals')
#     print()
# if query == 'he' or query == 'helium' or query == 'noble gases':
#     print('Element: Helium')
#     print('Atomic Weight: 4.0026')
#     print('Group: Noble Gases')
#     print()
# if query == 'ne' or query == 'neon' or query == 'noble gases':
#     print('Element: Neon')
#     print('Atomic Weight: 20.180')
#     print('Group: Noble Gases')
#     print()
# if query == 'ar' or query == 'argon' or query == 'noble gases':
#     print('Element: Argon')
#     print('Atomic Weight: 39.948')
#     print('Group: Noble Gases')
#     print()


# -----------------------------------------------
#  Train Ticket Challenge
# -----------------------------------------------
""" A train fare from Cheltenham to London is calculated in the following way:

    • £20 per station from start to destination for adults.
    • £5 extra per stop between 6am and 9am.
    • Half price for children.

    Write a program that allows the user to enter how many stations they need
    to pass through, how many adults, how many children and the time of day (as
    a number: 24 hour clock). The program should output the correct fare (see
    the Programming Companion PDF for test data."""


# stations = int(input('Enter number of stations: '))
# adults = int(input('Enter number of adults: '))
# children = int(input('Enter number of children: '))
# departure = int(input('Enter hour of departure (24 hrs): '))

# if departure >= 6 and departure <= 9:
#     fare = stations * 25
# else:
#     fare = stations * 20

# if adults > 0:
#     adult_fare = fare * adults
# else:
#     adult_fare = 0

# if children > 0:
#     child_fare = (fare * children) / 2
# else:
#     child_fare = 0

# print('Fare: £', adult_fare + child_fare)


# -----------------------------------------------
#  Hours Worked Challenge
# -----------------------------------------------
""" Write a program that asks the user for the number of hours worked this week
    and their hourly rate of pay. The program is to calculate the gross pay. If
    the number of hours worked is greater than 40, the extra hours are paid at
    1.5 times the rate. The program should display an error message if the
    number of hours worked is not in the range 0 to 60."""


# hours_worked = float(input('Enter hours worked: '))
# rate_of_pay = float(input('Enter hourly rate of pay: '))

# if hours_worked < 0 or hours_worked > 60:
#     print('Error: hours worked not in range 0-60')
# elif hours_worked > 40:
#     overtime_hours = hours_worked - 40
#     normal_hours = hours_worked - overtime_hours
#     normal_pay = normal_hours * rate_of_pay
#     overtime_pay = overtime_hours * (rate_of_pay * 1.5)
#     print('Gross pay:', normal_pay + overtime_pay)
# else:
#     print('Gross pay:', hours_worked * rate_of_pay)
