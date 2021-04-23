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


class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val    
    
# ingresa código aquí
pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())

class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

# ingresa código aquí
def push(self, val):
    self.__sum += val
    Pila.push(self, val)


    class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val  

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0


    def getSuma(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val


objetoPila = SumarPila()

for i in range(5):
    objetoPila.push(i)
print(objetoPila.getSuma())

for i in range(5):
    print(objetoPila.pop())


#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/propiedades-de-la-poo

#Variables de instancia
class ClaseEjemplo:
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

#Variable Case
class ClaseEjemplo:
    contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)

#Varia
class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        ClaseEjemplo.varia = val

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)

#Comprobando la existencia de un atributo 
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
print(objetoEjemplo.b)

#Try 
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

try:
    print(objetoEjemplo.b)
except AttributeError:
    pass

#hasattr
class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))

class ClaseEjemplo:
    a = 1
    def __init__(self):
        self.c = 2

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'c'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo, 'b'))
print(hasattr(ClaseEjemplo, 'a'))

#Metodo 
class conClase:
    def metodo(self):
        print("método")

obj = conClase()
obj.metodo()

#Métodos a detalle
class conClase:
    varia = 2
    def metodo(self):
        print(self.varia, self.var)

obj = conClase()
obj.var = 3
obj.metodo()

class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase()
obj.metodo()

#Métodos a detalle
'''es un método, y un método es una función, puedes hacer los mismos trucos con constructores y 
métodos que con las funciones ordinarias.
'''



class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)

# el manejo de los nombres

class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto()

#__dict__ es un diccionario. Otra propiedad incorporada que vale la pena mencionar es una cadena llamada __name__.
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)

#__module__ es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)

#__bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son superclases directas para la clase.
class SuperUno:
    pass

class SuperDos:
    pass

class Sub(SuperUno, SuperDos):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperUno)
printBases(SuperDos)
printBases(Sub)

#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/poo-m-eacute-todos-8


class MiClase:
    pass

obj = MiClase()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.entero = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)

print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)

#Herencia: ¿por qué y cómo?

class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)

#Cuando Python necesita que alguna clase u objeto deba ser presentado 
# como una cadena (es recomendable colocar el objeto como argumento 
# en la invocación de la función print()), intenta invocar 
# un método llamado __str__() del objeto y emplear la cadena que devuelve.

class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)

#La herencia es una práctica común (en la programación de objetos) de pasar atributos y métodos 
# de la superclase 
# (definida y existente) a una clase recién creada, llamada subclase.

#herencia de dos niveles
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass

#Herencia: issubclass()
#Python ofrece una función que es capaz de identificar una relación entre 
# dos clases, y aunque su diagnóstico no es complejo, puede verificar si una 
# clase particular es una subclase de cualquier otra clase.

class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()


#Herencia: isinstance()
#Como ya sabes, un objeto es la encarnación de una clase. Esto significa que 
# el objeto es como un pastel horneado usando una receta que se incluye 
# dentro de la clase.



#Herencia: el operador is
#También existe un operador de Python que vale la pena mencionar, ya que se 
# refiere directamente a los objetos: aquí está:

class ClaseMuestra:
    def __init__(self, val):
        self.val = val

ob1 = ClaseMuestra(0)
ob2 = ClaseMuestra(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)

str1 = "Mary tenía un "
str2 = "Mary tenía un corderito"
str1 += "corderito"

print(str1 == str2, str1 is str2)


#Cómo Python encuentra propiedades y métodos

class Super:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."

class Sub(Super):
    def __init__(self, nombre):
        Super.__init__(self, nombre)


obj = Sub("Andy")

print(obj)

#super().__init__(nombre)

#Intentemos hacer algo similar, pero con propiedades (más precisamente con: variables de clase).
# Probando propiedades: variables de clase
class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()

print(obj.subVar)
print(obj.supVar)



# Probando propiedades: variables de instancia
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 13

obj = Sub()

print(obj.subVar)
print(obj.supVar)

