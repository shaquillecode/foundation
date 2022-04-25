'''Build a Function that takes a list and tells you how many people passed the class'''

# I would like you to do this with a given list of grades

# Given a list of integers representing exam grades (whether they are curved or not), print a message telling me how many people passed or failed the class based on the fact that 55+ is passing and below is failing.

# Call this Function "Class report"
import random

def create_randum_list(x):
    li = []
    for i in range(x):
        randnum = random.randrange(0, 101)
        li.append(randnum)
    print(li)
    return li


def class_report(dataset = [99, 62, 96, 100, 85, 98, 81, 91, 54, 84]):
    passing = 0
    failing = 0

    for i,data in enumerate(dataset):
        if dataset[i] < 55:
            failing += 1
        else:
            passing += 1

    sentence = (f"You have {passing} passing students and {failing} failing students")

    print(sentence)
    return sentence

class_report(create_randum_list(10))
