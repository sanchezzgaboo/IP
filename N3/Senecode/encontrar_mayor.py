def encontrar_mayor(entrada: list)->int:
    """ Encontrar el elemento mayor
    Parámetros:
      entrada (list): La lista de números que se desea buscar
    Retorno:
      int: El número más grande en la lista, si está vacía -1.
    """
    
    numero_mas_grande = 0
    if entrada == []:
        numero_mas_grande = -1
    else:
        numero_mas_grande = entrada[0]
        for indice in entrada:
            if(numero_mas_grande < indice):
                numero_mas_grande = indice
    return numero_mas_grande


