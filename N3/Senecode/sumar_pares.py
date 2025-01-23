def sumar_pares(numeros: list)->int:
    """ Sumar posiciones pares
    Parámetros:
      numeros (list): La lista con los números a sumar.
    Retorno:
      int: La suma de los números de la lista que están en posiciones pares.
    """
    suma = 0
    for indice in range(0, len(numeros)):
        if(indice % 2 == 0):
            suma += numeros[indice]
    return suma