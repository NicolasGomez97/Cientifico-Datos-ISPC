def coordenadaZ(x,y):
    x=x+10
    y=y+15
    return x,y

#programa principal

x=int(input("Coordenada eje x: "))
y=int(input("Coordenada eje y: "))
for i in range(3):
    z=coordenadaZ(x,y)
    print(z)
    x=x+1
    print(x)
    y=y+1
    print(y)

print(x," . ",y)