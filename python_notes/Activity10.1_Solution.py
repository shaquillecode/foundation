#Activity 10.1
'''
Create a function that is given a list of numbers as a parameter.

Sort this list in any way other than using methods from the List object. That means no calling the “.sort()” or “sorted()” method.

CAN NOT USE the .sort() OR .sorted()
'''

#Solution


sampleData = [-5, -23, 5, 0, 23, -6, 23, 67]

#Step 1: Create the function name and pass a list as an argument
def sortList(dataset = [-5, -23, 5, 0, 23, -6, 23, 67]):

#Step 1.5: Create a new list object to pass in values to later (This will cost space...)
    li = []
#Step 2: Loop through the indices with 0 as the start point
    for i in range(0, len(dataset)):
#Step 3: Loop through the indices again with a nested loop BUT start at 1 or better said: (i + 1)
        for j in range(i+1, len(dataset)):
#Step 4: Compare if the value at i (0) and the next j(1) is greater or not. If i is smaller than j, perform the swap
            if(dataset[i] > dataset[j]):
                #What is the swap logic:
                dataset[i], dataset[j] = dataset[j], dataset[i]
                # temp = dataset[i]
                # dataset[i] = dataset[j]
                # dataset[j] = temp
    print(dataset)
    return dataset

sortList(sampleData)



#Step 5: #Perform the swap logic special in Python if Step 4 is True

#Step 6: When your loop finishes running, just return the list.


#Solution

'''
sampleData = [-5, -23, 5, 0, 23, -6, 23, 67]
def sortList(dataset):
    
    new_list = []

    while dataset:
        minimum = dataset[0]  # arbitrary number in list 
        for x in dataset: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        dataset.remove(minimum)    

    print(new_list)

sortList(sampleData)
'''

'''
def sortList2(dataset):

    #Loop through the list with indices of 0 as a start
    for i in range(len(dataset)):
        #Create a nested loop that will start at index 1
        for j in range(i + 1, len(dataset)):
            #Compare if the value at i (0) and the next j(1) is greater or not. If i is smaller than j, perform the swap
            if dataset[i] > dataset[j]:
                #This is the swap logic special in Python
                dataset[i], dataset[j] = dataset[j], dataset[i]

    print(dataset)

sortList2(sampleData)
'''
