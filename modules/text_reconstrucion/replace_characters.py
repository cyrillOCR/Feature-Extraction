def replace_character(finalText):
    file=open("replace.txt")
    #file.strip()
    replaced_text=finalText
    for line in file:
        line=line.strip()
        car_de_inlocuit, car_corect = line.split("-")
        print(car_de_inlocuit,car_corect)
        replaced_text=replaced_text.replace(car_de_inlocuit,car_corect)
        replaced_text = replaced_text.replace("\u02191\u02192","\u0219")
        replaced_text = replaced_text.replace("\u0219t1\u0219t2","\u0219t")
        replaced_text = replaced_text.replace("\u021B1\u021B2","\u021B")

    print(replaced_text)

text="dacădumn1n2eataști .iliatinește ... Eudomnl n2 !\u02191\u02192 ... \u0219t1\u0219t2...\u0103"
replace_character(text)