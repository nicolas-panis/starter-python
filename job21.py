def mySort(myList):
    sortedList = []
    while myList:
        sortedList.append(min(myList))
        myList.remove(min(myList))
    return sortedList

def myDisplay(myList):
    for value in myList:
        print(value, end = " ")

myList = [1,9,4,7,3]
myList2 = [1,9,4,7,3]
print(mySort(myList))
myDisplay(myList2)