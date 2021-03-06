# dupa aplicarea algoritmului dct si a cuantificatorului jpeg, pentru a obtine la inceputul listei rezultate valorile
# cele mai semnificative, vom parcurge matricea rezultata in zig-zag, astfel valorile cele mai nesemnificative
# (cele in jur de 0) vor fi la finalul listei

def zig_zag(quantize_result):
    zig_zag_list = []

    for q_element in quantize_result:
        k_list = [[] for i in range(15)]
        final_k_list = []

        # deoarece valorile de deasupra diagonalei secundare sunt cele mai semnificative,
        # pentru a optimiza intreg procesul, vom lua in considerare doar aceste valori
        # valorile ce se apropie de 0 nu vor mai fi luate in considerare
        for i in range(8):
            for j in range(7 - i):
                sum = i + j
                if sum % 2 == 0:
                    k_list[sum].insert(0, quantize_result[q_element][i][j])
                else:
                    k_list[sum].append(quantize_result[q_element][i][j])

        for elem in k_list:
            for i in elem:
                final_k_list.append(int(i))

        zig_zag_list.append(final_k_list)

    return zig_zag_list
