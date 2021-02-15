import pandas as pd
import numpy as np

datos = {'Nombre':['Chalio', 'Maria', 'Yolanda', 'Tina'],
'Calificaciones':['100','90','100','80'],
'Deporte':['Futbol','Natacion','Basquetbol','Beisbol'],
'Materias':['Calculo','Metodos Numericos','Cocina','Quimica']}

df = pd.DataFrame(datos)
print(df)
print('\n'*2)
#Datos no validos
#nan o not data value

datos2 = {'Nombre':['Chalio', 'Maria', 'Yolanda', 'N/A'],
'Calificaciones':['100','90',np.nan,'80'],
'Deporte':['Futbol','Natacion','Basquetbol','N/A'],
'Materias':['Calculo','Metodos Numericos','N/A','Quimica']}
df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*2)
print(df2.info())
print('\n'*2)


#Estadisticas Básicas
print(df2.describe())
print('\n'*2)
nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan, "0")
print(nuevo)
print('\n'*2)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how='any',inplace=True)
print(nuevo2)
print('\n'*2)

#Eliminar registros buscando por columna
columna = df2[df2['Nombre']!='N/A']
print(columna)
print('\n'*2)

#Llenar con 0 cualquier valor Nan en el DF
nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0,inplace=True)
print(nuevo3)
print('\n'*2)

#Estadistica
print(nuevo3.describe())
print('\n'*4)

#convertir a numeros enteros
nuevo2['Calificaciones'] = nuevo2.Calificaciones.astype(int)
print(nuevo2.describe())

#Estadistica forma individuales
print("Promedio",nuevo2['Calificaciones'].mean())