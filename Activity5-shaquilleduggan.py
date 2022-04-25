'''Tuples and Lists'''

#a.

tuple0 = ("Ether", 33324, "ADA", 2.06, "Bitc", 1058)

print(tuple0)

#b.

tuple1 = ("Ether", 33324, "ADA", ["one", "way"], "Bitc", True)

print(len(tuple1))
print(len(tuple1)- 1)

#c.

tuple2 = ("Ether", "ADA", "Bitc", "algo", True)

FTF = tuple2[3]

FTB = tuple2[-4]

print(FTF)

print(FTB)

#d.

tuple3 = ("Ether", "ADA", "Bitc")

print(len(tuple3))


myTuple0 = ("shaquille", "duggan", "fell", 0, 12)

mylist = ["shaquille"]

print(mylist)

print(type(myTuple0))

mylist[0] = "Bitcoin"

print (mylist)

# Tuples are immutable
# myTuple1 = ("Elon messed up", "duggan", "fell", 0, 12)

# myTuple1[1] = "Ethereum"

# print(myTuple1)-->Error message will appear in Terminal

# CRUD -Create Read Update Delete

myTuple2 = ("", "", "", "", True, "duggan", "slipped at", 12, "noon")

count_amount = myTuple2.count("")

print(count_amount)
print(myTuple2)

myTuple3= ("shaquille", "duggan", "fell", 0, 12, False)

solution = all(myTuple3)

print(solution)

mylist2 = ["ether", "ripple", 1.20, "algo", .65]

myTuple4 = tuple(mylist2)

print(type(myTuple4))
print(myTuple4)