#Cómo Python encuentra propiedades y métodos: continuación
#La herencia múltiple ocurre cuando una clase tiene más de una superclase.

#La clase Sub hereda todos los bienes de dos superclases, Izquierda y Derecha 
# (estos nombres están destinados a ser significativos).

class Izquierda:
    var = "I"
    varIzquierda = "II"
    def fun(self):
        return "Izquierda"


class Derecha:
    var = "D"
    varDerecha = "DD"
    def fun(self):
        return "Derecha"

class Sub(Izquierda, Derecha):
    pass


obj = Sub()

print(obj.var, obj.varIzquierda, obj.varDerecha, obj.fun())

#Cómo construir una jerarquía de clases

#El polimorfismo 
import time

class Vehiculo:
    def cambiardireccion(izquierda, on):
        pass

    def girar(izquierda):
        cambiardireccion(izquierda, True)
        time.sleep(0.25)
        cambiardireccion(izquierda, False)

class VehiculoOruga(Vehiculo):
    def control_de_pista(izquierda, alto):
        pass

    def cambiardireccion(izquierda, on):
        control_de_pista(izquierda, on)

class VehiculoTerrestre(Vehiculo):
    def girar_ruedas_delanteras(izquierda, on):
        pass

    def cambiardireccion(izquierda, on):
        girar_ruedas_delanteras(izquierda, on)


#La composición es el proceso de componer un objeto usando otros 
# objetos diferentes. Los objetos utilizados en la composición entregan un 
# conjunto de rasgos deseados (propiedades y / o métodos), podemos decir 
# que actúan como bloques utilizados para construir una estructura más 
# complicada.
import time

class Pistas:
    def cambiardireccion(self, izquierda, on):
        print("pistas: ", izquierda, on)

class Ruedas:
    def cambiardireccion(self, izquierda, on):
        print("ruedas: ", izquierda, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, izquierda):
        self.controlador.cambiardireccion(izquierda, True)
        time.sleep(0.25)
        self.controlador.cambiardireccion(izquierda, False)

conRuedas = Vehiculo(Ruedas())
conPistas = Vehiculo(Pistas())

conRuedas.girar(True)
conPistas.girar(False)

#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/excepciones-una-vez-m-aacute-s

#Más sobre excepciones
def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n

print(reciproco(2))
print(reciproco(0))

#El bloque try-except se puede extender de una manera más: agregando una 
# parte encabezada por la palabra clave reservada finally (debe ser la 
# última rama del código diseñada para manejar excepciones

def reciproco(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es el momento de decir adiós")
        return n

print(reciproco(2))
print(reciproco(0))

#Probablemente no te sorprenderá saber que las excepciones son clases. 
# Además, cuando se genera una excepción, se crea una instancia de un objeto 
# de la clase y pasa por todos los niveles de ejecución del programa, buscando 
# la rama "except" que está preparada para tratar con la excepc

def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)

#El primer caso parece de rutina, solo hay el nombre Exception despues de la palabra 
# clave reservada raise. Esto significa que el objeto de esta clase se ha creado 
# de la manera más rutinaria.

#El segundo y el tercer caso pueden parecer un poco extraños a primera vista, 
# pero no hay nada extraño, son solo las invocaciones del constructor. 
# En la segunda sentencia raise, el constructor se invoca con un argumento, y en el tercero, con dos.

def printargs(args):
	lng = len(args)
	if lng == 0:
		print("")
	elif lng == 1:
		print(args[0])
	else:
		print(str(args))

try:
	raise Exception
except Exception as e:
	print(e, e.__str__(), sep=' : ' ,end=' : ')
	printargs(e.args)

