''' Algoritmo que calcula el sueldo de un csv con los datos de los empleados
haciendo uso de la libreria pandas '''
#Importe de libreriras
import pandas as pd
#Leer el archivo csv
file = "./src/Empleados.csv"
dataframe = pd.read_csv(file)

#Funcion para calcular
def calculosalario(horas,costo,bono=3000):
    if horas >= 40:
        pago = horas * costo + bono
    else:
        pago = horas * costo
    return pago
#Pago por hora
pago_hora = int(input("Introduzca el pago por hora del empleado: "))  

#Iterar el dataframe
for iterador, index in dataframe.iterrows():
    #Llama a la funcion para calcular el pago  
    pago = calculosalario(index['Horas'], pago_hora)
    #Agrega el pago al dataframe  
    dataframe.loc[iterador, 'Pago'] = pago  
#Imprime el dataframe
print(dataframe)  