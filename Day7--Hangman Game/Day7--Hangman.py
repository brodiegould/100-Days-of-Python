import random
#to include the whole file and access items as an object, we use import
#import hangman_wordlist #include files
# ie. chosen_word = random.choice(hangman_wordlist.word_list)
#import hangman_art
# INSTEAD WE CAN CALL VARAIBLES TO USE THEM INLINE WITHOUT THE FILENAME.VARIABLE NOTATION
from hangman_art import logo, stages
from hangman_wordlist import word_list

lives = 6 # create a variable to track the number of lives. max lives = 6
print(logo)

# randomly select a word in the list, assign to 'chosen_word'
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"The answer is : {chosen_word}")

# create an empty list called 'display', then print a '_' for each letter
display = []
for _ in range(word_length):
    display += "_"

# while loop to allow user to guess until the display list is fully populated
end_of_game = False
while not end_of_game:
  
  guess = input("What letter would you like to guess? ").lower()

  # ** TRICKY PART TO REVIEW **
  # update each item to the guessed letter if it matches 
  for position in range(word_length): # position returns an index number -> 0,1,2,...N-1
      if chosen_word[position] == guess: # if the characters match
          display[position] = guess # populate the display list with guess variable

  if guess in display:
    print(f"you've already guessed {guess}")
  if guess not in chosen_word:
      print(f"{guess} was not in the word, you lose a life")
      lives -=1
      if lives == 0:
          end_of_game = True    
          print("You lose")
  print(f"{' '.join(display)}") #print the display 
    
  #check if the display list is full
  if "_" not in display:
      end_of_game = True  
      print("You win")
          
  print (stages[lives]) # print hangman image
