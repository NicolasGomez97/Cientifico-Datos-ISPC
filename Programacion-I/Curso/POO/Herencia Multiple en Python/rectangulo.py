from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,ancho,largo,color):
        FiguraGeometrica.__init__(self,ancho,largo)
        Color.__init__(self,color)
    
    def area(self):
        return self.get_ancho() * self.get_alto()
    
    def __str__(self):
        return super().__str__() + ", Color: "+ self.get_color()

