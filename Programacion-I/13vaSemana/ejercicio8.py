l= []
while True:
    l.append(str(input("Ingrese la asignatura del curso: ")))
    i = str(input("Quiere seguir agregando otra asiganatura: "))
    if i == "no":
        break

print(l)