lista = [[1,1,1],[1,1,1],[1,1,1]]

for fila in range(len(lista)):
    for columna in range(len(lista[0])):
        if((fila == 0  or fila == len(lista) - 1) and (columna == 0 or columna == len(lista[0]-1))):
            