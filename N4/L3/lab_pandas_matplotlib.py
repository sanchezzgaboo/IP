#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
N4-L3
"""

import ast
import pandas as pd
import matplotlib.pyplot as plt

#####################################################################################
# INSTRUCCIONES:
#####################################################################################
# Complete uno a uno, todos los siguientes TODOs.
# Este programa imprime mensajes para guiar lo que se espera como salida a ese punto (Ej: Que se debió producir una imagen).
# Las imágenes aparecerán en la pestaña 'Plots' de Spyder (debe seleccionarla en el cuadro de la parte superior derecha).
# IMPORTANTE: Es vital que lea y comprenda los enlaces a la documentación provista.
# No es necesario hacer ninguna entrega de este laboratorio.
# El laboratorio usa el dataset: Popular Video Games 1980 - 2023, cuya versión original se encuentra en:
# https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023
# El dataset proviene de Backloggd y contiene datos de videojuegos de 1980 a 2023.
#####################################################################################



# TODO 1:
# Asigne a `RUTA` un string con la *ruta completa* al archivo `games.csv`.
# El archivo debe estar en su directorio de trabajo de Spyder.
# Si está en Windows, use doble backslash: 'C:\\ruta\\completa\\games.csv'.
# IMPORTANTE: Obtendrá un error (No such file or directory...) si no ingresa la ruta completa y correcta al archivo .csv.
RUTA = 'C:\\Users\\gsanc\\OneDrive\\Documents\\Python\\IP\\N4\\L3\\games.csv'

# TODO 2:
# Revise el siguiente código, el cual carga el archivo `games.csv` en un DataFrame nombrado como `df`.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
df = pd.read_csv(RUTA)
print('- El DataFrame fue cargado exitosamente.')




# El siguiente código hace una limpieza y ajustes del DataFrame.
# NO es necesario comprenderlo pues es una sintaxis no estudiada en el curso.
# El propósito del código es dejar listo el dataset para que pueda usarlo en los TODOs restantes.
df = df.drop(columns=['Unnamed: 0'])
df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df.dropna()
df = df[df['release_date'] != 'releases on TBD']
df['genres'] = df['genres'].apply(ast.literal_eval)
df['main_genre'] = df['genres'].apply(lambda x: x[0] if len(x) > 0 else None)
column_order = ['title', 'release_date', 'team', 'rating', 'times_listed', 'number_of_reviews', 
                'genres', 'main_genre', 'summary', 'reviews', 'plays', 'playing', 'backlogs', 'wishlist']
df = df[column_order]
print('- El DataFrame fue ajustado/limpiado exitosamente.')




########################################################
# EXPLORACIÓN DEL DATAFRAME:
########################################################

# TODO 3:
# Copie y pegue en la consola de Spyder (parte inferior derecha) los siguientes tres comandos.
# Se usan para configurar Pandas para mostrar resultados más amplios.
# pd.set_option('display.max_colwidth', None)  # Ajusta la longitud de columnas (use reset_option para revertir)
# pd.set_option('display.max_row', 100)  # Muestra hasta 100 filas (ajuste según necesidad)
# pd.set_option('display.max_columns', 100)  # Muestra hasta 100 columnas (ajuste según necesidad)

# TODO 4:
# Copie y pegue la siguiente línea en la consola para obtener el número de filas y columnas:
# df.shape
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html

# TODO 5:
# Copie y pegue la siguiente línea en la consola para obtener los nombres de las columnas:
# df.columns
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.columns.html

# TODO 6:
# Copie y pegue la siguiente línea en la consola para obtener los tipos de datos y nombres de las columnas:
# df.dtypes
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dtypes.html

# TODO 7:
# Copie y pegue la siguiente línea en la consola para obtener información general del DataFrame:
# df.info()
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html

# TODO 8:
# Copie y pegue la siguiente línea en la consola para obtener estadísticas descriptivas del DataFrame:
# df.describe()
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html

# TODO 9:
# Copie y pegue la siguiente línea en la consola para *filtrar* las columnas 'title' y 'rating':
# df.filter(items=['title', 'rating'])
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html

# TODO 10:
# Copie y pegue la siguiente línea en la consola para revisar el formato de las fechas de lanzamiento:
# df['release_date'].head(3)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html


########################################################
# MANIPULANDO DATOS:
########################################################

# Esta línea corrige el formato de la columna 'release_date':
df['release_date'] = pd.to_datetime(df['release_date'])
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

# TODO 11:
# Verifique que el cambio anterior fue aplicado usando un método de exploración del DataFrame.


########################################################
# GRAFICANDO DATOS:
########################################################

# Este código agrega una columna 'release_year' con el año de lanzamiento:
df['release_year'] = df['release_date'].dt.year
df = df[['title', 'release_date', 'release_year', 'team', 'rating', 'times_listed', 
         'number_of_reviews', 'genres', 'main_genre', 'summary', 'reviews', 'plays', 
         'playing', 'backlogs', 'wishlist']]
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.year.html

# TODO 12:
# Verifique que la columna 'release_year' se creó correctamente. 
# ¿Cuál es el tipo tipo de dato de esta nueva columna? -> Int32

# TODO 13:
# Estudie MUY detalladamente el siguiente código usado para crear un gráfico de barras del número de juegos lanzados por año.
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
# DataFrame.groupby es una función que usará *recurrentemente* en evaluaciones de Nivel 4.
games_per_year = df.groupby('release_year').size()

ax = games_per_year.plot(kind='bar', figsize=(10, 6), fontsize='small', 
                         title='Número de videojuegos lanzados por año', 
                         xlabel='Año', ylabel='Número de Juegos')
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

ax.figure.tight_layout()
# matplotlib.pyplot.tight_layout() muestra una gráfica. Esta función hace parte de matplotlib.
# Ayuda: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html

plt.show()
# matplotlib.pyplot.show() muestra una gráfica. Esta función hace parte de matplotlib.
# Ayuda: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
print('- Gráfica de barras mostrada en \'Plots\' de Spyder')


# Esta línea crea un DataFrame con los juegos lanzados en 2022:
juegos_2022 = df[df['release_year'] == 2022]

# TODO 14:
# Copie y pegue la siguiente línea en la consola para verificar que solo hay juegos de 2022:
# juegos_2022['release_year'].unique()

# TODO 15:
# Estudie MUY detalladamente el siguiente código usado para generar un gráfico de pastel (pie chart) de los 5 géneros mejor calificados en 2022.
genre_ratings = juegos_2022.groupby("main_genre")["rating"].sum()
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

top_5_genres = genre_ratings.sort_values(ascending=False).head(5)
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

ax = top_5_genres.plot(kind="pie", figsize=(10, 6), autopct="%1.1f%%", title="Top 5 géneros en 2022")
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html

ax.figure.tight_layout()
plt.show()
print('- Gráfica de pastel mostrada en \'Plots\' de Spyder')

# TODO 16:
# Estudie MUY detalladamente el siguiente código usado para crear un gráfico de barras horizontales de los 10 juegos más populares en 2008.
# Ignore la advertencia (SettingWithCopyWarning...) si le aparece.
juegos_2008 = df[df['release_year'] == 2008]
# La siguiente línea solo asegura que los datos sean numéricos para así poder graficarlos.
# Este es un paso necesario, solo dadas las características del dataset usado en este laboratorio.
juegos_2008['playing'] = pd.to_numeric(juegos_2008['playing'], errors='coerce')
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html

top_10_juegos = juegos_2008.sort_values(by='playing', ascending=False).head(10)
ax = top_10_juegos.plot(kind='barh', x='title', y='playing', figsize=(10, 6), color='skyblue', title='Top 10 juegos en 2008')
# Ayuda: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
ax.invert_yaxis()
ax.figure.tight_layout()
plt.show()
print('- Gráfica de barras horizontales mostrada en \'Plots\' de Spyder')

# TODO 17:
# Estudie MUY detalladamente el siguiente código usado para crear un digrama de cajas (boxplot) de la distribución de 'rating' por género.
main_genre_rating = df[['main_genre', 'rating']]
main_genre = 'Shooter'  # Puede cambiar el género por otro o pedirlo al usuario (input()) si lo desea.
if main_genre in main_genre_rating['main_genre'].unique(): # Verifica si el género dado existe.
    filtered_genre_rating = main_genre_rating[main_genre_rating['main_genre'] == main_genre]
    ax = filtered_genre_rating.boxplot(column='rating', figsize=(10, 5), patch_artist=True)
# Ayuda: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html   
    ax.set_title(f'Distribución de Ratings para el género: {main_genre}')
    ax.figure.tight_layout()
    plt.show()
    print(f'- Boxplot mostrado en \'Plots\' de Spyder para: {main_genre}')
else:
    print(f'Error: El género "{main_genre}" no está en el DataFrame.')

# TODO 18:
# Explore más métodos de Pandas y matplotlib en:
# https://pandas.pydata.org/pandas-docs/stable/reference/series.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
# https://matplotlib.org/stable/api/
# ¿Está en capacidad de buscar su videojuego favorito? y si existe en el DataFrame, ¿está en capacidad de analizar/graficar sus datos?