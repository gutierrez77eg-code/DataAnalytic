#Ejercicio 1 Parametro posicionales

#def multiplicar(a,b):
#    resultado =  a * b
#    return resultado
#print(multiplicar(9,9))

#Parametros por defecto

#def bienvenida(nombre, mensaje ="¡BIENVENIDO!"):
#    print(mensaje, nombre)

#bienvenida("Enrique")
#bienvenida("Carla","Enhorabuena!!")

#Parametros indefinidos

#def calcular_promedio(*args):
 #   promedio= sum(args) / len(args)
 #   return round(promedio,2)
#print(calcular_promedio(50,40,2,8,90,199))

#Parametros de palabra clave indefinidas

#def concatenar_info (nombre,**kwargs):
#    info = F"Nombre: {nombre}\n"
#    for clave, valor in kwargs.items():
#        info += f"{clave}: {valor}\n"

#    return info
#print(concatenar_info("Enrique", edad=48,ciudad="Quilmes",ocupacion="Estudiante"))


#--------------------------------------------------------------------#
#Actividad 2***
import pandas as pd
df= pd.read_csv("ventas.csv")
print(df.head())

import pandas as pd
url = "https://docs.google.com/spreadsheets/d/18Rs8uJRa3AqyheVWIUqNDnYiBHqy-_H3cgVeDvWp2CY/export?format=csv"
df = pd.read_csv(url)
print(df.head())

import pandas as pd
df = pd.read_excel("ventas.xlsx")
print(df.head())