fichier = open("domains.xml", "r")
text = fichier.read()
fichier.close()

textsplit = text.split('"')

cpt = 0
for i in textsplit:
    if i == "id":
        cpt = cpt + 1
print(cpt)