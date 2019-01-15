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

