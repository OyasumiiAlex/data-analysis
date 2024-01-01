'''Algoritmo que imprime los datos de un CSV, iterando en su numero de filas'''
#Importe de libreriras
import pandas as pd
#Leer el archivo csv
ventasgas = pd.read_csv("./src/VentasGasLP.csv", header=0, index_col=0, encoding="ISO-8859-1")
#Imprime la cantidad de datos requeridos(en este caso son 10)
print(ventasgas.head(10))

