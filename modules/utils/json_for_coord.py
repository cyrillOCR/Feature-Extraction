import json

# cordonatele vor fi in formatul: x1 y1 x2 y2
# vom parsa acest json si vom obtine coordonatele fiecarei litere
def json_for_coord():
    file=open("coordonate10.txt")
    data={}

    coords=[]
    for line in file:
        line.strip()
        coord_for_a_line=line.split(' ')
        lista=[]
        lista.append(int(coord_for_a_line[0]))
        lista.append(int(coord_for_a_line[1]))
        lista.append(int(coord_for_a_line[2]))
        lista.append(int(coord_for_a_line[3]))
        coords.append(lista)
    data = {
        "coords": coords}
    file.close()
    print(data)
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile, indent=4)




json_for_coord()