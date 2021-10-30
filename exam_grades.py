# Your task if you choose to take it, is to write a function that is given a list of exam grades represented by Numbers/Integers; Calcualate the standard deviation of the exam grades represented by some numeric data set.

# What I want is for you to return to me a list with all of the exam values updated by itself PLUS the standard deviation.

# I want you to include something that states that if adding the standard deviation to the current exam score goes above 100, then I will simply pass that 100 right back into the list at that particular index, and for everything else, just add the standard deviation normally to the current exam score.

import random
import statistics

def stat1(n, x, y):
    l0 = []
    for i in range (0, n):
        random1 = random.randrange(x, y)
        l0.append(random1)
    dev = int(statistics.stdev(l0))
    l1 = [i + dev for i in l0]
    l2 = []
    for i in l1:
        if i >= 101:
            i = 100
        l2.append(i)
    l1 = l2        
    return l2

print(stat1(10, 30, 90))   