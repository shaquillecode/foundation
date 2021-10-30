#Warm Up:
#Write the prompt here so I don't have to do twice the work

#Write your solution here:
def sleep_in(weekday, vacation):
    #We sleep in IF it is NOT a weekday OR we ARE on vacation
    if(not weekday):
        return True
    elif(vacation):
        return True
    else: 
        return False


#Warm Up 2: 
#write the prompt 

#Write the solution here:
def monkey_trouble(a_smile, b_smile):
    #We are in trouble IF they are both smiling OR IF neither are smiling
    if(a_smile and b_smile):
        return True
    elif(not a_smile and not b_smile):
        return True
    else:
        return False

# print(monkey_trouble(True, False))

# def monkey_trouble(a_smile, b_smile):
#     if(a_smile == b_smile):
#         return True
#     else:
#         return False

# print(monkey_trouble(False, False))

# def monkey_trouble(a_smile, b_smile):
#     return a_smile == b_smile

# print(monkey_trouble(False, False))

#Warm Up 3:

#Solution: 
#GIVEN TWO INTEGER VALUES RETURN their SUM. IF they are the SAME number, RETURN TWICE their SUM. 

def sum_double(a, b):
    if(a == b):
        return (a + b) * 2
    else:
        return a + b

# print(sum_double(1,2))
# print(sum_double(3,2))
# print(sum_double(2,2))

#Warm Up 4

#Solution: 
#Prompt: GIVEN AN INT N, RETURN the ABSOLUTE DIFFERENCE BETWEEN n AND 21, except RETURN DOUBLE absolute difference IF n IS OVER 21.

# def diff21(n):
#     if(n > 21):
#         num = abs(n - 21)
#         return num * 2
#     else:
#         return abs(n - 21)

# def diff21(n):
#     if n <= 21: 
#         return 21 - n
#     else: 
#         return ((21 - n) * 2) * -1

# print(diff21(19)) #Should return 2
# print(diff21(10)) #Should return 11
# print(diff21(21)) #Should return 0

# def diff21(n):
#     if(n <= 21):
#         return (abs(n-21))
#     elif(n > 21):
#         return (abs(n-21) * 2)

# print(diff21(21))


#Warm Up 5: 

#Prompt: 
#We have a loud talking parrot. The "hour" PARAMETER is the current hour time in the range of 0..23. We are in trouble IF the parrot is talking AND the hour is BEFORE 7 or AFTER 20. RETURN True IF we are in Trouble. 

#Solution: 
def parrot_trouble(talking, hour):
    if(talking and (hour < 7 or hour > 20)):
        return True
    else: 
        return False

print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 7)) #True
print(parrot_trouble(False, 6)) #False