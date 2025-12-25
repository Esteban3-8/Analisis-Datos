print("HOAalasd ")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 6)
pd.set_option('display.max_columns', None)

# Cargar datasets del laboratorio
ventas_path = r'C:\Users\esteb\Downloads\n\lab_ventas.csv'
clientes_path = r'C:\Users\esteb\Downloads\n\lab_clientes.csv'


df_ventas = pd.read_csv(ventas_path, parse_dates=['fecha'])
df_clientes = pd.read_csv(clientes_path)

print("Leyendo archivos desde:")

print("Ventas:", ventas_path)
print("Clientes:", clientes_path)

df_ventas.head(), df_clientes.head()
 
# Muestra las primeras 5 filas
print(df_ventas.head())

print("-----------------------------------------------")

# Muestra las primeros 10 filas
print(df_clientes.head(10))



print("-----------------------------------------------")


 #Mostrar las  ultimas 5 filas
print(df_clientes.tail(5))


print("-----------------------------------------------")


# Mostrar una fila específica (por posición)
print(df_ventas.iloc[3])  # fila nuSmero 4



print("-----------------------------------------------")

# Mostrar filas 20 a 30
print(df_ventas.iloc[20:31])