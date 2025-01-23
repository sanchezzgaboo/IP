def contar_caracteres_repetidos(cadena: str)->int:
    """ Contar caracteres repetidos
    Parámetros:
      cadena (str): La cadena que se debe revisar.
    Retorno:
      int: La cantidad de caracteres diferentes que aparecen repetidos en la cadena.
    """
    repetidos = 0
    nueva_cadena = cadena
    for letra in cadena:
        nueva_cadena = nueva_cadena.replace(letra, "", 1)
        #while not caracter in nueva_cadena: intentar con while y centinela cuando se encuentre que se repite
        letra_actual = ""    
        for caracter in range(len(nueva_cadena)):
            if(nueva_cadena[caracter] == letra and letra_actual != nueva_cadena[caracter]):
                repetidos +=1
                letra_actual = nueva_cadena[caracter]
        nueva_cadena = nueva_cadena.replace(letra, "")
    return repetidos