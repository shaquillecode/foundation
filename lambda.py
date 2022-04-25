'''Lamda'''

example = [2, 4, 6, 20, 100]

def cubed(num):
    '''Cubed Function'''
    return num ** 3

cubedFunction = list(map(cubed, example))

cubedLambda = list(map(lambda x: x**3, example))

print(cubedFunction)
print(cubedLambda)
