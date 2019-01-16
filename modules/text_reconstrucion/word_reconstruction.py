def textReconstruction(letterList,coordsList):

   
    finalText = []
    wordText = []
    wordText.append(letterList[0])
    #print(coordsList)

    prag_cuvant = 90
    prag_rand=70
    nr=0
    for l in range(1, len(coordsList)):

        #y1, x1, y2, x2 = coordsList[l][0], coordsList[l][1], coordsList[l][2], coordsList[l][3]
        x1, y1, x2, y2 = coordsList[l][0], coordsList[l][1], coordsList[l][2], coordsList[l][3]
        if abs(y2 - coordsList[l - 1][1]) > prag_rand:
            nr += 1
            
            if letterList[l - 1] != "-":
                aux = []
                aux = wordText.copy()
                finalText.append(aux)
                wordText.clear()
                wordText.append(letterList[l])

        elif abs(x2- coordsList[l - 1][0]) > prag_cuvant:
            #print("cuvant nou")
            aux = []
            aux = wordText.copy()
            finalText.append(aux)
            wordText.clear()
            wordText.append(letterList[l])
        else:
            if letterList[l]!="-":
                wordText.append(letterList[l])
    

    return finalText

def on_same_line(cord1,cord2):

    if cord1[3] < cord2[1] and cord1[2]>cord2[0]:
        return False
    return True


def text_reconstruction(coords,letters):

    index = 0
    text = []
    line = []

    for (x1,y1,x2,y2) in coords:

        if  not line or on_same_line(line[-1][0],(x1,y1,x2,y2)):
            line.append(((x1,y1,x2,y2),letters[index]))

        else:
            text.append(list(line))
            line = [((x1,y1,x2,y2),letters[index])]
        index +=1    
    text.append(list(line))

    words_list = []

    for line in text:
        mean = 0
        summ = 0
        for index  in range (0,len(line)-1):
            space = abs(line[index][0][2] - line[index+1][0][0])
            summ+=space

        mean = summ / len(line)-1
        word = [list(line[0][0]),line[0][1]]
        for index in range(1,len(line)):
            space = abs(line[index-1][0][2] - line[index][0][0])
            
            if space < mean*2:
                word[1] = word[1] + line[index][1]
                if line[index][0][1]< word[0][1]:
                    word[0][1] = line[index][0][1]
                if line[index][0][3]> word[0][3]:
                    word[0][3] = line[index][0][3]
                word[0][2] = line[index][0][2]
            else:
                
                words_list.append(tuple(word))
                word = [list(line[index][0]),line[index][1]]

        words_list.append(tuple(word))
        
    return words_list
        
        

