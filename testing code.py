# Scrabble Game
#import random

#words = ['ponies']

#random_word = random.choice(words)

#letters = list(random_word)

#random.shuffle(letters)

#print(letters)


#def is_word_valid(word):
   # return word in words


#def calculate_score(word):
 #   score = 0
  #  for letter in word:
   #     if letter in "aeioulnrst":
    #        score += 1
     #   elif letter in "dg":
      #      score += 2
       # elif letter in "bcmp":
        #    score += 3
        #elif letter in "fhvwy":
         #   score += 4
        #elif letter in "k":
         #   score += 5
        #elif letter in "jx":
         #   score += 8
        #elif letter in "qz":
         #   score += 10
    #return score


#player_score = 0
#while True:
  #  player1_word = input("Player 1, enter a word: ")
  #  if player1_word in words:
  #      print("Word is valid!")
  #  break
#else:
   # print("Invalid word!")
    
    
#player1_score = 0
#while True:
  #  player1_word = input("Player 1, enter a word: ")
  #  if player1_word in words:
  #      player1_score += calculate_score(word)
   #     print("Valid word! Score:", player1_score)
    #    break
   # else:
    #    print("Invalid word. Please try again.")

import random

# A list of valid words
words = ["scrabble", "singleplayer", "multiplayer"]

def is_word_valid(word):
    return word in words

def calculate_score(word):
    score = 0
    for letter in word:
        if letter in "aeioulnrst":
            score += 1
        elif letter in "dg":
            score += 2
        elif letter in "bcmp":
            score += 3
        elif letter in "fhvwy":
            score += 4
        elif letter in "k":
            score += 5
        elif letter in "jx":
            score += 8
        elif letter in "qz":
            score += 10
    return score

# Ask the user to choose a game mode
mode = input("Choose a game mode (single/multi): ")

if mode == "single":
    # Single player mode
    # Ask the player to input a word
    player_word = input("Enter a word: ")

    # Check if the word is in the list of valid words
    if player_word in valid_words:
        print("Word is valid!")
    else:
        print("Invalid word!")

elif mode == "multi":
    computer_word = random.choice(words)
print("The computer's word is:", computer_word)

computer_score = 0
while True:
    if is_word_valid(word):
        computer_score += calculate_score(word)
        print("Valid word! Score:", computer_score)
        break
    else:
        print("Invalid word. Please try again.")
else:
    print("Invalid game mode selected. Please choose 'single' or 'multi'.")

