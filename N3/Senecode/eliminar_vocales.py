def eliminar_vocales(cadena: str)->str:
    """ Eliminar vocales
    Parámetros:
      cadena (str): Cadena de caracteres compuesta por letras, símbolos, números, espacios, entre otros.
    Retorno:
      str: Cadena de caracteres sin vocales minúsculas ni mayúsculas.
    """
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for vocal in vocales:
        cadena = cadena.replace(vocal, "")

    return cadena

print(eliminar_vocales("AAWEUAIUEA"))
