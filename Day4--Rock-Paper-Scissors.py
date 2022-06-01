# introduction to lists and randomness

# Python uses a Mersenne Twister as its Pseudo-RNG
import random #imports the random library
# how to get a random int within a range
# random_integer = random.randint(0,5)

# how to get a random float in a range of 0-5
# random_float = random.random()
# randomFive = random_float*5
# print(randomFive)

# COIN TOSS PROGRAM
def coinToss():
    random_int= random.randint(0,1)
    if random_int == 0:
        print("Heads")
    else:
        print("Tails")
        
coinToss()

# LISTS -> Data Structure - Arrays in Python
# Lists can hold strings, ints, floats
# treat indexing as an offset from the start of the list. 0 is the first state
# fruit = ["apple", "pear", "peach", "plum", "banana"]
# #to get apple
# fruit[0]
# #to get banana
# fruit[-1]

# #to change items
# fruit[0] = "Appol"

# print(fruit)

# #to add to the list (appending to the end)
# fruit.append("dragonfruit")

# print(fruit)

# # to add another list we use extend
# fruit.extend(["apricot", "orange"])
# print(fruit)

# # exercise to pick a random value from a list
# #string.split("character we use to divide it with")
# name_string = input("Enter everyones names seperated with a comma and spacespace")
# name_list = name_string.split(", ") # splits input with value specified as an array
# random_value=random.randint(0,len(name_list )-1 ) #need one less than the total range of items
# print(name_list[random_value] + " pays the bill")

# #another way to do this is using random.choice(listName)
# print(random.choice(name_list) + " pays the bill")

# INDEX OUT OF RANGE ERROR AND HOW TO HANDLE IT
# fruit = ["apple", "pear", "peach", "plum", "banana"]
# # fruit[len(fruit)] doesn't exist because this is beyond the size of our list
# # we frequently run into problems when we obtain the length of the list, and use that length
# fruit[len(fruit) -1] #to access the end of the list

# NESTED LISTS
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale","Tomaties", "Celery", "Potatoes"]
# # to sort these into fruits and vegetables, we could make two lists, but instead we could make a nested list
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1]) #to use a nested list, the first [] selects which nested list, and the second [] selects the value within that sub list

# Treasure map using nested lists
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ") #input uses 2 integers as an input without a space to map to a list 1. column, 2.row
# position_list = [int(a) for a in str(position)] # split input into digits
# #print(position_list)
# map[position_list[1] -1][position_list[0] -1] = "X" # select input col,row and place an X

# print(f"{row1}\n{row2}\n{row3}")

# PROJECT TO PLAY ROCK PAPER SCISSORS WITH THE PC

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#have to typecast the input, or else it accepts a string
# BY DEFAULT THE INPUT IS ALWAYS A STRING. HAVE TO TYPECAST IT
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))
computer_choice = random.randint(0,2) # random integer from 0-2 inclusive
# rock = 0, paper = 1, scissors = 2
values = [rock, paper, scissors]

if choice >= 3 or choice < 0:
    print("you typed a number outside of the range")
else: 
    print("You Chose\n")
    print(values[choice])

    print("PC Chose\n")
    print(values[computer_choice])
    if choice == computer_choice:
        print("tie")
    elif choice == computer_choice == 2 or choice == 1 and computer_choice == 0 or choice == 2 and computer_choice == 1:
        print("You Win")
    else:
        print("You Lost")