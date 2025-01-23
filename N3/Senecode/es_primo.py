def es_primo(numero: int)->bool:
    """ Encontrar si un número es primo
    Parámetros:
      numero (int): Entero que se busca ver si es primo
    Retorno:
      bool: Booleano que indica si el número entero recibido por parámetro es primo
    """
    es_primo = False
    for numeros_hasta in range(1, numero):
        if(numero%numeros_hasta == 0):
            es_primo = False
        else:
            es_primo = True
    return es_primo

print(es_primo(9))

    