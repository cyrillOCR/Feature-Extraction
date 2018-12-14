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
            #print("cuvant nou")
            aux=[]
            aux=wordText.copy()
            lineText.append(aux)
            wordText.clear()
            wordText.append(letterList[l])


        elif y1-list_of_coords[l-1][2]>prag_rand:
            #print("rand nou")
            aux2=[]
            aux2 = wordText.copy()
            lineText.append(aux2)
            wordText.clear()
            aux3 = []
            aux3 = lineText.copy()
            finalText.append(aux3)
            lineText.clear()
            wordText.clear()
            wordText.append(letterList[l])


        else :
            wordText.append(letterList[l])
            if l == len(list_of_coords) - 1:
                aux2 = []
                aux2 = wordText.copy()
                lineText.append(aux2)
                wordText.clear()
                aux3 = []
                aux3 = lineText.copy()
                finalText.append(aux3)

    print(finalText)


def main():
    prag_cuvant=1
    prag_rand=1
    #textReconstruction(['a', 'b', 'c', 'd', 'e'], "C:\\Users\\sfirn\\Desktop\\AI\\input.txt", prag_cuvant, prag_rand)
    textReconstruction(['E', 'm', 'i', 'e', 'z', 'u', 'l', 'n', 'o', 'p', 'ţ', 'i', 'i', ',',  # 14
                        'p', 'o', 'a', 't', 'e', 'f', 'i', 'ş', 'i', 'd', 'o', '-',  # 12
                        'u', 'ă', 'n', 'o', 'a', 'p', 't', 'e', 'a', '.',  # 10
                        'S', 'u', 'n', 't', 's', 'i', 'n', 'g', 'u', 'r', 'ă', ',', 'p', 'e', 'v', 'e', '-',  # 17
                        'r', 'a', 'n', 'd', 'ă', '.', 'D', 'e', 'a', 'i', 'c', 'i', 'n', 'u',  # 14
                        'p', 'o', 't', 'c', 'u', 'p', 'r', 'i', 'n', 'd', 'e', 't', 'o', 't', 'c', 'e', '-',  # 17
                        'r', 'u', 'l', 'c', 'u', 'p', 'r', 'i', 'v', 'i', 'r', 'e', 'a', '.']  # 14
                       , "C:\\Users\\vasil\\PycharmProjects\\taskAI\\input.txt", prag_cuvant, prag_rand)
main()