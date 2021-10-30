#Below here, I am creating an empty list, and I am demonstrating that you can make it with just 
#Empty Square Brackets. 
# myList = []
# print(myList)

#When declaring an empty Tuple. You cannot do it the same way as with Lists
#You must include a trailing comma at the end of the first element and before the closing parentheses
# myTuple = ("Tank",) -> IS a Tuple
# myTuple2 = ("Tank") -> IS NOT a Tuple


myTuple = ("Tank", "Tone", "Top", "Jim", "Acorns", "Baseball")
myTuple2 = (4, 3, 6, 7, 1)
# print(myTuple,type(myTuple))
# type(myTuple) -> Returns the Object Type of that Value


#To delete a tuple, use the keyword "del":
# del myTuple

#To print the minimum value item in your Tuple...
# print(min(myTuple))

#First Try:
#Tuple.Method()
#Example: Tuple.min() -> Doesn't work

#If that does not work, then try:
#Method(Tuple) 
#Example: min(Tuple) -> Does work

#Intro to Dictionaries in Python:
#A dictionary is a collection which is unordered, changeable, and indexed. There are no duplicate memebers
#allowed. More specifically and most definitely no duplicate keys allowed. 

#Creating an Empty Dictionary Version 1
myDictionary = {}
# print(type(myDictionary))

#Creating a Dictionary with Items Version 1: 
myDictionary = {"First_Name": "Elvis", "Last_Name": "Garcia", "age": 27}
print(myDictionary)
#Creating an Empty Dictionary Version 2: 
#Referencing the Constructor Method of the Dictionary Object Class in Python
# myDictionary3 = dict()
# print(type(myDictionary3))

#Creating a dictionary with Values Version 2: 
myDictionary2 = dict(First_Name = "Elvis", Last_Name = "Garcia", Age = 27)
print(myDictionary2)

#You DO NOT look up values in dictionary with Integers Indexes UNLESS the integer index IS the key.
#In which case, you must reference that specific Integer (no real sequence)

#Access a Value
# print(myDictionary2["First_Name"]) #-> "Elvis"
# print(myDictionary2["Last_Name"]) #-> "Garcia"
# print(type(myDictionary2["Age"])) #-> 27
#type(Object) -> The Type of the Object

#Let's not forget, that dictionaries are mutable data types in Python. Part of the Collection Object. 
#This means that we can operate CRUD on it. So let's start with adding an item to the dictionary.
#How will I actually create the syntax for adding one more key-value pair to my already existing 
#Dictionary?
myDictionary2["Job_Title"] = "Python Instructor"
print(myDictionary2)
#How can I make a new key in my dictionary called "Favorite_Food" and assign it a value of "Chinese Food"
myDictionary2["Favorite_Food"] = "Chinese Food"
print(myDictionary2)

#Getting Rid of Items in your Dictionary is as simple as: 
# myDictionary2.clear()
# print(myDictionary2)

#How do I get the keys from a given or already existing Dictionary?
#You use the .key() method on the Dictionary Object in order to get a tuple of your Keys.
#Because Strings and Tuples are immutable, the list of keys will be displayed as a Tuple.
print(myDictionary2.keys())

#How do I get the values from a gvien or already existing Dictionary?
print(myDictionary2.values())
#If given an arbitrary dictionary. The .items() method is better for getting BOTH the keys and the value, 
#seperated by commas
print(myDictionary2.items())

#This is useful for problems that require you to submit both an original copy of the dictionary, 
#and a copy that is modified.
#The .copy() method is what you use to create a copy of your dictionary
# newDictionary = myDictionary2.copy()
# print(newDictionary)

#Getting rid of single items in your dictionary Version 1:
#You use the .pop() method and specify as an arguement the KEY that you would like to get rid of.
#Its corresponsing value is automatically deleted as well. 
# print(myDictionary2)
# myDictionary2.pop("Last_Name")
# print(myDictionary2)

#Version 2 of deleting a single item from a dictionary
# del (myDictionary2["Age"])
# print(myDictionary2)