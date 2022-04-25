'''This is a function that returns to me the average value of the curved exam grades and original grades.'''
import statistics

def curved_exam_grades(data1):
    STDEV = statistics.stdev(data1)
    for i,data in enumerate(data1):
        if data1[i] + int(STDEV) > 100:
            data1[i] = 100
        else:
            data1[i] += int(STDEV)
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
