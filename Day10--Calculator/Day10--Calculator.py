#introduction to function outputs (return)
# functions without return types are useful to reduce the amount of code written when doing operations repeatedly
# functions with inputs are useful to modify an external variables

# functions with outputs
# when you want to pass the return of the function to a variable 
# when calling my_function() it will replace it with the number 3
# three = my_function() 
# def my_function():
#     three = 1+2
#     return three

# convert text to be title case (first letter capitalized)
# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name('brOdIe', 'gOulD')
# print(formatted_string)

# functions with more than one return statement. everything after return NEVER GETS EXECUTED
# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "at least one of the inputs is empty"
    
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"

# leap year program 
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(yr, mn):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     if mn > 12 or mn < 0:
#         return "Month is invalid"
#     if yr < 0:
#         return " Year is invalid"
#     if is_leap(yr) == True:
#         month_days[1] == 29
#         return month_days[mn - 1]
#     else:
#         return month_days[mn - 1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# DOC STRINGS - used to provide insight to the functions we write. triple quotations means the comment will be the prompt when you type the function in (it hovers)
# def my_function(input):
#     """Returns 1 + 2"""
#     return 1+2

# CALCULATOR PROGRAM
from art import logo


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
}

def calculator():
    print(logo)
    isRunning = True
    num1 = float(input("enter the first number: "))
    
    for key in operations:
        print(key)
        
    while isRunning == True:
        op = input("which of these operations would you like to do?") 
        num2 = float(input("enter the next number: "))
        math = operations[op]
        answer = math(num1,num2)
        print(f"{num1} {op} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or to start again, type 'n'") == 'y':
            num1 = answer
        else:
            isRunning = False
            calculator() # use recursion to restart the calculator function

# for recursion there must be a condition for it to run, or else it will run infinitely
calculator()