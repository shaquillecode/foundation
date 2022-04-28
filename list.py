'''Write a function that given a list will print out all the values in that list'''

NEW_LIST = [7, 14, 21, 28]

for element in NEW_LIST:
    print(element)

# Write a function that takes in one integer as a parameter
# AND will print out your name as many times as specified by the argument.
for i in range(7):
    print("my name is Shaq")

# - Write a function called isSorted which will be passed in a list of numbers
# - Your functions job is to determine if the list is in need of being sorted, or if it already came sorted.
# - Your function should return a boolean determining whether or not that is the case.

def is_it_sorted_or_not(my_list):
    '''Determines if the list is in need of being sorted'''
    for item in range(0, len(my_list)- 1):
        if my_list[item] > my_list[item + 1]:
            return False
    return True

RES = is_it_sorted_or_not(NEW_LIST)
print(RES)

# - Write a function that will be passed a String as a parameter.
# - Determine whether or not the String passed in is a Palindrome using booleans.
# - Returns True If your word is a palindrome(Word is the same if it is reversed).
# - Returns False If you're word is not a Palindrome.

def is_it_a_palindrome_or_not(string):
    '''Returns False If you're word is not a Palindrome'''
    if isinstance(string, str):
        og_word = list(string)

        reverse_word = og_word.copy()
        reverse_word.reverse()

        return True if (og_word == reverse_word) else False

RES = is_it_a_palindrome_or_not("RACECAR")
print(RES)
