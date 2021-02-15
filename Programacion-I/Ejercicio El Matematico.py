##Integrantes Ramiro Nicolás Gómez; Silvia Centeno-- Hecho por Silvia Centeno
from random import randint
numero = []
numero.insert(0, randint (20,100))
i = 0
print(numero)
while numero[i]!=1:
    if (numero[i]%2==0):
        numero.insert(i+1, numero[i] // 2)
        i+=1
    else:
        numero.insert(i+1, (numero[i]*3)+1)
        i+=1
print("La lista de números es: ", numero)
print("La cantidad de secuencias es: ", len(numero))
print("El número mayor es: ", max(numero))

##Integrantes Ramiro Nicolás Gómez; Silvia Centeno-- Hecho por Nicolas Gomez
from random import randint
while True:
    numeros = []
    numeros.insert(0, randint(20, 100))
    print(numeros)
    k = 0
    while True:
        if numeros[k] % 2 == 0:
            k += 1
            numeros.insert(k, numeros[k-1] // 2)
        else:
            if numeros[k] == 1:
                break
            k += 1
            numeros.insert(k, (numeros[k-1]*3)+1)
    break
print("La lista de numeros es: ", numeros)
print("Cuantas secuencias se hicieron: ", len(numeros))
print("El numero mayor es: ", max(numeros))