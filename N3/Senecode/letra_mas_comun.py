def letra_mas_comun(cadena: str)->str:
    """ Moda en una cadena
    Parámetros:
      cadena (str): La cadena en la que se quiere saber cuál es la letra más común
    Retorno:
      str: La letra más común en la cadena que ingresa como parámetro,  si son dos es la letra alfabéticamente
           posterior.
    """
    cuenta_maxima = 0
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace(".", "")
    cadena = cadena.replace(",", "")
    letra_mas_comun = cadena[0]
    for letra in cadena:
      cuenta = 0 #Siempre se reinicia la cuenta interna
      for caracter in cadena: #Segundo loop para comparar la primera con todas las demas, la segunda con todas las demas, etc.
        if caracter == letra: #Si son iguales
          cuenta +=1 #Se suma la cuenta
      if(cuenta > cuenta_maxima): #Al finalizar de analizar todas la ocurrencias, si es mayor a la cuenta previamente maxima
         cuenta_maxima = cuenta
         letra_mas_comun = letra #Se Asigna el caracter como la cuenta maxima
      if(cuenta==cuenta_maxima): #Si son iguales
         if(letra_mas_comun < letra):
            letra_mas_comun = letra #El alfabeticamente posterior
    return letra_mas_comun
        
print(letra_mas_comun("A VER SI ESTO ES DE TU TALLA, AMIGA ENORME"))