# ----------------------------------------------------------
# Code Challenge 1: Mastermind (Exemplar 1: Basic challenge)
# ----------------------------------------------------------

import random

# generate random four digit number
random_number = str(random.randint(1000, 9999))
no_of_attempts = 0

# main game loop
while True:

    correct_digits = 0
    no_of_attempts = no_of_attempts + 1

    # get player's guess
    player_guess = input("Enter a four digit number: ")

    # check players guess
    for i in range(4):
        if player_guess[i] == random_number[i]:
            correct_digits = correct_digits + 1

    # output result
    if player_guess == random_number:
        print("Congratulations! You guessed the gorman")
        print("No. of attempts:", no_of_attempts)
        break
    else:
        print("You got", correct_digits, "right. Try again.")
