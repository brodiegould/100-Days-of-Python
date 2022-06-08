# functions with parameters and arguements
# # a function that allows for input
# # when we call this function, we set name = "Brodie"
# # the something variable is the parameter
# # the name "Brodie" is the argument
# def greeting_with_name(name):
#     print(f"Howdy {name}")
# greeting_with_name("Brodie")

# # functions with multiple inputs
# def two_input_greeting(name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")
# two_input_greeting("Brodie","Victoria") # inputs have to be called on the proper order. otherwise name = 'Victoria' and location = 'Brodie'
# two_input_greeting(location="Victoria",name= 'Brodie') # we can explicitly specify the inputs so we can use any order we want


# # program that computes the amount of paint needed to paint a given area
# # one bucket of paint covers 5m^2
# # rounds up to the nearest can of paint
# import math
# def paint_calc(height, width, cover=5): # since the coverage is 5 by default, I set the default parameter to 5
#     cans = math.ceil((height * width) / cover)
#     print(f"You'll need {cans} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# #coverage = 5
# paint_calc(height=test_h, width=test_w,) #cover=coverage)

# prime number checker (number that is only divisible by 1 and itself)

# def prime_checker(number):
#     flag = False
#     div = 0
#     if number > 1:
#         for test in range(2,number):
#             if number % test == 0:
#                 flag = True
#                 div = test
#                 break
#     if flag == True:
#         print(f"This number is rational, divides by {div}")
#     else:
#         print(f"{number} is a prime number")
        
# n = int(input("Check this number: "))
# prime_checker(number=n)

# Project - Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(text_in,shift_by,cipher_dir):
    shift_by %= 26                                          # prevent overflow
    output_text = ""                                        # create an empty string 
    if direction == 'decode':
            shift_by *= -1                                  # shifts up or down by value   
    for char in text_in:                                    # loop through chars in a string
        if char in alphabet:
            position = alphabet.index(char)                 # look up index of letter in alphabet list
            new_position = (position + shift_by) % 26       # shift up or down, since shift_by becomes negative when decode is selected. shift by = shift_by * -1
            output_text+= alphabet[new_position]            # concatonate all letters
        else:
            output_text += char                             # if the input char isn't in the alphabet, ignore it and append it to the char
    print(f"the {cipher_dir}d text is {output_text}")

should_continue = True
while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text_in = text, shift_by = shift, cipher_dir = direction)
    run_again = input("Type 'yes' to run again, or type 'no' to finish")
    if run_again == 'no':
        should_continue = False
print("Goodbye")