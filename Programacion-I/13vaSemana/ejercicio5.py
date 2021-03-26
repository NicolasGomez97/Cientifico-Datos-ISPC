l1 = []
l2 = [] 
l3 = []
while True:
    v = str(input("ingrese la palbra para la lista 1: \n"))
    l1.append(v)
    print("Quiere continuar ingresando \n si o no")
    q = input()
    if ('no' == q):
        break

while True:
    v = str(input("ingrese la palbra para la lista 2: \n"))
    l2.append(v)
    print("Quiere continuar ingresando \n si o no")
    q = input()
    if ('no' == q):
        break

while True:
    v = str(input("ingrese la palbra para la lista 3: \n"))
    l3.append(v)
    print("Quiere continuar ingresando \n si o no")
    q = input()
    if ('no' == q):
        break

print(l1)
print(l2)
print(l3)
for i in l1:
    for j in l2:
        if (i == j):
                l1.remove(i)
                l2.remove(i)
        for k in l3:
            if (k == j):
                l3.remove(k)
                l2.remove(k)
            if (k == i):
                l3.remove(k)
                l1.remove(k)

print(l1)
print(l2)
print(l3)