print("Entrer votre texte")
fichier = open("output.txt", "w")
fichier.write(input())
fichier.close()

fichier = open("output.txt", "r")
print (fichier.read())
fichier.close()