try:
	raise Exception("mi excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)

try:
	raise Exception("mi", "excepción")
except Exception as e:
	print(e, e.__str__(), sep=' : ', end=' : ')
	printargs(e.args)



#Cómo crear tu propia excepción
#Esto se puede hacer al definir tus propias excepciones como subclases 
# derivadas de las predefinidas.

class MyZeroDivisionError(ZeroDivisionError):	
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("peores noticias")
	else:		
		raise ZeroDivisionError("malas noticias")

for mode in [False, True]:
	try:
		doTheDivision(mode)
	except ZeroDivisionError:
		print('División entre cero')


for mode in [False, True]:
	try:
		doTheDivision(mode)
	except MyZeroDivisionError:
		print('Mi división entre cero')
	except ZeroDivisionError:
		print('División entre cero original'


#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/excepciones-una-vez-m-aacute-s-6


class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje)
        self.pizza = pizza	


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso

class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(self, mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError.__init__(self, pizza, mensaje)
        self.queso = queso


def makePizza(pizza, queso):
	if pizza not in ['margherita', 'capricciosa', 'calzone']:
		raise PizzaError(pizza, "no hay tal pizza en el menú")
	if queso > 100:
		raise DemasiadoQuesoError(pizza, queso, "demasiado queso")
	print("¡Pizza lista!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
	try:
		makePizza(pz, ch)
	except DemasiadoQuesoError as tmce:
		print(tmce, ':', tmce.queso)
	except PizzaError as pe:
		print(pe, ':', pe.pizza)

#Generadores, dónde encontrarlos
#Un generador de Python es un fragmento de código 
# especializado capaz de producir una serie de valores y controlar el proceso de iteración. 

for i in range(5):
    print(i)

#El protocolo iterador es una forma en que un objeto debe comportarse 
# para ajustarse a las reglas impuestas por el contexto de las sentencias
#for e in. Un objeto conforme al protocolo iterador se llama iterador
#__iter__() el cual debe devolver el objeto en sí y que se invoca una vez
#  (es necesario para que Python inicie con éxito la iteración).
#__next__() el cual debe devolver el siguiente valor (primero, segundo, etc.) 
# de la serie deseada: será invocado por las sentencias for/in para pasar a la siguiente 
# iteración; si no hay más valores a proporcionar, el método deberá lanzar la excepción StopIteration.

class Fib:
	def __init__(self, nn):
		print("__init__")
		self.__n = nn
		self.__i = 0
		self.__p1 = self.__p2 = 1

	def __iter__(self):
		print("__iter__")		
		return self

	def __next__(self):
		print("__next__")				
		self.__i += 1
		if self.__i > self.__n:
			raise StopIteration
		if self.__i in [1, 2]:
			return 1
		ret = self.__p1 + self.__p2
		self.__p1, self.__p2 = self.__p2, ret
		return ret

for i in Fib(10):
	print(i)


#La sentencia yield

#Se puede ver a la palabra clave reservada yield como un hermano 
# más inteligente de la sentencia return, con una diferencia esencial.

def fun(n):
    for i in range(n):
        yield i


#Hay una limitación importante: dicha función no debe invocarse explícitamente 
# ya que no es una función; es un objeto generador.

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)


#generador para producir las primeras n potencias de 2

def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for v in potenciasDe2(8):
    print(v)


#Los generadores también pueden usarse dentro de listas de comprensión
def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

t = [x for x in potenciasDe2(5)]

print(t)

#Existen dos partes dentro del código, 
# ambas crean una lista que contiene algunas 
# de las primeras potencias naturales de diez

#La primer parte utiliza una forma rutinaria del bucle for, 
# mientras que la segunda hace uso de la comprensión de listas y construye 
# la lista en el momento, sin necesidad de un bucle o cualquier otro código

listaUno = []

for ex in range(6):
    listaUno.append(10 ** ex)


listaDos = [10 ** ex for ex in range(6)]

print(listaUno)
print(listaDos)

#Es una expresión condicional: una forma de seleccionar uno de dos valores 
# diferentes en función del resultado de una expresión booleana.
lst = []

for x in range(10):
    lst.append(1 if x % 2 == 0 else 0)

print(lst)

#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/generadores-y-cierres-7

#https://edube.org/learn/programming-essentials-in-python-part-2-spanish/generadores-y-cierres-8

