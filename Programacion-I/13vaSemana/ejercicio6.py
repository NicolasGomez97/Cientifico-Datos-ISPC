def verificaMail(e):
    for i in e:
        if (i == '@'):
            for i in e:
                if (i == '.'):
                    for i in e:
                        if (i == 'c'):
                            for i in e:
                                if (i == 'o'):
                                    for i in e:
                                        if (i == 'm'):
                                            print('el mail es valido')
                                            break
                                    break
                            break        
                    break
            break

e = str(input("Ingrese el email: "))
verificaMail(e)