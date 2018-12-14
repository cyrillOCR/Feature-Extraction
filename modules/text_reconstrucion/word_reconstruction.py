#
def textReconstruction(letterList,file,prag_cuvant,prag_rand):

    finalText=[]
   # finalText.append("mama")
    #print(finalText[0][0])
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

    first=list_of_coords[0]
    #for l in list_of_coords:
    currentWord=[]
    line=0
    word=0
    letter=0
    print(letterList[0])
    finalText.append(letterList[0])
    letter+=1
    for l in range(1,len(list_of_coords)):

        x1, y1, x2, y2 = list_of_coords[l][3], list_of_coords[l][0], list_of_coords[l][1], list_of_coords[l][2]
        if x1-list_of_coords[l-1][1]>prag_cuvant:
            print("cuvant nou")
            word+=1
            letter=0


        if y1-list_of_coords[l-1][2]>prag_rand:
            print("rand nou")
            line+=1
            word=0
            letter=0

        else:
            letter+=1
        finalText[line][word][letter]=letterList[l]

    print(finalText)
def main():
    prag_cuvant=1
    prag_rand=1
    textReconstruction(['a','b','c','d','e'], "C:\\Users\\vasil\\PycharmProjects\\taskAI\\input.txt",prag_cuvant,prag_rand)
main()