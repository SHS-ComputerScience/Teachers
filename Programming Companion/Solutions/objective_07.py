""" Name: <Enter your name>
    Date: <Enter today's date>

    ================================================
     PROGRAMMING COMPANION OBJECTIVE 07 (SOLUTIONS)
    ================================================

    KEY LEARNING POINTS:
    - Condition controlled iterations (loops)

    KEY WORDS:
    - while
"""

# -----------------------------------------------
#  Menu Selection Challenge
# -----------------------------------------------
""" Write a program that presents a simple menu to the user:

    1. Play Game 2. Instructions 3. Quit

    The program should ask the user for a number between 1 and 3 and will
    output “Let’s go” only when a valid entry is made, repeating the menu
    selection until a valid entry is made."""


# while True:
#     print('1. Play Game')
#     print('2. Instructions')
#     print('3. Quit')
    
#     option = int(input('Enter an option (1-3): '))

#     if option >= 1 and option <= 3:
#         print('Let\'s go!')
#         break


# -----------------------------------------------
#  Compound Interest Challenge
# -----------------------------------------------
""" Write a program that shows how compound interest grows in a bank savings
    account. The program should ask the user to input their current balance,
    the interest rate (0.04 would be 4%) and the desired balance to reach. The
    program should output the new balance each year until the desired balance
    is reached. Interest is added to the balance each year (see the Programming
    Companion PDF for details)."""


# balance = float(input('Enter your balance: '))
# interest_rate = float(input('Enter the interest rate (e.g. 0.05 for 5%): '))
# desired_balance = float(input('Enter desired balance: '))

# year = 0
# while balance < desired_balance:
#     year += 1
#     interest = balance * interest_rate
#     new_balance = balance + interest
#     print('Year {}: New balance = £{:.2f} + {}% (£{:.2f}) = £{:.2f}'.format(
#         year, balance, interest_rate * 100, interest, new_balance)
#     )
#     balance = new_balance


# -----------------------------------------------
#  Guess the Number Game Challenge
# -----------------------------------------------
""" The computer guesses a number between 1 and 100. The player has to try and
    guess the number in as few attempts as possible. When the user enters a
    number they are told if the guess is too high or too low until the number
    is guessed correctly. The player is told how many guesses they made. Write
    a program to play the game."""


# import random

# min = 1
# max = 100
# target_number = random.randint(min, max)

# count = 0
# while True:
#     guess = int(input('Enter your guess ({}-{}): '.format(min, max)))

#     if guess < target_number:
#         print('You guessed too low!')
#         min = guess
#         count += 1
#     elif guess > target_number:
#         print('You guessed too high!')
#         max = guess
#         count += 1
#     else:
#         print('Well done, you guessed the number in', count, 'guesses!')
#         break


# -----------------------------------------------
#  Gamertag Challenge
# -----------------------------------------------
""" Write a program to input a valid gamertag and keep asking for a new
    gamertag until a valid entry is made (see the Programming Companion PDF
    for details)."""


# # check the length of the gamertag entered
# invalid_gamertag = True  # renamed for improved logic

# while invalid_gamertag:
#     print('Gamertags must be 15 characters or less.')
#     gamertag = input('Enter your gamertag: ')
#     gamertag_length = len(gamertag)
#     if gamertag_length > 15:
#         print('Your gamertag is too long!')
#     else:
#         print('Gamertag accepted!')
#         break


# -----------------------------------------------
#  Rock, Paper, Scissors Challenge
# -----------------------------------------------
""" The computer and player choose one of rock, paper, or scissors. The output
    of the encounter is then displayed with rock beating scissors, scissors
    beating paper, and paper beating rock. The winner scores 1 point for a win.
    The score for both players should be output. The game is won when one
    player reaches 10 points."""


# import random

# player_score = 0
# computer_score = 0

# while player_score < 10 and computer_score < 10:
#     player = input('Rock, Paper or Scissors? ').upper()
#     computer = random.choice(('ROCK', 'PAPER', 'SCISSORS'))

#     if (
#         player == 'ROCK' and computer == 'SCISSORS' or
#         player == 'PAPER' and computer == 'ROCK' or
#         player == 'SCISSORS' and computer == 'PAPER'
#     ):
#         print(player, 'beats', computer)
#         player_score += 1
#     elif (
#         computer == 'ROCK' and player == 'SCISSORS' or
#         computer == 'PAPER' and player == 'ROCK' or
#         computer == 'SCISSORS' and player == 'PAPER'
#     ):
#         print(player, 'loses to', computer)
#         computer_score += 1
#     else:
#         print(player, 'ties with', computer)
    
#     print(
#         'Player\'s Score:', player_score, '|',
#         'Computer\'s Score:', computer_score)

# if player_score > computer_score:
#     print('You WIN!')
# else:
#     print('You LOSE!')


# -----------------------------------------------
#  Happy Numbers Challenge
# -----------------------------------------------
""" Write a program to output whether a chosen number is happy or sad (see the
    Programming Companion PDF for details)."""


# your code goes here...


# -----------------------------------------------
#  XP Challenge
# -----------------------------------------------
""" Write a program that:
    • Allows the user to keep entering XP for a game until it is 2000 or more.
    • When the XP reaches 100, 'Promoted to Corporal' is output.
    (See the Programming Companion PDF for details and extension task)."""


# your code goes here...
