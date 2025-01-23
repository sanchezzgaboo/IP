lista= [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

for fila in range(len(lista)):
    for columna in range(len(lista[0])):
        if(fila == 0):
            lista[fila][columna] = 1
        if(fila == len(lista) -1):
            lista[fila][columna] = 1
        if(columna == 0):
            lista[fila][columna] = 1
        if(fila == len(lista)//2 ):
            lista[fila][columna] = 1,

for item in lista:
    print(item)