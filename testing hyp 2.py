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
mode = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()

while mode not in mode_options:
    print("")
    print("Invalid mode option. Please try again.")
    print("------------------------------------------------------------------------")
    

print("------------------------------------------------------------------------")

difficulty_options =['E','N','H']
difficulty = input("Choose a difficulty! - Easy/Normal/Hard, {E/N/H}: ").upper()

def simulation():
    if difficulty_level == "e":
        computer_word = random.choice(words)
    elif difficulty_level == "n":
        computer_word = random.choice(words)
    else:
        computer_word = random.choice(words)
    
    print("The computer's word is:", computer_word)

    computer_score = 0
    while True:
        if word in words:
            if computer_word == word:
                computer_score += calculate_score(word)
                print("")
                print("Computer score:", computer_score)
                print("------------------------------------------------------------------------")
                break
            else:
                print("")
                print("Invalid word. Computer score: ", computer_score )
                print("------------------------------------------------------------------------")
        else:
            print("")
            print("Invalid word. Please enter a word from the following list: ", words)
            print("------------------------------------------------------------------------")

if mode == 'a':
    simulation()


