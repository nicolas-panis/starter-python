pts = 0
myList = []
myListPts = []
with open('dico_france.txt','r') as file:
   
    # reading each line    
    for line in file:
        str = "argent"
   
        # reading each word        
        for word in line.split():
            pts = 0
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
                            if str[j] == "a" or str[j] == "e" or str[j] == "i" or str[j] == "n" or str[j] == "o" or str[j] == "r" or str[j] == "s" or str[j] == "t" or str[j] == "u" or str[j] == "l":
                                pts = pts + 1
                            elif str[j] == "d" or str[j] == "g" or str[j] == "m":
                                pts = pts + 2
                            elif str[j] == "b" or str[j] == "c" or str[j] == "p":
                                pts = pts + 3
                            elif str[j] == "f" or str[j] == "h" or str[j] == "v":
                                pts = pts + 4   
                            elif str[j] == "j" or str[j] == "q":
                                pts = pts + 8
                            elif str[j] == "k" or str[j] == "w" or str[j] == "x" or str[j] == "y" or str[j] == "z":
                                pts = pts + 10
                            str = str.replace(str[j],"0")
                            
                
                if cpt == len(str):
                    if myListPts == []:
                        myListPts.append(pts)
                        myList.append(word)
                    elif min(myListPts) < pts:
                        myListPts.append(pts)
                        myList.append(word)
                    else:
                        myListPts.insert(0, pts)
                        myList.insert(0,word)
                    print(word)
    print(myList)
    print(myListPts)