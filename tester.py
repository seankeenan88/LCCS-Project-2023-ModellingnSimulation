import random

words = ["alpha", "bravo", "charlie", "delta"]

def new_game():
    word = random.choice(words)
    letters = list(word)
    random.shuffle(letters)
    return word, letters

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
            word, letters = new_game()
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
