str = input("Rentrer une chaîne de caractères: ")
def myUpper(str):
    new_string=""
    for i in str:
        if ord(i) >=97 and ord(i)< 123:
            new_string+=chr(ord(i)-32)
        else:
            new_string+=i
    return new_string

def myLower(str):
    new_string=""
    for i in str:
        if ord(i) >=65 and ord(i)< 90:
            new_string+=chr(ord(i)+32)
        else:
            new_string+=i
    return new_string


def myTitle(str):
    new_string = ""
    for i in range(len(str)):
        if i == 0:
            if ord(str[i]) >= 97 and ord(str[i]) < 123:
                new_string+=chr(ord(str[i])-32)
        elif str[i-1] == " ":
            if ord(str[i]) >=97 and ord(str[i]) < 123:
                new_string+=chr(ord(str[i])-32)
        else:
            new_string+= str[i]
    return new_string

def myClean(str):
    new_string = ""
    for i in range(len(str)):
        if i == 0:
            if str[i] == " ":
                pass
            else:
                new_string+= str[i]
        elif str[i-1] == " " and str[i] == " ":
            pass
        else: 
            new_string+= str[i]
    return new_string
str = "argent"
str = str.replace("a","o")
print(str)
fc = input("Choissiez la fonction désirée entre upper, lower, title ou clean: ")

if fc == "upper":
    print(myUpper(str))
elif fc == "lower":
    print(myLower(str))
elif fc == "title":
    print(myTitle(str))
elif fc == "clean":
    print(myClean(str))