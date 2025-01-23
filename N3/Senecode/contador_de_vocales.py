def conteo_vocales(cadena: str)->int:
    """ Contador de vocales
    Parámetros:
      cadena (str): Cadena de la cual se quieren contar sus vocales.
    Retorno:
      int: Retorna un número dependiendo de la posición de las vocales de la cadena.
    """
    retorno = 0
    letra_par = 0
    letra_impar = 0
    for caracter in range(0, len(cadena)):
        if(caracter % 2 == 0 and (cadena[caracter] == "a" or cadena[caracter] == "e" or cadena[caracter] == "i" or cadena[caracter] == "o" or cadena[caracter] == "u")):
            letra_par += 1
        elif(not caracter % 2 == 0 and (cadena[caracter] == "a" or cadena[caracter] == "e" or cadena[caracter] == "i" or cadena[caracter] == "o" or cadena[caracter] == "u")):
            letra_impar += 1
        
    if(letra_impar > letra_par):
        retorno = 1
    elif(letra_par > letra_impar):
        retorno = 2
    elif(letra_impar == letra_par):
        retorno = 0
    return retorno

