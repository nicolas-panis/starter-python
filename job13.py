cpt = 0
taillemot = int(input("Entrer la taille du mot: "))
with open('data.txt','r') as file:
   
    # reading each line    
    for line in file:
   
        # reading each word        
        for word in line.split():
   
            # displaying the words           
            # print(word)
            if len(word) == taillemot:
                cpt = cpt + 1     
print(cpt)