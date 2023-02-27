print("input 1: ")
nb1 = int(input())
print("input 2: ")
nb2 = int(input())
if nb1 < nb2:
    for i in range(nb1+1, nb2, 1):
        if nb1 == nb2:
            print("Valeurs égales")
        else:
            print (i)
else:
    for i in range(nb1-1, nb2, -1):
        if nb1 == nb2:
            print("Valeurs égales")
        else:
            print (i)