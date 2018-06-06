"""
===============================================
 PROGRAMMING COMPANION OBJECTIVE 04 (EXEMPLAR)
===============================================

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

# age = int(input("Enter age: "))

# if age >= 18:
#     print("Over 18")
# else:
#     print("Under 18")

# -----------------------------------------------
#  Water Temperature Challenge
# -----------------------------------------------

# temperature = float(input("Enter water temperature in Centigrade: "))

# if temperature <= 0:
#     print("The water is frozen")
# elif temperature >= 100:
#     print("The water is boiling")
# else:
#     print("The water is neither frozen nor boiling")

# -----------------------------------------------
#  Vocational Grade Challenge
# -----------------------------------------------

# test_mark = int(input("Enter test mark out of 100: "))

# if test_mark < 40:
#     print("FAIL")
# elif test_mark < 60:
#     print("PASS")
# elif test_mark < 80:
#     print("MERIT")
# else:
#     print("DISTINCTION")

# -----------------------------------------------
#  Extended Visual Dice Challenge
# -----------------------------------------------

# number = int(input("Enter number (1-6): "))

# print("ooooooooooooo")
# print("o           o")

# if number == 1:
#     print("o           o")
#     print("o     #     o")
#     print("o           o")
# elif number == 2:
#     print("o  #        o")
#     print("o           o")
#     print("o        #  o")
# elif number == 3:
#     print("o  #        o")
#     print("o     #     o")
#     print("o        #  o")
# elif number == 4:
#     print("o  #     #  o")
#     print("o           o")
#     print("o  #     #  o")
# elif number == 5:
#     print("o  #     #  o")
#     print("o     #     o")
#     print("o  #     #  o")
# else:
#     print("o  #     #  o")
#     print("o  #     #  o")
#     print("o  #     #  o")

# print("o           o")
# print("ooooooooooooo")

# -----------------------------------------------
#  Greatest Number Challenge
# -----------------------------------------------

# number_1 = int(input("Enter first number: "))
# number_2 = int(input("Enter second number: "))

# if number_1 > number_2:
#     print("The largest number is", number_1)
# else:
#     print("The largest number is", number_2)

# -----------------------------------------------
#  Nitrate Challenge
# -----------------------------------------------

# nitrate_level = float(input("Enter nitrate level (1-50): "))

# if nitrate_level > 10:
#     print("Dose 3ml")
# elif nitrate_level > 2.5:
#     print("Dose 2ml")
# elif nitrate_level > 1:
#     print("Dose 1ml")
# else:
#     print("Dose 0.5ml")

# -----------------------------------------------
#  Portfolio Grade Challenge
# -----------------------------------------------

# mark_1 = int(input("Enter analysis mark (max 25): "))
# mark_2 = int(input("Enter design mark (max 25): "))
# mark_3 = int(input("Enter implementation mark (max 25): "))
# mark_4 = int(input("Enter evaluation mark (max 25): "))

# total_mark = mark_1 + mark_2 + mark_3 + mark_4
# print(total_mark)

# if total_mark < 4:
#     print("U")
#     print(4 - total_mark, "needed to reach next band")
# elif total_mark < 13:
#     print("G")
#     print(13 - total_mark, "needed to reach next band")
# elif total_mark < 22:
#     print("F")
#     print(22 - total_mark, "needed to reach next band")
# elif total_mark < 31:
#     print("E")
#     print(31 - total_mark, "needed to reach next band")
# elif total_mark < 41:
#     print("D")
#     print(41 - total_mark, "needed to reach next band")
# elif total_mark < 54:
#     print("C")
#     print(54 - total_mark, "needed to reach next band")
# elif total_mark < 67:
#     print("B")
#     print(67 - total_mark, "needed to reach next band")
# elif total_mark < 80:
#     print("A")
#     print(80 - total_mark, "needed to reach next band")
# else:
#     print("A*")

# -----------------------------------------------
#  Cash Machine Challenge
# -----------------------------------------------

balance = 500
count_10 = 10
count_20 = 5
limit = 250

print("Current balance:", balance)
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount <= limit:
        initial_amount = amount
        # check if we have enough 20s
        if (amount // 20) <= count_20:
            #enough 20s
            count_20 = count_20 - (amount // 20)
            amount = amount - ((amount // 20) * 20)
        if amount > 0:
            # check if we have enough 10s
            if (amount // 10) <= count_10:
                #enough 10s
                count_10 = count_10 - (amount // 10)
                amount = amount - ((amount // 10) * 10)
            if amount > 0:
                print("This machine only dispenses £10 and £20 notes")
            else:
                balance = balance - initial_amount
                print("Transaction successful")
                print("Current balance:", balance)
    else:
        print("Amount exceeds daily limit of", limit)
else:
    print("Amount exceeds current balance")

# -----------------------------------------------
#  Periodic Table Challenge
# -----------------------------------------------



# -----------------------------------------------
#  Train Ticket Challenge
# -----------------------------------------------



# -----------------------------------------------
#  Hours Worked Challenge
# -----------------------------------------------
