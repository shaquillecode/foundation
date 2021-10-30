#Activity 9.1
#Create a function that takes in integers as a parameter. Perform some operation that will compare these values and order the numbers from least to greatest. Return these values as a set in a tuple. Remember to check the data type you are returning. Your function assumes that data type. 

#Create a function
#Solution to 9.1
'''
def leastToGreat(num1, num2, num3):
    #Perform some operation that will compare these values and order the numbers from least to greatest.
    #I am declaring variables to store the values of my greatest number, smallest number, and middle number.

    greatestNum = 0
    leastNum = 0
    middleNum = 0

    #Here I am working to get my greatest number
    if(num1 > num2 and num1 > num3):
        greatestNum = num1
    elif(num2 > num1 and num2 > num3):
        greatestNum = num2
    else:
        greatestNum = num3

    #By this line I know my greatest number
    #print(greatestNum)

    #Here I am working toward getting my smallest number
    if(num1 < num2 and num1 < num3):
        leastNum = num1
    elif(num2<num1 and num2<num3):
        leastNum = num2
    else:
        leastNum = num3

    #By This point, I know BOTH my smallest and biggest are now stored or available

    #print(leastNum)

    #Here I am working to extract the middle number:

    #If greatest number is num1, and the smallest is num2, then the middle is num3
    #If the greatest number is num2, and the smallest is num1, then the middle is STILL num3
    
    if((greatestNum == num1 and leastNum == num2) or (greatestNum == num2 and leastNum == num1)):
        middleNum = num3
    
    #If the greatest number is num2, and the smallest number is num3, then the middle number is num1
    #If the greatest number is num3 and the smallest number is num2 then the middle number is num1
    elif((greatestNum == num2 and leastNum == num3) or (greatestNum == num3 and leastNum == num1)):
        middleNum = num1
    #If the greatest number is num3, and the smallest number is num1, then the middle number is num2
    #If the greatest number is num1 and the smallest is num3, then the middle is num2
    else: 
        middleNum = num2

    #By now we should have our middle number as well
    #Let's test by printing
    #print(middleNum)

    #tup = tuple((leastNum, middleNum, greatestNum))
    tup2 = (leastNum, middleNum, greatestNum)

    return tup




print(leastToGreat(90, 23, 30))
print(type(leastToGreat(90, 23, 30)))
'''

#Method2 of solving Activity 9.1
#Lisandi and other's versions, short and sweet version:
'''
def L2G(num1, num2, num3):
    li = [num1, num2, num3]
    #Because lists are mutable you don't have to re-assign after sorting it
   
    #I am inserting the sorted list into a tuple constructor to turn it into a "sorted tuple", because it just traced the sorted list.
    tup = tuple(sorted(li))
    
    #Return that tuple that traced that sorted list, so it looks like a sorted tuple
    return tup
'''

#Activity 9.2
#Write a function that takes in a temperature in F, and converts it to C
#Then write one that does the reverse...

#If we were to think about how we solve this without using Python. You would use the conversion formula and plug in the value appropriately
#You will be doing the exact same thing in your function, the only difference is, that your function is prepared to convert any number, not just one specific one. 

#Activity 9.2 Solution

def f2c(tempF):
    celcius = (tempF - 32) * 5/9
    return celcius

#print(f2c(120))

def c2f(tempC):
    f = (tempC * 9/5) + 32
    return f

#print(c2f(40))



#Activity 9.3
#Write a program that will determine whether or not a student has a high enough test average to graduate. In order to be able to graduate you must attain an average test score of 75 or more (inclusive).

# - Your function will take a list with exactly 5 Integer values (might be generated at random, but it will ALWAYS be a list with exactly 5 Integers. Assume that there were 5 exams throughout the academic year.)

# - These Integers in the list represent exam grades throughout the year. Your function should calculate the average of the test scores and return whether or not this student will be able to graduate

# (Keep the integers between 1 -100 for test grades sake)

# - Think about the data type that you will be returning.

#Activity 9.3 Solution:
'''
def canGraduate(dataset):
    # I know that if I have EXACTLY 5 integers in my list everytime, then the index will always be 0, 1, 2, 3, 4.
    #To get the first exam grade
    firstExamScore = dataset[0]
    
    #To get the second exam grade
    secondExamScore = dataset[1]

    #To get the third exam grade
    thirdExamScore = dataset[2]

    #To get the fourth exam grade
    fourthExamGrade = dataset[3]

    #To get the final/fifth exam grade
    fifthExamGrade = dataset[4]

    #By here, I have a variable containing my 5 grades...
    #How do I get their average?

    #To get the average of any list of numbers, you ADD all the numbers together, and divide by the total number of elements. 

    #In this case, I have 5 elements, so I need to add all the exam scores together, and divide by 5

    sumOfExams = firstExamScore + secondExamScore + thirdExamScore + fourthExamGrade +fifthExamGrade

    average = sumOfExams / len(dataset)
    print(f"Your average is {average}")

    #Lastly, now that I know the average of the students grades, I must see if they scored higher than 75, if yes, then return true because this student can graduate
    #In any other case, they failed

    if(average >= 75):
        return True
    else: 
        return False

    
print(canGraduate([40, 75, 90, 65, 80]))
'''


#Activity 9.4
# 	Write a function that takes in a temperature as a parameter in Celsius and will return the following

# - If the temperature is 32 degrees Fahrenheit or less, return a message indicating something like -> its winter season.
# - If the temperature is between 33 degrees Fahrenheit and 55 degrees Fahrenheit, return a message indicating something like -> its fall season.
# - If the temperature is between 56 degrees Fahrenheit and 75 degrees Fahrenheit, return a message indicating something like -> its spring season.
# - If all the previous conditions fail, return a message to the console indicating something indicating something like -> Its summer season

#input(x)
#Literally takes input from a user. You can pass in an argument optionally to the input() method
#What pass you in is the message you would like to be displayed for your input
#What the user sees

def solution(tempC):
    # - 1. If the temperature is 32 degrees Fahrenheit or less, return a message indicating something like -> its winter season.
    #First thing you need to do is convert

    #One way to convert : Referencing Activity 9.2 solution function
    # f = c2f(tempC)
    
    #Another way to convert : Literally throwing the conversion formula directly
    f = (tempC * 9/5) + 32
    #Testing that it works...
    #print(f"F is: {f}")
    if(f <= 32.0):
        return "It's winter season"
    elif(f > 32.0 and f <= 55.0):
        return "It's fall season"
    elif(f > 56.0 and f <= 75.0):
        return "It's spring season"
    elif(f > 75.0):
        return "It's summer season"
    else:
        return "The apocalypse clearly is behind you..."



print(solution(20))















