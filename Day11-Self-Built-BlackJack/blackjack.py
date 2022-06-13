import random
from art import logo

Cards = {'Ace': 1,
         'Two': 2,
         'Three': 3,
         'Four': 4,
         'Five': 5,
         'Six': 6,
         'Seven': 7,
         'Eight': 8,
         'Nine': 9,
         'Ten': 10,
         'Jack': 10,
         'Queen': 10,
         'King': 10
         }

# draws 2 cards      
def new_deal():
    empty = []
    empty.append(pick_card())
    empty.append(pick_card()) 
    return empty

# returns our current score
def score(hand):
    score = 0
    for card in range(len(hand)):
        score += hand[card]
    return score

# selects a random card from the dictionary
def pick_card():
    choice = random.choice(list(Cards.items())) # returns a tuple with the key value pair
    if choice[0] == 'Ace':
        ace_val = input("Would you like Ace to be 1 or 11? Type '1' for 1, or type '11' for 11: ")
        if ace_val == '11':
            choice[1] = 11
    return choice[1]

# draws another card and appends it to the list
def another_draw(cards):
    cards.append(pick_card())
    return cards

# main gameplay function
def playGame():
    print(logo)
    ourCards = new_deal()
    theirCards = new_deal()

    print(f'Your Cards: {ourCards}, current score is {score(ourCards)}')
    print(f"Computer's first card: {theirCards[0]}")
    anotherCard = input("Type 'y' to get another card, type 'n' to pass")
    while anotherCard != 'n':
        ourCards = another_draw(ourCards)
        print(f'Your Cards: {ourCards}, current score is {score(ourCards)}')
        anotherCard = input("Type 'y' to get another card, type 'n' to pass")
    print(f'Your Final Hand: {ourCards}, final score is {score(ourCards)}')  
    if score(ourCards) > 21:
        print("You went over, loser")
    while score(theirCards) < 17:
        theirCards = another_draw(theirCards)
    print(f'Computers Final Hand: {theirCards}, final score is {score(theirCards)}')
    if score(theirCards) > 21:
        print("They went over, you win!")
    if score(theirCards) >= score(ourCards):
        print("They scored higher, you lose")
    else:
        print("You scored higher, you win")


# loop to control game plays
play=input("Do you want to play a game of Blackjack? Type 'y' or 'n'")
if play == 'n':
    print("Goodbye")
    playAgain = False
if play == 'y':
    playAgain = True
    
while playAgain == True:
    playGame()
    playSomeMore = input("Want to play again? type 'y' for yes, or 'n' to quit")
    if playSomeMore == 'n':
        print("Goodbye")
        playAgain = False
    