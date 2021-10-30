# - In this file I want you to create a Dictionary named car.
# - The car has a brand, a model, and year.
# - This dictionary should describe the following object:
# -1964 Ford Mustang
# - Use the “get” method of a dictionary to print the value of the “model” of the car.
# - Submit your file as an assignment on populi.


#  brand = Ford
#  model = Mustang
#  year = 1964

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

print(car)

print(type(car))

car2 = car.copy()

print(car2)

grabit = car.get("model")

print(grabit)

items = car.items()

print(items)
