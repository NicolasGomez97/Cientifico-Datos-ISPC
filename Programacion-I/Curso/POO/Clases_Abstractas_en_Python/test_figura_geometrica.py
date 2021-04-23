from cuadrado import Cuadrado
from figura_geometrica import FiguraGeometrica
from rectangulo import Rectangulo

#No se puede instanciar una clase abstracta
#figuraGeometrica = FiguraGeometrica(3,4)

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado.color)

rectangulo = Rectangulo(10,5,"Verde")
print(rectangulo.area())
print(rectangulo.color)



#Method Resolution Order
print(Cuadrado.mro())