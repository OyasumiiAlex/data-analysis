'''Algoritmo para la limpieza de datos de un DataSet
1. columna budget (presupuesto) asignar valor 0 en null
2. columna director_name asignar 'None' en valores null
3. En los atributos duration & imdb_score convertir a numeros positivos
4. En la columna country, convertir valores 'united states' a 'usa' 
'''
#Importacion de librerias
import pandas as pd
import numpy as np
#Lectura del CSV
movieread = pd.read_csv("./src/movie_sample.csv", header=0, index_col=0, encoding="ISO-8859-1")
#columna budget (presupuesto) asignar valor 0 en null
movieread['budget'] = movieread['budget'].fillna(0)
#columna director_name asignar 'None' en valores null
movieread['director_name'] = movieread['director_name'].replace(pd.np.nan, 'none')
movieread['director_name'] = movieread['director_name'].replace('Null', 'none')

movieread['duration'] = pd.to_numeric(movieread['duration'], errors='coerce')

movieread['imdb_score'] = pd.to_numeric(movieread['imdb_score'], errors='coerce')

#En los atributos duration & imdb_score convertir a numeros positivos
for i in range(len(movieread)):
    if movieread['duration'][i] < 0:
        movieread['duration'][i] = movieread['duration'][i] * -1

for i in range(len(movieread)):
    if movieread['imdb_score'][i] < 0:
        movieread['imdb_score'][i] = movieread['imdb_score'][i] * -1
#En la columna country, convertir valores 'united states' a 'USA' 
movieread['country'] = movieread['country'].replace('United States', 'USA')

print(movieread.head(25))

#Exportacion del nuevo CSV
movieread.reset_index().to_csv('DatosNuevosMovie.csv', header = True, index = False)