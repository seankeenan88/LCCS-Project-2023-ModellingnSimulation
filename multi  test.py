# Multiplayer code - new word for each player every new round and data is presented on graph
import random
from matplotlib import pyplot as plt
import csv


words = ["alpha", "bravo", "brick", "delta","money","python","phone","paper","single","zebra","stand","alive","slide","computer","quest","pencil","bottle","ghost","ruler"]
words2 = ["alpha", "bravo"]
words3 = ["alpha", "bravo", "brick", "delta"]
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
mode = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()

while mode not in mode_options:
    print("")
    print("Invalid mode option. Please try again.")
    print("------------------------------------------------------------------------")
    

print("------------------------------------------------------------------------")

ages = []

def singleplayer():
    if mode == "S":
        while True:
            try:
                print("")
                player_age = int(input("Please enter your age: "))
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                ("------------------------------------------------------------------------")


        
        ages.append(player_age)  # add age to the list
                
        player_score = 0
        while True:
            try:
                print("")
                num_plays = int(input("How many times do you want to play the game?: "))
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                ("------------------------------------------------------------------------")
        

        for i in range(num_plays):
            print("Game number:", i+1)
            print("")
            while True:
                word = random.choice(words)
                letters = list(word)
                random.shuffle(letters)
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






def multiplayer():
    if mode == "M":
        score_list1 = [0]
        score_list2 = [0]
        while True:
            try:
                print("")
                player1_age = int(input("Player 1, please enter your age: "))
                ages.append(player1_age)  # add age to the list
                print("")
                player2_age = int(input("Player 2, please enter your age: "))
                ages.append(player2_age)  # add age to the list
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                
        player1_score = 0
        while True:
            try:
                print("")
                num1_plays = int(input("How many times do you want to play the game?: "))
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                ("------------------------------------------------------------------------")
        

        
        
        for i in range(num1_plays):
            print("Game number:", i+1)
            print("")

            while True:
                word1 = random.choice(words)
                letters1 = list(word1)
                random.shuffle(letters1)
                print(letters1)
                print("")
                player1_word = input("Player 1, enter a word: ")
                
                if player1_word == word1:
                    player1_score += calculate_score(word1)
                    print("")
                    print("Good job! Player 1 score: ", player1_score)
                    print("")
                    score_list1.append(player1_score)
                    print(score_list1)
                    print("------------------------------------------------------------------------")
                    break
                else:
                    print("")
                    print("Invalid word. Please try again.")
                    print("------------------------------------------------------------------------")
                    
                
            


            player2_score = 0

            while True:
                word2 = random.choice(words)
                letters2 = list(word2)
                random.shuffle(letters2)
                print(letters2)
                print("")
                player2_word = input("Player 2, enter a word: ")
                
                if player2_word == word2:
                    player2_score += calculate_score(word2)
                    print("")
                    print("Good job! Player 2 score:", player2_score)
                    print("")
                    score_list2.append(player2_score)
                    print(score_list2)
                    print("------------------------------------------------------------------------")
                    break
                else:
                    print("")
                    print("Invalid word. Please try again.")
                    print("------------------------------------------------------------------------")

                    
        print(score_list2)
        print(score_list1)
        # plot data
        #plt.scatter(3,player1_age, label = 'player 1 age')
        #plt.scatter(3,player2_age, label = 'player 2 age')
        plt.plot(score_list1,label = "player 1 score")
        plt.plot(score_list2,label = "player 2 score")
        plt.title('Score Graph')
        plt.xlabel('Game number')
        plt.ylabel('Score')
        plt.show()
                      

def simulation():
    while True:
        try:
            print("")
            num3_plays = int(input("How many times do you want to play the game?: "))
            print("------------------------------------------------------------------------")
            break
        except ValueError:
            print("------------------------------------------------------------------------")
            print("Invalid input. Please enter a number.")
            ("------------------------------------------------------------------------")
            

    
    
    for i in range(num3_plays):
        print("Game number:", i+1)
        print("")
        
        print(letters)
        print("")
        

    computer_word = random.choice(words3)
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



