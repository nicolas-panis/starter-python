def arg(*arguments):
    myList = []
    for value in arguments:
        myList.append(value)
    myList.sort()
    print(myList)

arg(7,9,2,4,1,6)