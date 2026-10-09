#lista de numeros

numeros_lista=[]
numeros_lista=[1,2,3,4,5,6,7,8,9,10]


#tupla con meses

meses_tupla=()
meses_tupla=("enero", "febrero", "marzo", "abril", "mayo", "Junio", "julio","agosto", "Septiembre", "octubre", "noviembre", "diciembre")

#diccionario notas
notas_dicc={
    "Lorena": 9,
    "Pablo": 8,
    "Analia": 8
}


#conjunto numeros_unicos 
numeros_unicos={}
numeros_unicos={1,2,5,3,8,4,6,9,7,5}
#print("conjunto", numeros_unicos,"diccionario", notas_dicc, "lista", numeros_lista, "tupla", meses_tupla)

#modificacion y acceso Ejercicio 2

notas_dicc["Analia"]=9
#print(notas_dicc)


pares=[]
i=0

while(i<len(numeros_lista)):
     if (numeros_lista[i] % 2 == 0):
        pares.append(numeros_lista[i])
     i+=1
print(pares, "son par")

#usando list comprehension

impares=[numero for numero in numeros_lista if numero % 2 == 1]
print(impares, "Los Impares")

#Acceder tupla meses 

pos=len(meses_tupla)-1
print(meses_tupla[0], meses_tupla[pos])

#funciones normales y lambda 
#numero=int(input("ingrese numero:"))

"""
numero=int(input("ingrese numero:"))
def multiplicar_por_dos():
    resultado = numero * 2
    return resultado
resultado=multiplicar_por_dos()
multiplicar_por_dos()
print(resultado)"""

#nueva lista doble
doble=[]
i=0
def multiplicar_por_dos(numero):
    resultado = numero * 2
    return resultado

while(i<len(numeros_lista)):
    new=multiplicar_por_dos(numero=numeros_lista[i])
    doble.append(new)
    i+=1
print("Nueva lista:", doble)

 
#lambda
nueva_lista=[]
i=0
while(i<len(doble)):
    num_lamb=doble[i] *2 
    nueva_lista.append(num_lamb)
    i+=1
print("Lista Lambda", nueva_lista)


clase_practica=[]
for i in nueva_lista:
    clase_practica.append(i*3)

print(clase_practica)

resumido = [i * 4 for i in nueva_lista]
print(resumido)

#ver ranch instruccion nombrada range funcion que recibe tes valores (star, stop la ubicacion menos uno recorre 10 poniendo 11,
#  y el step los pasos en los que recorre de uno en uno o de dos en dos etc )
# ejemplo range(0,20,1) (desde donde comienza, hasta donde menos uno 19, y el ultimo es de uno en uno)


pares= [ i for i in numeros_lista if i % 2 == 0]

print(pares)

edades = [12, 14,22,33,51,21,13,42,21,24,11,14,12,32,21,24,25,52]
mayores =[ i for i in edades if i >= 18]
print(mayores)

verduleria={
    "nombre":"Pera","precio":120,
    "nombre":"Banana","precio":200,
    "nombre":"Manzana":"precio":98,
    "nombre":"Mandarina","precio":45
}

