
v = str(input("Ingrese Palabra: "))
vocal=["a","e","i","o","u"]
cont=0
for i in vocal:
    for j in v:
        if(i==j):
            cont+=1
print(cont)
