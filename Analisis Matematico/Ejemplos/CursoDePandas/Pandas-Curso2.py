import pandas as pd
import numpy as np
datos = pd.read_csv("C:/Users/Nicolas/Documents/Cientifico-Datos-ISPC/Programacion-I/Datasets/vgsales.csv/vgsales.csv")
print(datos.info())
print(datos.head())

nuevo = pd.DataFrame(datos)
print(nuevo)
nuevo = nuevo.replace(np.nan,"0")
print("****Impresión sin NaN****")
print(nuevo.info())
print("\n"*5)
print("****Estadísticas sin NaN****")
print(nuevo.describe())
print("\n"*5)
print("****Estadísticas solo numeros****")
print(nuevo.describe(include=[np.number]))
print("\n"*5)

