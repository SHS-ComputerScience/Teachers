""" Name: <Enter your name>
    Date: <Enter today's date>

    ================================================
     PROGRAMMING COMPANION OBJECTIVE 06 (SOLUTIONS)
    ================================================

    KEY LEARNING POINTS:
    - Count controlled iterations (loops)

    KEY WORDS:
    - for
"""

# -----------------------------------------------
#  Square Numbers challenge
# -----------------------------------------------
""" Write a program to output all the squares of a number between 1 and 20
    (see the Programming Companion PDF for flowchart)."""


# for counter in range(1, 21):
#     squared = counter * counter
#     print(counter, 'squared is', squared)


# -----------------------------------------------
#  9 Green Bottles Challenge
# -----------------------------------------------
""" Write a program that prompts the user to enter the number of bottles.

    The program outputs:

    9 green bottles sitting on the wall
    8 green bottles sitting on the wall
    7 green bottles sitting on the wall, etc. """


# number_of_bottles = int(input('Enter number of bottles: '))

# for bottle in range(number_of_bottles, -1, -1):
#     print(bottle, 'green bottles sitting on the wall')


# -----------------------------------------------
#  Times Table Challenge 1
# -----------------------------------------------
""" Write a program that asks the user to enter a number between 1 and 12.
    The program outputs the times table of that number between 1 and 12."""


# number = int(input('Enter a number between 1 and 12: '))

# for count in range(1, 13):
#     print(count, 'times', number, 'is', count * number)


# -----------------------------------------------
#  Fibonacci Sequence Challenge
# -----------------------------------------------
""" Write a program to produce the Fibonacci sequence of 20 numbers (see the
    Programming Companion PDF for details)."""


# n_minus_2 = 0
# n_minus_1 = 1
# print(1)

# for count in range(20):
#     fibonacci = n_minus_2 + n_minus_1
#     n_minus_2 = n_minus_1
#     n_minus_1 = fibonacci
#     print(fibonacci)


# -----------------------------------------------
#  Average Calculator Challenge
# -----------------------------------------------
""" Write a program that asks the user to enter how many numbers are to be
    averaged. The user can then enter the numbers. The program outputs the
    total and the mean."""


# total = 0
# count = int(input('How many numbers do you want to average? '))

# for i in range(count):
#     number = int(input('Enter number: '))
#     total += number

# print('Total =', total, '| Average =', total / count)


# -----------------------------------------------
#  FizzBuzz Challenge
# -----------------------------------------------
""" Write a program that outputs the numbers from 1 to 100. But for multiples
    of three output 'Fizz' instead of the number and for the multiples of five
    output 'Buzz'. For numbers which are multiples of both three and five
    output 'FizzBuzz'."""


# for number in range(1, 100):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)


# -----------------------------------------------
#  Times Table Challenge 2
# -----------------------------------------------
""" Write a program that could be used in an infant school to prompt a child
    with ten simple random 1 digit maths calculation, e.g. '4 * 7 = '. The user
    enters their answer and the computer tells them if they are correct. At the
    end of the test the program outputs how many problems the child got
    right."""


# import random

# score = 0

# for i in range(10):
#     number_1 = random.randint(1, 9)
#     number_2 = random.randint(1, 9)
#     answer = int(input('{}. {} x {} = '.format(i + 1, number_1, number_2)))

#     if answer == number_1 * number_2:
#         print('Correct! :)')
#         score += 1
#     else:
#         print('That\'s not right... :(')

# print('You got', score, 'out of 10 problems right!')


# -----------------------------------------------
#  ROT13 Challenge
# -----------------------------------------------
""" Write a program that allows the user to enter plain text, and the ROT13
    cipher is output. Extend the program to allow cipher text to be input, with
    the plain text output (see the Programming Companion PDF for details)."""


# lower_half = 'AaBbCcDdEeFfGgHhIiJjKkLlMm'
# upper_half = 'NnOoPpQqRrSsTtUuVvWwXxYyZz'

# plaintext = input('Enter message: ')
# ciphertext = ''

# # perform ROT13 on each alphabetic character
# for letter in plaintext:
#     if letter in lower_half:
#         ciphertext += upper_half[lower_half.index(letter)]
#     elif letter in upper_half:
#         ciphertext += lower_half[upper_half.index(letter)]
#     else:
#         ciphertext += letter

# print(ciphertext)


# # ~~~~~~~~~~
# # EXTENSION:
# # ~~~~~~~~~~


# lower_half = 'AaBbCcDdEeFfGgHhIiJjKkLlMm'
# upper_half = 'NnOoPpQqRrSsTtUuVvWwXxYyZz'

# mode = input('(E)ncipher plaintext or (D)ecipher ciphertext? ').upper()

# if mode == 'D':
#     # swap lower and upper halves if deciphering cipher text
#     first_half, second_half = upper_half, lower_half
#     valid_input = True
# elif mode == 'E':
#     # do not swap lower and upper halves if enciphering plain text
#     first_half, second_half = lower_half, upper_half
#     valid_input = True

# text = input('Enter message: ')
# processed_text = ''

# # perform ROT13 on each alphabetic character
# for letter in text:
#     if letter in first_half:
#         processed_text += second_half[first_half.index(letter)]
#     elif letter in second_half:
#         processed_text += first_half[second_half.index(letter)]
#     else:
#         processed_text += letter

# print(processed_text)


# -----------------------------------------------
#  Letter Game Challenge
# -----------------------------------------------
""" Write a program that asks the user to input a word. The program
    should then output the score for the word based on the letters used
    (see the Programming Companion PDF for details)."""


# letters = 'EARIOTNSLCUDPMHGBFYWKVXZJQ'
# score = 0

# word = input('Enter a word: ').upper()

# for letter in word:
#     score += letters.index(letter) + 1

# print('The word', word, 'has a score of', score)
