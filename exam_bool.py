'''This function that given a list of numbers, will return to me a list of booleans'''
# 2. Your function will take in a list of numbers, and if the values are less than 55 exclusive,
# then you substitute that list item with a "False".
# For all others, substitute the current list item value to "True".


def numbtobool(dataset):
    for i,data in enumerate(dataset):
        if dataset[i] < 55:
            dataset[i] = False
        else:
            dataset[i] = True

    print(type(dataset))
    return dataset

solution = numbtobool([99, 62, 96, 100, 85, 98, 81, 91, 54, 84])

print(solution)