# Multiplayer 100 points - score is calculated and winner is decided when reach 100 - NEED NEW WORD EVERY ROUND
words = ["alpha", "bravo", "brick", "delta","money","python","phone","paper","balls","trust","stand","alive","slide","computer","science","pencil","bottle","ghost","ruler"]
words2 = ["alpha","bravo","brick","delta"]
word = random.choice(words)
word1 = random.choice(words)
word2 = random.choice(words)
word3 = random.choice(words)
word4 = random.choice(words2)

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

print("------------------------------------------------------------------------")
print("Hypothesis number 1: This mode is when player reaches 100 points, they win.")
print("")

mode1_options = ["S", "M", "A"]
mode1 = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()

while mode1 not in mode1_options:
    print("")
    print("Invalid mode option. Please try again.")
    print("------------------------------------------------------------------------")
    mode1 = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()


def singleplayer2():
    while True:
            try:
                print("")
                player_age = int(input("Please enter your age: "))
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                ("------------------------------------------------------------------------")


    

    player_score = 0

    while player_score < 100:
        print("Current score:", player_score)
        print("")

        while True:
            word = random.choice(words)
            letters = list(word)
            random.shuffle(letters)
            print(letters)
            print("")
            player_word = input("Please enter a word: ")
            
            if player_word == word and valid_word(player_word):
                word_score = calculate_score(word)
                player_score += word_score
                print("")
                print("Good job! You scored", word_score, "points.")
                print("------------------------------------------------------------------------")
            else:
                print("")
                print("Invalid word. Please try again.")
                print("------------------------------------------------------------------------")
            
        



def multiplayer2():
    while True:
            try:
                print("")
                player1_age = int(input("Player 1, please enter your age: "))
                print("")
                player2_age = int(input("Player 2, please enter your age: "))
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")


    
    player1_score = 0
    player2_score = 0

    while player1_score < 100 and player2_score < 100:
        word1 = random.choice(words)
        letters1 = list(word1)
        random.shuffle(letters1)
        print(letters1)
        print("")
        player1_word = input("Player 1, enter a word: ")
        
        if player1_word == word1 and valid_word(player1_word):
            player1_score += calculate_score(word1)
            print("")
            print("Good job! Player 1 score:", player1_score)
            print("------------------------------------------------------------------------")
            if player1_score >= 100:
                print("Congratulations Player 1, you win!")
                print("------------------------------------------------------------------------")
                break
        else:
            print("")
            print("Invalid word. Please try again.")
            print("------------------------------------------------------------------------")

        word2 = random.choice(words)
        letters2 = list(word2)
        random.shuffle(letters2)
        print(letters2)
        print("")
        player2_word = input("Player 2, enter a word: ")
                
        if player2_word == word2 and valid_word(player2_word):
            player2_score += calculate_score(word2)
            print("")
            print("Good job! Player 2 score:", player2_score)
            print("------------------------------------------------------------------------")
            if player2_score >= 100:
                print("Congratulations Player 2, you win!")
                print("------------------------------------------------------------------------")
                break
        else:
            print("")
            print("Invalid word. Please try again.")
            print("------------------------------------------------------------------------")



def simulation2():
    if mode1 == 'A':
        print(letters)
        print("")
        
        computer_word = random.choice(words2)
        print("The computer's word is:", computer_word)
        
        computer_score = 0
        while computer_score < 100:
            if computer_word == word4:
                computer_score += calculate_score(word4)
                print("")
                print("Computer score:", computer_score)
                print("------------------------------------------------------------------------")
            else:
                print("")
                print("Invalid word. Computer score: ", computer_score )
                print("------------------------------------------------------------------------")
            
            computer_word = random.choice(words2) # choose a new word for the computer

        print("")
        print("The computer wins!")
        print("------------------------------------------------------------------------")


    


if mode1 == "S":
    singleplayer2()
elif mode1 == "M":
    multiplayer2()
elif mode1 == "A":
    simulation2()
    