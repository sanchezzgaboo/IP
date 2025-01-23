import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.util import random_noise


def cargar_imagen(ruta_imagen: str) -> list:
    '''
    Carga una imagen desde una ruta especificada y 
    la convierte en una lista.

    Parámetros:
        ruta_imagen (str): La ruta de la imagen a cargar.

    Retorna:
        (list): Una lista tridimensional que representa 
        la imagen cargada. Cada elemento de la lista es un 
        valor de píxel en el rango de 0 a 1.

    Nota: El método list.tolist() se utiliza para convertir 
    a una lista de Python.
    '''

    return mpimg.imread(ruta_imagen).tolist()

def convolucion_imagen(imagen: list, convolucion: list)->list:
    """ Convolución (matriz de tuplas)
    Parámetros:
      imagen (list): Matriz que representa la imagen.
      convolucion (list): Matriz de 3x3 de convolución (O VALOR IMPAR SIEMPRE)
    Retorno:
      list: Matriz que representa la imagen después de que se le aplique la convolución
    """
    imagen_original = imagen.copy()
    x = len(convolucion) // 2 #Encontrar el centro de la lista convolucion (x)
    y = len(convolucion[0]) //2 #Encontrar el centro de la lista convolucion (y)
    suma_convolucionR = 0
    suma_convolucionG = 0
    suma_convolucionB = 0
    for filaC in range(len(convolucion)):
        for columnaC in range(len(convolucion[0])):
            suma_convolucionR += convolucion[filaC][columnaC][0]
            suma_convolucionG += convolucion[filaC][columnaC][1]
            suma_convolucionB += convolucion[filaC][columnaC][2]
  
    for fila in range(len(imagen)):
        for columna in range(len(imagen[0])):
            productoR = 0
            productoG = 0
            productoB = 0
            #Detectar casos esquinas y determinar que la convolucion se haga 
            # con los valores mas cercanos en caso de que sea inexistente
            if(fila == 0 and columna == 0 ): #Si es la primer esquina, solo multiplicar con 4, 5, 7, 8
                for i in range(x+1):
                    for k in range(y+1): #Recorrer -> Actual, Derecha, Abajo del actual, Abajo Derecha
                        productoR += convolucion[x+i][y+k][0]*imagen_original[fila + i][columna + k][0]
                        productoG += convolucion[x+i][y+k][1]*imagen_original[fila + i][columna + k][1]
                        productoB += convolucion[x+i][y+k][2]*imagen_original[fila + i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB

            elif(fila == 0 and columna == len(imagen[0]) - 1): #SI es la segunda esquina, solo mult. con 3,4,6,7
                for i in range(x+1):
                    for k in range(y+1):
                        productoR += convolucion[x+i][y-k][0]*imagen_original[fila + i][columna - k][0]
                        productoG += convolucion[x+i][y-k][1]*imagen_original[fila + i][columna - k][1]
                        productoB += convolucion[x+i][y-k][2]*imagen_original[fila + i][columna - k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
            elif(fila == len(imagen)-1 and columna == 0): #Si es la tercera esquina, solo mult 1,2,4,5 
                for i in range(x+1):
                    for k in range(y+1):
                        productoR += convolucion[x-i][y+k][0]*imagen_original[fila - i][columna + k][0]
                        productoG += convolucion[x-i][y+k][1]*imagen_original[fila - i][columna + k][1]
                        productoB += convolucion[x-i][y+k][2]*imagen_original[fila - i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
            elif(fila == len(imagen)-1 and len(imagen[0]) - 1): #Si es la cuarta esquina, solo mult. 0,1,3,4
                for i in range(x+1):
                    for k in range(y+1):
                        productoR += convolucion[x-i][y-k][0]*imagen_original[fila - i][columna - k][0]
                        productoG += convolucion[x-i][y-k][1]*imagen_original[fila - i][columna - k][1]
                        productoB += convolucion[x-i][y-k][2]*imagen_original[fila - i][columna - k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB

            #Detectar casos paredes y determinar los valores mas cercanos en caso de ser inexistente.
            
            elif((fila == 0 and (columna != 0 or columna != len(imagen[0]) - 1))): #Caso Pared arriba
                for i in range(x+1):
                    for k in range((-1)*y, y+1): #Para acceder izquierda y derecha
                        productoR += convolucion[x+i][y+k][0] * imagen_original[fila + i][columna + k][0]
                        productoG += convolucion[x+i][y+k][1] * imagen_original[fila + i][columna + k][1]
                        productoB += convolucion[x+i][y+k][2] * imagen_original[fila + i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
            
            elif((fila == len(imagen) - 1 and (columna != 0 or columna != len(imagen[0]) - 1))): #Caso pared abajo
                for i in range(x+1):
                    for k in range((-1)*y, y+1): #Para acceder izquierda y derecha
                        productoR += convolucion[x-i][y+k][0]*imagen_original[fila - i][columna + k][0]
                        productoG += convolucion[x-i][y+k][1]*imagen_original[fila - i][columna + k][1]
                        productoB += convolucion[x-i][y+k][2]*imagen_original[fila - i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
             
            elif(columna == 0 and (fila != 0 or fila != len(imagen) - 1)): #Caso Pared Izq.
                for i in range(-1 * x, x+1):#Para acceder arriba y abajo
                    for k in range(y+1): 
                        productoR += convolucion[x+i][y+k][0]*imagen_original[fila + i][columna + k][0]
                        productoG += convolucion[x+i][y+k][1]*imagen_original[fila + i][columna + k][1]
                        productoB += convolucion[x+i][y+k][2]*imagen_original[fila + i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
            
            elif(columna == len(imagen[0])- 1 and (fila != 0 or fila != len(imagen) - 1)): #Caso Pared Derecha
                for i in range(-1 * x, x+1):#Para acceder arriba y abajo
                    for k in range(y+1): 
                        productoR += convolucion[x+i][y-k][0]*imagen_original[fila + i][columna - k][0]
                        productoG += convolucion[x+i][y-k][1]*imagen_original[fila + i][columna - k][1]
                        productoB += convolucion[x+i][y-k][2]*imagen_original[fila + i][columna - k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB
            
            #Caso interno

            else:
                for i in range(-1 *x , x+1):#Para acceder arriba y abajo
                    for k in range(-1 * y, y+1): 
                        productoR += convolucion[x+i][y+k][0]*imagen_original[fila + i][columna + k][0]
                        productoG += convolucion[x+i][y+k][1]*imagen_original[fila + i][columna + k][1]
                        productoB += convolucion[x+i][y+k][2]*imagen_original[fila + i][columna + k][2]

                imagen[fila][columna][0] = productoR/suma_convolucionR
                imagen[fila][columna][1] = productoG/suma_convolucionG
                imagen[fila][columna][2] = productoB/suma_convolucionB

    return imagen

convolucion = cargar_imagen("convolucionRGB.png")
imagen = cargar_imagen("kirby.png")
x = len(imagen)//2
y = len(imagen[0])//2
nueva_img = convolucion_imagen(imagen, convolucion)
plt.imshow(nueva_img)
plt.show()