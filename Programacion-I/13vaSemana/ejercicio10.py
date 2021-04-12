def listaNumeros1al10():
    l=[]
    for i in range(1,10+1):
        l.append(i)
    print(sorted(l,reverse=True))
