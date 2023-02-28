def arg(*arguments):
    myList = []
    for value in arguments:
        myList.append(value)
    for value in myList:
        if value % 2 == 0:
            print(value)

arg(1,2,3,4,5,6)