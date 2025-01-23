#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N4-L2
"""

import pandas as pd

#####################################################################################
# INSTRUCCIONES:
#####################################################################################   
# Complete uno a uno, todos los siguientes TODOs.
# IMPORTANTE: Es vital que lea y comprenda los enlaces a la documentación provista.
# No es necesario hacer ninguna entrega de este laboratorio.
# El laboratorio usa el dataset: The Movies Dataset, cuya versión original se encuentra en:
# https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
# El dataset contiene información de más de 45,000 películas.
#####################################################################################



# TODO 1:
# Asigne a `RUTA` un string con la *ruta completa* al archivo `movies.csv`.
# El archivo debe estar en su directorio de trabajo de Spyder.
# En Windows, use doble backslash para escapar: 'C:\\ruta\\completa\\movies.csv'.
# IMPORTANTE: Obtendrá un error (No such file or directory...) si no ingresa la ruta completa y correcta al archivo .csv.
RUTA = 'C:\\Users\\gsanc\\OneDrive\\Documents\\Python\\IP\\N4\\L2\\movies.csv'

# TODO 2:
# Revise el siguiente código. Si `RUTA` es correcta, cargará el archivo `movies.csv` en el DataFrame nombrado como `df`.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# Ignore esta advertencia si aparece:
# DtypeWarning: Columns (10) have mixed types. Specify dtype option on import or set low_memory=False.
df = pd.read_csv(RUTA)


########################################################
# EXPLORACIÓN DEL DATAFRAME:
########################################################

# TODO 3:
# Copie y pegue en la consola de Spyder (parte inferior derecha) el siguiente comando:
# df.shape
# Esto le mostrará el número de filas y columnas del DataFrame (en ese orden).
# Preguntas: ¿Cuántas filas (45466) y columnas (24) tiene?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html

# TODO 4:
# Copie y pegue en la consola:
# df.dtypes
# Esto le mostrará los tipos de datos y nombres de las columnas.
# Preguntas: ¿Cuál es el tipo de cada columna? ¿Cómo se llama cada columna?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html

# TODO 5:
# Copie y pegue en la consola:
# df.info()
# Esto le dará información general del DataFrame.
# Preguntas: ¿Cuántos elementos no nulos tiene cada columna? ¿Cuánta memoria ocupa?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

# TODO 6:
# Copie y pegue en la consola:
# pd.unique(df['title'])
# Esto mostrará los valores únicos en la columna 'title'.
# Puede usarlo en cualquier columna. Para ver todos los valores, convierta la salida en una lista.
# Remueva el comentario de ambas líneas y ejecútelas para ver la lista completa:
titulos_unicos = list(pd.unique(df['title']))
# Puede usar slicing para seleccionar:
print(titulos_unicos[:10])  # Muestra los primeros 10 títulos únicos
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.unique.html

# TODO 7:
# Copie y pegue en la consola:
# df.describe()
# Esto muestra estadísticas del DataFrame: count, mean, std, min, 25%, 50%, 75%, max.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html


########################################################
# ALGUNOS MÉTODOS ESTADÍSTICOS COMUNES:
########################################################

# TODO 8:
# Copie y pegue en la consola de Spyder (parte inferior derecha) el siguiente comando:
# df.min(skipna=True, numeric_only=True)
# Esto mostrará el mínimo de cada columna numérica.
# Los parámetros garantizan que se procesen solo valores numéricos y no nulos.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html

# TODO 9:
# Copie y pegue en la consola:
# df['runtime'].min()
# Esto mostrará la mínima duración de una película (columna 'runtime'): 0.0.
# Note que el método `min()` aquí se aplica solo a una columna.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.min.html

# TODO 10:
# Escriba en la consola un comando para mostrar el máximo de cada columna numérica.
# Preguntas: ¿Cuál es la máxima ganancia ('revenue') de una película? (2.787965e+09, es decir, 2787965087.0)
# ¿Cuál es la máxima duración ('runtime') de una película? (1.256000e+03, es decir, 1256.0)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.max.html

# TODO 11:
# Pregunta: ¿Cuál es la duración promedio ('runtime') de una película? (94.12819945578833)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html

# TODO 12:
# Pregunta: ¿Cuál es la desviación estándar de la columna 'vote_count'? (491.3103739397137)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.std.html

# TODO 13:
# Pregunta: ¿Cuántos votos se registraron en total para todas las películas ('vote_count')? (4995933.0)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html

# TODO 14:
# Copie y pegue en la consola de Spyder:
# df.head(1)
# Esto mostrará información de la primera fila del DataFrame.
# Si el resultado es incompleto, configure Pandas para mostrar más texto en la consola:
# Ejecute en la consola las tres siguientes líneas:
# pd.set_option('display.max_colwidth', None)  # Restablezca con pd.reset_option('display.max_colwidth')
# pd.set_option('display.max_row', 100)  # Muestra hasta 100 filas; ajuste el número según lo necesite
# pd.set_option('display.max_columns', 100)  # Muestra hasta 100 columnas; ajuste el número según lo necesite
# Vuelva a ejecutar: df.head(1) y observe el resultado.

# TODO 15:
# ¿Cómo mostraría la información de las primeras 5 filas?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html

# TODO 16:
# ¿Cómo mostraría la información de la última fila?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html

# TODO 17:
# ¿Cómo mostraría la información de las últimas 5 filas?
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html

# TODO 18:
# Copie y pegue en la consola de Spyder:
# df.columns
# Esto mostrará los nombres de todas las columnas del DataFrame.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html

# TODO 19:
# A veces es útil trabajar con un subconjunto del DataFrame original.
# La siguiente línea define una lista con las únicas columnas a copiar:
columnas_a_copiar = ['id', 'original_language', 'original_title', 'status', 'title', 'vote_count', 'revenue', 'runtime']
# La siguiente línea crea una copia independiente del subconjunto:
sub_df = df[columnas_a_copiar].copy()

# TODO 20:
# Use los comandos en la sección EXPLORACIÓN DEL DATAFRAME (más arriba)
# para explorar el nuevo DataFrame `sub_df` en lugar de `df`.

# TODO 21:
# Copie y pegue en la consola de Spyder:
# sub_df['original_language'].unique()
# Esto mostrará los valores únicos de la columna 'original_language'.
# Pregunta: ¿Hay alguna película cuyo idioma original sea Español ('es')?
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.unique.html

# TODO 22:
# Copie y pegue en la consola de Spyder:
# sub_df['original_language'].value_counts()
# Esto mostrará la frecuencia de cada idioma en la columna 'original_language'.
# Pregunta: ¿Cuántas películas tienen como idioma original Español ('es')? (994)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html

# TODO 23:
# ¿Leyó la documentación del método `value_counts()`?
# Si es así, ¿cuántas películas tienen el estado 'Released' en la columna 'status'? (Resultado esperado: 45014)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html


########################################################
# ORDENAMIENTO, FILTROS Y BÚSQUEDAS:
########################################################

# TODO 24:
# Copie y pegue en la consola de Spyder:
# sub_df.sort_values('title')
# Interprete el resultado y comprenda a cabalidad la función DataFrame.sort_values()
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# TODO 25:
# ¿Leyó la documentación del método `sort_values()`?
# Si es así, ¿cuál es el comando para ver las películas ordenadas de forma descendente por ganancia ('revenue')?
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

# TODO 26:
# Copie y pegue en la consola:
# sub_df.sort_values('revenue', ascending=False).head(5)
# Esto mostrará las 5 películas con las mayores ganancias.
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html

# TODO 27:
# Escriba en la consola el comando para obtener las 5 películas con las peores ganancias.
# Las películas deben incluir: 'La luna', 'Dear America: Letters Home from Vietnam', 'Code Black', 'The King of Arcades' y 'Anonymous Rex'.

# TODO 28:
# Copie y pegue en la consola de Spyder:
# sub_df[['title', 'revenue']].sort_values('revenue', ascending=False).head(5)
# Interprete el resultado.
# Note que se *filtran* solo dos columnas para facilitar la verificación de las 5 películas más rentables.

# TODO 29:
# Copie y pegue en la consola de Spyder:
# sub_df['runtime'] >= 90
# Interprete el resultado.
# Nota: Se muestra una Serie de valores booleanos (True o False) indicando si la duración de cada película es mayor o igual a 90 minutos.

# TODO 30:
# Copie y pegue en la consola:
# sub_df[sub_df['runtime'] >= 1000]
# Interprete el resultado.
# Nota: Se filtran las películas con un tiempo de duración de al menos 1000 minutos.

# TODO 31:
# Copie y pegue en la consola:
# (sub_df['runtime'] >= 1000).sum()
# Interprete el resultado (3).
# Nota: Se crea una Serie booleana y `.sum()` cuenta los valores True, indicando cuántas películas duran 1000 minutos o más.

# TODO 32:
# Copie y pegue la siguiente línea en la consola para obtener la información de la primera fila del DataFrame usando `iloc`:
# sub_df.iloc[0]
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html

# TODO 33:
# Copie y pegue la siguiente línea en la consola para obtener la información de la última fila del DataFrame usando `iloc`:
# sub_df.iloc[-1]

# TODO 34:
# Copie y pegue la siguiente línea en la consola para seleccionar las primeras 5 filas de la columna 'title' usando `iloc`:
# sub_df.iloc[:5, sub_df.columns.get_loc('title')]

# TODO 35:
# Copie y pegue las siguientes líneas en la consola para cambiar el valor de la primera celda (primera fila, primera columna) a 'N/A' usando `iloc`:
# sub_df.iloc[0, 0] = 'N/A'
# Verifique el cambio:
# sub_df.iloc[0, 0]

# TODO 36:
# Copie y pegue la siguiente línea en la consola para seleccionar las primeras 5 filas de la columna 'title' usando `loc`:
# sub_df.loc[:4, 'title']
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

# TODO 37:
# Copie y pegue la siguiente línea en la consola para seleccionar las filas donde 'vote_count' es mayor que 8 usando `loc`:
# sub_df.loc[sub_df['vote_count'] > 8]

# TODO 38:
# Copie y pegue la siguiente línea en la consola para cambiar el valor de la columna 'adult' a False donde 'vote_count' es menor que 10 usando `loc`:
# sub_df.loc[sub_df['vote_count'] < 10, 'adult'] = False

# TODO 39:
# Remueva el comentario de la siguiente línea para imprimir los valores de la columna 'adult' donde 'vote_count' es menor que 10:
# Deberían ser todos False si el cambio en el TODO 38 se realizó correctamente.
#print(sub_df.loc[sub_df['vote_count'] < 10, 'adult'])


########################################################
# OTRAS OPERACIONES ÚTILES:
########################################################

# TODO 40:
# Copie y pegue la siguiente línea en la consola para usar el método `rename` para cambiar el nombre de la columna 'title' a 'titulo':
# sub_df.rename(columns={'title': 'titulo'}, inplace=True)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html

# TODO 41:
# Copie y pegue la siguiente línea en la consola para usar el método `drop` para eliminar la columna 'original_title' del DataFrame:
# sub_df.drop('original_title', axis=1, inplace=True)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

# TODO 42:
# Copie y pegue la siguiente línea en la consola para usar el método `to_csv` para guardar el DataFrame modificado en un nuevo archivo CSV llamado 'nuevo_archivo.csv':
# sub_df.to_csv('/ruta/completa/a/nuevo_archivo.csv', index=False)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html