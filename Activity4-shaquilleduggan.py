#Variable Name = Variable Value

fname = "Shaquille"
lname = "Duggan"
favcolor = "black"
meal = "fish"

# fstring
print(f"My name is {fname} My last name is {lname} My favorite color is {favcolor} My favorite food is {meal}")

#Concatenation
firstname = "Shaquille"
lastname = "Duggan"
favcolor2 = "green"
meal2 = "chocolate"

fullname = firstname +" "+ lastname
print(fullname)

# or
fullname = firstname + lastname
print(fullname)

# or
fullname = f"{firstname} {lastname}"
print(fullname)

# Argument by Position

favcolor2 = "green"
lastname = " Duggan"
meal2 = "chocolate"
firstname ="Shaquille"

sentence = "My first name is {0} and My last name is {1} and My favorite color is {2} and My favorite food is {3}".format(firstname, lastname, favcolor2, meal2)
print(sentence)

#Argument by name

sentence7 = "My first name is {firstname} and My last name is {lastname} and My favorite color is {favcolor2} and My favorite food is {meal2}".format(firstname = "shaquille", lastname = "duggan", favcolor2 = "green", meal2 = "hot chocolate")
print(sentence7)