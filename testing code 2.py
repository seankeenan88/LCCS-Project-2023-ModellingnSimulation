import random

words = ["alpha", "bravo", "charlie", "delta"]
word = random.choice(words)
word1 = random.choice(words)
word2 = random.choice(words)
word3 = random.choice(words)

letters = list(word)
letters1 = list(word1)
letters2 = list(word2)
letters3 = list(word3)
random.shuffle(letters)
random.shuffle(letters1)
random.shuffle(letters2)
random.shuffle(letters3)

def valid_word(word):
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

mode_options = ["S", "M", "A"]
mode = input("Choose a game mode! - Singleplayer/Multiplayer/AI v Player, {S/M/A}: ").upper()

while mode not in mode_options:
    print("")
    print("Invalid mode option. Please try again.")
    print("------------------------------------------------------------------------")
    

print("------------------------------------------------------------------------")


# Singleplayer Mode
def singleplayer():
    if mode == "S":
        player_age = int(input("Please enter your age: "))
        print("------------------------------------------------------------------------")
        player_score = 0
        num_plays = int(input("How many times do you want to play the game?: "))
        print("------------------------------------------------------------------------")
        for i in range(num_plays):
            print("Game number:", i+1)
            print("")
            while True:
                print(letters)
                print("")
                player_word = input("Please enter a word: ")
                if player_word == word:
                    player_score += calculate_score(word)
                    print("")
                    print("Good job! Player score:", player_score)
                    print("------------------------------------------------------------------------")
                    break
                else:
                    print("")
                    print("Invalid word. Please try again.")
                    print("------------------------------------------------------------------------")


# Multiplayer Mode
def multiplayer():
    if mode == "M":
        player1_age = int(input("Player 1, please enter your age: "))
        player2_age = int(input("Player 2, please enter your age: "))
        print("------------------------------------------------------------------------")
        player1_score = 0
        num1_plays = int(input("How many times do you want to play the game?: "))
        print("------------------------------------------------------------------------")
        for i in range(num1_plays):
            print("Game number:", i+1)
            print("")

            while True:
                print(letters1)
                print("")
                player1_word = input("Player 1, enter a word: ")
                if player1_word == word1:
                    player1_score += calculate_score(word1)
                    print("")
                    print("Good job! Player 1 score:", player1_score)
                    print("------------------------------------------------------------------------")
                    break
                else:
                    print("")
                    print("Invalid word. Please try again.")
                    print("------------------------------------------------------------------------")


            player2_score = 0

            while True:
                print(letters2)
                print("")
                player2_word = input("Player 2, enter a word: ")
                if player2_word == word2:
                    player2_score += calculate_score(word2)
                    print("")
                    print("Good job! Player 2 score:", player2_score)
                    print("------------------------------------------------------------------------")
                    break
                else:
                    print("")
                    print("Invalid word. Please try again.")
                    print("------------------------------------------------------------------------")

            

            
def simulation():
    if mode == "A":
        print(letters)
        print("")

        computer_word = random.choice(words)
    print("The computer's word is:", computer_word)

    computer_score = 0
    while True:
        if computer_word == word:
            computer_score += calculate_score(word)
            print("")
            print("Computer score:", computer_score)
            break
        else:
            print("")
            print("Invalid word. Computer score: ", computer_score )
            print("------------------------------------------------------------------------")
            break


                
            
           
if mode == "S":
    singleplayer()
elif mode == "M":
    multiplayer()
elif mode == "A":
    simulation()

        
    