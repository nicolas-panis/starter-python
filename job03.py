print("Bonjour, quel âge as-tu ?") 
age = input()
if int(age) < 18:
    print("Tu es mineur")
else:
    print("Tu es majeur")