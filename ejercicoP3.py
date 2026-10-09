numeros = [1,2,3,4,5,6,7,8,9,10,55,88]

meses =("enero", "febrero"," marzo", "abril"," mayo", "junio", "julio", "agosto", "sept", "octubre", "diciembre")

notas= {
"Roberto":5,
"Oscar":9,
"Lorena":10}

numeros_unicos= {2,2,2,3,3,4,5,6,7,8}

notas["Roberto"] = 8

pares=[x for x in numeros if x % 2 == 0]
print(pares)

print(meses[0], meses[-1])

print(numeros, meses,notas, numeros_unicos, pares)