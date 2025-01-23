def palabras_intercaladas(cadena1: str, cadena2: str)->str:
    """ Palabras intercaladas
    Parámetros:
      cadena1 (str): Primera cadena de la cual se desean intercalar sus palabras.
      cadena2 (str): Segunda cadena de la cual se desean intercalar sus palabras.
    Retorno:
      str: Cadena con las palabras intercaladas de las dos cadenas de entrada.
    """
    palabras1 = cadena1.split(" ")
    palabras2 = cadena2.split(" ")
    mensaje = ""
    for indice in range(0, len(palabras1)):
        mensaje += palabras1[indice] + " "
        mensaje += palabras2[indice] + " "

    return mensaje.replace(" ", "_")

print(palabras_intercaladas("hola como estas", "bien y tu"))