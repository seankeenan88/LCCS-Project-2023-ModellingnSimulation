from random import randint

print("Dice simulation  and analysis program")
results = []     # initiating the variables
frequencies = [0,0,0,0,0,0]

#loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results
   
    #start to build up a list of frequencies for each value thrown
    if throw_result == 1:
        frequencies[0] = frequencies[0] + 1
    elif throw_result == 2:
        frequencies[1] = frequencies[1] + 1
       
print()
print("Results:", results)
print("Frequencies: ", frequencies)