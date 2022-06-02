# introductions to loops, range, fizzbuzz, numbers
#PYTHON FOR LOOP NOTATION
# for item in list_of_items:
# do something for each item
    
# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     #fruit is the index, when we loop through fruit is assigned each item individually
#     print(fruit + " Pie")

# CALCULATE AVERAGE
# total =0
# student_heights = input("Input a list of student heights ").split() #split numbers seperated by a space
# for n in range(0, len(student_heights)): #loop through the length of the list
#     student_heights[n] = int(student_heights[n]) #cast each value to an integer
#     total+= student_heights[n]
# average = total / len(student_heights)
# print("The average height is " + str(average))

# student_heights = input("Input a list of student heights ").split() #split numbers seperated by a space
# for n in range(0, len(student_heights)): #loop through the length of the list
#     student_heights[n] = int(student_heights[n]) #cast each value to an integer

# total = 0    
# for height in student_heights:
#     total += height
# num_students =0
# for students in student_heights:
#     num_students += 1
    
# average = total / num_students
# print("The average height is " + str(average))

# CALCULATE HIGHEST SCORE

#python has easy functions to look through arrays. max() gets max value, min() gets min, round() rounds the value to the nearest integer
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# high_score = 0
# for score in range(0, len(student_scores)): #we use range to handle arrays that index from 0, to len-1, since the range is in this form range(lower bound, upper bound) where upper bound isn't touched
#     if student_scores[score] > high_score:
#         high_score = student_scores[score]

# print("The highest score in the class is: "+ str(high_score))

# for loops also work without iterating over a list. We can specify a range of values
# for number in range( start, stop) where stop is the number after where we stop
# Gausses quick mathematics for adding 1-100
# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# program to add even numbers from 1 to 100 
# we can specify the increment of the range using the third value range(start, stop, increment by)
# even_sum = 0
# for i in range(0,101, 2):
#    # if i % 2 == 0:
#         even_sum+=i
# print(even_sum)

# FIZZBUZZ CODING CHALLENGE
# Your program should print each number from 1 to 100 in turn
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# `When the number is divisible by 5, then instead of printing the number it should print "Buzz".
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for i in range(0,101):
#     if i % 5 == 0 and i % 3 ==0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 ==0:
#         print("Fizz")
#     else:
#         print(str(i))

# FINAL PROJECT - PASSWORD GENERATOR PROGRAM
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = []
for i in range(nr_letters):
    password.append(letters[random.randint(0,25)])
for i in range(nr_symbols):
    password.append(symbols[random.randint(0,8)]) #rand int has an inclusive range, from 0 to 8 including 8
for i in range(nr_numbers):
    password.append(numbers[random.randint(0,9)])

random.shuffle(password)
password_string = ''.join(password)
print(password_string)



