import math
def cargar_restaurantes(nombre: str) -> dict:
    '''Generar un diccionario con todos los datos de los restaurantes

    Args:
        nombre (str): nombre del archivo a abrir

    Returns:
        dict: diccionario con los estados y estos a su vez asociados 
        a cada uno de los restaurantes presentes en ese estado
        y toda su informacion en formato de diccionario.
    '''    
    archivo = open(nombre, "r", encoding="utf-8")
    llaves = archivo.readline()
    llaves = llaves.split(",")
    restaurantes = archivo.readlines()
    diccionario_de_estados = {}
    for indice in range(1, len(restaurantes)):
        datos_restaurante = restaurantes[indice].strip().split(",")
        nombre = datos_restaurante[0]
        categoria = datos_restaurante[1]
        rating = datos_restaurante[2]
        latitud = datos_restaurante[3]
        longitud = datos_restaurante[4]
        ciudad = datos_restaurante[5]
        estado = datos_restaurante[6]
        precio = datos_restaurante[7]
        reseñas = datos_restaurante[8]
        delivery = False
        if(datos_restaurante[9] == 1):
            delivery = True
        direccion = datos_restaurante[10]
        diccionario_de_restaurante = { #Formato del diccionario
            "name":nombre,
            "category":categoria,
            "rating":rating,
            "latitude":float(latitud),
            "longitude":float(longitud),
            "city":ciudad,
            "state":estado,
            "price":precio,
            "review_count":reseñas,
            "delivery":delivery,
            "address": direccion
        }
        if(not estado in diccionario_de_estados): #Si no hay datos de ese estado, se crea la llave
            diccionario_de_estados[estado] = [diccionario_de_restaurante]
        else: #En caso de que ya exista, se actualiza y se agrega al final de la lista 
            diccionario_de_estados[estado].append(diccionario_de_restaurante)
    archivo.close()

    return diccionario_de_estados

def buscar_restaurantes_en_area(estados: dict, latitud_min: float, latitud_max: float, longitud_min: float, longitud_max: float) -> list:
    '''Encontrar todos los restaurantes en un area.

    Args:
        estados (dict): diccionario de estados
        latitud_min (float): latitud minima
        latitud_max (float): latitud maxima
        longitud_min (float): longitud minima
        longitud_max (float): longitud maxima

    Returns:
        list: devuelve una lista con todos los restaurantes en un area.
    '''    
    restaurantes_encontrados = []
    for estado in estados:
        for restaurante in estados[estado]:
            longitud = restaurante["longitude"]
            latitud = restaurante["latitude"]
            if(latitud>=latitud_min and latitud<=latitud_max and longitud>= longitud_min and longitud <= longitud_max):
                restaurantes_encontrados.append(restaurante)
    return restaurantes_encontrados


def buscar_restaurante_mas_sucursales(estados: dict, estado_buscado: str) -> dict:
    '''buscar el mayor numero de sucursales en estados

    Args:
        estados (dict): diccionario de estados
        estado_buscado (str): el estado donde buscar las sucursales

    Returns:
        dict: devuelve un diccionario con el nombre del restaurante con mas sucursales y el numero
    '''    
    mayor_sucursales = {"nombre_restaurante": "", "numero_sucursales": 0}
    cuenta = {}
    for restaurante in estados[estado_buscado]:
        nombre = restaurante["name"]
        if(not nombre in cuenta):
            cuenta[nombre] = 1
        else:
            cuenta[nombre] += 1

    cuenta_de_valores = list(cuenta.values())
    cuenta_de_llaves = list(cuenta.keys())
    valor_max = cuenta_de_valores[0]
    sucursal_max = cuenta_de_llaves[0]
    for i in range(1, len(cuenta_de_valores)): #Encontar el valor mas alto, y su llave asociada
        #Excluye el primer valor, este se asume que es el mas alto
        if(cuenta_de_valores[i] > valor_max):
            valor_max = cuenta_de_valores[i]
            sucursal_max = cuenta_de_llaves[i]

    mayor_sucursales["nombre_restaurante"] = sucursal_max
    mayor_sucursales["numero_sucursales"] = valor_max
    return mayor_sucursales


