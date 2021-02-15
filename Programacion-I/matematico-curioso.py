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