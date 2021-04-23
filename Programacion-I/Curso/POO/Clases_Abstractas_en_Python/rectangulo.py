from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)
    
    def area(self):
        return self.alto * self.ancho