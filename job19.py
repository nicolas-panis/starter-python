def arg(*arguments):
    myList = []
    for value in arguments:
        myList.append(value)
    
    sortedList = []
    while myList:
        sortedList.append(min(myList))
        myList.remove(min(myList))
    print(sortedList)

arg(7,9,2,4,1,6)