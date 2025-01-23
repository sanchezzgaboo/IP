lista = [[0,1,0,0,0],
         [1,1,1,1,0],
         [0,1,0,1,0],
         [2,1,1,1,0],
         [0,2,0,0,0]]
def sumar_vecinos(lista: list, coords: tuple) -> list:
    vecinos = []
    suma = 0
    fila = coords[0]
    columna = coords[1]
    if(fila == 0 and columna == 0):
        for i in range(0,2):
            for k in range(0,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((i,k))
    elif(fila == len(lista) - 1 and columna == 0):
        for i in range(-1,1):
            for k in range(0,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((len(lista) - 1 + i,k))
    elif(fila == 0 and columna == len(lista[0]) - 1):
        for i in range(0,2):
            for k in range(-1,1):
                if (i != 0 or k!= 0 ):
                    vecinos.append((i,len(lista[0])-1 + k))
    elif(fila == len(lista) - 1 and columna == len(lista[0]) - 1):
        for i in range(-1,1):
            for k in range(-1,1):
                if (i != 0 or k!= 0 ):
                    vecinos.append((len(lista)-1 + i,len(lista[0])-1 + k))
    elif(fila == 0 and (columna != 0 or columna != len(lista[0]) - 1)):
        for i in range(0,2):
            for k in range(-1,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((fila+i,columna + k))
    elif(fila == len(lista) - 1 and (columna != 0 or columna != len(lista[0]) - 1)):
        for i in range(-1,1):
            for k in range(-1,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((fila+i,columna + k))
    elif(columna == 0 and (fila != 0 or fila != len(lista) - 1)):
        for i in range(-1,2):
            for k in range(0,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((fila+i,columna + k))
    elif(columna == len(lista[0]) - 1 and (fila != 0 or fila != len(lista) - 1)):
        for i in range(-1,2):
            for k in range(-1,1):
                if (i != 0 or k!= 0 ):
                    vecinos.append((fila+i,columna + k))
    else:
        for i in range(-1,2):
            for k in range(-1,2):
                if (i != 0 or k!= 0 ):
                    vecinos.append((fila+i,columna + k))
    for item in vecinos:
        suma += lista[item[0]][item[1]]

    return suma

print(sumar_vecinos(lista, (2, 2)))