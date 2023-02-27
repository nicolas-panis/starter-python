print("Largeur: ")
largeur = int(input())
print("Hauteur: ")
hauteur = int(input())
i = 0
while i < hauteur:
    print("|", end='')
    j = 0
    if i == 0:
        j = 0
        while j < largeur:
            print("-", end='')
            j = j + 1
    elif i == hauteur - 1:
        j = 0
        while j < largeur:
            print("-", end='')
            j = j + 1
    else:
        j = 0
        while j < largeur:
            print(" ", end='')
            j = j + 1
    print("|")
    i = i + 1

