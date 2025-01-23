# -*- coding: utf-8 -*-

'''

Ejemplo Nivel 4: Visor de imágenes
'''

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from matplotlib.colors import rgb_to_hsv


def cargar_imagen(ruta_imagen: str) -> list:
    '''
    Carga una imagen desde una ruta especificada y la convierte en una lista.

    Parámetros:
        ruta_imagen (str): La ruta de la imagen a cargar.

    Retorna:
        (list): Una lista tridimensional que representa la imagen cargada.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Nota: El método list.tolist() se utiliza para convertir la matriz en una lista de Python.
    Esto puede ser útil para la manipulación de datos y la compatibilidad con otras librerías de Python.
    '''
    imagen = None
    if ruta_imagen !='':
        try:
            imagen = mpimg.imread(ruta_imagen).tolist()
        except FileNotFoundError:
            print(f'Error: no se encontró la imagen en la ruta proporcionada: {ruta_imagen}\n\n')
    else:
        # Imagen de prueba para practicar:
        imagen = [
            [  # Primera fila de píxeles
                [1.0, 1.0, 0.0],  # Primer píxel: Amarillo
                [1.0, 1.0, 0.0],  # Segundo píxel: Amarillo
                [0.0, 1.0, 0.0]   # Tercer píxel: Verde
            ],
            [  # Segunda fila de píxeles
                [0.0, 0.0, 1.0],  # Cuarto píxel: Azul
                [0.0, 0.0, 1.0],  # Quinto píxel: Azul
                [0.0, 0.0, 0.0]   # Sexto píxel: Negro
            ],
            [  # Tercera fila de píxeles
                [1.0, 0.0, 0.0],  # Séptimo píxel: Rojo
                [1.0, 0.0, 0.0],  # Octavo píxel: Rojo
                [1.0, 1.0, 1.0]   # Noveno píxel: Blanco
            ]
        ]

    return imagen


def visualizar_imagen(imagen: list) -> None:
    '''
    Visualiza una imagen a partir de una lista.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna: 
        None: La función sólo muestra la imagen.

    Nota: Esta función utiliza matplotlib.pyplot.imshow(...) para visualizar la imagen y 
    matplotlib.pyplot.show() para mostrarla.
    '''
    plt.imshow(imagen)
    plt.show()


def convertir_negativo(imagen: list) -> list:
    '''
    Convierte una imagen a negativo.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna:
        (list): Imagen convertida a negativo.

    Nota: Se calcula restando cada componente RGB de 1.
    '''
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            for componente in range(3):
                imagen[fila][columna][componente] = 1 - imagen[fila][columna][componente]
    return imagen


