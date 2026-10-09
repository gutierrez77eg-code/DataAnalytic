
#importamos el csv para revisar como estan los datos y comenzar la depuracion
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_ventas = pd.read_csv("ventas.csv")
df_marketing = pd.read_csv("Marketing.csv")


#print(df_ventas.head())
#print(df_ventas.info())
#print(df_ventas.duplicated().sum())
    #arrojo resultado 0
#print(df_ventas.isnull().sum())
    #Importe 40 resultados null
#print(df_ventas[df_ventas["Importe"].isnull()])
    #los datos nulos son solamente en la columna de Importe
#print(df_ventas.info())
    #El dataset contiene 954 registros y la variable Importe presenta 40 valores non-null.
#print(df_ventas["Importe"].head(20)) #Revisamos como estan cargados los importes

df_ventas_job = df_ventas
df_ventas_job["Importe"] = (df_ventas_job["Importe"].str.replace("$","",regex=False).astype(float))
df_ventas_job['Importe'] = pd.to_numeric(df_ventas_job['Importe'],errors='coerce')

#modificamos los valores de Importe de str a float y cambiamos a numerico con panda a toda la columna

df_ventas_job["Fecha"].head(5)
df_ventas_job["Fecha"] = pd.to_datetime(df_ventas_job["Fecha"], format='%d/%m/%Y')

#Data columns (total 5 columns):
#   Column        Non-Null Count  Dtype         
#---  ------        --------------  -----         
# 0   Fecha         954 non-null    datetime64[us]
# 1   Vendedor      954 non-null    str           
# 2   Sede Entrega  954 non-null    str           
# 3   Producto      954 non-null    str           
# 4   Importe       914 non-null    float64       
#dtypes: datetime64[us](1), float64(1), str(3)
#-----------------------------------------

#print(df_ventas["Vendedor"].unique())
#print(df_ventas["Sede Entrega"].unique())
#print(df_ventas["Producto"].unique())

#------------------------------------------------
# 4   Importe       914 non-null    float64       
#dtypes: datetime64[us](1), float64(1), str(3)
#memory usage: 37.4 KB
#None
#<StringArray>
#['Vendedor 10',  'Vendedor 4',  'Vendedor 3',  'Vendedor 5',  'Vendedor 7',
#  'Vendedor 2',  'Vendedor 1',  'Vendedor 6',  'Vendedor 9',  'Vendedor 8',
# 'Vendedor 11', 'Vendedor 12']
#Length: 12, dtype: str
#<StringArray>
#['Sede D', 'Sede A', 'Sede C', 'Sede B']
#Length: 4, dtype: str
#<StringArray>
#['Producto Z', 'Producto Y', 'Producto W', 'Producto U', 'Producto V',
# 'Producto X', 'Producto Q', 'Producto O', 'Producto R', 'Producto P',
# 'Producto S', 'Producto N', 'Producto T']
#Length: 13, dtype: str
#----------------------------------------------------

df_ventas_job['mes'] = df_ventas_job['Fecha'].dt.month
df_ventas_job['año'] = df_ventas_job['Fecha'].dt.year

#df_ventas_job['total_mensual'] = df_ventas_job["Importe"] * df_ventas_job["mes"]

#df_ventas_enero= df_ventas_job[df_ventas_job['mes']==1]['total_mensual'].sum()

for col in ["Vendedor", "Sede Entrega", "Producto"]:
    df_ventas_job[col] = df_ventas_job[col].str.strip().str.lower()
#quitamos los espacios sobrantes en los extremos y convertimos todo a minusculas

ventas_mensual = df_ventas_job.groupby(['año','mes'])['Importe'].sum().reset_index()
ventas_mensual = ventas_mensual.rename(
    columns={'Importe':'Importe_mesual'}
)

#print(ventas_mensual) Se agrupo datos por año y mes, sumando las ventas mensuales y se cambio el nombre de la columna importe a importe_mensual

#--------------------------------------------------------------------
#----------Consigna 3-----------------------------------------------
 
 #se decidio por un diccionario ya que con el mismo podemos tener una lista de diccionario en el cual se ingres un parametro y su valor

vent = [
    {
     "producto":"cubierta",
     "precio": 30000,
     "cantidad": 4
    },
    {
     "producto":"llantas",
     "precio": 15000,
     "cantidad": 4
    },
    {
     "producto":"faroles",
     "precio": 20000,
     "cantidad":2
    }
]

#for venta in vent:
#    print(venta['producto'])
#    print(venta['cantidad'])
#    print(venta['precio'])
#    print("-----------------")

resumen_productos = df_ventas_job.groupby("Producto")["Importe"].sum()
resumen_productos = resumen_productos.sort_values(ascending=False)
tablas_resumen = resumen_productos.reset_index()
tablas_resumen.columns = ["Producto", "Ingresos"]
Ingresos_totales = df_ventas_job["Importe"].sum()
tablas_resumen["Porcentaje"]=(
    tablas_resumen["Ingresos"] / Ingresos_totales
)*100


#print("Valores nulos de Importes",df_ventas_job["Importe"].isna().sum())
#print(resumen_productos)
#print("Ingresos totales:", round(Ingresos_totales, 2))
#print(tablas_resumen.round(2))


#plt.figure(figsize=(10, 6))

#plt.bar(
#    tablas_resumen["Producto"],
#    tablas_resumen["Ingresos"]
#)

#plt.title("Ingresos acumulados por producto")
#plt.xlabel("Producto")
#plt.ylabel("Ingresos")
#plt.xticks(rotation=45)
#plt.tight_layout()
#plt.show()

#------------------------------------------------------------------
#-----------ejercicio 4 -------------------------------------------

#print(df_marketing.columns)
#print(df_marketing.head(5))
#print("Productos de ventas:")
#print(df_ventas_job["Producto"].unique())
#print("\n Productos de marketing:")
#print(df_marketing["producto"].unique())

df_marketing_job = df_marketing
df_marketing_job["fecha_inicio"]=pd.to_datetime(
    df_marketing_job["fecha_inicio"],
    dayfirst=True
)
df_integrado=pd.merge(
    df_ventas_job,
    df_marketing_job,
    how="cross"
)
df_integrado=df_integrado[
    (df_integrado["Fecha"]>= df_integrado["fecha_inicio"])&
    (df_integrado["Fecha"]<= df_integrado["fecha_fin"])
]
print("Datos integrados:")
print(df_integrado.head(5))