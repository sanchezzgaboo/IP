# -*- coding: utf-8 -*-
"""
Aplicación de Empresas Colombianas

@author: Cupi2
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as mpatches

def cargar_datos(ruta: str) -> pd.DataFrame:
    '''Carga los datos del archivo csv

    Args:
        ruta (str): ruta del archivo csv

    Returns:
        pd.DataFrame: devuelve un dataframe del archivo
    '''    
    datos = pd.read_csv(ruta)
    return datos

def top_20_departamentos_mas_macroempresas(df: pd.DataFrame) -> None:
    '''utiliza el dataframe y crea una grafica de barras horizontal con los departamentos y el numero de empresas 
    en cada departamento

    Args:
        df (pd.DataFrame): datos del csv
    '''    
    regiones = df["DEPARTAMENTO"].value_counts().head(20)
    ax = regiones.plot(kind='barh', figsize=(12, 10), fontsize='small')
    ax.set_xlabel("Numero de Macroempresas", fontsize=12)
    ax.set_ylabel("Departamento", fontsize=12)
    ax.set_title("Top 20 Departamentos con Mas Macroempresas.", fontsize=12)
    ax.invert_yaxis()
    ax.figure.tight_layout()
    plt.show()

def participacion_porcentual_ingresos_operacionales(df: pd.DataFrame) -> None:
    '''genera un piechart de la participacion porcentual de cada region dados sus ingresos operacionales.

    Args:
        df (pd.DataFrame): dataframe de los datos.
    '''    
    participacion = df.groupby('REGION')["INGRESOS_OP"].sum().sort_values(ascending=False)
 
    ax = participacion.plot(kind='pie', figsize=(12, 10), legend=True, label="", autopct="%1.1f%%")
    ax.figure.tight_layout()
    plt.show()

def distribucion_utilidades_region(df: pd.DataFrame, region: str) -> None:
    '''Crea boxplots de las utilidades totales

    Args:  
        df (pd.DataFrame): datos de csv en formato dataframe.
    '''    
    if region in df["REGION"].unique():

        df_region = df[df["REGION"] == region]
        utilidad = pd.Series(df_region["UTILIDAD"])
        
        df_region = {f"{region}": utilidad}
        df_utilidad_region = pd.DataFrame(data=df_region)
        ax = df_utilidad_region.boxplot(column= [f"{region}"])

        ax.figure.tight_layout()
        plt.show()

# Requerimiento 5:
def crear_matriz(dataframe: pd.DataFrame) -> tuple:
    """
    Crea una matriz que representa la suma de la utilidad para cada MACROSECTOR en cada DEPARTAMENTO.

    Parámetros:
        dataframe (pd.DataFrame): DataFrame que contiene los datos de las macroempresas.

    Retorno:
        tuple: Una tupla que contiene:
            - list: Matriz bidimensional con la utilidad por DEPARTAMENTO y MACROSECTOR.
                    La utilidad permanece en billones de pesos, redondeada a dos cifras decimales.
            - list: Lista de DEPARTAMENTO, en el mismo orden de las filas de la matriz.
            - list: Lista de MACROSECTOR, en el mismo orden de las columnas de la matriz.
    """
    # Obtiene listas únicas y ordenadas de DEPARTAMENTO y MACROSECTOR:
    departamentos = dataframe["DEPARTAMENTO"].sort_values().unique().tolist()
    macrosectores = dataframe["MACROSECTOR"].sort_values().unique().tolist()
    # Inicializa una lista vacía para almacenar la matriz bidimensional de utilidades,
    # donde cada sublista representará a las utilidades por macrosector para un departamento:
    matriz = []
    organizado = dict(dataframe.groupby(["DEPARTAMENTO", "MACROSECTOR"])['UTILIDAD'].sum())
    for departamento in departamentos:
        sectores = []
        for macrosector in macrosectores:
            if (departamento, macrosector) in organizado:
                sectores.append(round(organizado[departamento,macrosector],2))
            else:
                sectores.append(0.0)
        matriz.append(sectores[::]) #Copia por si acaso el valor cambia no se
    return (matriz, departamentos, macrosectores)



def suma_utilidades_macrosector(matriz: tuple, macrosector: str) -> float:
    '''suma las utilidades por macrosector

    Args:
        matriz (tuple): la matriz en forma de tuple (valores, departamento, macrosector)
        macrosector (str): el macrosector a sumar

    Returns:
        float: suma de utilidades por macrosector redondeado a 2 cifras
    '''    
    suma = 0
    if macrosector in matriz[2]:
        indice_macrosector = 0
        encontrado = False
        while indice_macrosector < len(matriz[2]) and not encontrado:
            if(macrosector == matriz[2][indice_macrosector]):
                encontrado = True
            else:
                indice_macrosector +=1
        for departamento in range(len(matriz[1])):
            suma += matriz[0][departamento][indice_macrosector] 
    return round(suma,2)

def suma_utilidades_totales(matriz: tuple) -> float:
    '''suma de todas las utilidades de todos los macrosectores de todos los departamentos.

    Args:
        matriz (tuple): la matriz en forma de tuple (valores, departamento, macrosector)


    Returns:
        float: suma de todas las utilidades de todos los departamentos de todos los macrosectores.
    '''    
    suma = {}
    for macrosector in range(len(matriz[2])):
        suma[matriz[2][macrosector]] = suma_utilidades_macrosector(matriz, matriz[2][macrosector])
    return suma



def encontrar_primera_utilidad_negativa(matriz: tuple) -> tuple:
    '''encuentra la primera utilidad negativa de la matriz.

    Args:
        matriz (tuple): la matriz en forma de tuple (valores, departamento, macrosector)


    Returns:
        tuple: devuelve las coordenadas de la primera utilidad negativa y su correspondiente valor. (departamento, macrosector, valor)
    '''    
    valor_retorno = (None, None, None)
    encontrado = False
    departamento = 0
    while departamento < len(matriz[1]) and not encontrado:
        macrosector = 0
        while macrosector < len(matriz[2]) and not encontrado:
            if matriz[0][departamento][macrosector] < 0:
                valor_retorno = (matriz[1][departamento], matriz[2][macrosector], matriz[0][departamento][macrosector])
                encontrado = True
            else:
                macrosector += 1
        departamento += 1
    return valor_retorno

# Función auxiliar para el Requerimiento 9 (OPCIONAL):
# IMPORTANTE: El Requerimiento 9 es opcional y no afectará su calificación negativamente si decide no implementarlo. 
# Si lo implementa correcta y completamente, obtendrá un bono.
def cargar_coordenadas(nombre_archivo: str) -> dict:
    """
    Carga las coordenadas de los departamentos de Colombia desde un archivo de texto.

    El archivo de texto tiene el siguiente formato:
    DEPARTAMENTO;X;Y
    AMAZONAS;100;200
    ANTIOQUIA;300;400 
    ...
    
    Parámetros:
        nombre_archivo (str): Nombre del archivo de texto que contiene las coordenadas de los departamentos.

    Retorno:
        dict: Diccionario donde las llaves son los nombres de los departamentos y los valores son tuplas
              con las coordenadas (x, y) de cada departamento.
    """   
    deptos = {}
    
    archivo = open(nombre_archivo, encoding="utf8")
    archivo.readline()
    linea = archivo.readline()
    
    while len(linea) > 0:
        linea = linea.strip()
        datos = linea.split(";")
        # Almacena el nombre del departamento y sus coordenadas (x, y) en el diccionario:
        deptos[datos[0]] = (int(datos[1]),int(datos[2]))
        linea = archivo.readline()

    archivo.close()
    
    return deptos

def graficar_mapa(matriz: tuple, macrosector: str) -> None:
    '''grafica el mapa de colombia con un cuadrado con el color correspondiente a los valores de la utilidad del macrosector

    Args:
        matriz (tuple): la matriz en forma de tuple (valores, departamento, macrosector)
        macrosector (str): macrosector a graficar
    '''    
    mapa = mpimg.imread("mapa.png")
    
    coordenadas = cargar_coordenadas("coordenadas.txt") #X y Y ESTAN AL REVES
    fig, ax = plt.subplots()
    ax.imshow(mapa)
    ax.axis("off")
    colores = { 
    "< 0": [0.15, 0.15, 0.66], 
    "0 a <0.1": [0.38, 0.65, 0.87], 
    "0.1 a <1": [0.56, 0.93, 0.56], 
    "1 a <10": [0.95, 0.90, 0.25], 
    "10 a <50": [0.98, 0.65, 0.13], 
    ">=50": [0.84, 0.15, 0.15] 
    }
    if macrosector in matriz[2]:
        indice_macrosector = matriz[2].index(macrosector)
        for departamento in range(len(matriz[1])):
            cords = coordenadas[matriz[1][departamento]][::-1] #Arreglar X Y
            x = cords[0]
            y = cords[1]
            if(matriz[0][departamento][indice_macrosector] < 0) : 
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores["< 0"], rotation_point="center"))
            elif(0<=matriz[0][departamento][indice_macrosector] < 0.1):
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores["0 a <0.1"], rotation_point="center"))
            elif(0.1<=matriz[0][departamento][indice_macrosector] < 1):
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores["0.1 a <1"], rotation_point="center"))
            elif(1<=matriz[0][departamento][indice_macrosector] < 10):
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores["1 a <10"], rotation_point="center"))
            elif(10<=matriz[0][departamento][indice_macrosector] < 50):
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores["10 a <50"], rotation_point="center"))
            elif(matriz[0][departamento][indice_macrosector] >= 50):
                ax.add_patch(mpatches.Rectangle([x-13/2,y-13/2], 13, 13, facecolor=colores[">=50"], rotation_point="center"))
    
    legends = [] 
    for i in colores: 
        legends.append(mpatches.Patch(color=colores[i], label=i)) 
        plt.legend(handles=legends, loc=3, fontsize="large") 
        plt.title( "Utilidad por departamento en el macrosector '{}'".format(macrosector), fontsize="large" ) 
    plt.show()