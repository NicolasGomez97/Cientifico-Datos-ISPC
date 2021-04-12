pila = []

def push(val):
    pila.append(val)


def pop():
    val = pila[-1]
    del pila[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())


class Pila:    # define la clase Pila
    def __init__(self):    # define la función del constructor
        print("¡Hola!")

objetoPila = Pila()    # instanciando el objeto

class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())