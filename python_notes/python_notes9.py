"""Warm up Exercises"""
def sleep_in(weekday, vacation):
    ''' We sleep in IF it is NOT a weekday OR we ARE on vacation'''
    if not weekday or vacation:
        return True
    return False


def monkey_trouble(a_smile, b_smile):
    '''We are in trouble IF they are both smiling OR IF neither are smiling'''
    if a_smile and b_smile or not a_smile and not b_smile :
        return True
    return False

print(monkey_trouble(True, False))



def sum_double(num1, num2):
    '''GIVEN TWO INTEGER VALUES RETURN their SUM.
    IF they are the SAME number, RETURN TWICE their SUM.'''
    if num1 == num2:
        return (num1 + num2) * 2
    return num1 + num2

# print(sum_double(1,2))
# print(sum_double(3,2))
# print(sum_double(2,2))


def diff21(num):
    '''GIVEN AN INT N, RETURN the ABSOLUTE DIFFERENCE BETWEEN n AND 21,
    except RETURN DOUBLE absolute difference IF n IS OVER 21.'''

    if num <= 21:
        return 21 - num
    return ((21 - num) * 2) * -1

print(diff21(19)) #Should return 2
print(diff21(10)) #Should return 11
print(diff21(21)) #Should return 0



#Prompt:
#We have a loud Talking parrot.
# The "hour" PARAMETER is the current hour time in the range of 0..23.
#  We are in trouble IF the parrot is talking AND the hour is BEFORE 7 or AFTER 20.
# RETURN True IF we are in Trouble.

#Solution:
def parrot_trouble(talking, hour):
    '''Talking parrot'''
    if(talking and (hour < 7 or hour > 20)):
        return True
    return False

print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 7)) #True
print(parrot_trouble(False, 6)) #False
