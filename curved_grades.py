import statistics 
# Now I would like you to write a function that returns to me the average value of the curved exam grades and original grades.

def curved_exam_grades(data1):
    stDev = statistics.stdev(data1)
    for i in range(len(data1)):
        if(data1[i] + int(stDev) > 100):
            data1[i] = 100
        else:
            data1[i] += int(stDev)
    return data1

def averagegrades(data2):
    meanOfGrades = statistics.mean(data2)
    return meanOfGrades

def averagecurvedgrades(data3):
    meanOfCurved = statistics.mean(data3)
    return meanOfCurved

print([99, 62, 96, 100, 85, 98, 81, 91, 54, 84])
print(curved_exam_grades([99, 62, 96, 100, 85, 98, 81, 91, 54, 84]))

print(averagegrades([99, 62, 96, 100, 85, 98, 81, 91, 54, 84]))
print(averagecurvedgrades(curved_exam_grades([99, 62, 96, 100, 85, 98, 81, 91, 54, 84])))