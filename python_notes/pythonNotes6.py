#Conditionals are represented by If/Else Statements
#If/Else conditions are used to decide to do something based on something being true or being false

# x = 39873486776287364
# y = 9837423984724

#Comparison Operators 
#Examples of Comparison Operators are:
#(>, <, >=, <=, ==, !=) -> These are used to compare values 

#A simple example using comparison operators and the if/else statement: 
# if(y > x):
#     print(f"{y} is greater than {x}")
# elif(x == y):
#     print(f"{x} is equal to {y}")
# elif(y < x):
#     print(f"{y} is less than {x}")
# elif(x >= y): 
#     print(f"{x} is greater than or equal to {y}")
# elif(x <= y):
#     print(f"{x} is less than or equal to {y}")
# elif(x != y):
#     print(f"{x} does not equal {y}")
# else:
#     print("You sure you did this right?")


#Logical Operators -> and, or, not 
#These are the used to combine conditional statements, or one or more truth values

#and 
#AND: If and only if the left and the right operand are BOTH true, will the result be true.
#OR: If either the left operand, or the right operand are true, the result will be true. 
#NOT: If the value is True, it is now false. If the value was false, it is now true. 

x = 33873
y = 8764
if( not((y > x)  and  (x != y))  ):
    print("Will I see this?") #Will I see this or will it fail?
else:
    print("Im in the Else Statement")

#Coming Soon to a theater near you: 
#1. Membership Operators
#2. Identity Operators
