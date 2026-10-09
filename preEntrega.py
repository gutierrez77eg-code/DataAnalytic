import pandas as pd
ventas = pd.read_csv("ventas.csv")
marketing = pd.read_csv("marketing.csv")
clientes = pd.read_csv("clientes.csv")

#print(ventas[ventas.isnull().any(axis=1)])
print(clientes.duplicated(keep=False).sum())
print(ventas.columns.tolist())
#print(ventas["Vendedor"].unique())
#print(ventas["Vendedor"].value_counts())
print(ventas["Sede Entrega"].unique())
print(ventas["Importe"].dtype)
