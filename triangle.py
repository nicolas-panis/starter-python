print("Entrer une hauteur: ", end='')
hauteur = int(input())
hauteurglobal = hauteur
i = 0
while i < hauteurglobal:
    j = 0
    nbsp = i
    while j < hauteur - 1:
        print(' ', end = '')
        j = j + 1
    hauteur = hauteur - 1
    print("/", end = "")
    if hauteur == 0:
        nbsp = nbsp * 2
        while nbsp > 0:
            print('_', end = "")
            nbsp = nbsp - 1
    elif nbsp > 0:
        nbsp = nbsp * 2
        while nbsp > 0:
            print(' ', end = "")
            nbsp = nbsp - 1
    print("\\")
    i = i + 1