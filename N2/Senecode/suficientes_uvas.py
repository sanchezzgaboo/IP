def suficientes_uvas(cantidad_ivan: int, cantidad_nicolas: int, cantidad_adriana: int, cantidad_verde: int, cantidad_morada: int, cantidad_negra: int)->str:
    """ ¿Suficientes Uvas?
    De los amigos, se sabe además que:

    Iván come exclusivamente uvas verdes
    Nicolás odia las uvas negras, por lo que solamente come uvas verdes o moradas
    Adriana come cualquier tipo de uva, pues todas le encantan

    Parámetros:
      cantidad_ivan (int): La cantidad de uvas que Iván desea comer
      cantidad_nicolas (int): La cantidad de uvas que Nicolás desea comer
      cantidad_adriana (int): La cantidad de uvas que Adriana desea comer
      cantidad_verde (int): La cantidad de uvas verdes de las que disponen los amigos
      cantidad_morada (int): La cantidad de uvas moradas de las que disponen los amigos
      cantidad_negra (int): La cantidad de uvas negras de las que disponen los amigos
    Retorno:
      str: La función retorna "felices", si todos los amigos pueden comer la cantidad de uvas que quieren;
           "casi", si dos de los 3 amigos pueden comer la cantidad de uvas que quieren; "fallamos", si
           solamente 1 amigo puede comer la cantidad de uvas que quiere; "al menos somos amigos", si ninguno de
           los amigos puede comer la cantidad de uvas que quiere.
    """
    contador = 0
    moradas_y_verdes = cantidad_verde + cantidad_morada
    if(cantidad_ivan <= cantidad_verde and cantidad_ivan != 0):
        contador += 1
        cantidad_verde -= cantidad_ivan
        moradas_y_verdes = cantidad_verde + cantidad_morada
    if(cantidad_nicolas <= moradas_y_verdes and cantidad_nicolas != 0):
        contador += 1
        moradas_y_verdes -= cantidad_nicolas
    if(cantidad_adriana <= moradas_y_verdes + cantidad_negra and cantidad_adriana != 0):
        contador += 1
    mensaje = ""
    if(contador == 0):
        mensaje = "al menos somos amigos"
    if(contador == 1):
        mensaje = "fallamos"
    if(contador == 2):
        mensaje = "casi"
    if(contador == 3):
        mensaje = "felices"
    return mensaje

print(suficientes_uvas(2,2,2,2,0,0))