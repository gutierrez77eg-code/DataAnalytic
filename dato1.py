diccionario={"nombre":"Enri", "Edad": 47, "localidad":"Quilmes"}
diccionario["nombre"]="Rodolfo"
print(diccionario)

mi_cojunto={1,2,3,3,4,}
print(mi_cojunto)

tupla1=(1,3.23,"eje")
print(tupla1)

lista_uno=[3,4.44,"radio","disco"]
print(lista_uno)

suma= lambda x, y: x+y
print(suma(5,3))


edades=[12,34,32,23,55,3,6,17]
mayor=list(filter(lambda edades: edades >= 18, edades))
print(mayor)

#Ahora aumentamos un anio a las edades

edades_prox_anio =list(map(lambda edades: edades + 1, edades))
print(mayor, edades_prox_anio)

automoviles=[ 
        {
        "marca":"peugeot",
        "modelo":"206",
        "anio":"2008"
        },

            {
            "marca":"ford",
           "modelo":"fiesta",
          "anio":"2015"
          },

         {
         "marca":"chevrolet",
          "modelo":"astra",
          "anio":"2020"
         },

         {
          "marca":"toyota",
          "modelo":"corola",
          "anio":"2019"
        },

        {
         "marca":"renault",
         "modelo":"12",
         "anio":"1998"
         },
         {
            "marca":"fiat",
            "modelo":"uno scr",
            "anio":"1995"
            },
        {
         "marca":"honda",
         "modelo":"civic",
         "anio":"2001"
         }        
]

print(automoviles)




