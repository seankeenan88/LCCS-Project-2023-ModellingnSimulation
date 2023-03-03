import csv
import random
from matplotlib import pyplot as plt

words = ["alpha", "bravo", "brick", "delta","money","python","phone","paper","balls","trust","stand","alive","slide","computer","science","pencil","bottle","ghost","ruler"]
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


# Singleplayer Mode
def singleplayer():
    if mode == "S":
        while True:
            try:
                print("")
                player_age = int(input("Please enter your age: "))
                ages.append(player_age)  # add age to the list
                print("------------------------------------------------------------------------")
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                ("------------------------------------------------------------------------")
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
        while True:
            try:
                print("")
                player1_age = int(input("Player 1, please enter your age: "))
                ages.append(player1_age)  # add age to the list
                print("")
                player2_age = int(input("Player 2, please enter your age: "))
                ages.append(player2_age)  # add age to the list
                break
            except ValueError:
                print("------------------------------------------------------------------------")
                print("Invalid input. Please enter a number.")
                
        player1_score = 0
        print("------------------------------------------------------------------------")
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
                    
                score_list1 = []
                score_list1.append(player1_score)
            


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
                    
                score_list2 = []
                score_list2.append(player2_score)

            print (score_list2)
            print(score_list1)
            # plot data
            plt.scatter(3,player1_age,label = 'player 1 age')
            plt.scatter(2,player2_age,label = 'player 2 age')
            plt.plot(score_list1,label = "player 1 score")
            plt.plot(score_list2m,label = "player 2 score")
            plt.title('Age - Best Performers')
            plt.xlabel('Age')
            plt.ylabel('Score')
            plt.show()
        
# Simulation Mode           
def simulation():
    num3_plays = int(input("How many times do you want the computer to play the game?: "))
    print("------------------------------------------------------------------------")
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




# write ages to CSV file
with open('ages.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ages'])
    for age in ages:
        writer.writerow([age])

# read ages from CSV file
ages = []
with open('ages.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        ages.append(int(row[0]))

# sort ages from worst to best
ages.sort()

# plot data
plt.plot(player1_age, '')
plt.plot(player2_age, '')
plt.title('Age - Best Performers')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()



# CSV (store results) Save age, winners, player points
#txtfile = (open('Multiplayer_Results.txt', 'a')) # write or append txt file

#txtfile.writelines(f' {player1_score}') # write a line with the index and winner

#txtfile.writelines('\n') # new line

#txtfile.close() # close the file



#Plot = input("Do you want to plot the game?(y/n): ")
#if Plot == "y":
 #   plt.plot(Data1,label="Best age")
 #   plt.plot(Data2,label="Worst age")
 #   plt.xlabel("Game Number")
 #   plt.ylabel("Age")
 #   plt.title("Game Results")
 #   plt.legend()
 #       plt.show()