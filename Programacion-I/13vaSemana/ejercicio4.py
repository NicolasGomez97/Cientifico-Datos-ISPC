l1 = []
l2 = [] 
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
print(l1)
print(l2)
for i in l1:
    for j in l2:
        if (i == j):
            l1.remove(i)

print(l1)
print(l2)
