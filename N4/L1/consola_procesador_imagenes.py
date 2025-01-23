# -*- coding: utf-8 -*-

'''
Ejemplo Nivel 4: Visor de imágenes
'''

import procesador_imagenes as pi


def ejecutar_cargar_imagen(ruta: str) -> list:
    imagen = pi.cargar_imagen(ruta)
    if imagen:
        print('Imagen cargada éxitosamente\n')
        pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_binarizar_imagen(imagen: list) -> list:
    umbral = float(input('Ingrese el umbral para binarizar (valor entre 0 y 1): '))
    print('Procesando imagen...')
    imagen = pi.binarizar_imagen(imagen, umbral)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_convertir_negativo(imagen: list) -> list:
    print('Procesando la imagen...')
    imagen = pi.convertir_negativo(imagen)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_reflejar_imagen(imagen: list) -> list:
    print('Procesando la imagen...')
    imagen = pi.reflejar_imagen(imagen)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_convertir_a_grises(imagen: list) -> list:
    print('Procesando la imagen...')
    imagen = pi.convertir_a_grises(imagen)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_ajustar_brillo(imagen: list) -> list:
    ajuste = float(input('Ingrese el ajuste de brillo (valor entre -1 y 1): '))
    print('Procesando la imagen...')
    imagen = pi.ajustar_brillo(imagen, ajuste)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_aplicar_filtro_umbral(imagen: list) -> list:
    umbral = float(input('Ingrese el umbral para colorear rojo (valor entre 0 y 1): '))
    print('Procesando la imagen...')
    imagen = pi.aplicar_filtro_umbral(imagen, umbral)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_aplicar_filtro_sepia(imagen: list) -> list:
    print('Procesando la imagen...')
    imagen = pi.aplicar_filtro_sepia(imagen)
    pi.visualizar_imagen(imagen)
    return imagen


def ejecutar_obtener_coordenadas_pixel_verde(imagen: list) -> list:
    print('Buscando el pixel totalmente verde...')
    coordenadas = pi.buscar_pixel_verde(imagen)
    if coordenadas:
        print(f'Se encontró un pixel totalmente verde en las coordenadas: {coordenadas}\n')
    else:
        print('No se encontró el pixel totalmente verde.')


def ejecutar_aplicar_filtro_personalizado(imagen: list) -> list:
    # Cambie esta función si necesita solicitar al usuario datos:
    print('Procesando la imagen...')
    imagen = pi.aplicar_filtro_personalizado(imagen)
    pi.visualizar_imagen(imagen)
    return imagen


def imprimir_menu_principal():
    '''
    Imprime los items del menú principal de la aplicación.
    '''
    print('*' * 50)
    print('PROCESADOR DE IMÁGENES')
    print('*' * 50)
    print('1. Cargar imagen')
    print('2. Restaurar imagen original')
    print('3. Negativo')
    print('4. Reflejar')
    print('5. Binarizar')
    print('6. Escala de grises')
    print('7. Ajustar brillo')
    print('8. Aplicar filtro umbral')
    print('9. Aplicar filtro sepia')
    print('10. Obtener coordenadas del punto verde')
    print('11. Aplicar *filtro personalizado*')
    print('12. Salir')
    print('*' * 50, end='\n\n')
    
def procesar_opcion() -> None:
    salir = False
    imagen = None
    ruta = ''
    while not salir:
        imprimir_menu_principal()
        opcion = int(input('Ingrese la opción deseada: '))      
        if opcion == 1:
            ruta = input('Ingrese el nombre del archivo imagen o *Enter* para cargar la imagen de prueba: ')
            imagen = ejecutar_cargar_imagen(ruta)
        elif imagen and opcion != 12:
            if opcion == 2:
                print('Restaurando la imagen original...')
                imagen = ejecutar_cargar_imagen(ruta)
            elif opcion == 3:
                imagen = ejecutar_convertir_negativo(imagen)
            elif opcion == 4:
                imagen = ejecutar_reflejar_imagen(imagen)
            elif opcion == 5:
                imagen = ejecutar_binarizar_imagen(imagen)
            elif opcion == 6:
                imagen = ejecutar_convertir_a_grises(imagen)
            elif opcion == 7:
                imagen = ejecutar_ajustar_brillo(imagen)
            elif opcion == 8: 
                imagen = ejecutar_aplicar_filtro_umbral(imagen)
            elif opcion == 9: 
                imagen = ejecutar_aplicar_filtro_sepia(imagen)
            elif opcion == 10: 
                ejecutar_obtener_coordenadas_pixel_verde(imagen)
            elif opcion == 11: 
                imagen = ejecutar_aplicar_filtro_personalizado(imagen)
        elif opcion == 12:
            print('\nCerrando el procesador de imágenes...\n')
            salir = True
        else:
            if not imagen:
                print('\nError: No se ha cargado ninguna imagen.\n')
            else:
                print('\nError: El valor ingresado es inválido.')

procesar_opcion()