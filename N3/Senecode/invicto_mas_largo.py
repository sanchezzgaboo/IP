def invicto_mas_largo(goles_diccionarios: list, goles_adversario: list)->int:
    """ Invictos
    Parámetros:
      goles_diccionarios (list): Los goles anotados por Diccionarios F.C en cada una de las fechas. Se
                                 garantiza que cada elemento de la lista es un entero no negativo.
      goles_adversario (list): Los goles anotados por los adversarios de Diccionarios F.C en cada una de las
                               fechas. Se garantiza que cada elemento de la lista es un entero no negativo.
    Retorno:
      int: Retorna la cantidad máxima de fechas consecutivas en que el equipo Diccionarios F.C no perdió
           durante la temporada anterior.
    """
    contador = 0
    contador_max = 0
    for fecha in range(len(goles_diccionarios)):
        if(goles_diccionarios[fecha] - goles_adversario[fecha] >= 0):
            contador += 1
        if(fecha == len(goles_adversario) - 1 or goles_diccionarios[fecha] - goles_adversario[fecha] < 0):
            if(contador>contador_max):
                contador_max = contador
            contador = 0
    return contador_max

print(invicto_mas_largo( [1, 0, 1, 0, 1, 0, 0],  [1, 1, 1, 1, 2, 0, 0]))