'''Metodo de webscraping a una pagina web, consumiendo datos especificos
para finalmente almacenarlos en un csv'''
#Importe de librerias
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Obtencion de datos mediante el URL del sitio
r = requests.get('https://www.nike.com/mx/w/ninos-calzado-v4dhzy7ok')
reshtml = BeautifulSoup(r.text, 'lxml')
#accede a la clase e indice de los articulos
url = reshtml.find(class_="product-grid css-1hl0l1w").find_all('a')

iterador = 1

link_productos = []
nombre_articulos = []

for i in url:

    if iterador % 2 == 0:
        link_productos.append(i['href'])
        nombre_articulos.append(i.text)
    iterador += 1

df = pd.DataFrame({'Nombre producto': nombre_articulos,'Link de producto': link_productos})
#Exporta el archivo csv
df.to_csv('scvproductos.csv',index=False)