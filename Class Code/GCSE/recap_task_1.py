running = True

name = input('Please enter your name: ')
print('Hello,', name)

age = input('Please enter your age: ')
birth_year = 2019 - int(age)
print('You were born in', birth_year)

if (birth_year % 4 == 0 and 
    birth_year % 100 != 0 or 
    year % 400 == 0):
    print("You were born in a leap year")
else:
    print("You were not born in a leap year")

repeat = input('Do you want to enter a new name and age? (y/n) ')
if repeat.lower() == 'n':
    running = False