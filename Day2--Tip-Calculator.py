# primative data types in Python

# Strings are handled as an array of chars
# This method is called subscripting
#print("Hello"[4])

# Integers contain no quotes
#print(123 + 456)

# to handle large numbers and make them pretty, we can add underscores to replace where we would normally visualize a number with commas. ie 1,234,567
from dataclasses import asdict


bigNum = 1_234_567

# Floats are floating point numbers that deal with decimals 
# *PYTHONS FLOAT TYPE IS DOUBLE
PI = 3.14159

# Boolean numbers have a binary outcome (Note the capital on the first letter)
T = True
F = False

# Type Errors, and Type conversions
num_char = len(input("What is your name?"))
# print("your name has" + num_char + "characters.")
# Since we are concatonating a string to an integer, we throw a type error
# To check the type of data being used, we can use the type() function
print(type(num_char)) #checks type

#this throws an error since we are trying to merge a string with an integer
#to avoid this error we can do a type conversion. to convert to a string we do str()
new_num_char = str(num_char)
print("your name has " + new_num_char + "characters.")

# ** TYPE CONVERSIONS
a = float(123) #adds a decimal place to 123.0
print(type(a))
print(a)

# to convert to float do float(), to convert to strings to concatonate #'s, do str()


# splitting an int into its hamming weight values and adding them
var = input("Enter a 2 digit number")
a=var[0]
b=var[1]
print(int(a) + int(b))

# For division in python, dividing two ints will result in a float
# print(type(3/7))
# to handle exponents, 2 ^4 looks like
# 2 ** 4

# Python follows BEMDAS, where it handles MD and AS as equal importance, so it just goes left to right
# () 
# ** 
# * / READS LEFT TO RIGHT
# + - READS LEFT TO RIGHT
# print (3 * 3 + 3 / 3 - 3)
# order of operations here is (3*3) + (3/3) - 3 = 7


# CHALLENGE - BMI CALCULATOR 
# returns your BMI with type conversions
#BMI = weight(kg) / height^2(m)
weight = input("Enter your weight in kg ")
height = input("Enter your height in m ")
# below the double asterisk doesn't work since the input function KEYBOARD INPUTS AUTOMATICALLY BECOME STRINGS
bmi = int(weight)/float(height) ** 2
# since this outputs as a float, we have to trim the decimal places off, then change it to a string after for printing
bmi_int = int(bmi)

print("your BMI is " + str(bmi_int))

# to round numbers in python we can use round(, # of digits)
print(round(2.66666666666666,2))

# floor division returns an integer automatically
print(type(8 // 3))

# NOTE EVERY DIVISION AUTOMATICALLY RETURNS A FLOAT, EVEN WHEN DIVIDING WHOLE NUMS

# F STRINGS IS A WAY WE MIX STRINGS AND DATA TYPES
score = 0
isWinning = True
height = 1.8
#one way is 
print("your score is " + str(score))

# we can accomplish this by using F-Strings as follows
print( f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# CHALLENGE - YOUR LIFE IN WEEKS
# a program using f-strings that tells us how many days, weeks and months we have left if we live until 90
# outputs you have x days, y weeks, and z months left
yourAge = int(input(("How old are you? ")))
months = (90 - yourAge) * 12
weeks = (90 - yourAge) * 52
days = (90 - yourAge) * 365

print(f"you have {days} days, {weeks} weeks, and {months} months left on earth. make it count!")


# PROJECT - Tip Calculator
# asks for how much the total bill is, how much you want to tip, and how many people want to split the bill
# should round to 2 decimal places

print("Welcome to the tip calculator!")
bill = float(input("How much was the total bill?"))
tip = int(input("How much tip would you like to give? 15%, 18%, 20% "))
people = int(input("How many people are splitting the bill? "))
bill_split = round((bill / people) * (1+ (tip/100)),2)
print(f"each person pays ${bill_split}")
# another way we could handle this is by formatting the float into a string with 2 decimal places
# bill_split = {":.2f"}.format((bill / people) * (1+ (tip/100)))