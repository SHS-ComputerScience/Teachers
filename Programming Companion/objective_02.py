"""
===============================================
 PROGRAMMING COMPANION OBJECTIVE 02 (EXEMPLAR)
===============================================

KEY LEARNING POINTS:
 - Inputting strings and numbers into variables

KEY WORDS:
 - input()
 - int()
 - float()

"""

# -----------------------------------------------
#  Simple Adder Challenge
# -----------------------------------------------

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

print("You entered numbers", number_1, "and", number_2)
print("They add up to", number_1 + number_2)

# -----------------------------------------------
#  Test Marks Challenge
# -----------------------------------------------

test_mark_1 = int(input("Enter first test mark: "))
test_mark_2 = int(input("Enter second test mark: "))
test_mark_3 = int(input("Enter third test mark: "))

average = (test_mark_1 + test_mark_2 + test_mark_3) / 3

print("The average test mark is", average)

# -----------------------------------------------
#  Temperature Converter Challenge
# -----------------------------------------------

temperature_f = float(input("Enter temperature in Fahrenheit: "))
temperature_c = (temperature_f - 32) * (5/9)

print("The temperature in Centigrade is", temperature_c)

# -----------------------------------------------
#  Height & Weight Challenge
# -----------------------------------------------

height_inches = float(input("Enter height in inches: "))
weight_stones = float(input("Enter weight in stones: "))

height_cm = height_inches * 2.54
weight_kg = weight_stones * 6.364

print("The height in centimetres is", height_cm)
print("The weight in kilograms is", weight_kg)

# -----------------------------------------------
#  Toy Cars Challenge
# -----------------------------------------------

hours_worked = float(input("Enter number of hours worked: "))
toycars_made = int(input("Enter number of toy cars made: "))

wages = (hours_worked * 9) + (toycars_made * 0.6)

print("The wages for the day are £%.2f" % wages)

# -----------------------------------------------
#  Fish Tank Volume Challenge
# -----------------------------------------------

length_cm = float(input("Enter tank length in cm: "))
depth_cm = float(input("Enter tank depth in cm: "))
height_cm = float(input("Enter tank height in cm: "))

volume_litres = (length_cm * depth_cm * height_cm) / 1000
volume_gallons = volume_litres / 4.55

print("The volume of water required to fill the tank in litres is", volume_litres)
print("The volume of water required to fill the tank in gallons is", volume_gallons)

# -----------------------------------------------
#  Circle Properties Challenge
# -----------------------------------------------

diameter = float(input("Enter diameter of circle: "))

radius = diameter / 2
area = 3.14 * (radius**2)
circumference = 3.14 * diameter

print("The radius of the circle is", radius)
print("The area of the circle is", area)
print("The circumference of the circle is", circumference)

arc_angle = int(input("Enter arc angle: "))
arc_length = (circumference * arc_angle) / 360

print("The arc length is", arc_length)