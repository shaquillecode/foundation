# Now I would like to have a function that takes a list and tells me how many people passed the class

# I would like you to do this with a given list of grades

# Given a list of integers representing exam grades (whether they are curved or not), print a message telling me how many people passed or failed the class based on the fact that 55+ is passing and below is failing.

# Call this Function "Class report"


import random

def createrandumlist(x):
    li = []
    for i in range(x):
        randnum = random.randrange(0, 101)
        li.append(randnum)
        print(li)

def class_report(dataset = [99, 62, 96, 100, 85, 98, 81, 91, 54, 84]):
    passing = 0
    failing = 0

    for i in range(len(dataset)):
        if(dataset[i]< 55):
            failing += 1
        else:
            passing += 1

    sentence = (f"You have {passing} passing students and {failing} failing students")

    print(sentence)
    return sentence
createrandumlist(10)
class_report([45, 66, 77, 33, 88])