def textReconstruction(letterList,file,prag_cuvant,prag_rand):

    fd = open(file, "r")
    index = fd.readlines()
    list_of_coords = []
    for i in range(len(index)):
        list_of_coords.append(index[i].lstrip('(').rstrip(')\n').split(','))
    for i in range(len(list_of_coords)):
        for j in range(4):
            list_of_coords[i][j]=int(list_of_coords[i][j])
        list_of_coords[i]=tuple(list_of_coords[i])
        print(list_of_coords[i])


    finalText=[]
    lineText=[]
    wordText=[]
    wordText.append(letterList[0])

    for l in range(1,len(list_of_coords)):
        x1, y1, x2, y2 = list_of_coords[l][3], list_of_coords[l][0], list_of_coords[l][1], list_of_coords[l][2]

        if x1-list_of_coords[l-1][1]>prag_cuvant:
            print("cuvant nou")
            lineText.append(wordText)
            wordText.clear()
            wordText.append(letterList[l])


        elif y1-list_of_coords[l-1][2]>prag_rand:
            print("rand nou")
            finalText.append(lineText)
            lineText.clear()
            wordText.clear()
            wordText.append(letterList[l])


        else :
            wordText.append(letterList[l])

    for i in range(0,len(finalText)):
        print(finalText[i])


def main():
    prag_cuvant=1
    prag_rand=1
    textReconstruction(['a','b','c','d','e'], "C:\\Users\\Andrada\\Desktop\\AI_Modul\\input.txt",prag_cuvant,prag_rand)
main()