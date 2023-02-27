def add(*arguments):
    cpt = 0
    for value in arguments:
        cpt += 1
    return cpt

print(add(1,2,3,4,1))