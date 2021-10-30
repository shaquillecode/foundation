#Find the largest number between 3 numbers

#Example 1
# 9, 3, 4 -> 9
#If 9 is greater than 3, and if 9 is greater than 4 -> The largest number is 9, I'm safe to return that 9
#Tranlate to Code: 
#If num1 is greater than num2, and if num1 is greater than num3 -> Then the largest number is num1, it's 
#safe to return num1

#Example 2
#7, 10, 3 -> 10
#If 7 is greater than 10, and 7 is greater than 3 -> The largest is 7
#Elif 10 is greater than 7, and 10 is greater than 3 -> The largest is 10
#Else 3 is the largest
#Translate to Code:
#If num1 is greater than num2, and if num1 is greater than num3 -> Then the largest number is num1, it's 
#safe to return num1
#Elif num2 is greater than num1 and if num2 is greater than num3 -> num2 is the greatest
#Else its num3 -> it's safe to return num3

#Example 3
#4, 5, 6 -> 6
#If 4 is greater than 5 and 4 is greater than 6 -> If yes, 4 is largest
#Elif 5 is greater than 4 and 5 is greater than 6 -> The largest number is 5
#Else it's 6
#Translate to Code:
#If num1 is greater than num2, and if num1 is greater than num3 -> Then the largest number is num1, it's 
#safe to return num1
#Elif num2 is greater than num1 and if num2 is greater than num3 -> num2 is the greatest
#Else its num3

# def largestNumber(num1, num2, num3):
    #Get the largest one
    #Translate to Code:
    #If num1 is greater than num2, and if num1 is greater than num3 -> Then the largest number is num1, it's 
    #safe to return num1
    #Elif num2 is greater than num1 and if num2 is greater than num3 -> num2 is the greatest
    #Else its num3
#     if(num1 > num2 and num1 > num3):
#         return num1
#     elif(num2 > num1 and num2 > num3):
#         return num2
#     else:
#         return "The greatest number is: " + str(num3)


# # print("The greatest number is: \n" + str(largestNumber(45 ,130, 9)))
# print(largestNumber(4, 6, 90))

#The input is not usually your problem, it's something the user gives you
#The outcomes is not in your control, it's something the process spits  out
#Your job, is to develop that process
#Input Process Output, this is a thing in programming. Your job is the middle part. 

#Simulate a traffic light using Conditionals in Python
#Let's think about traffic lights
#Objects have properties, and behavior. Properties get put in variables. Behaviors
#are references to functionaility
#Lets think: 
#What Properties does a Traffic Light have: (The most obvious ones):
#They have:
#1. Green Light
#2. Red Light
#3. Yellow Light

#What behaviors do these properties exhibit?:
#1. Green light means go
#2  Red light means stop
#3  Yellow light means slow down/proceed with caution

#So I know based on my properties and my behaviors, that I want to simulate a traffic
#light that has a green light, yellow light and red light
#I also know that their behaviors are if green -> go, if yellow -> slow, if red -> stop

def trafficLightSimulation():
    #First thing I want to do is assign the properties of the traffic into variables.
    green = False
    yellow = False
    red = False

    #Since I know that these specific properties have a specific behavior, then I know
    #That in order to perform its function, it must be true that it is active.
    #How can I represent active and inactive? Sounds like 0 and 1? Sounds like True of False?
    #Sounds like a Boolean

    #if green -> go
    if(green):
        print("You are good to go")
    elif(yellow):
        print("Slow down, tiger")
    elif(red): 
        print("Stop")
    else:
        print("Are you sure that's a traffic light?")



trafficLightSimulation()