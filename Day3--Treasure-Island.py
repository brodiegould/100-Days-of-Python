#refresher on if statements, global/local name spacing, scope, logical operators
# ********************************************************************************
# if/else
# number = int(input("Which number do you want to check?"))
# if number % 2 == 1:
#     print("The number is odd")
# else:
#     print("The number is even")


# BMI CALCULATOR WITH ADVICE
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # Since each if statement is achieved and executed sequentially, we don't have to set upper and lower bounds for it to execute. Just need to start low and work up
# BMI = round(weight / (height ** 2))
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.") 
# elif  BMI < 33:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 40:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")
    
# PROGRAM TO DETERMINE IF A YEAR IS A LEAP YEAR
# Ever year divisable by 4 is a leap year, except every year that is also evenly divisible by 100, unless the year is also evenly divisible by 400
# year = int(input("Enter the year to test"))
# if ((year %4) == 0) and ((year % 100) ==0) or ((year % 400) ==0):
#     print("its a leap year")
# else:
#     print("its not a leap year")

# PROGRAM TO DETERMINE COST OF THE BILL WHEN ORDERING PIZZA
#small = 15, medium = 20, large = 25
# pepperoni on small = 2, peps on medium = 3, peps on large = 3
# extra cheese = 1 for all
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == 'S':
#     bill = 15

# elif size == 'M':
#     bill = 20

# elif size == 'L':
#     bill = 25

# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill+=2
#     else:
#         bill+=3
        
# if extra_cheese == 'Y':
#         bill+=1
# print(f"your final bill is:{bill}")

# ****************************************************************
# Logical operators in python
# and 
# or
# not

# string occurance counter PROGRAM
# print("Welcome to the Love Calculator!")
# name1 = (input("What is your name? \n")).lower()
# name2 = (input("What is their name? \n")).lower()
# tens = 0
# ones = 0
# # name 1 count
# tens+= name1.count('t')
# tens+= name1.count('r')
# tens+= name1.count('u')
# tens+= name1.count('e')

# ones+= name1.count('l')
# ones+= name1.count('o')
# ones+= name1.count('v')
# ones+= name1.count('e')

# #name 2 count
# tens+= name2.count('t')
# tens+= name2.count('r')
# tens+= name2.count('u')
# tens+= name2.count('e')

# ones+= name2.count('l')
# ones+= name2.count('o')
# ones+= name2.count('v')
# ones+= name2.count('e')

# score = tens*10 + ones
# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >=40 and score <=50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")

# DAY 3 PROJECT - CHOOSE YOUR OWN ADVENTURE USING IF/ELSE/ELIF AND LOGICAL OPERATORS
#use 3 single quotes to print multiple lines to the console
print('''
                                      .=.
                                "|||"
                               _.===._                            _
                            .-".'   '."-.                        (_)
                           ." ."     ". ".                    _   |   _
                           |+-+-------+-+|                  _(_)\ | /(_)_
                     +    |---+-------+---|    +           (_)---| |---(_)
                   _="=_  :|||:|_|_|_|:|||:  _="=_              |_|_|
                   |:::|  |   |  \|/  |   |  |:::|               | |
                  | ... |_|...-=) + (=-...|_| ... |              | |
        \_._._._._| ||| | o . o . o . o . o | ||| |_._._._._/    | |
        |  _   _  |  _  | _   _   _   _   _ |  _  |  _   _  |    | |
 ._._._.| |.| |.| | |.| ||.| |.| |.| |.| |.|| |.| | |.| |.| |_._.| |.
     _  |    __   |  _  |-------------------|  _  |   __    |  _ | |
    | | |   |  |  | | | | ::   .-"""-.   :: | | | |  |  |   | | || ||
    |.| |   |..|  | |.| |     | .-"-. |     | |.| |  |..|   | |.|| ||
        :         |     | .-. | |   | | .-. |     |         '    | |
                :     : |_|_|_|   |_|_|_| :     :              | |
                          _/=============\_                      | |
                           
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
stage1 = input("You/'re at a crossroad, where do you want to go? Type 'left' or 'right'?").lower()
stage2 = None
stage3 = None

if stage1 == 'left':
    stage2 = input("You\'ve come to a lake. there is an island in the middle of the lake. type 'swim' to swim across or type  to wait 'wait'?").lower()
    if stage2 == 'wait':
        stage3 = input("pick a door - red blue, yellow, magic door").lower()
        if stage3 == 'yellow':
            print("You Win!")
        elif stage3 == 'red':
            print("Burned by fire. Game Over.")
        elif stage3 == 'blue':
            print("Eaten by beasts. Game Over.")
        elif stage3 == 'magic door':
            print("Nice try wise guy, you giga loose now")
        else:
            print("Game Over.")
    else:
        print("Attacked by a trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")



