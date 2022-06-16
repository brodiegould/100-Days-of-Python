# introduction to scope
# local scope exists within a function
# global scope exists across the entire file

# every variable and function you give a name has its own namespace

# TO MAKE A LOCAL VARIABLE GLOBAL, WE CAN WRITE 'global' BEFORE IT, BUT THIS IS BAD PRACTICE

# python doesn't have block scope, meaning 
# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level< 5:
#         new_enemy = enemies[0]
        
# print(new_enemy) # won't print as new_enemy doesn't exist in the file scope
# THROWS NAME ERROR

# to modify in the global scope

# to differentiate global constants, in python we use all capitals
PI = 3.1415926
from art import logo

# number guessing game between 1 and 100. easy mode has 10 lives, wheras hard mode has 5 lives
import random
EASY_LIVES = 10
HARD_LIVES = 5

def easy_game():
    lives = EASY_LIVES
    number = random.randint(1,100)
    print(f"hint, the number is {number}")

    for loop in range(lives):
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        if guess == number:
            print(f"You win, the answer was {number}")
            return
        elif guess > number:
            print("Too High")
            print("Guess Again")
        elif guess < number:
            print("Too Low")
            print("Guess Again")
        lives -=1
    
def hard_game():
    lives = HARD_LIVES
    number = random.randint(1,100)
    print(f"hint, the number is {number}")
    for loop in range(lives):
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a Guess: "))
        if guess == number:
            print(f"You win, the answer was {number}")
            return
        elif guess > number:
            print("Too High")
            print("Guess Again")
        elif guess < number:
            print("Too Low")
            print("Guess Again")
        lives -=1 
            
print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 and 100")
print("Easy mode gives you 10 guesses, and hard mode gives you 10 guesses")
mode = input("type 'e' for easy mode, or type 'h' for hard mode: ")
if mode == 'e':
    easy_game()
elif mode == 'h':
    hard_game()
else:
    print("You entered an invalid input")
    mode = input("type 'e' for easy mode, or type 'h' for hard mode")
    
