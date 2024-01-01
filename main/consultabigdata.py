'''
En esta segunda actividad utilizará métodos de la biblioteca Pandas y Dataframe, 
para poder generar consultas que permitan dar respuesta a 
los siguientes criterios de evaluación:
1. Obtener el acumulado de ventas totales de Gas LP del segundo semestre del año 2007 en Chiapas
2. Identificar las 5 estados con mayores ventas de Gas LP durante el año 2008 ordenadas de mayor a menor

'''
#Importe de librerias 
import pandas as pd
import natsort as ns
import numpy as np
#Lectura del archivo CSV
consgas = pd.read_csv("./src/VentasGasLP.csv", header=0, index_col=0, encoding="ISO-8859-1")
#Creacion de dataFrame
df = pd.DataFrame(consgas)
#Primera consulta   
print("---------------Total de venta de GASLP en 2007-------------")
print("Entidad: Chiapas")
print(consgas.iloc[[4],[3]])
#segunda consulta
print("-----------5 Estados con mayor venta durante el 2008 (mayor a menor----------)")
#Primera forma (ordenar todo la base de datos de mayor a menor)
print("Primera forma")
df1 = pd.DataFrame(np.sort(df.values, axis=0), index= df.index, columns= df.columns)
print(df1)
#Segunda forma: Ordenar solo la columna 2008
print("Segunda forma")
df.sort_values(by = ['2008'], ascending =[False])
print(df)


