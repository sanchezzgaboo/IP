def entero_minimo(l: int, r: int, d: int)->int:
    """ Entero Mínimo
    Parámetros:
      l (int): El número entero positivo que describe el número inferior del rango [l,r]
      r (int): El número entero positivo que describe el número superior del rango [l,r]
      d (int): El número entero positivo por el cual la respuesta x debe ser divisible, para ser válida.
    Retorno:
      int: El entero positivo más pequeño que cumple con ser divisible entre el número d, y no pertenece al
           rango de números [l,r]
    """
    x = d
    #(0, 5, 3)
    #en caso de que d este entre 0 y 5, toca encontrar el siguiente multiplo, que esté por fuera del rango.
    #Para hacer esto, toca truncar la division con el valor más grande del rango, ya que esto nos dara el valor más cercano para escapar
    #Le sumas 1 para que en caso de que sea 1 no nos de el mismo valor y podamos salir
    #multiplicas por d

    if( x <= r and x >= l):
        x = ((r//d) +1) * d
    
    return x