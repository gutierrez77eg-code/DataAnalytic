#import pandas as pd
#id drive= "lif-MuSk6Yj-tlExTInqX9HVbmp5_XjSj"
#url = f"https://drive.usercontent.google.com/download?id={id_drive}"&export


#df = pd.read_csv("ventas.cvs")
#df = pd.url

# df (Data Frame)
#df["Vendedor"] == "Vendedor 10"


def mostrar_informacio(nombre, **kwargs):
    info = f"nombre: {nombre}\n"
    for clave, valor in kwargs.items():
        info += f"{clave}: {valor}\n"
    return info
print (mostrar_informacio("Roberto", edad=30, ciudad="Quilmes", profesion="Analista"))

def funcion_completa(param1, param2=10, *args, kwarg1=none, **kwargs):
    print(f"param1: {param1}, param2: {param2}, args: {args}, kwarg1: {kwarg1}, kwargs: {kwargs}")