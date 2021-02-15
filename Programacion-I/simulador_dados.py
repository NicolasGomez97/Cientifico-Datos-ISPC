from random import random

def simulador_d():
    suma_dados = 0
    dado1 = int(random() * 6 + 1)
    dado2 = int(random() * 6 + 1)
    suma_dados = dado1 + dado2
    print('El primer dado salio: ', dado1, '\nEl Segundo dado salio: ', dado2, "\nLa suma es:", suma_dados)


def seguir_jugado():
    while True:
        i=0
        print("Tiene que ingresar un Si o No")
        try:
            r = input('Quiere seguir tirando: \n')
            if r.lower() == 'si':
                pass
            elif r.lower() == 'no':
                pass
        except:
            print("Tiene que ingresar Si o No")
        else:
                if r.lower() == 'si':
                    return simulador_d(), seguir_jugado()
                elif r.lower() == 'no':
                    break
        print('Valor no valido')
        print("Tiene que poner un SI O NO")
        con = input("Desea continuar: ")
        con = con.upper()
        if con == "NO":
            break
def juego():
    print("Bienvenido al Juego")
    simulador_d()
    seguir_jugado()

juego()