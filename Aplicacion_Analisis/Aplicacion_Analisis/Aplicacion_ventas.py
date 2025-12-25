import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


df = pd.read_excel('registro_ventas_250.xlsx')

top_5 = (df.groupby('vendedor')['ingreso_total']
         .sum()
         .sort_values(ascending=False)
         .head(5)
         .reset_index())

print("----Top 5 vendedores por ingreso total----")
print(top_5)



top_3_productos = (df.groupby(['producto', 'categoria'])['ingreso_total']
                  .sum()
                  .sort_values(ascending=False)
                  .head(3)
                  .reset_index())

print("TOP 3 PRODUCTOS POR INGRESO TOTAL:")
print(top_3_productos.to_string(index=False, formatters={'ingreso_total': '${:,.2f}'.format}))



df['descuento'] = pd.to_numeric(df['descuento'], errors='coerce')

con = df[df['descuento'] > 0]['unidades'].mean()
sin = df[df['descuento'] == 0]['unidades'].mean()

print(f"Con descuento: {con:.1f} unidades")
print(f"Sin descuento: {sin:.1f} unidades")
print(f"Diferencia: {con - sin:.1f} unidades")

if con > sin:
    print("✅ Las ventas con descuento tienen MÁS unidades en promedio")
else:
    print("❌ Las ventas con descuento NO tienen más unidades en promedio")