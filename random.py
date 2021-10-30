# Write a function that will take in an integer as a parameter, and create a list of the size passed in as an argument.

# Populate that list with random numbers between 0 - 1023.

# You are to use the getrandbits() method from the random module to populate your list.

import random 

def createRandomList(num):
    li = []
    randnum = random.getrandbits(10)
    
    for i in range(num):
        li.append(randnum)
    print(li)

createRandomList(5)


# I want you to create a function that will Generate a Random List.

# But I want the values passed in to range between 20 - 40 specifically do not include the 40.
import random

def createRandomRange(num):
    li = []
    RandRange = random.randrange(20,40)
    
    for i in range(num):
        li.append(RandRange)
    print(li)
    return li

createRandomRange(5)  

# Create a function that plays Rock, Paper, Scissors with you.
# - You ask the user for INPUT
# - Remeber the rules:
# Paper Covers Rock
# Rock Beats Scissors
# Scissors Cut Paper

# # HINT

# - How can I make a RANDOM Choice between those... Then may be compare that computers choice to the user input....
# - Since the computers choice can be 3 different values, what can you use to store a sequence of values
# - 3 values is the 3 values, do you know a way to generate a random number between 0 and 3? Will it be inclusive of 3


import random

def rockpaperscissors():
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    shaq = [{rock},{paper}, {scissors}]
    computeroptions = [{rock},{paper}, {scissors}]
    computerguess = random.choice(computeroptions)
    shaqguess = random.choice(shaq)

    if(shaqguess == {rock} and computerguess == {paper}):
        print(f"You lose!, {computerguess} beats {shaqguess}")
    elif(shaqguess == {paper} and computerguess == {scissors}):
        print(f"You lose!, {computerguess} beats {shaqguess}")
    elif(shaqguess == {scissors} and computerguess == {rock}):
        print(f"You lose!, {computerguess} beats {shaqguess}")
    elif(shaqguess == computerguess):
        print(" You picked the same thing, start over.")
    else:
        print(f"You win!, {shaqguess} beats {computerguess}")
        

solution = rockpaperscissors()

print(solution)