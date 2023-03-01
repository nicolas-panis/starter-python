cpt = 0
with open('dico_france.txt','r') as file:
   
    # reading each line    
    for line in file:
        str = "argent"
   
        # reading each word        
        for word in line.split():
            cpt = 0
            # displaying the words           
            # print(word) 
            # if str in word:
            #     print(word)
            if len(word) == len(str):
                for i in range(len(word)):
                    for j in range(len(str)):
                        if str[j] == word[i]:
                            cpt = cpt + 1
                            str = str.replace(str[j],"0")
                            
                
                if cpt == len(str):
                    print(word)