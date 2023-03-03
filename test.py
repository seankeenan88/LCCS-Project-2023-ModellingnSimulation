import random

words = ["alpha", "bravo", "charlie", "delta"]

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

def play_game():
    word = random.choice(words)
    letters = list(word)
    random.shuffle(letters)
    print("Your letters are:", " ".join(letters))
    player_score = 0
    while True:
        guess = input("Enter a word: ").lower()
        if not valid_word(guess):
            print("Invalid word. Try again.")
            continue
        if set(guess) - set(word):
            print("Invalid word. Not all letters are present. Try again.")
            continue
        score = calculate_score(guess)
        print("Score for", guess, "is", score)
        player_score += score
        if guess == word:
            print("Congratulations! You found the word", word, "and earned a total score of", player_score)
            break
    print("------------------------------------------------------------------------")

mode_options = ["S", "M", "A"]
mode = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()

while mode not in mode_options:
    print("Invalid mode option. Please try again.")
    mode = input("Choose a game mode! - Singleplayer/Multiplayer/AI Simulation, {S/M/A}: ").upper()
print("------------------------------------------------------------------------")

if mode == "S":
    play_game()
elif mode == "M":
    num_games = int(input("How many games do you want to play? "))
    for i in range(num_games):
        print("Game", i+1)
        play_game()
elif mode == "A":
    num_plays = int(input("How many times do you want the computer to play the game? "))
    for i in range(num_plays):
        print("Game", i+1)
        play_game()



if difficulty == "E":
    difficulty_easy()