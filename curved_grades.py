# #Activity 11.2:

# Now I would like you to write a function that returns to me the average value of the curved exam grades and original grades.

import statistics 

grades = [99, 62, 96, 100, 85, 98, 81, 91, 54, 84]

def curved_exam_grades(data1):
    stDev = statistics.stdev(data1)
    for i in range(len(data1)):
        if(data1[i] + int(stDev) > 100):
            data1[i] = 100
        else:
            data1[i] += int(stDev)
    return data1

def averagegrades(dataset):
    gradelist = [99, 62, 96, 100, 85, 98, 81, 91, 54, 84]
    meanofgrades = statistics.mean(gradelist)
    return meanofgrades

def averagecurvedgrades(dataset):
    curvedgradelist = [100, 77, 100, 100, 100, 100, 96, 100, 69, 99]
    meanofCurved = statistics.mean(curvedgradelist)
    return meanofCurved

print(grades)
print(curved_exam_grades(grades))

print(averagegrades(grades))
print(averagecurvedgrades(grades))