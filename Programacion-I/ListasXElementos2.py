"""
Problema:
    
Tengo 10 listas 10 elementos c/u, pero la cantidad de listas puede ampliarse.

Las listas tiene nombre con letras, desde la "a".

Quiero tomar de uno cada elemento de las listas y calcular una media.
O sea a[1]+b[1]+c[1]..... / n

Y necesito la media de cada lista.

Ej:
a=[1,2,3,4,5,6,7,8,9,0]
b=[10,9,8,7,6,5,4,3,2,1]
"""

import numpy as np
import statistics as sta
cantidadListas=int(input("Ingrese el número de listas: "))
cantidadElementos=int(input("Ingrese la cantidad de elementos para las listas: "))
newLista=[]
diccionario={}

for i in range(cantidadListas):
    nombreLista=input("Ingrese el nombre de la lista: ")
    for j in range(cantidadElementos):
        item=int(input("Ingrese el elemnto "+ str(j) + " de la lista "+  str(i) +" "))
        newLista.append(int(item))
        diccionario[nombreLista]=newLista
    newLista=newLista[cantidadElementos:]
    print(diccionario)

#print("\nNota promedio de la clase")
#nota = 0
#for n,d in diccionario.items():
    #nota += diccionario['a'] # es igual a nota = nota + d['nota']
#print(nota/len(diccionario))

#val = diccionario.values()
#print(val)
#print (sta.mean(newLista))