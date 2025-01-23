# -*- coding: utf-8 -*-
"""
Aplicación de Empresas Colombianas

@author: Cupi2
"""

import pandas as pd
import empresas as e

# Funciones para visualización de la matriz (se usan únicamente en la función: ejecutar_crear_matriz())
    
def imprimir_matriz(info_matriz: tuple) -> None:
    """
    Imprime la matriz de utilidades por macrosector y departamento en un formato tabular simple.

    La primera columna (departamentos) tiene un ancho de 25, mientras que las demás columnas tienen un ancho de 13.
    """
    matriz, departamentos, macrosectores = info_matriz
    print("Matriz de utilidades por macrosector y departamento:")

    # Ancho de la primera columna y el resto:
    ancho_primera_columna = 25
    ancho_otras_columnas = 13

    # Crea el encabezado de la tabla con bordes superiores:
    header = ajustar_texto("Deptos / Macros", ancho_primera_columna)
    for j in range(len(macrosectores)):
        header += ajustar_texto(macrosectores[j], ancho_otras_columnas)
    border_line = "+" + "-" * (len(header) - 2) + "+"  # Línea de borde superior e inferior
    
    print(border_line)  # Borde superior
    print("|" + header + "|")  # Encabezado con bordes laterales
    print(border_line)  # Línea divisoria debajo del encabezado

    # Imprime cada fila de la matriz:
    for i in range(len(departamentos)):
        # Cada fila comienza con el nombre del departamento:
        row = ajustar_texto(departamentos[i], ancho_primera_columna)
        
        # Añade cada valor de utilidad, ajustado al ancho de las demás columnas:
        for j in range(len(macrosectores)):
            row += ajustar_texto(str(matriz[i][j]), ancho_otras_columnas)
        
        print("|" + row + "|")  # Fila con bordes laterales
    
    print(border_line)  # Borde inferior

def ajustar_texto(texto: str, longitud: int) -> str:
    """
    Ajusta el texto a una longitud específica.

    Si el texto es más corto que la longitud, se rellena con espacios al final.

    Parámetros:
        texto (str): Texto a ajustar.
        longitud (int): Longitud deseada del texto ajustado.

    Retorno:
        str: Texto ajustado a la longitud especificada.
    """
    return texto + " " * (longitud - len(texto))
####


# Funciones de ejecución:
    
def ejecutar_graficar_top_20_departamentos_con_mas_macroempresas(dataframe: pd.DataFrame) -> None:
    """
    Ejecuta la función que genera un gráfico de barras horizontal de los 20 departamentos con más macroempresas.
    """
    e.top_20_departamentos_mas_macroempresas(dataframe)


def ejecutar_graficar_participacion_ingresos_por_region(dataframe: pd.DataFrame) -> None:
    """
    Ejecuta la opción que genera un pie chart que muestra la participación de cada región en el total de ingresos operacionales.
    """
    e.participacion_porcentual_ingresos_operacionales(dataframe)


def ejecutar_graficar_boxplot_distribucion_utilidades_por_region(dataframe: pd.DataFrame) -> None:
    """
    Ejecuta la función que genera un boxplot que muestra la distribución de las utilidades para una región específica.

    La función solicita al usuario el nombre de la región.
    """
    region = input("Ingrese la region a graficar: ")
    e.distribucion_utilidades_region(dataframe, region)


def ejecutar_crear_matriz(dataframe: pd.DataFrame) -> tuple:
    """
    Ejecuta la función que crea una matriz que representa la suma de la utilidad para cada MACROSECTOR en cada DEPARTAMENTO.
    
    Imprime la matriz usando la función imprimir_matriz() si está es no vacía e informa de error en caso contrario.

    Retorno:
        tuple: La tupla (matriz, departamentos, macrosectores) generada, donde cada posición (f, c) en matriz muestra la
               utilidad total para un macrosector en un departamento, departamentos es una lista que contiene los nombres 
               de los departamentos (en el mismo orden que las filas de la matriz) y macrosectores es una lista que contiene 
               los nombres de los macrosectores (en el mismo orden que las columnas de la matriz).
    """
    matriz_info = e.crear_matriz(dataframe)
    
    if matriz_info is not None and len(matriz_info) == 3:
        matriz, departamentos, macrosectores = matriz_info
        if matriz != [] and departamentos != [] and macrosectores != []:
            imprimir_matriz(matriz_info)
    else:
        print("Error: La matriz no se ha creado correctamente.")
        
    return matriz_info


def ejecutar_suma_utilidad_macrosector(matriz_info: tuple) -> None:
    """
    Ejecuta la función que suma las utilidades para el macrosector dado por parámetro usando la matriz.

    La función le solicita al usuario el macrosector a evaluar y muestra como resultado la suma de utilidades en formato:
    "La suma de utilidades para el macrosector {Nombre del macrosector consultado} es {Suma de utilidades}."
    """
    macrosector = input("Ingrese el macrosector a sumar: ")
    print(f"La suma de utilidades para el macrosector {macrosector} es {e.suma_utilidades_macrosector(matriz_info, macrosector.upper())}")


