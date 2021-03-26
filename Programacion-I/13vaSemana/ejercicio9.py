def dicMaterias():
    d = {}
    while True:
        m = str(input("Ingrese Materia: "))
        n = float(input("Ingrese Nota que sacaste: "))
        d[m]=n
        i = str(input('Quiere Seguir ingresando Materias y Notas: \n'))
        if i == 'no':
            break
    for i,y in list(d.items()):
        if y >= 6.0:
            d.pop(i)
    print(d)
