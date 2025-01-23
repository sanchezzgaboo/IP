def eliminar_caracteres_repetidos(cadena: str)->str:
    """ Eliminar caracteres repetidos
    Parámetros:
      cadena (str): Cadena de la cual se desean eliminar los caracteres repetidos.
    Retorno:
      str: Cadena sin los caracteres repetidos.
    """
    caracteres_repetidos = 0
    letra_previa = ""
    for letra in cadena:
        if(letra == letra_previa):
            caracteres_repetidos += 1
        if(caracteres_repetidos == len(cadena)):
            cadena.replace((caracteres_repetidos+1)*letra, letra)
        else:
            cadena = cadena.replace((caracteres_repetidos+1)*letra, letra)
            caracteres_repetidos = 0
        letra_previa = letra

    return cadena

print(eliminar_caracteres_repetidos("tesssssssso"))
