class Caja:
    def __init__(self,alto,ancho,largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def calcular_volumen(self):
        return self.largo*self.ancho*self.alto
    
al = int(input("Ingrese el Alto de la caja: "))
an = int(input("Ingrese el Ancho de la caja"))
la = int(input("Ingrese el Largo de la Caja:"))

caja = Caja(al,an,la)

print(caja.calcular_volumen())