def ejecutar_suma_utilidades_todos_macrosectores(matriz_info: tuple) -> None:
    """
    Ejecuta la función que suma las utilidades de cada macrosector usando la matriz.

    Para cada macrosector, se muestra un mensaje en el formato:
    "La suma de utilidades para el macrosector {Nombre del macrosector consultado} es {Suma de utilidades}."
    """
    diccionario = e.suma_utilidades_totales(matriz_info)
    for macrosector in diccionario:
        print(f"La suma de utilidades de {macrosector.lower()} es de {diccionario[macrosector]}")



def ejecutar_primera_utilidad_negativa(matriz_info: tuple) -> None:
    """
    Ejecuta la función que detecta la primera utilidad negativa (pérdida) en la matriz y retorna la tupla correspondiente
        con DEPARTAMENTO, MACROSECTOR y UTILIDAD.

    Si se encuentra una utilidad negativa, muestra el mensaje:
    "La primera utilidad negativa fue detectada en el departamento {Nombre del departamento} para el macrosector {Nombre del macrosector consultado} con un valor de {Utilidad negativa}."

    Si no se encuentra, muestra:
    "No se encontró ninguna utilidad negativa en la matriz."
    """
    resultado = e.encontrar_primera_utilidad_negativa(matriz_info)
    if(resultado is None):
        print("No se encontró ninguna utilidad negativa en la matriz.")
    else:
        print(f"La primera utilidad negativa fue detectada en el departamento {resultado[0]} para el macrosector {resultado[1]} con un valor de {resultado[2]}.")


def ejecutar_mapa_utilidades(matriz_info: tuple) -> None:
    """
    Ejecuta la función que genera un mapa de Colombia con cada departamento coloreado según la utilidad del macrosector especificado.

    La función le solicita al usuario el macrosector para el cual se desea visualizar la utilidad en el mapa.
    """
    macrosector = input("Ingrese el macrosector a graficar: ")
    e.graficar_mapa(matriz_info, macrosector.upper())


# Menú principal de la aplicación:
def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación de análisis de información de macroempresas.
    """
    archivo = input("Ingrese el nombre del archivo de datos o presione Enter si este se llama empresas.csv: ")
    if archivo == "":
        archivo = "empresas.csv"
    empresas = e.cargar_datos(archivo)
    matriz_info = None
    print("\nDatos cargados exitosamente.\n")
    ejecutando = True
    print("#"*70)
    print("Bienvenido a la aplicación de análisis de macroempresas de Colombia.")
    print("#"*70)
    while ejecutando == True:
        ejecutando, matriz_info = mostrar_menu_aplicacion(empresas, matriz_info)
        if ejecutando == True:
            input("Presione Enter para continuar...")

def mostrar_menu_aplicacion(empresas: pd.DataFrame, matriz_info) -> bool:
    print("\nMenú de opciones:")
    print("1. Graficar top 20 departamentos con más macroempresas.")
    print("2. Graficar participación porcentual de ingresos por región.")
    print("3. Graficar boxplot de distribución de utilidades por región.")
    print("4. Crear matriz de utilidades por macrosector y departamento.")
    print("5. Sumar utilidades para un macrosector específico.")
    print("6. Sumar utilidades de todos los macrosectores.")
    print("7. Buscar primera utilidad negativa.")
    print("8. Graficar mapa de utilidades por departamento para un macrosector.")
    print("9. Salir")

    opcion = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True
    
    MSG_INFO = "Error: Primero debe crear la matriz de utilidades (opción 4)."

    if opcion == "1":
        ejecutar_graficar_top_20_departamentos_con_mas_macroempresas(empresas)
    elif opcion == "2":
        ejecutar_graficar_participacion_ingresos_por_region(empresas)
    elif opcion == "3":
        ejecutar_graficar_boxplot_distribucion_utilidades_por_region(empresas)
    elif opcion == "4":
        matriz_info = ejecutar_crear_matriz(empresas)
    elif opcion == "5":
        if matriz_info is not None:
            ejecutar_suma_utilidad_macrosector(matriz_info)
        else:
            print(MSG_INFO)
    elif opcion == "6":
        if matriz_info is not None:
            ejecutar_suma_utilidades_todos_macrosectores(matriz_info)
        else:
            print(MSG_INFO)
    elif opcion == "7":
        if matriz_info is not None:
            ejecutar_primera_utilidad_negativa(matriz_info)
        else:
            print(MSG_INFO)
    elif opcion == "8":
        if matriz_info is not None:
            ejecutar_mapa_utilidades(matriz_info)
        else:
            print(MSG_INFO)
    elif opcion == "9":
        print("¡Gracias por usar la aplicación de análisis de macroempresas!")
        continuar_ejecutando = False
    else:
        print("Opción inválida. Inténtelo de nuevo.")

    return continuar_ejecutando, matriz_info

# Punto de entrada de la aplicación:
if __name__ == "__main__":
    iniciar_aplicacion()