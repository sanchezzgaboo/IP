# -*- coding: utf-8 -*-
"""
CupiTikTok:

@author: Cupi2
"""


def construir_creador(
    nombre: str,
    pais: str,
    categorias: str,
    likes: int,
    vistas: int,
    seguidores: int,
    fecha_ultima_publicacion: int,
) -> dict:
    """
    Crea un diccionario con la información de un creador de contenido.

    Parámetros:
    nombre (str): Nombre del creador de contenido.
    pais (str): País de origen del creador de contenido.
    categorias (str): Categoría de los videos del creador de contenido.
    likes (int): Cantidad de likes que ha recibido el creador de contenido.
    vistas (int): Cantidad de vistas que ha recibido el creador de contenido.
    seguidores (int): Cantidad de seguidores que tiene el creador de contenido.
    fecha_ultima_publicacion (int): Fecha de la última publicación del creador
        de contenido en formato YYYYMMDD.

    Retorno:
    dict: Diccionario con la información del creador de contenido.
    """
    creador = {
        "nombre": nombre,
        "pais": pais,
        "categorias": categorias,
        "likes": likes,
        "vistas": vistas,
        "seguidores": seguidores,
        "fecha_ultima_publicacion": fecha_ultima_publicacion,
    }
    
    return creador


def buscar_creador_por_nombre(nombre: str, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca si entre los creadores de contenido dados, hay uno con el nombre ingresado.

    Parámetros:
        nombre (str): Nombre del creador de contenido a buscar.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario del creador de contenido con el nombre ingresado por el usuario.
            Retorna None si no hay ningún creador con ese nombre. Si dos creadores
            o más tienen el mismo nombre, retorna el primero encontrado.
    """
    creador = {}
    if(c1["nombre"].lower() == nombre.lower()): 
        creador = c1
    if(c2["nombre"].lower() == nombre.lower()):
        creador = c2
    if(c3["nombre"].lower() == nombre.lower()):
        creador = c3
    if(c4["nombre"].lower() == nombre.lower()):
        creador = c4
    return creador


def filtrar_creadores_por_categoria(categoria: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados según la categoría ingresada.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores que hacen contenido de la categoría dada,
            separados por comas. Retorna None si no hay ningún creador que haga
            parte de la categoría de interés ingresada.
    """
    resultados = ""
    contador_de_creadores = 0
    if(categoria.lower() in c1["categorias"].lower()):
        resultados += f"{c1['nombre']}"
        contador_de_creadores += 1
    if(categoria.lower() in c2["categorias"].lower()):
        if(contador_de_creadores == 0):
            resultados += f"{c2['nombre']}"
        else:
            resultados += f", {c2['nombre']}"
        contador_de_creadores += 1

    if(categoria.lower() in c3["categorias"].lower()):
        if(contador_de_creadores == 0):
            resultados += f"{c3['nombre']}"
        else:
            resultados += f", {c3['nombre']}"
        contador_de_creadores += 1

    if(categoria.lower() in c4["categorias"].lower()):
        if(contador_de_creadores == 0):
            resultados += f"{c4['nombre']}"
        else:
            resultados += f", {c4['nombre']}"
        contador_de_creadores += 1
    if(contador_de_creadores == 0):
        resultados = None
    return resultados

def calcular_promedio_vistas(c1: dict, c2: dict, c3: dict, c4: dict) -> float:
    """
    Calcula el promedio de vistas de todos los creadores de contenido dados.

    Parámetros:
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        float: Promedio de vistas de todos los creadores de contenido dados,
            redondeado a dos cifras decimales.
    """
    return round((c1["vistas"] + c2["vistas"] + c3["vistas"] +c4["vistas"]) / 4, 2)


def filtrar_creadores_por_vistas(minimo_vistas: int, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Filtra a los creadores de contenido dados que superen un mínimo de vistas (umbral).

    Parámetros:
        minimo_vistas (int): Umbral de vistas.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: Nombres de los creadores de contenido dados que superan el mínimo
            de vistas ingresado, separados por comas. Retorna el mensaje "Ninguno"
            si ningún creador de contenido supera el umbral.
    """
    resultados = ""
    contador_de_creadores = 0
    if(c1["vistas"]>=minimo_vistas):
        resultados += f"{c1['nombre']}"
        contador_de_creadores += 1
    if(c2["vistas"]>=minimo_vistas):
        if(contador_de_creadores == 0):
            resultados += f"{c2['nombre']}"
        else:
            resultados += f", {c2['nombre']}"

        contador_de_creadores += 1

    if(c3["vistas"]>=minimo_vistas):
        if(contador_de_creadores == 0):
            resultados += f"{c3['nombre']}"
            print(resultados)

        else:
            resultados += f", {c3['nombre']}"
            print(resultados)

        contador_de_creadores += 1
    if(c4["vistas"]>=minimo_vistas):
        if(contador_de_creadores == 0):
            resultados += f"{c4['nombre']}"
            print(resultados)

        else:
            resultados += f", {c4['nombre']}"
            print(resultados)

        contador_de_creadores += 1
    if(contador_de_creadores == 0):
        resultados = "Ninguno"
    return resultados


def calcular_rating_creador(creador: dict) -> float:
    """
    Calcula el rating de un creador de contenido con base en su número de
    seguidores, likes y vistas usando la fórmula F1.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.

    Retorno:
        float: El rating del creador de contenido, redondeado a dos cifras
            decimales. Este valor se encuentra entre 0 y 100.
    """
    S_MAX = 600_000
    L_MAX = 100_000_000
    V_MAX = 100_000_000
    valor = ((creador["seguidores"]/S_MAX)*0.5)+((creador["likes"]/L_MAX)*0.3)+((creador["vistas"]/V_MAX)*0.2)
    return(round((valor, 2)))


def calcular_puntaje_afinidad(creador: dict, categoria: str, minimo_rating: float, pais: str) -> float:
    """
    Calcula el puntaje de afinidad entre un creador de contenido y un
    usuario basándose en una categoría, un país y un rating mínimo dados.

    Parámetros:
        creador (dict): Diccionario que representa a un creador de contenido.
        categoria (str): Categoría de interés para el usuario.
        minimo_rating (float): Rating mínimo que debe tener el creador de contenido.
            Este valor se encuentra entre 0 y 100.
        pais (str): Nombre del país de interés para el usuario.

    Retorno:
        float: El puntaje de afinidad que tiene un creador con un usuario,
            redondeado a dos cifras decimales.
    """
    puntaje = 0
    if(creador["categorias"] == categoria):
        puntaje += 3
    if(creador["pais"] == pais):
        puntaje += 2
    elif(creador["pais"] != pais):
        puntaje -= 1
    if(calcular_rating_creador(creador) < minimo_rating):
        puntaje -= 5
    elif(calcular_rating_creador(creador) >= minimo_rating):
        puntaje += 2
    return round(puntaje, 2)
    

def buscar_creador_favorito(categoria: str, rating: float, pais: str, c1: dict, c2: dict, c3: dict, c4: dict) -> str:
    """
    Busca el creador de contenido con el mayor puntaje de afinidad, teniendo
        en cuenta la categoría, el país y un rating mínimo especificados.

    Parámetros:
        categoria (str): Categoría de interés para el usuario.
        rating (float): Rating mínimo que debe tener el creador de contenido.
        pais (str): Nombre del país de interés para el usuario.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        str: El nombre del creador de contenido con mayor puntaje de afinidad
            y su puntaje obtenido como sigue: "{nombre} con puntaje {puntaje_afinidad}",
            por ejemplo: "Code_Destroyer2002 con puntaje 100".
            Si dos creadores resultan con el mismo puntaje de afinidad, se retorna la
            información del que tenga el nombre alfabéticamente anterior/menor 
            (considerando el orden de sus caracteres en el abecedario). 
    """
    afinidad1 = calcular_puntaje_afinidad(c1, categoria, rating, pais)
    afinidad2 = calcular_puntaje_afinidad(c2, categoria, rating, pais)
    afinidad3 = calcular_puntaje_afinidad(c3, categoria, rating, pais)
    afinidad4 = calcular_puntaje_afinidad(c4, categoria, rating, pais)
    creador = c1.copy() #Creador Actual
    creador2 = {} #Creador Siguiente
    afinidad_mas_grande = afinidad1 #Asumir que la afinidad mas grande es la primera
    if(afinidad_mas_grande < afinidad2):
        afinidad_mas_grande = afinidad2 #Si afinidad 1 es menor que la 2, se asigna la 2, ya que esta sería mas grande.
        creador = c2.copy()
    elif(afinidad_mas_grande == afinidad2):
        creador2 = c2.copy()
        if(creador["nombre"].lower() < creador2["nombre"].lower()): 
            #SI el nombre del primero es alfabeticamente menor, creador se mantiene.
            creador = creador
        else:
            #En otro caso, el creador se decide que es el Segundo, ya que este seria el alfabeticamente menor
            creador = creador2.copy()
    if(afinidad_mas_grande < afinidad3):
        afinidad_mas_grande = afinidad3
        creador = c3.copy()
    elif(afinidad_mas_grande == afinidad3):
        creador2 = c3.copy()
        if(creador["nombre"].lower() < creador2["nombre"].lower()):
            creador = creador
        else:
            creador = creador2.copy()
    if(afinidad_mas_grande < afinidad4):
        afinidad_mas_grande = afinidad4
        creador = c4.copy()
    elif(afinidad_mas_grande == afinidad4):
        creador2 = c4.copy()
        if(creador["nombre"].lower() < creador2["nombre"].lower()):
            creador = creador
        else:
            creador = creador2.copy()
    resultado = f"{creador['nombre']} con puntaje {afinidad_mas_grande}"
    return(resultado)

def calcular_anio(fecha: int) -> int:
    return fecha // 10000

def calcular_mes(fecha: int) -> int:
    return (fecha - (int(f"{fecha // 10000}_0000"))) // 100

def calcular_dia(fecha: int) -> int:
    return (fecha - (int(f"{fecha // 10000}_0000")) - (fecha - (int(f"{fecha // 10000}_0000"))) // 100 * 100)

def calcular_fecha_exacta(fecha_de_referencia: int, creador: dict) -> dict:
    diccionario_fechas = {}
    diccionario_fechas["nombre"] = creador["nombre"]
    
    '''
    Si el mes es negativo, restale 1 al año y calcula los meses correctos
    '''
    if(calcular_mes(fecha_de_referencia) - calcular_mes(creador["fecha_ultima_publicacion"])<0):
        diccionario_fechas["anios"] = calcular_anio(fecha_de_referencia) - calcular_anio(creador["fecha_ultima_publicacion"]) - 1
        diccionario_fechas["meses"] = calcular_mes(fecha_de_referencia) + 12 - calcular_mes(creador["fecha_ultima_publicacion"])
    elif(calcular_mes(fecha_de_referencia) - calcular_mes(creador["fecha_ultima_publicacion"])>=0):
        diccionario_fechas["anios"] = calcular_anio(fecha_de_referencia) - calcular_anio(creador["fecha_ultima_publicacion"])
        diccionario_fechas["meses"] = calcular_mes(fecha_de_referencia) - calcular_mes(creador["fecha_ultima_publicacion"])
    
    '''
    Si el dia es negativo, restale 1 al mes y calcula los días correctos, 
    también toma en cuenta que algunos meses tienen 31 dias y otros 30
    '''
    if(calcular_dia(fecha_de_referencia) - calcular_dia(creador["fecha_ultima_publicacion"]) < 0):
        diccionario_fechas["meses"] -= 1
        if(calcular_mes(fecha_de_referencia) != 1 or calcular_mes(fecha_de_referencia) != 3 or calcular_mes(fecha_de_referencia) != 5 or calcular_mes(fecha_de_referencia) != 7 or calcular_mes(fecha_de_referencia) != 8 or \
            calcular_mes(fecha_de_referencia) != 10 or calcular_mes(fecha_de_referencia) != 12):
            diccionario_fechas["dias"] = (31 - calcular_dia(creador["fecha_ultima_publicacion"]) + calcular_dia(fecha_de_referencia))
        else:
            diccionario_fechas["dias"] = (30 - calcular_dia(creador["fecha_ultima_publicacion"]) + calcular_dia(fecha_de_referencia))
    elif (calcular_dia(fecha_de_referencia) - calcular_dia(creador["fecha_ultima_publicacion"]) >= 0):
        diccionario_fechas["dias"] = calcular_dia(fecha_de_referencia) - calcular_dia(creador["fecha_ultima_publicacion"])  
    
    return diccionario_fechas
    


def buscar_creador_inactivo(fecha_de_referencia: int, c1: dict, c2: dict, c3: dict, c4: dict) -> dict:
    """
    Busca al creador de contenido que lleva el mayor tiempo sin publicar
        con base en una fecha ingresada por parámetro y la llave
        fecha_ultima_publicacion.

    Parámetros:
        fecha_de_referencia (int): Fecha con la que se busca hacer el análisis
            de actividad en formato YYYYMMDD.
        c1 (dict): Diccionario que representa al primer creador de contenido.
        c2 (dict): Diccionario que representa al segundo creador de contenido.
        c3 (dict): Diccionario que representa al tercer creador de contenido.
        c4 (dict): Diccionario que representa al cuarto creador de contenido.

    Retorno:
        dict: Diccionario con las llaves: "nombre", "dias", "meses" y "anios",
            cuyos valores son respectivamente el nombre del creador más inactivo y 
            el tiempo de inactividad en años, meses y días.
            Si dos creadores tienen el mismo tiempo sin publicar, retorna el
            que tenga menos seguidores.
            Si la fecha ingresada es anterior a todas las fechas de última publicación,
            retorna None.
    """
    año_c1 = fecha_de_referencia - c1["fecha_ultima_publicacion"]
    año_c2 = fecha_de_referencia - c2["fecha_ultima_publicacion"]
    año_c3 = fecha_de_referencia - c3["fecha_ultima_publicacion"]
    año_c4 = fecha_de_referencia - c4["fecha_ultima_publicacion"]
    creador = c1.copy() #Creador actual
    creador2 = {} #Creador a Comparar
    diccionario_de_retorno = {}
    none = {"none": None} #Un diccionario que contiene None, utilizado para retornar 
    año_mas_viejo = año_c1 #Asumir que el año mas viejo es el primero.
    
    if(año_mas_viejo < año_c2):
        año_mas_viejo = año_c2
        creador = c2.copy()
    elif(año_mas_viejo == año_c2):
        creador2 = c2.copy()
        if(creador["seguidores"] < creador2["seguidores"]):
            creador = creador
        else:
            creador = creador2.copy()
            
    if(año_mas_viejo < año_c3):
        año_mas_viejo = año_c3
        creador = c3.copy()
    elif(año_mas_viejo == año_c3):
        creador2 = c3.copy()
        if(creador["seguidores"] < creador2["seguidores"]):
            creador = creador
        else:
            creador = creador2.copy()
            
    if(año_mas_viejo < año_c4):
        año_mas_viejo = año_c4
        creador = c4.copy()
    elif(año_mas_viejo == año_c4):
        creador2 = c4.copy()
        if(creador["seguidores"] < creador2["seguidores"]):
            creador = creador
        else:
            creador = creador2.copy()
            
    if(año_mas_viejo<0):
        diccionario_de_retorno = none.copy()

    else:
        diccionario_de_retorno = calcular_fecha_exacta(fecha_de_referencia, creador).copy()
        
    return diccionario_de_retorno