def estandarizar_direcciones(estados: dict) -> None:
    '''Intercambia las abreviaciones de las direcciones por la direccion completa. 
    Se actualiza el diccionario de estados

    Args:
        estados (dict): diccionario de estados

    Returns:
        _type_: No devuelve nada
    '''    
    abreviaciones = {
        "st": "Street",
        "ave": "Avenue",
        "sq": "Square",
        "hwy": "Highway",
        "blvd": "Boulevard",
        "rd": "Road",
        "dr": "Drive",
        "ln": "Lane",
        "ct": "Court",
        "pl": "Place",
        "pk": "Park",
        "cir": "Circle",
        "expy": "Expressway",
        "trl": "Trail",
        "rte": "Route",
        "mt": "Mount",
        "fwy": "Freeway"
    }
    for estado in estados: #Todos los estados
        for restaurante in estados[estado]: #Todos los restaurantes en el estado
            direccion = restaurante["address"].split(" ")
            for palabra in range(len(direccion)):
                if(direccion[palabra].lower() in abreviaciones):
                   direccion[palabra] = abreviaciones[direccion[palabra].lower()]
            restaurante["address"] = " ".join(direccion)

    return None
            
def buscar_restaurantes_palindromos(estados: dict) -> list:
    '''Busca si el nombre de un restaurante es palindromo

    Args:
        estados (dict): diccionario de estado

    Returns:
        list: devuelve una lista de todos los restaurantes palindromos.
    '''    
    lista_de_palindromos = []
    for estado in estados: #Todos los estados
        for restaurante in estados[estado]: #Todos los restaurantes en el estado
            nombre = restaurante["name"].lower().replace(" ", "")
            if(nombre == nombre[::-1]):
                lista_de_palindromos.append(restaurante)

    return lista_de_palindromos

def cambiar_lista(estados: dict) -> dict:
    nuevo_dict = {}
    for estado in estados:
        for restaurante in estados[estado]:
            if(restaurante["category"] not in nuevo_dict):
                nuevo_dict[restaurante["category"]] = []
                nuevo_dict[restaurante["category"]].append(restaurante)
                del restaurante["category"]

            else:
                nuevo_dict[restaurante["category"]].append(restaurante)
                del restaurante["category"]
    estados = nuevo_dict
    return nuevo_dict

print(cambiar_lista(cargar_restaurantes("restaurantes_prueba.csv")))

def buscar_restaurante_cercano(estados: dict, latitud_ref: float, longitud_ref: float) -> dict:
    '''Buscar el restaurante mas cercano de todos.

    Args:
        estados (dict): diccionario de estados
        latitud_ref (float): latitud del punto de partida
        longitud_ref (float): longitud del punto de partida

    Returns:
        dict: devuelve el restaurante mas cercano
    '''    
    distancia_pasada = 10000000000000 #Asumir que esta es la distancia mas grande al inicio
    indice_restaurante = 0
    indice_estado = ""
    for estado in estados: #Todos los estados
        for restaurante in range(len(estados[estado])): #Todos los restaurantes en el estado
            longitud = estados[estado][restaurante]["longitude"]
            latitud = estados[estado][restaurante]["latitude"]
            distancia = math.sqrt(((latitud_ref-latitud)**2  + (longitud_ref-longitud)**2))
            if(distancia < distancia_pasada):
                distancia_pasada = distancia
                indice_restaurante = restaurante
                indice_estado = estado
    return estados[indice_estado][indice_restaurante]

def buscar_restaurante_preferido(estados: dict, latitud_min: float, latitud_max: float, longitud_min: float, longitud_max: float, precio_maximo: str, minimo_reviews: int, rating_minimo: float) -> dict:
    '''Buscar el restaurante que se acople al usuario.

    Args:
        estados (dict): diccionario de estados
        latitud_min (float): latitud min
        latitud_max (float): latitud max
        longitud_min (float): longitud min
        longitud_max (float): longitud max
        precio_maximo (str): precio maximo "$"
        minimo_reviews (int): cantidad minima de reviews
        rating_minimo (float): rating minimo

    Returns:
        dict: devuelve el primer restaurante que cumpla con los parametros
    '''    
    restaurantes = buscar_restaurantes_en_area(estados, latitud_min, latitud_max, longitud_min, longitud_max)
    i = 0
    restaurante_encontrado = {}
    encontro_restaurante = False
    while i < len(restaurantes) and not encontro_restaurante:
        restaurante = restaurantes[i]
        precio = restaurante["price"]
        reviews = restaurante["review_count"]
        rating = restaurante["rating"]
        if(len(precio.split()) <= len(precio_maximo.split()) and float(reviews) >= minimo_reviews and float(rating) >= rating_minimo):
            encontro_restaurante = True
            restaurante_encontrado = restaurantes[i]

    return restaurante_encontrado