def reflejar_imagen(imagen: list) -> list:
    '''
    Refleja una imagen horizontalmente.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna:
        (list): Imagen reflejada.

    Nota: Intercambia las columnas desde los extremos hacia el centro.
    Tips: Solo es necesario recorrer hasta la mitad de cada fila.
    '''
    for fila in range(len(imagen)//2):
        valor_arriba = imagen[fila]
        valor_abajo = imagen[len(imagen) - 1 - fila]
        imagen[fila] = valor_abajo
        imagen[len(imagen) - 1 - fila] = valor_arriba
    return imagen


def binarizar_imagen(imagen: list, umbral: float) -> list:
    '''
    Binariza una imagen usando un umbral.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.
        umbral (float): Umbral de binarización (0 a 1).

    Retorna:
        (list): Imagen binarizada.

    Nota: Si el promedio de RGB es mayor o igual al umbral, se convierte en blanco; si no, en negro.
    Tips: Use `sum(...)` para calcular el promedio de manera eficiente.
    '''
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            if(sum(imagen[fila][columna])/3 >= umbral):
                imagen[fila][columna] = [255, 255, 255]
            else:
                imagen[fila][columna] = [0, 0, 0]
    return imagen


def convertir_a_grises(imagen: list) -> list:
    '''
    Convierte una imagen a escala de grises.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna: 
        (list): La imagen en escala de grises.

    Nota: El promedio de los componentes RGB se usa para crear un color gris uniforme.
    Tips: Multiplique el promedio por 3 para crear un tono de gris.
    '''
    # TODO3: Complete la función tal y como se describe en la documentación.
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            promedio = sum(imagen[fila][columna])/3
            imagen[fila][columna] = [3*promedio, 3*promedio, 3*promedio]
    return imagen


def ajustar_brillo(imagen: list, ajuste: float) -> list:
    '''
    Ajusta el brillo de una imagen.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.
        ajuste (float): El valor de ajuste de brillo (se asume entre -1 y 1).

    Retorna: 
        (list): La imagen con el brillo ajustado.

    Nota: Suma el ajuste a cada componente RGB y limita los valores entre 0 y 1.
    Tips: Use `max()` y `min()` para mantener los valores dentro del rango.
    '''
    # TODO4: Complete la función tal y como se describe en la documentación.
    for fila in range(len(imagen)):
        for columa in range(len(imagen[0])):
            ajustes = [(imagen[fila][columa][0] + imagen[fila][columa][0]*ajuste ), (imagen[fila][columa][1] + imagen[fila][columa][1]*ajuste ), (imagen[fila][columa][2] + imagen[fila][columa][2]*ajuste )]
            imagen[fila][columa] = ajustes
    return imagen


def aplicar_filtro_umbral(imagen: list, umbral: float) -> list:
    '''
    Aplica un filtro de umbral a una imagen.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.
        umbral (float): El umbral para el filtro.

    Retorna: 
        (list): La imagen con el filtro de umbral aplicado.

    Nota: Si el promedio de RGB supera el umbral dado, el píxel se convierte a rojo.
    '''
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            if (sum(imagen[fila][columna]) / 3) > umbral:
                imagen[fila][columna] = [1, 0, 0]  # Rojo
    return imagen


def aplicar_filtro_sepia(imagen: list) -> list:
    '''
    Aplica un filtro sepia a la imagen.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna: 
        (list): La imagen con el filtro sepia aplicado.

    Nota: El filtro sepia se aplica ajustando los valores de los componentes RGB de cada píxel de la imagen 
    de acuerdo con las siguientes fórmulas:
        R' = 0.393R + 0.769G + 0.189B
        G' = 0.349R + 0.686G + 0.168B
        B' = 0.272R + 0.534G + 0.131B
    Si algún valor R', G' o B' es mayor que 1, se establece en 1.
    '''
    # TODO5: Complete la función tal y como se describe en la documentación.
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            R = imagen[fila][columna][0]
            G = imagen[fila][columna][1]
            B = imagen[fila][columna][2]
            
            imagen[fila][columna] = (0.393*R + 0.769*G + 0.189*B, 0.349*R + 0.686*G + 0.168*B, 0.272*R + 0.534*G + 0.131*B)
            
    
    return imagen


def buscar_pixel_verde(imagen: list) -> tuple:
    '''
    Busca un pixel totalmente verde en una imagen.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna: 
        (tuple): Coordenadas (fila, columna) del primer píxel verde encontrado.
        Si no se encuentra ningún píxel verde, devuelve None.

    Nota: El recorrido se detiene tan pronto como se encuentra el píxel verde.
    '''
    coordenadas = None
    encontrado = False
    i = 0
    k = 0
    while i < len(imagen) and not encontrado:
        while k < len(imagen[0]):
            if imagen[i][k] == [0,1,0]:
                coordenadas=(i,k)
                encontrado = True
            k += 1
        i += 1
    return coordenadas

def hueToRgb(p, q, t):
    retorno = 0
    if (t < 0): 
        t += 1
    if (t > 1):
        t -= 1
    if (t < 1/6): 
        retorno = p + (q - p) * 6 * t
    if (t < 1/2): 
        retorno = q
    if (t < 2/3): 
        retorno = p + (q - p) * (2/3 - t) * 6
    return retorno


def aplicar_filtro_personalizado(imagen: list) -> list:
    '''
    Cambia los colores puros encontrados (únicamente el verde, azul, negro y blanco) y
    aplica los colores de la bandera de Colombia en tres franjas de la imagen con un tamaño ajustado.

    Parámetros:
        imagen (list): Una lista tridimensional que representa la imagen a la que se va a aplicar el filtro.
        Cada elemento de la lista es un valor de píxel en el rango de 0 a 1.

    Retorna: 
        (list): La imagen con los filtros aplicados.
    '''
    # TODO7: Reemplace este filtro de ejemplo, por su filtro personalizado.
    
    #popart1
    imagen1 = imagen.copy()
    for fila in range(len(imagen1)):
        for columna in range(len(imagen1[0])):
            if(imagen1[fila][columna][2] > 0.5):
                imagen1[fila][columna] = [0,0,1]
    
    #popart2
    
    #popart3
    
    #popart4
    
    imagen.extend(imagen1)
    for fila in range(len(imagen)//2):
        imagen[fila].extend(imagen1[fila])
    
    return imagen