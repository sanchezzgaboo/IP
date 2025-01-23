# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:06:02 2024

@author: gsanc
"""

import doctest

def contar_creadores_por_pais(c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    '''
    Cuenta el número de creadores por país.
    El conteo se retorna en un diccionario que tiene los países como llaves y
    sus conteos como valores.

    Parámetros:
    c1 (dict): Diccionario que representa al primer creador de contenido.
    c2 (dict): Diccionario que representa al segundo creador de contenido.
    c3 (dict): Diccionario que representa al tercer creador de contenido.
    c4 (dict): Diccionario que representa al cuarto creador de contenido.
             
    Retorno:
    dict: Diccionario con los países como llaves y el número de creadores 
    de ese país como valores.

    Ejemplo con diferentes países:

    >>> c1 = {"nombre": "Creador1", "pais": "Colombia"}
    >>> c2 = {"nombre": "Creador2", "pais": "México"}
    >>> c3 = {"nombre": "Creador3", "pais": "Colombia"}
    >>> c4 = {"nombre": "Creador4", "pais": "Perú"}
    >>> contar_creadores_por_pais(c1, c2, c3, c4)
    {'Colombia': 2, 'México': 1, 'Perú': 1}

    Ejemplo con todos los creadores del mismo país:

    >>> c1 = {"nombre": "Creador1", "pais": "Argentina"}
    >>> c2 = {"nombre": "Creador2", "pais": "Argentina"}
    >>> c3 = {"nombre": "Creador3", "pais": "Argentina"}
    >>> c4 = {"nombre": "Creador4", "pais": "Argentina"}
    >>> contar_creadores_por_pais(c1, c2, c3, c4)
    {'Argentina': 4}
   
    '''
    #TODO: # Implemente aquí la función contar_creadores_por_pais(...)
    contador1 = 1
    contador2 = 1
    contador3 = 1
    
    pais = c1["pais"]
    pais2 = c2["pais"]
    pais3 = c3["pais"]
    pais4 = c4["pais"]

    diccionario_creadores = {}
    
    if(pais == pais2):
       contador1 += 1
       diccionario_creadores[f"{pais}"] = contador1
    if(pais == pais3):
        contador1 +=1
        diccionario_creadores[f"{pais}"] = contador1
    if(pais == pais4):
        contador1 += 1
        diccionario_creadores[f"{pais}"] = contador1
    else:
        if(pais2 == pais3):
            contador2 += 1
            diccionario_creadores[f"{pais3}"] = contador2
        if(pais2==pais4):
            contador2 += 1
            diccionario_creadores[f"{pais4}"] = contador2
        else:
            diccionario_creadores[f"{pais2}"] = 1
            if(pais3 == pais4):
                contador3 += 1
                diccionario_creadores[f"{pais3}"] = contador3
            else:
                diccionario_creadores[f"{pais4}"] = 1
        
    
    return diccionario_creadores
        

doctest.run_docstring_examples(contar_creadores_por_pais, globals(), verbose=True)