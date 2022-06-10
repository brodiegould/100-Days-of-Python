# introduction to dictionaries and nesting
# Dictionaries are made up of {Key : Value} pairs
# KEYS MUST BE IMMUTABLE ie. int, float, string, bool, but NOT a list or another dictionary because lists or dictionaries can change
# programming_dictionary = {
#     "Bug": "An error in a program",
#     "Function": "A piece of code that runs over again",
#     "Loop": "The action of iterating over something repeatedly",
# }

# # to retrieve something from the dictionary, we access it with the key
# print(programming_dictionary["Bug"])

# # to insert an item into the dictionary
# programming_dictionary["Print"] = "The act of displaying to the console window"


# # to create an empty dictionary
# empty_dictionary = {}

# # to wipe an existing dictionary, we just write it as an empty dictionary
# # programming_dictionary = {}

# # to edit an item in a dictionary, we access the key and redefine the value
# programming_dictionary["Bug"] = "A moth flying outside"
# print(programming_dictionary)

# # to loop through keys and values in a dictionary
# for key in programming_dictionary:
#     print(key) # accesses keys
#     print(programming_dictionary[key]) # accesses values 

# grading program 
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}
# create empty dictionary called student_grades
student_grades = {}
# add grades to student_grades
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding" # pass key into student_grades, and write value to "outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)

# NESTING another data type inside a dictionary ie. list or dictionary

# nesting a list inside a dictionary
nested_list_dict = {
    "France": ["Paris", "South"],
    "Germany": ["Berlin", "Munich", "Stuttgard"]
}
# nesting a list inside a dict inside a dict
nested_dict_dict = {
    "France": {"cities_visited" : ["Paris", "Lille", "South"], "total_visits": 12}, #a dictionary named "cities_visited", with values of paris,south, and a key of total_visits with a value 12
    "Germany": {"cities_visited" :["Berlin", "Munich", "Stuttgard"], "beer_drank": 100}     # a list nested in a dictionary, inside a dictionary
}

#nesting a dictionary inside of a list
nested_dict_list = [
    {   # dict 1
        "country":"France", 
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {   # dict 2
        "country":"Germany", 
        "cities_visited": ["Berlin", "Munich", "Stuttgard"],
        "beer_drank":100
    },
]

# travel log program
travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# a function to allow for adding of countries to travel_log
def add_new_country(city, visits, cities_list):
    new_country = {}
    new_country["country"] = city
    new_country["visits"] = visits
    new_country["cities"] = cities_list
    
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# FINAL PROJECT - Blind Auction Program
# show logo from art.py
from art import logo
print(logo)

# import to clear command window
import os
clear = lambda: os.system('cls')

# find the highest bid and declare them the winner
def find_winner(bidding_record):
    winning_bid = 0
    for key in bidders:
        if int(bidders[key]) > int(winning_bid):
            winning_bid = bidders[key]
            person = key
    print(f"The winner is {person} with a bid of {winning_bid}")
    

# collect user input for bids and store them in a dictionary
still_bidding = True
bidders = {}
while still_bidding == True:
    name = input("Enter name of the bidder")
    bid = input("Enter this persons bid")
    bidders[name] = bid # create an entry in the dictionary
    more_bids = input("Is there another bid? type anything to continue, type 'n' to close auction")
    if more_bids == 'n':
        still_bidding = False
    else:
        clear()


find_winner(bidders)      
