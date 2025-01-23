def conteo_min_y_max(num_min: int, num_max: int, numeros: list)->str:
    """ Min y Max
    Parámetros:
      num_min (int): Valor entero que representa el límite inferior para la búsqueda.
      num_max (int): Valor entero que representa el límite superior para la búsqueda.
      numeros (list): Lista con los n números a evaluar.
    Retorno:
      str: Mensaje de la forma "Hay X menores, Y mayores y Z dentro del intervalo". X,Y y Z corresponden a los
           números menores a min, los números mayores a max y los números entre min y max, respectivamente.
    """
    numeros.sort()
    rango_inf = 0
    rango_sup = 0
    quitar_arriba=0
    quitar_abajo = 0
    for indice in numeros:
        if(indice > num_max):
            #Que hacer si los numeros dentro de la lista superan el limite superior
            rango_sup += 1
        if(indice == num_max):
            #que hacer si es igual
            quitar_arriba +=1
        if(indice < num_min):
            #Que hacer si los numeros dentro de la lista son inferiores al limite inferior
            rango_inf += 1
        if(indice == num_min):
            #que hacer si es igual
            quitar_abajo+=1
          
    for cantidad in range(rango_sup):
        numeros.pop() #Quitar arriba y asignar
    for cantidad in range(rango_inf):
        numeros.pop(0) #Quitar abajo y asignar
    if(numeros !=[]):
        for cantidad in range(quitar_arriba):
            numeros.pop()
        for cantidad in range(quitar_abajo):
            numeros.pop(0)
        
    return f"Hay {rango_inf} menores, {rango_sup} mayores y {len(numeros)} dentro del intervalo"

print(conteo_min_y_max(0,5, [6,7,8,9]))