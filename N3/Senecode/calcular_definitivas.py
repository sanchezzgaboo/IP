def calcular_definitivas(estudiantes: list)->list:
    """ Aproximación de Notas
    Parámetros:
      estudiantes (list): Una lista de diccionarios que representan a los estudiantes que han finalizado el
                          curso, con su nota final sin aproximar.  Cada diccionario tiene las siguientes
                          llaves: "nombre": (str) el nombre del estudiante.  "nota": (float), un float que
                          representa la nota sin aproximar del estudiante.
    Retorno:
      list: La función retorna una lista de diccionarios, con tantos diccionarios como estudiantes había en la
            lista inicial, pero con sus notas aproximadas. El orden de los diccionarios debe ser el mismo de la
            lista de entrada. Cada uno de los diccionarios retornados debe tener las llaves: "nombre" (str) y
            "nota" (float).     
    """
    lista_retorno = []
    for persona in estudiantes:
        nota_redondeada = 0
        if(persona["nota"] >= 4.5):
            nota_redondeada = 5.0
        elif(persona["nota"] >= 3.5):
            nota_redondeada = 4.0
        elif(persona["nota"] >= 2.5):
            nota_redondeada = 3.0 
        elif(persona["nota"] < 2.5):
            nota_redondeada = 1.5

        lista_retorno.append({"nombre":persona["nombre"], "nota":nota_redondeada})
    return lista_retorno
     