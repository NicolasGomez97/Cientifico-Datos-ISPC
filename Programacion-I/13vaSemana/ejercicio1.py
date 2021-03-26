n = int(input("Introduce el numero de veces: \n"))

def triangulo(a):
    for i in range(n+1):
        print("*"*i)

def trianguloInv(a):
    for i in range(n+1):
        espacios= n-i
        print(" "*espacios+"*"*i)

def trianguloCentrado(a):
    for i in range(n+1):
        espacios= n-i
        print(" "*espacios+"* "*i)


trianguloInv(n)
triangulo(n)
trianguloCentrado(n)
